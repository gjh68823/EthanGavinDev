//Can't figure it out. W/e.
#include <iostream>
#include <bitset>

using namespace ROOT::VecOps;

RVec<float> neononpromptweight(std::vector<float>& ptbinsPrompt, std::vector<float>& ptbinsFake, std::vector<float>& etabinsel, std::vector<float>& etabinsmu, std::vector<std::vector<float>>& ePromptRates, std::vector<std::vector<float>>& mPromptRates, std::vector<std::vector<float>>& tPromptRates, std::vector<std::vector<float>>& eFakeRates, std::vector<std::vector<float>>& mFakeRates, std::vector<std::vector<float>>& tFakeRates, RVec<float>& Loose4Lepton_pt, RVec<float>& Loose4Lepton_eta, RVec<int>& Loose4Lepton_ID, RVec<int>& Loose4Lepton_isTight){
  
  std::cout << "-------------------------" << std::endl;

  double termWeight;
  double p[4];
  double f[4];
  double leptonFactor;
  RVec<float> totalWeight = {0.0,0.0};
  double faketerm[4];
  double promptterm[4];
  double product = 1;
  float product3 = 1;
  int count;
  int tcombo;
  double etabin;

  // return totalWeight;
  
  //std::cout << "product initialized to " << product << std::endl;
  
  //  std::cout << "Running over how many leptons? " << Loose4Lepton_pt.size() << std::endl;
  for (int i = 0; (i < Loose4Lepton_pt.size()); i++) { // index

    int ptbinPrompt = (std::upper_bound(ptbinsPrompt.begin(), ptbinsPrompt.end(), Loose4Lepton_pt[i]) - ptbinsPrompt.begin())-1;
    int ptbinFake = (std::upper_bound(ptbinsFake.begin(), ptbinsFake.end(), Loose4Lepton_pt[i]) - ptbinsFake.begin())-1;

    //std::cout << "Grabbing ptbin " << ptbin << " for pt = " << Loose4Lepton_pt[i] << ", and etabin " << etabin << " for abseta = " << abs(Loose4Lepton_eta[i]) << std::endl;
    if (Loose4Lepton_ID[i] == 11){
      //    std::cout << "Lepton is Electron" <<  std::endl;
      etabin = (std::upper_bound(etabinsel.begin(), etabinsel.end(), Loose4Lepton_eta[i]) - etabinsel.begin()) - 1;
      p[i] = ePromptRates[ptbinPrompt][etabin];
      f[i] = eFakeRates[ptbinFake][etabin];
    } else if (Loose4Lepton_ID[i] == 13){
      etabin = (std::upper_bound(etabinsmu.begin(), etabinsmu.end(), abs(Loose4Lepton_eta[i])) - etabinsmu.begin()) - 1;
      p[i] = mPromptRates[ptbinPrompt][etabin];
      f[i] = mFakeRates[ptbinFake][etabin];
      //  std::cout << "Lepton is Muon and p=" << p[i] << "and f=" << f[i] <<  std::endl;
    } else {
      // Taus use the same etabins as muons, and they do not have different fake rate ptbins since always from MC
      etabin = (std::upper_bound(etabinsmu.begin(), etabinsmu.end(), abs(Loose4Lepton_eta[i])) - etabinsmu.begin()) - 1;
      // std::cout << "Lepton is Tau" <<  std::endl;
      p[i] = tPromptRates[ptbinPrompt][etabin];
      f[i] = tFakeRates[ptbinPrompt][etabin];
    }
    if(Loose4Lepton_isTight[i] == 0){
      // std::cout << "Lepton Is Loose" << std::endl;
      promptterm[i] = f[i];
      faketerm[i] = p[i];
    } else {
      // std::cout << "Lepton Is Tight" << std::endl;
      promptterm[i] = (1-f[i]);
      faketerm[i] = (1-p[i]);
    }
    product *= (1/(p[i]-f[i]));
    if (i == 2) product3 = product;
    // std::cout << "Product is " << product << std::endl;
  }
  for (int combo = 0; combo < 15; ++combo){ // index cases
    if(((Loose4Lepton_pt.size() == 3)) && combo > 6) continue;
    
    termWeight = product;
    // std::cout << "Combo = " << combo << ", and in binary is " << std::bitset<4>(combo) << std::endl;
    for (int i = 0; (i < Loose4Lepton_pt.size()); ++i) {
      if((combo >> i) & 1){
	termWeight *= promptterm[i] * p[i];
	//	std::cout << "\t lepton " << i << " fell into prompt, and multiplier is" << (promptterm[i] * p[i]) << std::endl;
      } else {
	termWeight *= faketerm[i] * f[i];
	//	std::cout << "\t lepton " << i << " fell into fake, and multiplier is " <<  (faketerm[i] * f[i]) << std::endl;
      }      
    }
    
    tcombo = combo;
    count = 0;
    while (tcombo) {
      tcombo &= (tcombo - 1);
      count++;
    }
    //std::cout << "count ended up as " << count << ", and Sum(Loose4Lepton_isTight) is " << Sum(Loose4Lepton_isTight) << std::endl;
    if ((Sum(Loose4Lepton_isTight) & 1) != (count & 1)){
      termWeight *= -1;
      //    std::cout << "\t Decided to flip negative!" << std::endl;
    }
    // std::cout << "Term weight ended up as " << termWeight << std::endl;
    totalWeight[0] += termWeight;
  }
  if (Loose4Lepton_pt.size() == 3) {
    totalWeight[1] = totalWeight[0];
    std::cout << "Returning weight = " << totalWeight[0] << ", " << totalWeight[1] << ", " << product << std::endl;
    return totalWeight;
  }
  for (int combo = 0; combo < 7; ++combo){ // index cases
    
    termWeight = product3;
    // std::cout << "Combo = " << combo << ", and in binary is " << std::bitset<4>(combo) << std::endl;
    for (int i = 0; (i < 3); ++i) {
      if((combo >> i) & 1){
	termWeight *= promptterm[i] * p[i];
	//	std::cout << "\t lepton " << i << " fell into prompt, and multiplier is" << (promptterm[i] * p[i]) << std::endl;
      } else {
	termWeight *= faketerm[i] * f[i];
	//	std::cout << "\t lepton " << i << " fell into fake, and multiplier is " <<  (faketerm[i] * f[i]) << std::endl;
      }      
    }
    
    tcombo = combo;
    count = 0;
    while (tcombo) {
      tcombo &= (tcombo - 1);
      count++;
    }
    //std::cout << "count ended up as " << count << ", and Sum(Loose4Lepton_isTight) is " << Sum(Loose4Lepton_isTight) << std::endl;
    if ((Sum(Loose4Lepton_isTight) & 1) != (count & 1)){
      termWeight *= -1;
      //    std::cout << "\t Decided to flip negative!" << std::endl;
    }
    // std::cout << "Term weight ended up as " << termWeight << std::endl;
    totalWeight[1] += termWeight;
  }
  
  std::cout << "Returning weight = " << totalWeight[0] << ", " << totalWeight[1] << ", " << product << std::endl;
  // std::cout << "===============================================================================" << std::endl;
  return totalWeight;
}

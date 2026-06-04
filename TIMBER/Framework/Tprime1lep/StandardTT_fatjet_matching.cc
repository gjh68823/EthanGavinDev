using namespace std;
using namespace ROOT::VecOps;

auto get_daughters(int id) {
  vector<unsigned int> daughters;
  for (unsigned int d = id; d < nGenPart; d++){
	if (GenPart_genPartIdxMother[d]!=id){continue;}
	daughters.push_back(d); //get a list of all the daughters of this particle
      }

  return daughters;
}

auto fatjet_matching(string sample, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<float> &GenPart_mass, RVec<float> &GenPart_pt, RVec<float> &GenPart_phi, RVec<float> &GenPart_eta, RVec<short> &GenPart_genPartIdxMother, RVec<int> &GenPart_status, RVec<unsigned short> &GenPart_statusFlags)
{
  RVec<int> pID; //particle id of the parent
  RVec<int> pStatus; //where in the chain the parent particle is?
  RVec<float> pPt;
  RVec<float> pEta;
  RVec<float> pPhi;
  RVec<float> pM;
  
  RVec<float> d0Pt;
  RVec<float> d0Eta;
  RVec<float> d0Phi;
  RVec<float> d0M;
  
  RVec<float> d1Pt;
  RVec<float> d1Eta;
  RVec<float> d1Phi;
  RVec<float> d1M;
  
  RVec<float> d2Pt;
  RVec<float> d2Eta;
  RVec<float> d2Phi;
  RVec<float> d2M;

  for(unsigned int i = 0; i < nGenPart; i++){
    int p = i; //initialize the parent idx
    int id = GenPart_pdgId[p];
    
    bool hasRadiation = false;
    bool hasLepton = false;

    if(abs(id) == 23 || abs(id) == 24 || abs(id) == 25 || abs(id) == 6){
      vector<unsigned int> daughters = get_daughters(id);

      //check for radiation and leptons
      for (unsigned int j = 0; j < daughters.size(); j++){
	int dID = GenPart_pdgId[daughters[j]];
	if(abs(dID) == abs(id)) {hasRadiation = true;} //check for radiation
	else if(abs(dID) == 24 || abs(dID) == 23) { //check t->Wb->leptons and H->WW->leptons, check H->ZZ->leptons
	  vector<unsigned int>granddaughters = get_daughters(daughters[j]);
	  if(abs(GenPart_pdgId[granddaughters[0]]) > 10 && abs(GenPart_pdgId[granddaughters[0]]) < 17) {hasLepton = true}
	  if(abs(GenPart_pdgId[granddaughters[1]]) > 10 && abs(GenPart_pdgId[granddaughters[1]]) < 17) {hasLepton = true}

	}
	else if(abs(dID) > 10 && abs(dID) < 17) {hasLepton = true;}
      }

      //skip this particle if...
      if(hasRadiation) continue;
      if(hasLepton) continue;
      if(GenPart_pt[p] < 175) continue;
      
      vector<unsigned int>siblings = get_daughters(GenPart_genPartIdxMother[p]);
      
      if(abs(id) == 24) { //if W
	float dRWb = 1000;//could cut this down if we want, not necessary
	float dRWW = 1000;

	//find topmost mother of a repeating chain
	while(GenPart_genPartIdxMother[p] != -1 && abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 24) {p = GenPart_genPartIdxMother[p]}

	if(abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 6) {
	  //dr btwn current particle and its sibling
	  float dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[1]], GenPart_phi[p], GenPart_phi[siblings[1]]);
	  
	  if(GenPart_pdgId[sibling[1]] == 24) {
	    dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[0]], GenPart_phi[p], GenPart_phi[siblings[0]]);}
	  if(dr < dRWb) dRWb = dr;
	  
	}else if(abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 25){
	  float dr = 1000;
	  
	  if(GenPart_pdgId[p]*GenPart_pdgId[siblings[0]] > 0) {
	    dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[1]], GenPart_phi[p], GenPart_phi[siblings[1]]); 
	  }else{
	    dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[0]], GenPart_phi[p], GenPart_phi[siblings[0]]);
	  }
	  if(dr < dRWW) dRWW = dr;
	}
	
	if(dRWW < 0.8) continue; //W from merged H
	if(dRWb < 0.8) continue; //W from merged t
      } //end of if W
      
      if(abs(id) == 23) { //if Z
	float dRZZ = 1000;

	//find topmost mother of a repeating chain
	while(GenPart_genPartIdxMother[p] != -1 && abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 23) {p = GenPart_genPartIdxMother[p]}
	
	if(GenPart_genPartIdxMother[p] == 25) {
	  float dr = 1000;
	  if(GenPart_pdgId[p]*GenPart_pdgId[siblings[0]] > 0) {
	    dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[1]], GenPart_phi[p], GenPart_phi[siblings[1]]); 
	  }else{
	    dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[0]], GenPart_phi[p], GenPart_phi[siblings[0]]);
	  }
	  if(dr < dRZZ) dRZZ = dr;
	}
	if(dRZZ < 0.8) continue; // Z from merged H
      }
      
      if(daughters.size() < 2) {
	std::cout << daughters.size() << " daughters from " << GenPart_pdgId[p] << std::endl;
      }

      pStatus.push_back(GenPart_status[p]);
      pID.push_back(GenPart_pdgId[p]);
      pPt.push_back(GenPart_pt[p]);
      pEta.push_back(GenPart_eta[p]);
      pPhi.push_back(GenPart_phi[p]);
      pM.push_back(GenPart_mass[p]);

      if(abs(id) != 6) {
	d0Status.push_back(GenPart_status[daughters[0]]);
	d0ID.push_back(GenPart_pdgId[daughters[0]]);
	d0Pt.push_back(GenPart_pt[daughters[0]]);
	d0Eta.push_back(GenPart_eta[daughters[0]]);
	d0Phi.push_back(GenPart_phi[daughters[0]]);
	d0M.push_back(GenPart_mass[daughters[0]]);

	d1Status.push_back(GenPart_status[daughters[1]]);
	d1ID.push_back(GenPart_pdgId[daughters[1]]);
	d1Pt.push_back(GenPart_pt[daughters[1]]);
	d1Eta.push_back(GenPart_eta[daughters[1]]);
	d1Phi.push_back(GenPart_phi[daughters[1]]);
	d1M.push_back(GenPart_mass[daughters[1]]);

	d2Status.push_back(-99.9);
	d2ID.push_back(-99.9);
	d2Pt.push_back(-99.9);
	d2Eta.push_back(-99.9);
	d2Phi.push_back(-99.9);
	d2M.push_back(-99.9);
      }else{ //if is t
	if(abs(GenPart_pdgId[daughters[0]]) == 24) {
	  W = daughters[0];
	  b = daughters[1];
	}else{
	  W = daughters[1];
	  b = daughters[0];
	}

	//insert weird photon stuff here.

	vector<unsigned int> W_daughters = get_daughters(W);
	if(GenPart_pdgId[W_daughters[0]] == 22 || GenPart_pdgId[W_daughters[1]] == 22) {
	  std::cout << "W has a photon daughter" << std::endl;
	}

	d0Status.push_back(GenPart_status[b]);
	d0ID.push_back(GenPart_pdgId[b]);
	d0Pt.push_back(GenPart_pt[b]);
	d0Eta.push_back(GenPart_eta[b]);
	d0Phi.push_back(GenPart_phi[b]);
	d0M.push_back(GenPart_mass[b]);

	d1Status.push_back(GenPart_status[W_daughters[0]]);
	d1ID.push_back(GenPart_pdgId[W_daughters[0]]);
	d1Pt.push_back(GenPart_pt[W_daughters[0]]);
	d1Eta.push_back(GenPart_eta[W_daughters[0]]);
	d1Phi.push_back(GenPart_phi[W_daughters[0]]);
	d1M.push_back(GenPart_mass[W_daughters[0]]);

        d2Status.push_back(GenPart_status[W_daughters[1]]);
	d2ID.push_back(GenPart_pdgId[W_daughters[1]]);
	d2Pt.push_back(GenPart_pt[W_daughters[1]]);
	d2Eta.push_back(GenPart_eta[W_daughters[1]]);
	d2Phi.push_back(GenPart_phi[W_daughters[1]]);
	d2M.push_back(GenPart_mass[W_daughters[1]]);
    
      }
    }
  }

  for(unsigned int i = 0; i < goodCleanFatJet_Pt.size(); i++){
    //define a tlv for fatjets
  
    float minDR = 1000;
    float matchedPt= -99;
    int matchedID = 0;
    bool isWmatched = false;
    bool isHmatched = false;
    bool isZmatched = false;
    bool isTmatched = false;
    bool isJmatched = false;
    bool isBmatched = false;
    TLorentzVector truePart, d1, d2, d3;

    //collapse the loops, dont put things into vectors, just continue the previous loop here?
    
    for(unsigned int i = 0, i < pPt.size(); i++) {
      truePart.SetPtEtaPhiM(pPt[i], pEta[i], pPhi[i], pM[i]);

      //TODO: add good clean fatjet Timber branches into here. need pt, eta, phi, mass
      //also need sj_idx1/2 may need to implement goodclean versions in timber, and subjet_hadronFlavour from NanoAOD file
      //
    
      if(DeltaR(trueW) < minDR) {
      
      }
    }
  }
  return //vector of goodCleanFatJet_truth;
    //might be nice to return a vect of vects, containing truth, matched pt,
    //truth values are the parent particle
    //matched pt is what it sounds like
    } // '/t' tabs in on couts


  



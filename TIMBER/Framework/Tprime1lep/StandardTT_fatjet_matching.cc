using namespace std;
using namespace ROOT::VecOps;

auto get_daughters(int idx, unsigned int length, RVec<short> GenPart_genPartIdxMother) {
  vector<unsigned int> daughters;
  for (unsigned int d = idx; d < length; d++){
	if (GenPart_genPartIdxMother[d]!=idx){continue;}
	daughters.push_back(d); //get a list of all the daughters of this particle
      }

  return daughters;
}

auto fatjet_matching(string sample, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<float> &GenPart_mass, RVec<float> &GenPart_pt, RVec<float> &GenPart_phi, RVec<float> &GenPart_eta, RVec<short> &GenPart_genPartIdxMother, RVec<int> &GenPart_status, RVec<unsigned short> &GenPart_statusFlags, RVec<float> &gcFatJet_pt, RVec<float> &gcFatJet_eta, RVec<float> &gcFatJet_phi, RVec<float> &gcFatJet_M, RVec<short> &gcFatJet_subj_idx1, RVec<short> &gcFatJet_subj_idx2, RVec<unsigned char> &SubJet_hadronFlavour)
{
  RVec<int> pID; //particle id of the parent
  RVec<int> pStatus; //where in the chain the parent particle is?
  RVec<float> pPt;
  RVec<float> pEta;
  RVec<float> pPhi;
  RVec<float> pM;
  
  RVec<int> d0ID;
  RVec<int> d0Status;
  RVec<float> d0Pt;
  RVec<float> d0Eta;
  RVec<float> d0Phi;
  RVec<float> d0M;
  
  RVec<int> d1ID;
  RVec<int> d1Status;
  RVec<float> d1Pt;
  RVec<float> d1Eta;
  RVec<float> d1Phi;
  RVec<float> d1M;
  
  RVec<int> d2ID;
  RVec<int> d2Status;
  RVec<float> d2Pt;
  RVec<float> d2Eta;
  RVec<float> d2Phi;
  RVec<float> d2M;

  std::cout << "Inside fatjet_matching. Will now beign matching:" << std::endl;
  std::cout << "There are " << nGenPart << " particles in total."  << std::endl;
  std::cout << "===================================" << std::endl;
  for(unsigned int i = 0; i < 30; i++){ //Changed top of range from nGenPart to 30
    int p = i; //initialize the parent idx
    int id = GenPart_pdgId[p];
    std::cout << "Starting particle " << i << " it is a: " << id << " Mother is " << GenPart_genPartIdxMother[i] << " of type " << GenPart_pdgId[GenPart_genPartIdxMother[i]] << std::endl;
    
    bool hasRadiation = false;
    bool hasLepton = false;

    if(abs(id) == 23 || abs(id) == 24 || abs(id) == 25 || abs(id) == 6){
      std::cout << "\t Now checking for leptons and radiation." << std::endl;
      vector<unsigned int> daughters = get_daughters(p, nGenPart, GenPart_genPartIdxMother);

      //check for radiation and leptons
      for (unsigned int j = 0; j < daughters.size(); j++){
	      int dID = GenPart_pdgId[daughters[j]];
	      if(abs(dID) == abs(id)) {hasRadiation = true;} //check for radiation
	      else if(abs(dID) == 24 || abs(dID) == 23) { //check t->Wb->leptons and H->WW->leptons, check H->ZZ->leptons
	        vector<unsigned int>granddaughters = get_daughters(daughters[j], nGenPart, GenPart_genPartIdxMother);
	        if(abs(GenPart_pdgId[granddaughters[0]]) > 10 && abs(GenPart_pdgId[granddaughters[0]]) < 17) {hasLepton = true;}
	        if(abs(GenPart_pdgId[granddaughters[1]]) > 10 && abs(GenPart_pdgId[granddaughters[1]]) < 17) {hasLepton = true;}

	      }
	      else if(abs(dID) > 10 && abs(dID) < 17) {hasLepton = true;}
      }

      //if(hasRadiation || hasLepton || GenPart_pt[p] < 175) {
      //	      std::cout << "\t \t Particle either has radiation, a lepton, or is too soft. skip this one." << std::endl;
      //      continue;
      //}
      
      //skip this particle if...
      if(hasRadiation) {
	std::cout << "Particle has radiation" << std::endl; continue;}
      if(hasLepton) {
	std::cout << "Particle has lepton" << std::endl; continue;}
      if(GenPart_pt[p] < 175) {
	std::cout << "Particle too soft, pt = " << GenPart_pt[p] << std::endl; continue;}
      
      vector<unsigned int> siblings = get_daughters(GenPart_genPartIdxMother[p], nGenPart, GenPart_genPartIdxMother);
      
      if(abs(id) == 24) { //if W
	std::cout << "\t particle is a W, will now investigate the dR." << std::endl;
	
	float dR = 1000;

	//find topmost mother of a repeating chain
	while(GenPart_genPartIdxMother[p] != -1 && abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 24) {p = GenPart_genPartIdxMother[p];}

	if(abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 6) { //dRWB
	  //dr btwn current particle and its sibling
	  dR = (GenPart_eta[p], GenPart_eta[siblings[1]], GenPart_phi[p], GenPart_phi[siblings[1]]);
	  
	  if(abs(GenPart_pdgId[siblings[1]]) == 24) {
	    dR = DeltaR(GenPart_eta[p], GenPart_eta[siblings[0]], GenPart_phi[p], GenPart_phi[siblings[0]]);}
	  
	}else if(abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 25){ //dRWW
	  if(GenPart_pdgId[p]*GenPart_pdgId[siblings[0]] > 0) {
	    dR = DeltaR(GenPart_eta[p], GenPart_eta[siblings[1]], GenPart_phi[p], GenPart_phi[siblings[1]]); 
	  }else{
	    dR = DeltaR(GenPart_eta[p], GenPart_eta[siblings[0]], GenPart_phi[p], GenPart_phi[siblings[0]]);
	  }
	}

	std::cout << "\t \t dR = " << dR << std::endl;
	
	if(dR < 0.8) continue; 
      } //end of if W
      
      if(abs(id) == 23) { //if Z
	float dRZZ = 1000;

	std::cout << "\t particle is a Z, will now investigate the dR." << std::endl;

	//find topmost mother of a repeating chain
	while(GenPart_genPartIdxMother[p] != -1 && abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 23) {p = GenPart_genPartIdxMother[p];}
	
	if(abs(GenPart_genPartIdxMother[p]) == 25) {
	  float dr = 1000;
	  if(GenPart_pdgId[p]*GenPart_pdgId[siblings[0]] > 0) {
	    dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[1]], GenPart_phi[p], GenPart_phi[siblings[1]]); 
	  }else{
	    dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[0]], GenPart_phi[p], GenPart_phi[siblings[0]]);
	  }
	  if(dr < dRZZ) dRZZ = dr;
	}
	std::cout << "\t \t dR = " << dRZZ << std::endl;
	if(dRZZ < 0.8) continue; // Z from merged H
      }
      
      if(daughters.size() < 2) {
	std::cout << daughters.size() << " daughters from " << GenPart_pdgId[p] << std::endl;
	continue;
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

        d2Status.push_back(-99);
        d2ID.push_back(-99);
        d2Pt.push_back(-99.9);
        d2Eta.push_back(-99.9);
        d2Phi.push_back(-99.9);
        d2M.push_back(-99.9);

      }else{ //if is t
	//Can mess around with value if needed
	unsigned int W = 1000;
	unsigned int b = 1000;
	
	if(abs(GenPart_pdgId[daughters[0]]) == 24) {
	  W = daughters[0];
	  b = daughters[1];
	  std::cout << "\t W is 0th daughter: " << GenPart_pdgId[W] << ", b is: " << GenPart_pdgId[b] << std::endl;
	}else{
	  W = daughters[1];
	  b = daughters[0];
	  std::cout <<  "\t W is 1st daughter: " << GenPart_pdgId[W] << ", b is: " << GenPart_pdgId[b] << std::endl;
	}
	
	vector<unsigned int> W_daughters = get_daughters(W, nGenPart, GenPart_genPartIdxMother);
	
	while(W_daughters.size() == 1) {
	  W = W_daughters[0];
	  W_daughters = get_daughters(W, nGenPart, GenPart_genPartIdxMother);
	  std::cout << ".";
	}
	if(GenPart_pdgId[W_daughters[0]] == 22 || GenPart_pdgId[W_daughters[1]] == 22) {
	  std::cout << "\t \t W has a photon daughter" << std::endl;
	}

	while(W_daughters.size() == 1){
	  W = W_daughters[0];
	  W_daughters = get_daughters(W, nGenPart, GenPart_genPartIdxMother);
	  std::cout << ".";
	}
	if(GenPart_pdgId[W_daughters[1]] == 22) W = W_daughters[0];

	while(W_daughters.size() == 1) {
	  W = W_daughters[0];
	  W_daughters = get_daughters(W, nGenPart, GenPart_genPartIdxMother);
	  std::cout << ".";
	}
	std::cout << std:: endl;
	if(GenPart_pdgId[W_daughters[1]] == 22) std::cout << "Weird W to photon decay happening..." << std::endl;	
 
	std::cout <<  "\t W is 1st daughter: " << GenPart_pdgId[W] << ", b is: " << GenPart_pdgId[b] << std::endl;

       	d0Status.push_back(GenPart_status[b]);
	d0ID.push_back(GenPart_pdgId[b]);
	d0Pt.push_back(GenPart_pt[b]);
	d0Eta.push_back(GenPart_eta[b]);
	d0Phi.push_back(GenPart_phi[b]);
	d0M.push_back(GenPart_mass[b]);

	//std::cout << "\t \t b has been assigned" << std::endl;
	std::cout << "\t \t Now assigning W daughters: " << GenPart_pdgId[W_daughters[0]] << ", " << GenPart_pdgId[W_daughters[1]] << std::endl;
	
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

  RVec<float> fatjet_truth;
  RVec<float> fatjet_matchedPt;\

  std::cout << "===================== True Particle Candidates ====================" << std::endl;
  std::cout << pID << std::endl;


  std::cout << "===================== Investigating " << gcFatJet_pt.size() << " fatJets ====================" << std::endl;
  for(unsigned int i = 0; i < gcFatJet_pt.size(); i++){
    TLorentzVector fatjet, truePart, d0, d1, d2;
    
    fatjet.SetPtEtaPhiM(gcFatJet_pt[i], gcFatJet_eta[i], gcFatJet_phi[i], gcFatJet_M[i]);
    std::cout << "fatjet " << i << std::endl;
    float minDR = 1000;
    float matchedPt= -99;
    int matchedID = 0;
    bool isWmatched = false;
    bool isHmatched = false;
    bool isZmatched = false;
    bool isTmatched = false;
    bool isJmatched = false;
    bool isBmatched = false;

    for(unsigned int j = 0; j < pPt.size(); j++){
      truePart.SetPtEtaPhiM(pPt[j], pEta[j], pPhi[j], pM[j]);

      if(fatjet.DeltaR(truePart) < minDR) {
	std::cout << "\t fatjet DeltaR with truePart " << j << " = " << fatjet.DeltaR(truePart) << std::endl;
	minDR = fatjet.DeltaR(truePart);
	matchedPt = pPt[j];
	matchedID = abs(pID[j]);
	d0.SetPtEtaPhiM(d0Pt[j], d0Eta[j], d0Phi[j], d0M[j]);
	d1.SetPtEtaPhiM(d1Pt[j], d1Eta[j], d1Phi[j], d1M[j]);
	d2.SetPtEtaPhiM(d2Pt[j], d2Eta[j], d2Phi[j], d2M[j]);
	std::cout << "\t Succesfully initialized daughter TLorentz Vecs" << std::endl;
      }
    }
    
    bool WallDsInJet = false;
    bool TallDsInJet = false;
    if(matchedID != 6 && fatjet.DeltaR(d0) < 0.8 && fatjet.DeltaR(d1) < 0.8) WallDsInJet = true;
    if(matchedID == 6 && fatjet.DeltaR(d0) < 0.8 && fatjet.DeltaR(d1) < 0.8 && fatjet.DeltaR(d2) < 0.8) TallDsInJet = true;
    if(minDR < 0.8 && matchedID == 24 && WallDsInJet) isWmatched = true;
    if(minDR < 0.8 && matchedID == 25 && WallDsInJet) isHmatched = true;
    if(minDR < 0.8 && matchedID == 23 && WallDsInJet) isZmatched = true;
    if(minDR < 0.8 && matchedID == 6  && TallDsInJet) isTmatched = true;
    
    if(isWmatched || isZmatched || isHmatched || isTmatched) {
      std::cout << "\t Found a match for the fatjet: W - " << isWmatched << ", H - " << isHmatched << ", Z - " << isZmatched << ", t - " << isTmatched << std::endl;
	fatjet_matchedPt.push_back(matchedPt);
    }else{
      std::cout << "\t did not find a match for the fatjet" << std::endl;
      fatjet_matchedPt.push_back(-99.9);
    
    if(not (isWmatched && matchedPt > 200) && not (isZmatched && matchedPt > 200) && not (isTmatched && matchedPt > 400) && not (isHmatched && matchedPt > 300)) {
      std::cout << "\t matchedPt (" << matchedPt << ") does not meet requirements. Investigating subjets" << std::endl;
      int firstsub = gcFatJet_subj_idx1[i];
      int secondsub = gcFatJet_subj_idx2[i];
      
      if(firstsub > -1) {
	std::cout << "\t \t first subjet hadron flavour is: "<< int(SubJet_hadronFlavour[firstsub]) << std::endl;
	if(int(SubJet_hadronFlavour[firstsub]) == 5) isBmatched = true;}
      if(secondsub > -1) {
	std::cout << "\t \t second subjet hadron flavour is: "<< int(SubJet_hadronFlavour[secondsub]) << std::endl;
	if(int(SubJet_hadronFlavour[secondsub]) == 5) isBmatched = true;}
      
      if(not isBmatched) {
	std::cout << "\t \t \t jet is light quarks." << std::endl;
	isJmatched = true;
      }else{
	std::cout << "\t \t \t jet is b matched" << std::endl;
      }
    }

    if(isJmatched) fatjet_truth.push_back(0);
    if(isTmatched && matchedPt > 400) fatjet_truth.push_back(6);
    if(isHmatched && matchedPt > 300) fatjet_truth.push_back(25);
    if(isZmatched && matchedPt > 200) fatjet_truth.push_back(23);
    if(isWmatched && matchedPt > 200) fatjet_truth.push_back(24);
    if(isBmatched) fatjet_truth.push_back(5);

    fatjet_matchedPt.push_back(matchedPt);
    }
  }
  std::cout << "=============== Done with FatJets =================" << std::endl << std::endl << std::endl;
  //RVec<RVec<float>> gcFatJetTruth = {fatjet_truth, fatjet_matchedPt};
  //return gcFatJetTruth;
  return fatjet_truth;
}


  



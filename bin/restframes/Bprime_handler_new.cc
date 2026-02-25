#include "include/RestFramesHandler.hh"

#include "TLorentzVector.h"
#include "TVector3.h"
#include "include/RestFrames.hh"
#include <ROOT/RVec.hxx>
#include <algorithm>
#include <iostream>
//#include <array> //TODO think about replacing std::array<float, 4> with RVec<float>?
#include <memory>
#include <mutex>
#include <random>

using namespace RestFrames;
using namespace ROOT::VecOps;

class Bprime_RestFrames_Handler_new : public RestFramesHandler {
    private:

        // Reconstruction frames
        std::unique_ptr<DecayRecoFrame> BBbar;
        std::unique_ptr<DecayRecoFrame> B;
        std::unique_ptr<DecayRecoFrame> Bbar;
        
	std::unique_ptr<DecayRecoFrame> tau11;
	std::unique_ptr<DecayRecoFrame> tau12;
        std::unique_ptr<VisibleRecoFrame> b1;
	
	std::unique_ptr<DecayRecoFrame> tau21;
	std::unique_ptr<DecayRecoFrame> tau22;
        std::unique_ptr<VisibleRecoFrame> b2;

        std::unique_ptr<VisibleRecoFrame> l11;
        std::unique_ptr<InvisibleRecoFrame> nu11;
        
	std::unique_ptr<VisibleRecoFrame> l12;
	std::unique_ptr<InvisibleRecoFrame> nu12;

        std::unique_ptr<VisibleRecoFrame> l21;
        std::unique_ptr<InvisibleRecoFrame> nu21;
        
	std::unique_ptr<VisibleRecoFrame> l22;
        std::unique_ptr<InvisibleRecoFrame> nu22;

        // Groups
        std::unique_ptr<CombinatoricGroup> JETS;
	std::unique_ptr<CombinatoricGroup> LEPS; // TODO: Implement from example

        std::unique_ptr<InvisibleGroup> INV;
        
        // Jigsaws
	std::unique_ptr<SetMassInvJigsaw> NuNuM;	// TODO: Update
	std::unique_ptr<SetRapidityInvJigsaw> NuNuR;	// TODO: Update
	//std::unique_ptr<MinMassDiffInvJigsaw> MinDeltaMt;
        std::unique_ptr<ContraBoostInvJigsaw> MinMB;	// TODO:
	
	//std::unique_ptr<MinMassChi2CombJigsaw> MinChi2;
	std::unique_ptr<MinMassesCombJigsaw> MinMll;	// TODO
	std::unique_ptr<MinMassesCombJigsaw> MinMllb;	// TODO
	//std::unique_ptr<MinMassDiffCombJigsaw> MinDiffJets;

	
	std::unique_ptr<MinMassesSqInvJigsaw> MinMTau1;	// TODO
	std::unique_ptr<MinMassesSqInvJigsaw> MinMTau2;	// TODO:

	void define_tree() override;
	void define_groups_jigsaws() override;

    public:
        Bprime_RestFrames_Handler_new();
	// TODO: Update function instantiation
        RVec<double> calculate_doubles(TLorentzVector &lepton1, TLorentzVector &lepton2, TLorentzVector &lepton3, TLorentzVector &lepton4, TVector3 &met3, TLorentzVector &jet1, TLorentzVector &jet2); //, TLorentzVector &jet4);
	//std::tuple<float,float>
	
	RVec<TLorentzVector> calculate_vecs();
};

Bprime_RestFrames_Handler_new::Bprime_RestFrames_Handler_new() {
    initialize();
};

void Bprime_RestFrames_Handler_new::define_tree() {
	//std::cout << "\n\n\nDefine Tree Start\n\n\n";
	
	LAB.reset(new LabRecoFrame("LAB","LAB"));
    	BBbar.reset(new DecayRecoFrame("BBbar", "B#bar{B}"));
    	LAB->AddChildFrame(*BBbar);

    	// Vector Like B quark particle production
    	B.reset(new DecayRecoFrame("B", "B"));
    	BBbar->AddChildFrame(*B);

    	// B -> b1 tau11 tau12
    	b1.reset(new VisibleRecoFrame("b1","b1"));
    	tau11.reset(new DecayRecoFrame("tau11", "tau11"));
	tau12.reset(new DecayRecoFrame("tau12", "tau12"));
    	B->AddChildFrame(*b1);
    	B->AddChildFrame(*tau11);
	B->AddChildFrame(*tau12);

    	// tau11 -> l11 nu11
    	l11.reset(new VisibleRecoFrame("l11", "#it{l11}"));
    	nu11.reset(new InvisibleRecoFrame("nu", "#nu 11"));
    	tau11->AddChildFrame(*l11);
    	tau11->AddChildFrame(*nu11);
    	
	// tau12 -> l12 nu12
    	l12.reset(new VisibleRecoFrame("l12", "#it{l12}"));
    	nu12.reset(new InvisibleRecoFrame("nu", "#nu 12"));
    	tau12->AddChildFrame(*l12);
    	tau12->AddChildFrame(*nu12);
    	
	// Vector Like Bbar Quark particle production	
    	Bbar.reset(new DecayRecoFrame("Bbar", "#bar{B}"));
    	BBbar->AddChildFrame(*Bbar);
	
    	// Bbar -> b2 tau21 tau22
    	b2.reset(new VisibleRecoFrame("b2","b2"));
    	tau21.reset(new DecayRecoFrame("tau21", "tau21"));
	tau22.reset(new DecayRecoFrame("tau22", "tau22"));
    	Bbar->AddChildFrame(*b2);
    	Bbar->AddChildFrame(*tau21);
	Bbar->AddChildFrame(*tau22);

	// tau21 -> l21 nu21
    	l21.reset(new VisibleRecoFrame("l21", "#it{l21}"));
    	nu21.reset(new InvisibleRecoFrame("nu", "#nu 21"));
    	tau21->AddChildFrame(*l21);
    	tau21->AddChildFrame(*nu21);
	
	// tau22 -> l22 nu22
    	l22.reset(new VisibleRecoFrame("l22", "#it{l22}"));
    	nu22.reset(new InvisibleRecoFrame("nu", "#nu 22"));
    	tau22->AddChildFrame(*l22);
    	tau22->AddChildFrame(*nu22);

	//std::cout << "\n\n\nDefine Tree end\n\n\n";
}

void Bprime_RestFrames_Handler_new::define_groups_jigsaws() {
    //std::cout << "\n\n\ndefine_groups_jigsaws start\n\n\n";
    // Combinatoric Group for jets
    JETS.reset(new CombinatoricGroup("JETS", "Jet Jigsaws"));
    JETS->AddFrame(*b1);
    JETS->AddFrame(*b2);

    // jet frames must have at least one element
    JETS->SetNElementsForFrame(*b1, 1);
    JETS->SetNElementsForFrame(*b2, 1);
    
    // Combinatoric Group for Leptons TODO
    LEPS.reset(new CombinatoricGroup("LEPS", "Lep Jigsaws"));
    LEPS->AddFrame(*l12);
    LEPS->AddFrame(*l22);

    // jet frames must have at least one element
    LEPS->SetNElementsForFrame(*l12, 1);
    LEPS->SetNElementsForFrame(*l22, 1);
    
    // Invisible Group for Neutrino
    INV.reset(new InvisibleGroup("INV", "MET Jigsaws"));
    INV->AddFrame(*nu11);
    INV->AddFrame(*nu12);
    INV->AddFrame(*nu21);
    INV->AddFrame(*nu22);

    // -------------------- Define Jigsaws for reconstruction trees --------------
    std::string jigsaw_name;

    // 1 Minimize difference Mt jigsaws                not: Minimize equal (vector) top masses neutrino jigsaws
    jigsaw_name = "M_{4 #nu} = f(4 #it{l})";
    NuNuM.reset(new SetMassInvJigsaw("NuNuM", jigsaw_name));
    INV->AddJigsaw(*NuNuM); 
    
    // 2 
    jigsaw_name = "#eta_{4 #nu} = #eta_{4 #it{l}}";
    NuNuR.reset(new SetRapidityInvJigsaw("NuNuR", jigsaw_name));
    INV->AddJigsaw(*NuNuR);
    //NuNuR->AddVisibleFrame(*b1); 
    NuNuR->AddVisibleFrame(*l11); 
    NuNuR->AddVisibleFrame(*l12); 
    //NuNuR->AddVisibleFrame(*b2); 
    NuNuR->AddVisibleFrame(*l21); 
    NuNuR->AddVisibleFrame(*l22); 
    //+*b+*Tbar);	//TODO not sure about this line

    // 3

    jigsaw_name = "min M_{B}, M_{B} = M_{Bbar}";
    MinMB.reset(new ContraBoostInvJigsaw("MinMB", jigsaw_name));
    INV->AddJigsaw(*MinMB);
    
    MinMB->AddVisibleFrames(B->GetListVisibleFrames(), 0);
    MinMB->AddVisibleFrames(Bbar->GetListVisibleFrames(), 1);
    MinMB->AddInvisibleFrames(B->GetListInvisibleFrames(), 0);
    MinMB->AddInvisibleFrames(Bbar->GetListInvisibleFrames(), 1);

    // 4 MinMTau1->

    jigsaw_name = "min M_{#tau_{1}}, M_{#tau_{11}} = M_{#tau_{12}}";
    MinMTau1.reset(new MinMassesSqInvJigsaw("MinMTau1", jigsaw_name, 2));
    INV->AddJigsaw(*MinMTau1);
    
    MinMTau1->AddVisibleFrames(tau11->GetListVisibleFrames(), 0);
    MinMTau1->AddVisibleFrames(tau12->GetListVisibleFrames(), 1);
    MinMTau1->AddInvisibleFrames(tau11->GetListInvisibleFrames(), 0);
    MinMTau1->AddInvisibleFrames(tau12->GetListInvisibleFrames(), 1);
    MinMTau1->AddMassFrame(*l21, 0);
    MinMTau1->AddMassFrame(*l22, 0);
    
    //

    jigsaw_name = "min M_{#tau_{2}}, M_{#tau_{21}} = M_{#tau_{22}}";
    MinMTau2.reset(new MinMassesSqInvJigsaw("MinMTau2", jigsaw_name, 2));
    INV->AddJigsaw(*MinMTau2);
    
    MinMTau2->AddVisibleFrames(tau21->GetListVisibleFrames(), 0);
    MinMTau2->AddVisibleFrames(tau22->GetListVisibleFrames(), 1);
    MinMTau2->AddInvisibleFrames(tau21->GetListInvisibleFrames(), 0);
    MinMTau2->AddInvisibleFrames(tau22->GetListInvisibleFrames(), 1);
    MinMTau2->AddMassFrame(*l11, 0);
    MinMTau2->AddMassFrame(*l12, 0);

    //
    jigsaw_name = "min M_{ll}";
    MinMll.reset(new MinMassesCombJigsaw("MinMll", jigsaw_name));

    LEPS->AddJigsaw(*MinMll);
    MinMll->AddCombFrame(*l12, 0);
    MinMll->AddCombFrame(*l22, 1);
    MinMll->AddObjectFrames(*l11+*l12, 0);
    MinMll->AddObjectFrames(*l21+*l22, 1);
    
    //
    jigsaw_name = "min M_{llb}";
    MinMllb.reset(new MinMassesCombJigsaw("MinMllb", jigsaw_name));

    JETS->AddJigsaw(*MinMllb);
    MinMllb->AddCombFrame(*b1, 0);
    MinMllb->AddCombFrame(*b2, 1);
    MinMllb->AddObjectFrames(*l11+*l12+*b1, 0);
    MinMllb->AddObjectFrames(*l21+*l22+*b2, 1);
    
    // MinMassDiffInv was ok, not best
    /*jigsaw_name = "min ( M_{T}- M_{Tbar} )^{2}";
    MinDeltaMt.reset(new MinMassDiffInvJigsaw("MinDeltaMt", jigsaw_name, 2));
    INV->AddJigsaw(*MinDeltaMt);
    MinDeltaMt->AddInvisibleFrame(*nu, 0);
    //MinDeltaMt.AddInvisibleFrame(Nb_R4, 1);
    MinDeltaMt->AddVisibleFrames(*l+*b, 0);
    MinDeltaMt->AddVisibleFrame(*Tbar, 1); //OR *J0+*J1, 1) ???
    MinDeltaMt->AddMassFrame(*T, 0);
    MinDeltaMt->AddMassFrame(*Tbar, 1);
    //MinDeltaMt.AddMassFrame(Lb_R4, 1); //???
*/
    // 4 Combinatoric Jigsaws 
    // MinMassesSqCombJigsaw worked but same problem as MinMassesCombJigsaw
    // MinMassDiffCombJigsaw Initialized Analysis but fell into some infinite loop
    // MinMassChi2ComJigsaw works very well
    /*jigsaw_name = "Minimize Chi^2";
    MinChi2.reset(new MinMassChi2CombJigsaw("MinChi2", jigsaw_name, 2, 2));
    JETS->AddJigsaw(*MinChi2);
    MinChi2->AddObjectFrame(*l, 0);
    MinChi2->AddObjectFrame(*b, 0);
    MinChi2->AddCombFrame(*b, 0);
    MinChi2->AddObjectFrame(*Tbar, 1);
    MinChi2->AddCombFrame(*Tbar, 1);
    MinChi2->SetMass(1435, 0);
    MinChi2->SetSigma(205.2, 0);
    MinChi2->SetMass(1456, 1);
    MinChi2->SetSigma(173.2, 1); */ 

    // MinMassesCombJigsaw, combinatoric jigsaws for everything else...
/*    jigsaw_name = "Minimize M(b #it{l} ) , M(Tbar)"; //M(J0 J1 )
    
    MinMJets.reset(new MinMassesCombJigsaw("MinCombJets", jigsaw_name));
    JETS->AddJigsaw(*MinMJets);
    MinMJets->AddFrames(*l+*b,0);
    MinMJets->AddFrame(*Tbar,1);
*/

    /*
    // MinMassDiffCombJigsaw
    jigsaw_name = "min ( M_{T}- M_{Tbar} )^{2}";
  
    MinDiffJets.reset(new MinMassDiffCombJigsaw("MinDiffJets", jigsaw_name, 2, 1)); // last param is the # of object frames that need to be calculated.  2 doesn't work
    JETS->AddJigsaw(*MinDiffJets);
    MinDiffJets->AddObjectFrames(*l+*b, 0);
    MinDiffJets->AddCombFrame(*b, 0);
    MinDiffJets->AddObjectFrame(*Tbar, 1); 
    MinDiffJets->AddCombFrame(*Tbar, 1);
    */
    /*
    MinDiffJets->AddVisibleFrames(*l+*b, 0);
    MinDiffJets->AddVisibleFrame(*Tbar, 1); //OR *J0+*J1, 1) ???
    MinDiffJets->AddMassFrame(*T, 0);
    MinDiffJets->AddMassFrame(*Tbar, 1);
    */
    //std::cout << "\n\n\ndefine_groups_jigsaws end\n\n\n";
};

RVec<double> Bprime_RestFrames_Handler_new::calculate_doubles(TLorentzVector &lepton1, TLorentzVector &lepton2, TLorentzVector &lepton3, TLorentzVector &lepton4, TVector3 &met3, TLorentzVector &jet1, TLorentzVector &jet2) { //, TLorentzVector &jet4) {
    
    //std::cout << "\n\n\ncalculate_doubles start\n\n\n";

    before_analysis();
    
    //std::cout << "\n\n\n\tbefore_analysis(); DONE\n\n\n";

    INV->SetLabFrameThreeVector(met3);	
    l11->SetLabFrameFourVector(lepton1);	// Negative Lepton
    l21->SetLabFrameFourVector(lepton3);	// Negative Lepton

    //std::cout << "\n\n\n\tmet3, l1, and l3 LabFrameFourVectors set\n\n\n";

    std::vector<RFKey> JETS_ID; // ID for tracking jets in tree
    JETS_ID.push_back(JETS->AddLabFrameFourVector(jet1));
    JETS_ID.push_back(JETS->AddLabFrameFourVector(jet2));
    //b->SetLabFrameFourVector(jet4));
    
    //std::cout << "\n\n\n\tJETS_ID.push_back(jet 1 and 2); DONE\n\n\n";

    std::vector<RFKey> LEPS_ID; // ID for tracking antileptons in tree
    LEPS_ID.push_back(LEPS->AddLabFrameFourVector(lepton2));
    LEPS_ID.push_back(LEPS->AddLabFrameFourVector(lepton4));
     
    //std::cout << "\n\n\n\tLEPS_ID.push_back(lepton 2 and 4); DONE\n\n\n";

    LAB->AnalyzeEvent(); // analyze the event

    //std::cout << "\n\n\n\tAnalyzeEvent(); DONE";

    RVec<double> observables; // = {BBbar_mass, BBar...,B_mass};

    observables.push_back(BBbar->GetMass());
    observables.push_back(BBbar->GetCosDecayAngle());
    observables.push_back(BBbar->GetDeltaPhiDecayAngle());
    
    //std::cout << "\n\n\n\tobservables.push_back(BBbar); DONE\n\n\n";

    observables.push_back(B->GetMass());
    observables.push_back(B->GetCosDecayAngle());
    observables.push_back(B->GetDeltaPhiDecayAngle());
    
    //std::cout << "\n\n\n\tobservables.push_back(B); DONE\n\n\n";

    observables.push_back(Bbar->GetMass());
    observables.push_back(Bbar->GetCosDecayAngle());
    observables.push_back(Bbar->GetDeltaPhiDecayAngle());
    
    //std::cout << "\n\n\n\tobservables.push_back(Bbar); DONE\n\n\n";

    observables.push_back(tau11->GetMass());
    observables.push_back(tau12->GetMass());
    observables.push_back(tau21->GetMass());
    observables.push_back(tau22->GetMass());

    //std::cout << "\n\n\n\tobservables.push_back(taus); DONE\n\n\n";

    observables.push_back(BBbar->GetDeltaPhiVisible());
    observables.push_back(BBbar->GetDeltaPhiDecayVisible());
    observables.push_back(BBbar->GetDeltaPhiBoostVisible());
    observables.push_back(BBbar->GetVisibleShape());
    
    //std::cout << "\n\n\n\tobservables.push_back(more BBbar); DONE\n\n\n";

  //observables.push_back(b->GetDeltaPhiDecayAngle());		DON'T GET this, doesn't work, ERRORS
//wasn't able to save any l nor nu things

    //TODO moved? after_analysis();

    /*std::default_random_engine generator;
    std::bernoulli_distribution dist(0.5);
    bool which = dist(generator);
    
    if (which) return std::make_tuple(calc_mass_Tbar, calc_mass_T); */
    
    after_analysis();
    
    //std::cout << "\n\n\ncalculate_doubles about to return\n\n\n";
    return observables; //std::make_tuple(calc_mass_T, calc_mass_Tbar);
};

// calculate_vecs() returns all the important four vectors of the frames in the tree
RVec<TLorentzVector> Bprime_RestFrames_Handler_new::calculate_vecs() {
    std::cout << "\n\n\nccalculate_vecs start\n\n\n";
    RVec<TLorentzVector> observables;
    //TODO UPDATE
    observables.push_back(BBbar->GetFourVector());
    
    observables.push_back(B->GetFourVector());
    observables.push_back(B->GetFourVector(*BBbar));
    
    observables.push_back(Bbar->GetFourVector());
    observables.push_back(Bbar->GetFourVector(*BBbar));
    
    observables.push_back(tau11->GetFourVector());
    observables.push_back(tau11->GetFourVector(*BBbar));
    observables.push_back(tau11->GetFourVector(*B));
    
    observables.push_back(b1->GetFourVector());
    observables.push_back(b1->GetFourVector(*BBbar));
    observables.push_back(b1->GetFourVector(*B));
    
    // no 4vecs for l and nu because it didn't work 

    after_analysis();
    
    //std::cout << "\n\n\ncalculate_vecs about to return\n\n\n";
    return observables;
};


// Thread index can stay the same
// lepton: float -> RVec<float>
// MET_ptcorr, MET_phicorr
// gcBJet_...
// Also need charge information (Good4Lepton_charge) passed in
class Bprime_RestFrames_Container_new : public RestFramesContainer {
    public:
        Bprime_RestFrames_Container_new(int num_threads);
        RestFramesHandler *create_handler() override;

	RVec<double> return_doubles(int thread_index, RVec<float> lepton_pt, RVec<float> lepton_eta, RVec<float> lepton_phi, RVec<float> lepton_mass, RVec<float> lepton_charge, RVec<float> bjet_pt, RVec<float> bjet_eta, RVec<float> bjet_phi, RVec<float> bjet_mass, float met_pt, float met_phi);
	
	RVec<TLorentzVector> return_vecs(int thread_index);
};

Bprime_RestFrames_Container_new::Bprime_RestFrames_Container_new (int num_threads) : RestFramesContainer(num_threads){
    initialize();
};

RestFramesHandler * Bprime_RestFrames_Container_new::create_handler() {
    return new Bprime_RestFrames_Handler_new;
}

// return_doubles() returns all the masses, cos angles, and deltaPhi angles of the frames in the tree
RVec<double> Bprime_RestFrames_Container_new::return_doubles(int thread_index, RVec<float> lepton_pt, RVec<float> lepton_eta, RVec<float> lepton_phi, RVec<float> lepton_mass, RVec<float> lepton_charge, RVec<float> bjet_pt, RVec<float> bjet_eta, RVec<float> bjet_phi, RVec<float> bjet_mass, float met_pt, float met_phi) {
  //std::cout << "\n\n\nreturn_doubles start\n\n\n";
    
  // TODO: return nonsense observables if only 3 leptons
  if (lepton_pt.size() <= 3) {
    RVec<double> nonsense = {-999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0};
    return nonsense;
  }

  // This pointer should explicitly not be deleted!
  Bprime_RestFrames_Handler_new *rfh = static_cast<Bprime_RestFrames_Handler_new *>(get_handler(thread_index));
  
  TLorentzVector bjet_1;
  TLorentzVector bjet_2;
  
  TLorentzVector lepton1;	// Negative
  TLorentzVector lepton2;
  TLorentzVector lepton3;	// Negative
  TLorentzVector lepton4;
  
  TVector3 met3;
  
  //std::cout << "\n\n\nAbout to loop over leptons\nLength of Lepton Charge: " << lepton_charge.size() << std::endl;    
  // Loop over lepton charge
  // Find positive and negative leptons
  int pos_leptons[2] = {-1, -1};
  int neg_leptons[2] = {-1, -1};
  int size = lepton_charge.size();
  for (int i = 0; i < size; i++) {
    if (lepton_charge[i] < 0) {
      if (neg_leptons[0] == -1) neg_leptons[0] = i;
      else if (neg_leptons[1] == -1) neg_leptons[1] = i;
      //else std::cout << "More than 2 negative leptons" << std::endl;
    } else {
      if (pos_leptons[0] == -1) pos_leptons[0] = i;
      else if (pos_leptons[1] == -1) pos_leptons[1] = i;
      //else std::cout << "More than 2 positive leptons" << std::endl;
    }
  }
  
  if (pos_leptons[0] < 0 || pos_leptons[1] < 0 || neg_leptons[0] < 0 || neg_leptons[1] < 0) {
    RVec<double> nonsense = {-999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0, -999.0};
    return nonsense;
  }
  
  lepton1.SetPtEtaPhiM(lepton_pt[neg_leptons[0]], lepton_eta[neg_leptons[0]], lepton_phi[neg_leptons[0]], lepton_mass[neg_leptons[0]]);  
  lepton2.SetPtEtaPhiM(lepton_pt[pos_leptons[0]], lepton_eta[pos_leptons[0]], lepton_phi[pos_leptons[0]], lepton_mass[pos_leptons[0]]);  
  lepton3.SetPtEtaPhiM(lepton_pt[neg_leptons[1]], lepton_eta[neg_leptons[1]], lepton_phi[neg_leptons[1]], lepton_mass[neg_leptons[1]]); 
  lepton4.SetPtEtaPhiM(lepton_pt[pos_leptons[1]], lepton_eta[pos_leptons[1]], lepton_phi[pos_leptons[1]], lepton_mass[pos_leptons[1]]);
  
  //std::cout << "Done with Leptons" << std::endl;
  
  bjet_1.SetPtEtaPhiM(bjet_pt[0], bjet_eta[0], bjet_phi[0], bjet_mass[0]);
  bjet_2.SetPtEtaPhiM(bjet_pt[1], bjet_eta[1], bjet_phi[1], bjet_mass[1]);
  
  double MET_px  = met_pt*std::cos(met_phi);
  double MET_py  = met_pt*std::sin(met_phi);
  met3  = TVector3(MET_px, MET_py, 0.0);
  
  //std::cout << "\n\n\n\tin return_doubles, about to call calculate_doubles\n\n\n" << std::endl;
  
  RVec<double> observables = rfh->calculate_doubles(lepton1, lepton2, lepton3, lepton4, met3, bjet_1, bjet_2); 
  //std::cout << "\n\n\nin return_doubles, about to return\n\n" << std::endl;
  return observables;
}


// return_vecs() returns all the four vectors/TLorentzVectors of the frames in the tree
RVec<TLorentzVector> Bprime_RestFrames_Container_new::return_vecs(int thread_index) {
  // This pointer should explicitly not be deleted!
  //std::cout << "\n\n\nin return_vecs, about to get the handler\n\n\n" << std::endl;
  Bprime_RestFrames_Handler_new *rfh = static_cast<Bprime_RestFrames_Handler_new *>(get_handler(thread_index));
  //std::cout << "\n\n\nin return_vecs, about to call calculates_vecs\n\n" << std::endl;
  return rfh->calculate_vecs();
  //std::cout << "\n\n\ndone with calculate vecs\n\n" << std::endl;
}

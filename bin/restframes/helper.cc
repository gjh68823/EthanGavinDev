 // processDecayTree(), returnVectors()
// These two functions help to differentiate between the bW and (H/Z)t trees
#include <iostream>

// TODO: UPDATE
RVec<double> processDecayTree(Bprime_RestFrames_Container_new * B_rfc, int thread_index, float lepton_pt, float lepton_eta, float lepton_phi, float lepton_mass, RVec<float> fatjet_pt, RVec<float> fatjet_eta, RVec<float> fatjet_phi, RVec<float> fatjet_mass, RVec<float> fatjet_DeepFlav, float met_pt, float met_phi, RVec<float> jet_pt, RVec<float> jet_eta, RVec<float> jet_phi, RVec<float> jet_mass, RVec<float> jet_DeepFlav, RVec<float> isoAK4) {
  RVec<double> result;
  result = B_rfc->return_doubles(thread_index, lepton_pt, lepton_eta, lepton_phi, lepton_mass, fatjet_pt, fatjet_eta, fatjet_phi, fatjet_mass, fatjet_DeepFlav, met_pt, met_phi);
  return result;
}
/*
RVec<TLorentzVector> returnVectors(Tprime_RestFrames_Container_W * W_rfc, Tprime_RestFrames_Container_t * t_rfc, int thread_index, RVec<float> jet_DeepFlav, RVec<float> isoAK4) {
  int i = isoAK4.size(); //0;
  //for (; (isoAK4[i] != 1 || jet_DeepFlav[i] <= 0.9) && i < isoAK4.size(); i++); // find the first stand alone ak4 b-tagged jet
  
  RVec<TLorentzVector> result;
  if (i == isoAK4.size()) { // didn't find a good b jet so we're at the bW decay tree
    result = W_rfc->return_vecs(thread_index);
    //std::cout << "Returned W vectors " << std::endl;
  } else { // we're at the (H/Z)t tree
    //std::cout << "whoops, at the t tree" << std::endl;
    result = t_rfc->return_vecs(thread_index);
  }
  return result;
}
*/

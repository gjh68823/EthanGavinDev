
CompileCpp("""
#include <cmath>

float calcMT(float lep_pt, float lep_phi, float met_pt, float met_phi) {
    float dphi = TVector2::Phi_mpi_pi(lep_phi - met_phi);
    return std::sqrt(2.0 * lep_pt * met_pt * (1.0 - std::cos(dphi)));
}

float deltaR(float eta1, float phi1, float eta2, float phi2) {
    float deta = eta1 - eta2;
    float dphi = TVector2::Phi_mpi_pi(phi1 - phi2);
    return std::sqrt(deta*deta + dphi*dphi);
}
""")
from TIMBER.Analyzer import *
from TIMBER.Tools.Common import *
import ROOT
from ROOT import TFile
import sys, os
import gc

gc.disable()

from TIMBER.Tools.RestFramesHandler import load_restframes
import correctionlib
correctionlib.register_pyroot_binding()

sys.path.append('../../')
sys.path.append('../../../')

# ------------------ Command Line Arguments and Parsing -------------------
inputFiles = sys.argv[1] #fileList
# Are all the files running if 0 and 8?
testNum1 = sys.argv[2]   #first file in the list to use
testNum2 = sys.argv[3]   #last file in the list to use
year = sys.argv[4]       #2022, 2022EE, 2023, 2023BPix

# Make the New .txt file from line testNum1 to testNum2 because TIMBER can handle .txt of .root's files
print(f"Input File Path: {inputFiles}")
with open(inputFiles) as fp:
  lines = fp.readlines()

start = int(testNum1)
end = int(testNum2)

print(f"TestNum 1: {start} and TestNum 2: {end}")

print("Adding files to trimmed_input.txt")
filelist = []
for i, line in enumerate(lines):
  if i in range(start,end+1):
    filelist.append(line.strip())
print(filelist)

print("Number of Entries:",len(filelist))
print("list contents:",filelist)
sampleName = filelist[0]
print(f"Sample Name: {sampleName}")

# Parse the incoming file names to assign labels
isSig = ("Bprime" in sampleName)
isMadgraphBkg = (("QCD" in sampleName) or ("madgraphMLM" in sampleName))
isTOP = (("Mtt" in sampleName) or ("ST" in sampleName) or ("ttZ" in sampleName) or ("ttW" in sampleName) or ("ttH" in sampleName) or ("TTTo" in sampleName))
isTT = (("TT_Tune" in sampleName) or ("Mtt" in sampleName) or ("TTTo" in sampleName))
isVV = (("WW_" in sampleName) or ("WZ_" in sampleName) or ("ZZ_" in sampleName))
isSM = ("Muon" in sampleName)
isSE = (("SingleElectron" in sampleName) or ("EGamma" in sampleName))
isMC = not (("Single" in sampleName) or ("Muon" in sampleName) or ("EGamma" in sampleName) or ("MuonEG" in sampleName) or ("Tau/" in sampleName))
dataset = int(-1)
if "MuonEG" in sampleName: dataset = 2
elif ("Muon" in sampleName) or ("Muon0" in sampleName) or ("Muon1" in sampleName): dataset = 1
elif ("EGamma" in sampleName) or ("EGamma0" in sampleName) or ("EGamma1" in sampleName): dataset = 3
elif "Tau/" in sampleName: dataset = 4


#'root://cms-xrd-global.cern.ch//store/data/Run2018A/SingleMuon/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v2/2550000/28FF17A8-95EB-FD41-A55B-2EFAF2D6AF91.root'
tokens = sampleName.split("/")
sample = tokens[7] # was 5
era = ''
ver = ''
if not isMC:
  runera = tokens[6] # was 4
  process = tokens[9] # was 7
  era = runera[-1] # last char
  print(process)
  ver = process[process.find('_')+1:process.find('_')+3]
del tokens

jecera = ''
if not isMC:
  jecera = era
  if year == '2022':
    jecera = 'CD'
  elif year == '2023':
    if(ver != 'v4'):
      jecera = 'Cv123'
    else:
      jecera = 'Cv4'

if isMC:
  if (("_ext1" in sampleName)): era = "ext1"
  if (("_ext2" in sampleName)): era = "ext2"
  if (("_ext3" in sampleName)): era = "ext3"

region = "Signal"
if isTT:
  region = "TTbar" # TPrimeTPrime or BPrimeBPrime
elif not isSig:
  region = "DataBkg"

print('============== RUN SETTINGS ===============')
print('isMC = ',isMC)
print('isSig = ',isSig)
print('sample = ',sample)
print('era = ',era)
print('jecera = ',jecera)
print('ver = ',ver)
print('region = ',region)
print('dataset = ', dataset)
def analyze(jesvar):
  ROOT.gInterpreter.ProcessLine('string jesvar = "' + jesvar + '"; ')

  # Create analyzer instance
  # is filelist still what you want it be here
  a = analyzer(filelist)
  # ─────────────────────────────────────────────
  # Trigger
  # ─────────────────────────────────────────────
  trigCuts = CutGroup("trigCuts")
  trigCuts.Add("HLT", "HLT_Mu17 == 1 || HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30 == 1")
  a.Apply(trigCuts)

  # ─────────────────────────────────────────────
  # Loose lepton definitions + counts
  # ─────────────────────────────────────────────
  eandmuVars = VarGroup("eandmuVars")
  eandmuVars.Add("looseMuons", "Muon_pt >= 15 && abs(Muon_eta) < 2.4 && Muon_looseId == 1 && abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5 && Muon_pfIsoId >= 2")
  eandmuVars.Add("looseElectrons", "Electron_pt > 10 && abs(Electron_eta) < 2.5 && Electron_mvaIso_WP90 == 1")
  eandmuVars.Add("nLooseMuons",     "Sum(looseMuons)")
  eandmuVars.Add("nLooseElectrons", "Sum(looseElectrons)")
  eandmuVars.Add("nLooseLeptons",   "nLooseMuons + nLooseElectrons")
  a.Apply(eandmuVars)

  # ─────────────────────────────────────────────
  # Single loose lepton veto
  # ─────────────────────────────────────────────
  lepVeto = CutGroup("lepVeto")
  lepVeto.Add("single_loose_lepton", "nLooseLeptons == 1")
  a.Apply(lepVeto)

  # ─────────────────────────────────────────────
  # Lepton kinematics
  # (safe to index [0] — exactly one lepton survives)
  # ─────────────────────────────────────────────
  lepVars = VarGroup("lepVars")
  lepVars.Add("isMuon",   "nLooseMuons == 1")
  lepVars.Add("lep_pt",   "isMuon ? Muon_pt  [looseMuons][0] : Electron_pt  [looseElectrons][0]")
  lepVars.Add("lep_eta",  "isMuon ? Muon_eta [looseMuons][0] : Electron_eta [looseElectrons][0]")
  lepVars.Add("lep_phi",  "isMuon ? Muon_phi [looseMuons][0] : Electron_phi [looseElectrons][0]")
  lepVars.Add("lep_mass", "isMuon ? Muon_mass[looseMuons][0] : Electron_mass[looseElectrons][0]")
  a.Apply(lepVars)

  # ─────────────────────────────────────────────
  # MET and mT
  # ─────────────────────────────────────────────
  metVars = VarGroup("metVars")
  metVars.Add("mT", "calcMT(lep_pt, lep_phi, MET_pt, MET_phi)")
  a.Apply(metVars)

  metCuts = CutGroup("metCuts")
  metCuts.Add("MET_cut", "MET_pt < 25.0")
  metCuts.Add("mT_cut",  "mT < 25.0")
  a.Apply(metCuts)

  # ─────────────────────────────────────────────
  # Jet mask + count
  # Lead-jet indexing is deferred until AFTER the
  # nGoodJets cut to avoid empty-vector segfaults
  # ─────────────────────────────────────────────
  jetMaskVars = VarGroup("jetMaskVars")
  jetMaskVars.Add("Jet_dR_lep", "ROOT::VecOps::Map(Jet_eta, Jet_phi, [&](float eta, float phi){ return deltaR(eta, phi, lep_eta, lep_phi); })")
  jetMaskVars.Add("goodJet_mask", "Jet_pt > 30.0 && Jet_jetId >= 2 && Jet_dR_lep > 1.0")
  jetMaskVars.Add("nGoodJets",    "Sum(goodJet_mask)")
  a.Apply(jetMaskVars)

  jetCuts = CutGroup("jetCuts")
  jetCuts.Add("jet_requirement", "nGoodJets >= 1")
  a.Apply(jetCuts)

  # Lead jet kinematics + Z veto variable
  leadJetVars = VarGroup("leadJetVars")
  leadJetVars.Add("jet0_pt",   "Jet_pt  [goodJet_mask][0]")
  leadJetVars.Add("jet0_eta",  "Jet_eta [goodJet_mask][0]")
  leadJetVars.Add("jet0_phi",  "Jet_phi [goodJet_mask][0]")
  leadJetVars.Add("jet0_mass", "Jet_mass[goodJet_mask][0]")
  leadJetVars.Add("lepJet_invM", "ROOT::VecOps::InvariantMass("
      "    ROOT::RVec<float>{lep_pt,   jet0_pt},"
      "    ROOT::RVec<float>{lep_eta,  jet0_eta},"
      "    ROOT::RVec<float>{lep_phi,  jet0_phi},"
      "    ROOT::RVec<float>{lep_mass, jet0_mass})")
  a.Apply(leadJetVars)

  zVeto = CutGroup("zVeto")
  zVeto.Add("Z_veto", "!(lepJet_invM > 81.1 && lepJet_invM < 101.1)")
  a.Apply(zVeto)

  # ─────────────────────────────────────────────
  # Tight ID definitions
  # LooseMu_isTight / LooseEl_isTight are already
  # sub-vectors filtered to loose candidates only,
  # so [0] gives the single surviving lepton's result
  # ─────────────────────────────────────────────
  tightVars = VarGroup("tightVars")
  tightVars.Add("LooseMu_isTight",
      "Muon_mediumId[looseMuons == true] == 1 && Muon_pfIsoId[looseMuons == true] >= 3")
  tightVars.Add("LooseEl_isTight",
      "Electron_mvaIso_WP90[looseElectrons == true] == 1")
  tightVars.Add("lepPassesTight",
      "isMuon ? (bool)LooseMu_isTight[0] : (bool)LooseEl_isTight[0]")
  a.Apply(tightVars)

  # ─────────────────────────────────────────────
  # Fake rate histograms
  # ─────────────────────────────────────────────
  pt_bins  = [10, 15, 20, 25, 30, 40, 50, 70, 100]
  eta_bins = [-2.5, -2.0, -1.5, -0.5, 0.5, 1.5, 2.0, 2.5]

  checkpoint = a.GetActiveNode()

  a.SetActiveNode(checkpoint)
  a.Cut("isMuon_den", "isMuon == true")
  hDen_mu = a.DataFrame.Histo2D(
      ("hDen_mu", "Muon fake rate denominator;p_{T} [GeV];#eta",
      len(pt_bins)-1,  ROOT.std.vector('double')(pt_bins),
      len(eta_bins)-1, ROOT.std.vector('double')(eta_bins)),
      "lep_pt", "lep_eta"
  )

  a.SetActiveNode(checkpoint)
  a.Cut("isEle_den", "isMuon == false")
  hDen_el = a.DataFrame.Histo2D(
      ("hDen_el", "Electron fake rate denominator;p_{T} [GeV];#eta",
      len(pt_bins)-1,  ROOT.std.vector('double')(pt_bins),
      len(eta_bins)-1, ROOT.std.vector('double')(eta_bins)),
      "lep_pt", "lep_eta"
  )

  # ─────────────────────────────────────────────
  # Numerator — split by flavor
  # ─────────────────────────────────────────────
  a.SetActiveNode(checkpoint)
  a.Cut("isMuon_num", "isMuon == true && lepPassesTight == true")
  hNum_mu = a.DataFrame.Histo2D(
      ("hNum_mu", "Muon fake rate numerator;p_{T} [GeV];#eta",
      len(pt_bins)-1,  ROOT.std.vector('double')(pt_bins),
      len(eta_bins)-1, ROOT.std.vector('double')(eta_bins)),
      "lep_pt", "lep_eta"
  )

  a.SetActiveNode(checkpoint)
  a.Cut("isEle_num", "isMuon == false && lepPassesTight == true")
  hNum_el = a.DataFrame.Histo2D(
      ("hNum_el", "Electron fake rate numerator;p_{T} [GeV];#eta",
      len(pt_bins)-1,  ROOT.std.vector('double')(pt_bins),
      len(eta_bins)-1, ROOT.std.vector('double')(eta_bins)),
      "lep_pt", "lep_eta"
  ))


  finalFile = sample + era + "_" + year + "_" + str(testNum1) + ".root"
  if not isMC:
    finalFile = sample + era + ver + "_" + year + "_" + str(testNum1) + ".root";

  mode = 'RECREATE'
  if jesvar != "Nominal":
    mode = 'UPDATE'
  #print('\n(1)\n')
  #sys.setprofile(trace_calls)

  hDen_mu.GetValue()
  hDen_el.GetValue()
  hNum_mu.GetValue()
  hNum_el.GetValue()

  a.Snapshot(columns, finalFile, "Events_"+jesvar, lazy=False, openOption=mode, saveRunChain=True)
  outFile = ROOT.TFile(finalFile, "UPDATE")

  for hDen, hNum, label in [
      (hDen_mu, hNum_mu, "mu"),
      (hDen_el, hNum_el, "el"),
  ]:
      den = hDen.GetValue()
      num = hNum.GetValue()
      fr  = num.Clone(f"hFakeRate_{label}")
      fr.Divide(den)
      den.Write()
      num.Write()
      fr.Write()

  outFile.Close()
analyze("Nominal")

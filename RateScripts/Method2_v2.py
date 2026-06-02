from TIMBER.Analyzer import analyzer, VarGroup, CutGroup
from TIMBER.Tools.Common import CompileCpp
import ROOT
import array


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


CompileCpp('TIMBER/Framework/include/common.h') # Compile (via gInterpreter) commonly used c++ code
CompileCpp('TIMBER/Framework/Tprime1lep/cleanjet.cc') # Compile Our vlq c++ code
CompileCpp('TIMBER/Framework/Tprime1lep/utilities.cc') # Compile Our vlq c++ code
CompileCpp('TIMBER/Framework/Tprime1lep/lumiMask.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/selfDerived_corrs.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/corr_funcs.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/topographInput.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/manualreco.cc')

debug = False
PNetL = {'2022':0.047,'2022EE':0.0499,'2023':0.0358,'2023BPix':0.0359} #PN
yrstr = {'2022':"Run3-22CDSep23-Summer22-NanoAODv12",'2022EE':"Run3-22EFGSep23-Summer22EE-NanoAODv12",'2023':"Run3-23CSep23-Summer23-NanoAODv12",'2023BPix':"Run3-23DSep23-Summer23BPix-NanoAODv12"}
jmetags = {'2022':'2025-09-23','2022EE':'2025-10-07','2023':'2025-10-07','2023BPix':'2025-10-07'}
jecyr = {'2022':"Summer22_22Sep2023_RunCD",'2022EE':"Summer22EE_22Sep2023_Run"+jecera,'2023':"Summer23Prompt23",'2023BPix':"Summer23BPixPrompt23"}
jecver = {'2022':"V3",'2022EE':"V3",'2023':"V2",'2023BPix':"V3"}
jetvetoname = {'2022':"Summer22_23Sep2023_RunCD_V1",'2022EE':"Summer22EE_23Sep2023_RunEFG_V1",'2023':"Summer23Prompt23_RunC_V1",'2023BPix':"Summer23BPixPrompt23_RunD_V1"}


jsonfile = "./TIMBER/data/LumiJSON/"
if '2022' in year:
  jsonfile = jsonfile + "Cert_Collisions2022_355100_362760_Golden.json"
elif '2023' in year:
  jsonfile = jsonfile + "Cert_Collisions2023_366442_370790_Golden.json"
else:
  print(f'ERROR: Can\'t parse the year to assign a golden json file. Expected 2022(EE) or 2023(BPix). Got: {year}\n')

ROOT.gInterpreter.Declare("""
    const auto myLumiMask = lumiMask::fromJSON(\"""" + jsonfile + """\");
  """)
ROOT.gInterpreter.Declare("""
string year = \"""" + year + """\";
string sample = \"""" + sample + """\";
string jecera = \"""" + jecera + """\";
string region = \"""" + region + """\";
string ver = \"""" + ver + """\";

bool isMC = """+str(isMC).lower()+""";
bool debug = """+str(debug).lower()+""";
bool isSig = """+str(isSig).lower()+""";
int dataset = """+str(dataset)+""";
""")
ROOT.gInterpreter.Declare("""
float PNetL = """+str(PNetL[year])+""";
string yrstr = \""""+yrstr[year]+"""\";
string jmetag = \""""+jmetags[year]+"""\";
string jecyr = \""""+jecyr[year]+"""\";
string jecver = \""""+jecver[year]+"""\";
string jetvetoname = \""""+jetvetoname[year]+"""\";
""")

# *************** muonisocorr does not match the muon definition !!!!! (change to mediumPFIso hopefully) *****************
ROOT.gInterpreter.Declare("""
auto jetvetocorrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/"+yrstr+"/"+jmetag+"/jetvetomaps.json.gz");

auto jetvetocorr = jetvetocorrset->at(jetvetoname);
""")

print('Finished declaring corrections')

ROOT.gInterpreter.Declare("""
auto ak4corrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/"+yrstr+"/"+jmetag+"/jet_jerc.json.gz");
auto ak8corrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/"+yrstr+"/"+jmetag+"/fatJet_jerc.json.gz");

auto ak4corr = ak4corrset->compound().at(jecyr+"_"+jecver+"_DATA_L1L2L3Res_AK4PFPuppi");
auto ak4corrL1 = ak4corrset->at(jecyr+"_"+jecver+"_DATA_L1FastJet_AK4PFPuppi");
auto ak8corr = ak8corrset->compound().at(jecyr+"_"+jecver+"_DATA_L1L2L3Res_AK8PFPuppi");
""")


print('============== RUN SETTINGS ===============')
print('isMC = ',isMC)
print('isSM = ',isSM)
print('isSE = ',isSE)
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


  #Golden JSON

  gjsonVars = VarGroup('GoldenJsonVars')
  gjsonCuts = CutGroup('GoldenJsonCuts')
  gjsonVars.Add("passesJSON", "goldenjson(myLumiMask, run, luminosityBlock)") # function name, parameters are branches in the file or defined objects
  gjsonCuts.Add("Data passes Golden JSON", "passesJSON == 1")
  a.Apply([gjsonVars,gjsonCuts])


  # ─────────────────────────────────────────────
  # Loose lepton definitions + counts
  # ─────────────────────────────────────────────
  eandmuVars = VarGroup("eandmuVars")
  eandmuVars.Add('looseElectrons', 'Electron_pt > 10 && abs(Electron_eta) < 2.5 && (Electron_mvaIso_WP90 == 1)')
  eandmuVars.Add('looseMuons', 'Muon_pt >= 15 && abs(Muon_eta) < 2.4 && Muon_looseId == 1 && abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5 && Muon_pfIsoId >= 2')
  eandmuVars.Add("nLooseMuons",     "Sum(looseMuons)")
  eandmuVars.Add("nLooseElectrons", "Sum(looseElectrons)")
  eandmuVars.Add("nLooseLeptons",   "nLooseMuons + nLooseElectrons")
  eandmuVars.Add("isMuon",   f"nLooseMuons == 1 && HLT_Mu17 == 1 && {str(isSM).lower()}")
  eandmuVars.Add("isEl",   f"nLooseElectrons == 1 && HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30 == 1 && {str(isSE).lower()}")         
  a.Apply(eandmuVars)

  # ─────────────────────────────────────────────
  # Single loose lepton veto
  # ─────────────────────────────────────────────
  lepVeto = CutGroup("lepVeto")
  lepVeto.Add("single_loose_lepton", "nLooseLeptons == 1")
  lepVeto.Add("isVIPlepton", "isMuon || isEl")
  a.Apply(lepVeto)

  # ─────────────────────────────────────────────
  # Lepton kinematics
  # (safe to index [0] — exactly one lepton survives)
  # ─────────────────────────────────────────────
  lepVars = VarGroup("lepVars")
  lepVars.Add("lep_pt",   "isMuon ? Muon_pt  [looseMuons][0] : Electron_pt  [looseElectrons][0]")
  lepVars.Add("lep_eta",  "isMuon ? Muon_eta [looseMuons][0] : Electron_eta [looseElectrons][0]")
  lepVars.Add("abslep_eta", "abs(lep_eta)")
  lepVars.Add("lep_phi",  "isMuon ? Muon_phi [looseMuons][0] : Electron_phi [looseElectrons][0]")
  lepVars.Add("lep_mass", "isMuon ? Muon_mass[looseMuons][0] : Electron_mass[looseElectrons][0]")
  a.Apply(lepVars)


  # -------------------- EL and MUON Definitions --------------------
  eandmuVars = VarGroup('ElandMuVars')

  #Good Electrons
  #eandmuVars.Add('looseElectrons', 'Electron_pt > 10 && abs(Electron_eta) < 2.5 && (Electron_mvaIso_WP90 == 1)')
  eandmuVars.Add('NlooseElecs', 'Sum(looseElectrons)')
  #eandmuVars.Add('goodElectrons', 'Electron_pt > 10 && abs(Electron_eta) < 2.5 && (Electron_mvaIso_WP80 == 1)')
  #eandmuVars.Add('NgoodElecs', 'Sum(goodElectrons)')

  eandmuVars.Add('LooseEl_pt','Electron_pt[looseElectrons]')
  eandmuVars.Add('LooseEl_eta','Electron_eta[looseElectrons]')
  eandmuVars.Add('LooseEl_phi', 'Electron_phi[looseElectrons]')
  eandmuVars.Add('LooseEl_mass', 'Electron_mass[looseElectrons]')
  eandmuVars.Add('LooseEl_charge', 'Electron_charge[looseElectrons]')
  eandmuVars.Add('LooseEl_ID', 'ROOT::VecOps::RVec<int>(NlooseElecs, 11)')
  eandmuVars.Add('LooseEl_isTight','Electron_mvaIso_WP80[looseElectrons] == 1')

  # eandmuVars.Add('GoodEl_pt','Electron_pt[goodElectrons == true]')
  # eandmuVars.Add('GoodEl_eta','Electron_eta[goodElectrons == true]')
  # eandmuVars.Add('GoodEl_phi','Electron_phi[goodElectrons == true]')
  # eandmuVars.Add('GoodEl_mass','Electron_mass[goodElectrons == true]')
  # eandmuVars.Add('GoodEl_ID', 'ROOT::VecOps::RVec<int>(NgoodElecs, 11)')
  # eandmuVars.Add('GoodEl_mtforTau', 'ROOT::VecOps::RVec<int>(NgoodElecs, -1)')
  # eandmuVars.Add('GoodEl_charge', 'Electron_charge[goodElectrons == true]')

  #Good Muons
  #eandmuVars.Add('looseMuons', 'Muon_pt >= 15 && abs(Muon_eta) < 2.4 && Muon_looseId == 1 && abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5 && Muon_pfIsoId >= 2')
  eandmuVars.Add('NlooseMuons', 'Sum(looseMuons)')
  #eandmuVars.Add('goodMuons', 'Muon_pt >= 15 && abs(Muon_eta) < 2.4 && Muon_mediumId == 1 && abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5 && Muon_pfIsoId >= 3')
  #eandmuVars.Add('NgoodMuons', 'Sum(goodMuons)')

  eandmuVars.Add('LooseMu_pt','Muon_pt[looseMuons]')
  eandmuVars.Add('LooseMu_eta','Muon_eta[looseMuons]')
  eandmuVars.Add('LooseMu_phi', 'Muon_phi[looseMuons]')
  eandmuVars.Add('LooseMu_mass', 'Muon_mass[looseMuons]')
  eandmuVars.Add('LooseMu_charge', 'Muon_charge[looseMuons]')
  eandmuVars.Add('LooseMu_ID', 'ROOT::VecOps::RVec<int>(NlooseMuons, 13)')
  eandmuVars.Add('LooseMu_isTight','Muon_mediumId[looseMuons] == 1 && Muon_pfIsoId[looseMuons] >= 3')

  
  # ------------------------ LEPTON Definitions and Selection -------------------------
  lVars = VarGroup('LeptonVars')

  lVars.Add('ilLepton', 'ROOT::VecOps::Concatenate(looseElectrons, looseMuons)')
  lVars.Add('lLepton', 'ROOT::VecOps::Concatenate(ilLepton, looseTau)')
  lVars.Add('NlooseLeptons', 'Sum(lLepton)')
  lVars.Add('ilLepton_pt', 'ROOT::VecOps::Concatenate(LooseEl_pt, LooseMu_pt)')
  lVars.Add('lLepton_pt', 'ROOT::VecOps::Concatenate(ilLepton_pt, LooseTau_pt)')
  lVars.Add('ilLepton_eta', 'ROOT::VecOps::Concatenate(LooseEl_eta, LooseMu_eta)')
  lVars.Add('lLepton_eta', 'ROOT::VecOps::Concatenate(ilLepton_eta, LooseTau_eta)')
  lVars.Add('ilLepton_phi', 'ROOT::VecOps::Concatenate(LooseEl_phi, LooseMu_phi)')
  lVars.Add('lLepton_phi', 'ROOT::VecOps::Concatenate(ilLepton_phi, LooseTau_phi)')
  lVars.Add('ilLepton_mass', 'ROOT::VecOps::Concatenate(LooseEl_mass, LooseMu_mass)')
  lVars.Add('lLepton_mass', 'ROOT::VecOps::Concatenate(ilLepton_mass, LooseTau_mass)')
  lVars.Add('ilLepton_charge', 'ROOT::VecOps::Concatenate(LooseEl_charge, LooseMu_charge)')
  lVars.Add('lLepton_charge', 'ROOT::VecOps::Concatenate(ilLepton_charge, LooseTau_charge)')
  lVars.Add('ilLepton_ID', 'ROOT::VecOps::Concatenate(LooseEl_ID, LooseMu_ID)')
  lVars.Add('lLepton_ID', 'ROOT::VecOps::Concatenate(ilLepton_ID, LooseTau_ID)')
  lVars.Add('ilLepton_isTight', 'ROOT::VecOps::Concatenate(LooseEl_isTight, LooseMu_isTight)')
  lVars.Add('lLepton_isTight', 'ROOT::VecOps::Concatenate(ilLepton_isTight, LooseTau_isTight)')

  lVars.Add("lLepton_ptargsort","ROOT::VecOps::Reverse(ROOT::VecOps::Argsort(lLepton_pt))")
  lVars.Add("LooseLepton_pt","reorder(lLepton_pt,lLepton_ptargsort)")
  lVars.Add("LooseLepton_eta","reorder(lLepton_eta,lLepton_ptargsort)")
  lVars.Add("LooseLepton_phi","reorder(lLepton_phi,lLepton_ptargsort)")
  lVars.Add("LooseLepton_mass","reorder(lLepton_mass,lLepton_ptargsort)")
  lVars.Add("LooseLepton_charge","reorder(lLepton_charge,lLepton_ptargsort)")
  lVars.Add("LooseLepton_ID","reorder(lLepton_ID,lLepton_ptargsort)")
  lVars.Add("LooseLepton_isTight","reorder(lLepton_isTight,lLepton_ptargsort)")

  lVars.Add("Loose4Lepton_pt", "NlooseLeptons >= 4 ? ROOT::VecOps::Take(LooseLepton_pt, 4) : ROOT::VecOps::Take(LooseLepton_pt, 3)")
  lVars.Add("Loose4Lepton_eta", "NlooseLeptons >= 4 ? ROOT::VecOps::Take(LooseLepton_eta, 4) : ROOT::VecOps::Take(LooseLepton_eta, 3)")
  lVars.Add("Loose4Lepton_phi", "NlooseLeptons >= 4 ? ROOT::VecOps::Take(LooseLepton_phi, 4) : ROOT::VecOps::Take(LooseLepton_phi, 3)")
  lVars.Add("Loose4Lepton_mass", "NlooseLeptons >= 4 ? ROOT::VecOps::Take(LooseLepton_mass, 4) : ROOT::VecOps::Take(LooseLepton_mass, 3)")
  lVars.Add("Loose4Lepton_charge", "NlooseLeptons >= 4 ? ROOT::VecOps::Take(LooseLepton_charge, 4) : ROOT::VecOps::Take(LooseLepton_charge, 3)")
  lVars.Add("Loose4Lepton_ID", "NlooseLeptons >= 4 ? ROOT::VecOps::Take(LooseLepton_ID, 4) : ROOT::VecOps::Take(LooseLepton_ID, 3)")
  lVars.Add("Loose4Lepton_isTight", "NlooseLeptons >= 4 ? ROOT::VecOps::Take(LooseLepton_isTight, 4) : ROOT::VecOps::Take(LooseLepton_isTight, 3)")

  lVars.Add("hasBosonishMass", "hasBosonishMfunc(Loose4Lepton_pt, Loose4Lepton_eta, Loose4Lepton_phi, Loose4Lepton_mass, Loose4Lepton_ID, Loose4Lepton_charge)")

  tVars = VarGroup('TauVars')
  tVars.Add('goodTaumu', 'Tau_pt > 20 && abs(Tau_eta) < 2.5 && abs(Tau_dz) < 0.2 && Tau_idDeepTau2018v2p5VSmu >= 1')
  tVars.Add('NgoodTaumu', 'Sum(goodTaumu)')

  tVars.Add('goodTaue', 'goodTaumu == 1 && Tau_idDeepTau2018v2p5VSe >= 2')
  tVars.Add('NgoodTaue', 'Sum(goodTaue)')

  #tVars.Add('goodTau', 'goodTaue == 1 && Tau_idDeepTau2018v2p5VSjet >= 4')
  #tVars.Add('NgoodTau', 'Sum(goodTau)')
  tVars.Add('looseTau', 'goodTaue == 1 && Tau_idDeepTau2018v2p5VSjet >= 2')
  tVars.Add('NlooseTau', 'Sum(looseTau)')

  tVars.Add('LooseTau_eta', 'Tau_eta[looseTau == true]')
  tVars.Add('LooseTau_pt', 'Tau_pt[looseTau == true]')
  tVars.Add('LooseTau_phi', 'Tau_phi[looseTau == true]')
  tVars.Add('LooseTau_mass', 'Tau_mass[looseTau == true]')
  tVars.Add('LooseTau_charge', 'Tau_charge[looseTau == true]')
  tVars.Add('LooseTau_ID', 'ROOT::VecOps::RVec<int>(NlooseTau, 15)')
  tVars.Add('LooseTau_isTight','Tau_idDeepTau2018v2p5VSjet[looseTau == true] >= 4')

  a.Apply(eandmuVars)
  a.Apply([tVars,lVars])



  jVars = VarGroup('JetCleaningVars')

  jVars.Add("Jet_P4", "fVectorConstructor(Jet_pt,Jet_eta,Jet_phi,Jet_mass)")
  #jVars.Add("FatJet_P4", "fVectorConstructor(FatJet_pt,FatJet_eta,FatJet_phi,FatJet_mass)")
  jVars.Add("Jet_EmEF","Jet_neEmEF + Jet_chEmEF")
  jVars.Add("DummyZero","float(0.0)")

  jVars.Add("cleanedJets", "cleanJetsData(run,debug,year,ak4corr,ak4corrL1,ak8corr,Jet_P4,Jet_rawFactor,Jet_muonSubtrFactor,Jet_area,Jet_EmEF,Jet_jetId,Jet_P4,Jet_jetId,Rho_fixedGridRhoFastjetAll,DummyZero,DummyZero)") # muon and EM factors unused in this call, args 16-17 are dummies
  jVars.Add("cleanMets", "cleanJetsData(run,debug,year,ak4corr,ak4corrL1,ak8corr,Jet_P4,Jet_rawFactor,Jet_muonSubtrFactor,Jet_area,Jet_EmEF,Jet_jetId,Jet_P4,Jet_jetId,Rho_fixedGridRhoFastjetAll,RawPuppiMET_pt,RawPuppiMET_phi)") # lepton args unused in this call, args 16-17 are dummies
  #jVars.Add("cleanFatJets", "cleanJetsData(debug,year,ak4corr,ak4corrL1,ak8corr,FatJet_P4,FatJet_rawFactor,FatJet_rawFactor,FatJet_area,FatJet_area,FatJet_jetId,FatJet_P4,FatJet_jetId,Rho_fixedGridRhoFastjetAll,DummyZero,DummyZero)") # args 12, 14, 16, 17 are dummies
  #jVars.Add("NcleanJets", "Sum(cleanedJets)")
  jVars.Add("cleanJet_pt", "cleanedJets[0]")
  jVars.Add("cleanJet_eta", "cleanedJets[1]")
  jVars.Add("cleanJet_phi", "cleanedJets[2]")
  jVars.Add("cleanJet_mass", "cleanedJets[3]")
  #jVars.Add("cleanFatJet_pt", "cleanFatJets[0]")
  #jVars.Add("cleanFatJet_eta", "cleanFatJets[1]")
  #jVars.Add("cleanFatJet_phi", "cleanFatJets[2]")
  #jVars.Add("cleanFatJet_mass", "cleanFatJets[3]")


  # ------------------ Jet Calculations ------------------
  jVars.Add("minDR_lepsJets","minDR_jets_gtau(nJet, cleanJet_eta, cleanJet_phi, NlooseLeptons, Loose4Lepton_eta, Loose4Lepton_phi)")
  jVars.Add("goodcleanJets", "cleanJet_pt > 30 && abs(cleanJet_eta) < 2.5 && Jet_jetId > 1 && minDR_lepsJets > 0.4 ")
  jVars.Add("NgoodcleanJets", "Sum(goodcleanJets)")

  jVars.Add("gcJet_HT","Sum(cleanJet_pt[goodcleanJets == true])")
  jVars.Add("gcJet_pt_unsort", "cleanJet_pt[goodcleanJets == true]")
  jVars.Add("gcJet_ptargsort","ROOT::VecOps::Reverse(ROOT::VecOps::Argsort(gcJet_pt_unsort))")

  jVars.Add("gcJet_pt","reorder(gcJet_pt_unsort,gcJet_ptargsort)")
  jVars.Add("gcJet_eta", "reorder(cleanJet_eta[goodcleanJets == true],gcJet_ptargsort)")
  jVars.Add("gcJet_phi", "reorder(cleanJet_phi[goodcleanJets == true],gcJet_ptargsort)")
  jVars.Add("gcJet_mass", "reorder(cleanJet_mass[goodcleanJets == true],gcJet_ptargsort)")

  jVars.Add("gcJet_vetomap", "jetvetofunc(jetvetocorr, gcJet_eta, gcJet_phi)")
  if (isMC):
      jVars.Add("gcJet_hflav", "reorder(Jet_hadronFlavour[goodcleanJets == true],gcJet_ptargsort)")

  jVars.Add("gcJet_PNet", "reorder(Jet_btagPNetB[goodcleanJets == true],gcJet_ptargsort)")
  jVars.Add("gcJet_PNetL", "gcJet_PNet > PNetL")
  jVars.Add("NJets_PNetL", "Sum(gcJet_PNetL)")

  jVars.Add("gcBJet_eta", "gcJet_eta[gcJet_PNetL]")
  jVars.Add("gcBJet_phi", "gcJet_phi[gcJet_PNetL]")
  jVars.Add("gcBJet_pt", "gcJet_pt[gcJet_PNetL]")
  jVars.Add("gcBJet_mass", "gcJet_mass[gcJet_PNetL]")

  jVars.Add("gcJet_ht", "Sum(gcJet_pt)")
  
  a.Apply(jVars)

  # ─────────────────────────────────────────────
  # MET and mT
  # ─────────────────────────────────────────────
  metVars = VarGroup("metVars")
  metVars.Add("corrMET_pt","cleanMets[4][0]")
  metVars.Add("corrMET_phi","cleanMets[4][1]")
  metVars.Add("mT", "calcMT(lep_pt, lep_phi, corrMET_pt, corrMET_phi)")
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
  jetMaskVars.Add("Jet_dR_lep","sqrt((cleanJet_eta - lep_eta)*(cleanJet_eta - lep_eta) + (cleanJet_phi - lep_phi)*(cleanJet_phi - lep_phi))")
  jetMaskVars.Add("goodJet_mask", "cleanJet_pt > 30.0 && Jet_jetId >= 2 && Jet_dR_lep > 1.0")
  jetMaskVars.Add("nGoodJets",    "Sum(goodJet_mask)")
  #jetMaskVars.Add("lepJet_invM","ROOT::VecOps::Map(cleanJet_pt, cleanJet_eta, cleanJet_phi, cleanJet_mass, [](float jpt, float jeta, float jphi, float jmass){TLorentzVector j, l; j.SetPtEtaPhiM(jpt, jeta, jphi, jmass); l.SetPtEtaPhiM(lep_pt, lep_eta, lep_phi, lep_mass); return (j + l).M();})")
  #jetMaskVars.Add("lep_p4","ROOT::Math::PtEtaPhiMVector(lep_pt, lep_eta, lep_phi, lep_mass)")
  #jetMaskVars.Add("jet_p4","ROOT::VecOps::Map(cleanJet_pt, cleanJet_eta, cleanJet_phi, cleanJet_mass,[](float pt, float eta, float phi, float m){ return ROOT::Math::PtEtaPhiMVector(pt, eta, phi, m);})")
  #jetMaskVars.Add("lepJet_invM","VecOps::Map(jet_p4, [](auto const &j){ return (j + lep_p4).M(); })")
  #jetMaskVars.Add("lepJet_invM", "VecOps::Map(jet_p4, lep_p4, [](auto const &j, auto const &l){ return (j + l).M(); })")
  jetMaskVars.Add(
    "lepJet_invM",
    "sqrt("
    "(cleanJet_mass + lep_mass)*(cleanJet_mass + lep_mass) + "
    "2*("
    "  sqrt(cleanJet_pt*cleanJet_pt + cleanJet_mass*cleanJet_mass) * "
    "  sqrt(lep_pt*lep_pt + lep_mass*lep_mass) "
    "- cleanJet_pt*lep_pt*cosh(cleanJet_eta - lep_eta)"
    "+ cleanJet_pt*lep_pt*cos(cleanJet_phi - lep_phi)"
    "))")
  jetMaskVars.Add("Z_veto", "!(lepJet_invM > 81.1 && lepJet_invM < 101.1)")
  jetMaskVars.Add("nBadJets","Sum(Z_veto)")
  a.Apply(jetMaskVars)

  jetCuts = CutGroup("jetCuts")
  jetCuts.Add("jet_requirement", "nGoodJets >= 1 && nBadJets == 0")
  a.Apply(jetCuts)

  # Lead jet kinematics + Z veto variable
  leadJetVars = VarGroup("leadJetVars")
  leadJetVars.Add("jet0_pt",   "Jet_pt  [goodJet_mask][0]")
  leadJetVars.Add("jet0_eta",  "Jet_eta [goodJet_mask][0]")
  leadJetVars.Add("jet0_phi",  "Jet_phi [goodJet_mask][0]")
  leadJetVars.Add("jet0_mass", "Jet_mass[goodJet_mask][0]")
  a.Apply(leadJetVars)


  # ─────────────────────────────────────────────
  # Tight ID definitions
  # LooseMu_isTight / LooseEl_isTight are already
  # sub-vectors filtered to loose candidates only,
  # so [0] gives the single surviving lepton's result
  # ─────────────────────────────────────────────
  tightVars = VarGroup("tightVars")
  #tightVars.Add("LooseMu_isTight",
  #    "Muon_mediumId[looseMuons == true] == 1 && Muon_pfIsoId[looseMuons == true] >= 3")
  #tightVars.Add("LooseEl_isTight",
  #    "Electron_mvaIso_WP90[looseElectrons == true] == 1")
  tightVars.Add("lepPassesTight",
      "isMuon ? (bool)LooseMu_isTight[0] : (bool)LooseEl_isTight[0]")
  a.Apply(tightVars)

  # ─────────────────────────────────────────────
  # Fake rate histograms
  # ─────────────────────────────────────────────
  pt_bins  = [10, 15, 20, 25, 30, 40, 50, 70, 100]
  etabinsmu = [0.0, 0.9, 1.2, 2.1, 2.4]
  etabinsel = [-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]


  pt_binsarr = array.array('d', pt_bins)
  etabinsmuarr = array.array('d', etabinsmu)
  etabinselarr = array.array('d', etabinsel)

 
  checkpoint = a.GetActiveNode()

  a.SetActiveNode(checkpoint)
  a.Cut("isMuon_den", "(isMuon == true) && (HLT_Mu17 == 1)")
  hDen_mu = a.DataFrame.Histo2D(
      ("hDen_mu", "Muon fake rate denominator;p_{T} [GeV];#eta",
      len(pt_bins)-1,  pt_binsarr,
      len(etabinsmu)-1, etabinsmuarr),
      "lep_pt", "abslep_eta"
  )

  a.SetActiveNode(checkpoint)
  a.Cut("isEle_den", "isMuon == false && HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30 == 1")
  hDen_el = a.DataFrame.Histo2D(
      ("hDen_el", "Electron fake rate denominator;p_{T} [GeV];#eta",
      len(pt_bins)-1,  pt_binsarr,
      len(etabinsel)-1, etabinselarr),
      "lep_pt", "lep_eta"
  )

  # ─────────────────────────────────────────────
  # Numerator — split by flavor
  # ─────────────────────────────────────────────
  a.SetActiveNode(checkpoint)
  a.Cut("isMuon_num", "isMuon == true && lepPassesTight == true && HLT_Mu17 == 1")
  hNum_mu = a.DataFrame.Histo2D(
      ("hNum_mu", "Muon fake rate numerator;p_{T} [GeV];#eta",
      len(pt_bins)-1,  pt_binsarr,
      len(etabinsmu)-1, etabinsmuarr),
      "lep_pt", "abslep_eta"
  )

  a.SetActiveNode(checkpoint)
  a.Cut("isEle_num", "isMuon == false && lepPassesTight == true && HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30 == 1")
  hNum_el = a.DataFrame.Histo2D(
      ("hNum_el", "Electron fake rate numerator;p_{T} [GeV];#eta",
      len(pt_bins)-1,  pt_binsarr,
      len(etabinsel)-1, etabinselarr),
      "lep_pt", "lep_eta"
  )


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

  #a.Snapshot(columns, finalFile, "Events_"+jesvar, lazy=False, openOption=mode, saveRunChain=True)
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

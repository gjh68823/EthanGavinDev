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

# ------------------ TIMBER Analyzer inputs ------------------

num_threads = 1

# Import the C++
CompileCpp('TIMBER/Framework/include/common.h') # Compile (via gInterpreter) commonly used c++ code
CompileCpp('TIMBER/Framework/Tprime1lep/cleanjet.cc') # Compile Our vlq c++ code
CompileCpp('TIMBER/Framework/Tprime1lep/utilities.cc') # Compile Our vlq c++ code
CompileCpp('TIMBER/Framework/Tprime1lep/lumiMask.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/selfDerived_corrs.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/corr_funcs.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/topographInput.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/manualreco.cc')
ROOT.gInterpreter.ProcessLine('#include "TString.h"')

# Enable using 4 threads
ROOT.ROOT.EnableImplicitMT(num_threads)

# load rest frames handler
handler_name = 'Bprime_handler_new.cc'
class_name = 'Bprime_RestFrames_Container_new'
load_restframes(num_threads, handler_name, class_name, 'B_rfc')

#CompileCpp('bin/restframes/helper.cc')
# Essentially just called return doubles
# Now we implement directly

# ------------------ Important Variables ------------------
debug = False

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

def analyze(jesvar):
  ROOT.gInterpreter.ProcessLine('string jesvar = "' + jesvar + '"; ')

  # Create analyzer instance
  # is filelist still what you want it be here
  a = analyzer(filelist)

  print('==========================INITIALIZED ANALYZER========================')

  # ------------------ Golden JSON Data ------------------
  # change the jsonfile path to somewhere they have it in TIMBER
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

  print('========= loaded lumimask ============')

  ROOT.gInterpreter.ProcessLine('initialize(year);')


  # ------------------ correctionsLib corrections ------------------

  PNetL = {'2022':0.047,'2022EE':0.0499,'2023':0.0358,'2023BPix':0.0359} #PN
  yrstr = {'2022':"Run3-22CDSep23-Summer22-NanoAODv12",'2022EE':"Run3-22EFGSep23-Summer22EE-NanoAODv12",'2023':"Run3-23CSep23-Summer23-NanoAODv12",'2023BPix':"Run3-23DSep23-Summer23BPix-NanoAODv12"}
  jmetags = {'2022':'2025-09-23','2022EE':'2025-10-07','2023':'2025-10-07','2023BPix':'2025-10-07'}
  jecyr = {'2022':"Summer22_22Sep2023_RunCD",'2022EE':"Summer22EE_22Sep2023_Run"+jecera,'2023':"Summer23Prompt23",'2023BPix':"Summer23BPixPrompt23"}
  jecver = {'2022':"V3",'2022EE':"V3",'2023':"V2",'2023BPix':"V3"}
  jetvetoname = {'2022':"Summer22_23Sep2023_RunCD_V1",'2022EE':"Summer22EE_23Sep2023_RunEFG_V1",'2023':"Summer23Prompt23_RunC_V1",'2023BPix':"Summer23BPixPrompt23_RunD_V1"}


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

  # ------------------ Flag Cuts ------------------
  flagCuts = CutGroup('FlagCuts')
  flagCuts.Add('Bad Event Filters', 'Flag_EcalDeadCellTriggerPrimitiveFilter == 1 && Flag_goodVertices == 1 && Flag_eeBadScFilter == 1 && Flag_globalSuperTightHalo2016Filter == 1 && Flag_BadPFMuonFilter == 1 && Flag_BadPFMuonDzFilter == 1')
  flagCuts.Add('Event has jets', 'nJet > 0') # need jets   && nFatJet > 0

  # ------------------ Golden JSON (Data) || GEN Info (MC) ------------------
  gjsonVars = VarGroup('GoldenJsonVars')
  gjsonCuts = CutGroup('GoldenJsonCuts')
  gjsonVars.Add("passesJSON", "goldenjson(myLumiMask, run, luminosityBlock)") # function name, parameters are branches in the file or defined objects
  gjsonCuts.Add("Data passes Golden JSON", "passesJSON == 1")

  # ------------------ Tau selection criteria ----------------
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

  # tVars.Add('GoodTau_eta', 'Tau_eta[goodTau == true]')
  # tVars.Add('GoodTau_phi', 'Tau_phi[goodTau == true]')
  # tVars.Add('GoodTau_pt', 'Tau_pt[goodTau == true]')
  # tVars.Add('GoodTau_mass', 'Tau_mass[goodTau == true]')
  # tVars.Add('GoodTau_ID', 'ROOT::VecOps::RVec<int>(NgoodTau, 15)')
  # tVars.Add('GoodTau_DM', 'Tau_decayMode[goodTau == true]')
  # if (isMC):
  #    tVars.Add('GoodTau_genmch', 'Tau_genPartFlav[goodTau == true]')
  # tVars.Add('GoodTau_charge', 'Tau_charge[goodTau == true]')

  # -------------------- EL and MUON Definitions --------------------
  eandmuVars = VarGroup('ElandMuVars')

  #Good Electrons
  eandmuVars.Add('looseElectrons', 'Electron_pt > 10 && abs(Electron_eta) < 2.5 && (Electron_mvaIso_WP90 == 1)')
  eandmuVars.Add('NlooseElecs', 'Sum(looseElectrons)')
  #eandmuVars.Add('goodElectrons', 'Electron_pt > 10 && abs(Electron_eta) < 2.5 && (Electron_mvaIso_WP80 == 1)')
  #eandmuVars.Add('NgoodElecs', 'Sum(goodElectrons)')

  eandmuVars.Add('LooseEl_pt','Electron_pt[looseElectrons == true]')
  eandmuVars.Add('LooseEl_eta','Electron_eta[looseElectrons == true]')
  eandmuVars.Add('LooseEl_phi', 'Electron_phi[looseElectrons == true]')
  eandmuVars.Add('LooseEl_mass', 'Electron_mass[looseElectrons == true]')
  eandmuVars.Add('LooseEl_charge', 'Electron_charge[looseElectrons == true]')
  eandmuVars.Add('LooseEl_ID', 'ROOT::VecOps::RVec<int>(NlooseElecs, 11)')
  eandmuVars.Add('LooseEl_isTight','Electron_mvaIso_WP80[looseElectrons == true] == 1')

  # eandmuVars.Add('GoodEl_pt','Electron_pt[goodElectrons == true]')
  # eandmuVars.Add('GoodEl_eta','Electron_eta[goodElectrons == true]')
  # eandmuVars.Add('GoodEl_phi','Electron_phi[goodElectrons == true]')
  # eandmuVars.Add('GoodEl_mass','Electron_mass[goodElectrons == true]')
  # eandmuVars.Add('GoodEl_ID', 'ROOT::VecOps::RVec<int>(NgoodElecs, 11)')
  # eandmuVars.Add('GoodEl_mtforTau', 'ROOT::VecOps::RVec<int>(NgoodElecs, -1)')
  # eandmuVars.Add('GoodEl_charge', 'Electron_charge[goodElectrons == true]')

  #Good Muons
  eandmuVars.Add('looseMuons', 'Muon_pt >= 15 && abs(Muon_eta) < 2.4 && Muon_looseId == 1 && abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5 && Muon_pfIsoId >= 2')
  eandmuVars.Add('NlooseMuons', 'Sum(looseMuons)')
  #eandmuVars.Add('goodMuons', 'Muon_pt >= 15 && abs(Muon_eta) < 2.4 && Muon_mediumId == 1 && abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5 && Muon_pfIsoId >= 3')
  #eandmuVars.Add('NgoodMuons', 'Sum(goodMuons)')

  eandmuVars.Add('LooseMu_pt','Muon_pt[looseMuons == true]')
  eandmuVars.Add('LooseMu_eta','Muon_eta[looseMuons == true]')
  eandmuVars.Add('LooseMu_phi', 'Muon_phi[looseMuons == true]')
  eandmuVars.Add('LooseMu_mass', 'Muon_mass[looseMuons == true]')
  eandmuVars.Add('LooseMu_charge', 'Muon_charge[looseMuons == true]')
  eandmuVars.Add('LooseMu_ID', 'ROOT::VecOps::RVec<int>(NlooseMuons, 13)')
  eandmuVars.Add('LooseMu_isTight','Muon_mediumId[looseMuons == true] == 1 && Muon_pfIsoId[looseMuons == true] >= 3')

  # eandmuVars.Add('GoodMu_pt','Muon_pt[goodMuons == true]')
  # eandmuVars.Add('GoodMu_eta','Muon_eta[goodMuons == true]')
  # eandmuVars.Add('GoodMu_phi','Muon_phi[goodMuons == true]')
  # eandmuVars.Add('GoodMu_mass','Muon_mass[goodMuons == true]')
  # eandmuVars.Add('GoodMu_ID', 'ROOT::VecOps::RVec<int>(NgoodMuons, 13)')
  # eandmuVars.Add('GoodMu_mtforTau', 'ROOT::VecOps::RVec<int>(NgoodMuons, -1)')
  # eandmuVars.Add('GoodMu_charge', 'Muon_charge[goodMuons == true]')


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

  lCuts = CutGroup('Lepton Cuts')
  lCuts.Add('NlooseLeptons >= 3', 'NlooseLeptons >= 3')
  lCuts.Add('hasBosonishMass == 0', 'hasBosonishMass == 0')


  # ------------------ JET Cleaning and JERC ------------------
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

  # ------------------ MET Selection ------------------
  metVars = VarGroup('METVars')
  metVars.Add("corrMET_pt","cleanMets[4][0]")
  metVars.Add("corrMET_phi","cleanMets[4][1]")
  # This function needs work to understand it, and the output is a vector.
  # I'm not sure it's for PuppiMET, it might actually be for PFMET...
  #metVars.Add("corrMET_pt", "METptfunc(METcorr, METyr, isMC, cleanMET_pt, cleanMET_phi, PV_npvs)")
  #metVars.Add("corrMET_phi", "METphifunc(METcorr, METyr, isMC, cleanMET_pt, cleanMET_phi, PV_npvs)")

  metCuts = CutGroup('METCuts')
  metCuts.Add("Pass PuppiMET pt > 50", "corrMET_pt > 50")

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

  jCuts = CutGroup('JetCuts')
  jCuts.Add('NgoodcleanJets >= 2', 'NgoodcleanJets >= 2')
  jCuts.Add('1 B Jet Pass (Loose)', 'NJets_PNetL >= 1')



  # # --------------- Prompt Rate Calculations -------------
  preTagCuts = CutGroup("preTagCuts")
  preTagCuts.add("Flavor_XOR_Cut", "(looseElectrons && looseMuons) || (looseElectrons && looseTau) || (looseMuons && looseTau)")

  tagDefVars = VarGroup("tagTestVariables")
  tagDefVars.Add("TagMu","Muon_pt > 30 && abs(Muon_eta)<2.4 && Muon_tightId==1 && Muon_pfIsoId>=3 && abs(Muon_dz) < 0.5 && Muon_dxy < 0.2")
  tagDefVars.Add("ProbeMu",'Muon_pt >= 15 && abs(Muon_eta) < 2.4 && Muon_looseId == 1 && abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5 && Muon_pfIsoId >= 2')
  tagDefVars.Add("ProbeTau","goodTaue == 1 && Tau_idDeepTau2018v2p5VSjet >= 2")
  tagDefVars.Add("ProbeMunoTag","TagMu == 0 && ProbeMu == 1")
  tagDefVars.Add("TagMunoProbe","ProbeMu == 0 && TagMu == 1")
  tagDefVars.Add("TagEl","Electron_pt > 40 && (abs(Electron_eta)<1.442 || (abs(Electron_eta)>1.566 && abs(Electron_eta)<2.5)) && Electron_cutBased>=4 ")
  tagDefVars.Add("ProbeEl",'Electron_pt > 10 && abs(Electron_eta) < 2.5 && (Electron_mvaIso_WP90 == 1)')
  tagDefVars.Add("nTagMu","(int) Sum(TagMu)")
  tagDefVars.Add("nTagEl","(int) Sum(TagEl)")
  tagDefVars.Add("nProbeMu","(int) Sum(ProbeMu)")
  tagDefVars.Add("nProbeEl","(int) Sum(ProbeEl)")
  tagDefVars.Add("passTagMuTrig","(IsoMu27)")
  tagDefVars.Add("passTagElTrig","(HLT_Ele35_WPTight_Gsf == 1 || HLT_Ele38_WPTight_Gsf == 1 || HLT_Photon200)")
  tagDefVars.Add("tagMu_idx", "Nonzero(TagMu)")
  tagDefVars.Add("probeMu_idx", "Nonzero(ProbeMu)")
  tagDefVars.Add("tagEl_idx", "Nonzero(TagEl)")
  tagDefVars.Add("probeEl_idx", "Nonzero(ProbeEl)")
  tagDefVars.Add("probeTau_idx", "Nonzero(ProbeTau)")
  tagDefVars.Add("has_tau_mu", "probeTau_idx.size() > 0 && tagMu_idx.size() > 0")
  tagDefVars.Add("has_tau_el", "probeTau_idx.size() > 0 && tagEl_idx.size() > 0")
  tagDefVars.Add("has_mu_el", "probeMu_idx.size() > 0 && tagEl_idx.size() > 0")
  tagDefVars.Add("has_el_mu", "tagMu_idx.size() > 0 && probeEl_idx.size() > 0")
  tagDefVars.Add("probe_idx", "has_tau_mu ? probeTau_idx[0] : (has_tau_el ? probeTau_idx[0] : (has_mu_el ? probeMu_idx[0] :(has_el_mu ? probeEl_idx[0] : -1))")
  tagDefVars.Add("tag_idx", "has_tau_mu ? tagMu_idx[0] : (has_tau_el ? tagEl_idx[0] : (has_mu_el ? tagEl_idx[0] :(has_el_mu ? tagMu_idx[0] : -1))")
  tagDefVars.Add('LooseTau_isTight','Tau_idDeepTau2018v2p5VSjet[looseTau == true] >= 4')
  tagDefVars.Add('LooseEl_isTight','Electron_mvaIso_WP80[looseElectrons == true] == 1')
  tagDefVars.Add('LooseMu_isTight','Muon_mediumId[looseMuons == true] == 1 && Muon_pfIsoId[looseMuons == true] >= 3')
  tagDefVars.Add("tag_eta","(has_tau_mu || has_el_mu) ? Muon_eta[tag_idx] : ((has_tau_el || has_mu_el) ? Electron_eta[tag_idx] : 0)")
  tagDefVars.Add("tag_phi","(has_tau_mu || has_el_mu) ? Muon_phi[tag_idx] : ((has_tau_el || has_mu_el) ? Electron_phi[tag_idx] : 0)")
  tagDefVars.Add("probe_eta","(has_tau_mu || has_tau_el) ? Tau_eta[probe_idx] : (has_mu_el ? Muon_eta[probe_idx]: (has_el_mu ? Electron_eta[probe_idx] : 0))")
  tagDefVars.Add("probe_phi","(has_tau_mu || has_tau_el) ? Tau_phi[probe_idx] : (has_mu_el ? Muon_phi[probe_idx] : (has_el_mu ? Electron_phi[probe_idx] : 0))")
  tagDefVars.Add("tag_flavor","(has_tau_mu || has_el_mu) ? 13 : ((has_tau_el || has_mu_el) ? 11 : -1)")
  tagDefVars.Add("probe_flavor","(has_tau_mu || has_tau_el) ? 15 : (has_mu_el ? 13: (has_el_mu ? 11 : -1))")
  tagDefVars.Add("dR_jet_tag", "DeltaR(gcJet_eta, gcJet_phi, tag_eta, tag_phi)")
  tagDefVars.Add("dR_jet_probe", "DeltaR(gcJet_eta, gcJet_phi, probe_eta, probe_phi)")
  tagDefVars.Add("avoidant_Bjet", "((dR_jet_tag > 0.4) && (dR_jet_probe > 0.4))")
  tagDefVars.Add("n_avoidant_Bjet", "(int) Sum(avoidant_Bjet)")
  tagDefVars.Add("probe_pt", "(probe_flavor == 11) ? Electron_pt[probe_idx] : ((probe_flavor == 13) ? Muon_pt[probe_idx] : ((probe_flavor == 15) ? Tau_pt[probe_idx] : -9999999999999))")
  tagDefVars.Add("n_valid_channels", "(int)(has_tau_mu + has_tau_el + has_mu_el + has_el_mu)")
  tagDefVars.Add("n_tags_in_channel", "has_tau_mu  ? (int)tagMu_idx.size()  : (has_tau_el ? (int)tagEl_idx.size()  : (has_mu_el  ? (int)tagEl_idx.size()  : (has_el_mu  ? (int)tagMu_idx.size()  : 0)))")
  tagDefVars.Add("n_probes_in_channel","has_tau_mu  ? (int)probeTau_idx.size() : (has_tau_el ? (int)probeTau_idx.size() : (has_mu_el  ? (int)probeMu_idx.size()  : (has_el_mu  ? (int)probeEl_idx.size()  : 0)))")
  tagDefVars.Add("probe_isTight","(has_tau_mu || has_tau_el) ? LooseTau_isTight[probe_idx] : (has_mu_el ? LooseMu_isTight[probe_idx]: (has_el_mu ? LooseEl_isTight[probe_idx] : 0))")

  postTagCuts = CutGroup("postTagCuts")
  postTagCuts.Add("has_tag", "(tag_flavor != -1)")
  postTagCuts.Add("has_avoidant_Bjet","n_avoidant_BJet > 0")
  tagProbeUniquenessCuts = cutGroup("tagProbeUniquenessCuts")
  tagProbeUniquenessCuts.Add("unique_channel", "n_valid_channels == 1")
  tagProbeUniquenessCuts.Add("unique_tag",     "n_tags_in_channel == 1")
  tagProbeUniquenessCuts.Add("unique_probe",   "n_probes_in_channel == 1")

  #---------Z Boson and B Jet

  zBJTagDefVars = VarGroup("zBJTagVariables")

  # Channel flags — reuse existing idx vectors
  zBJTagDefVars.Add("has_mu_mu", "tagMu_idx.size() > 0 && probeMu_idx.size() > 0")
  zBJTagDefVars.Add("has_el_el", "tagEl_idx.size() > 0 && probeEl_idx.size() > 0")
  zBJTagDefVars.Add("n_zBJ_valid_channels", "(int)(has_mu_mu + has_el_el)")

  # Index and flavor selection (mu-mu takes priority, mirroring opposite-flavor logic)
  zBJTagDefVars.Add("zBJ_tag_idx",    "has_mu_mu ? tagMu_idx[0]   : (has_el_el ? tagEl_idx[0]   : -1)")
  zBJTagDefVars.Add("zBJ_probe_idx",  "has_mu_mu ? probeMu_idx[0] : (has_el_el ? probeEl_idx[0] : -1)")
  zBJTagDefVars.Add("zBJ_tag_flavor", "has_mu_mu ? 13             : (has_el_el ? 11             : -1)")

  # Kinematics — branch on flavor once, reuse for mass
  zBJTagDefVars.Add("zBJ_tag_pt",    "(zBJ_tag_flavor == 13) ? Muon_pt[zBJ_tag_idx]    : Electron_pt[zBJ_tag_idx]")
  zBJTagDefVars.Add("zBJ_tag_eta",   "(zBJ_tag_flavor == 13) ? Muon_eta[zBJ_tag_idx]   : Electron_eta[zBJ_tag_idx]")
  zBJTagDefVars.Add("zBJ_tag_phi",   "(zBJ_tag_flavor == 13) ? Muon_phi[zBJ_tag_idx]   : Electron_phi[zBJ_tag_idx]")
  zBJTagDefVars.Add("zBJ_probe_pt",  "(zBJ_tag_flavor == 13) ? Muon_pt[zBJ_probe_idx]  : Electron_pt[zBJ_probe_idx]")
  zBJTagDefVars.Add("zBJ_probe_eta", "(zBJ_tag_flavor == 13) ? Muon_eta[zBJ_probe_idx] : Electron_eta[zBJ_probe_idx]")
  zBJTagDefVars.Add("zBJ_probe_phi", "(zBJ_tag_flavor == 13) ? Muon_phi[zBJ_probe_idx] : Electron_phi[zBJ_probe_idx]")

  # Invariant mass via ROOT::Math::PtEtaPhiMVector with correct particle masses
  zBJTagDefVars.Add("zBJ_pair_mass", "(ROOT::Math::PtEtaPhiMVector(zBJ_tag_pt, zBJ_tag_eta, zBJ_tag_phi, (zBJ_tag_flavor==13 ? 0.10566 : 0.000511)) + ROOT::Math::PtEtaPhiMVector(zBJ_probe_pt, zBJ_probe_eta, zBJ_probe_phi, (zBJ_tag_flavor==13 ? 0.10566 : 0.000511))).M()")

  # B-jet avoidance — require at least one b-jet well separated from both tag and probe
  zBJTagDefVars.Add("zBJ_dR_jet_tag", "DeltaR(gcJet_eta, gcJet_phi, zBJ_tag_eta, zBJ_tag_phi)")
  zBJTagDefVars.Add("zBJ_dR_jet_probe", "DeltaR(gcJet_eta, gcJet_phi, zBJ_probe_eta, zBJ_probe_phi)")
  zBJTagDefVars.Add("zBJ_avoidant_Bjet", "(zBJ_dR_jet_tag > 0.4) && (zBJ_dR_jet_probe > 0.4)")
  zBJTagDefVars.Add("zBJ_n_avoidant_Bjet", "(int) Sum(zBJ_avoidant_Bjet)")

  # Uniqueness counts — same pattern as opposite-flavor
  zBJTagDefVars.Add("n_zBJ_tags_in_channel", "has_mu_mu ? (int)tagMu_idx.size()   : (has_el_el ? (int)tagEl_idx.size()   : 0)")
  zBJTagDefVars.Add("n_zBJ_probes_in_channel", "has_mu_mu ? (int)probeMu_idx.size() : (has_el_el ? (int)probeEl_idx.size() : 0)")


  zBJPostTagCuts = CutGroup("zBJPostTagCuts")
  zBJPostTagCuts.Add("zBJ_has_tag",           "zBJ_tag_flavor != -1")
  zBJPostTagCuts.Add("zBJ_unique_channel",    "n_zBJ_valid_channels == 1")
  zBJPostTagCuts.Add("zBJ_unique_tag",        "n_zBJ_tags_in_channel == 1")
  zBJPostTagCuts.Add("zBJ_unique_probe",      "n_zBJ_probes_in_channel == 1")
  zBJPostTagCuts.Add("zBJ_distinct_objects",  "zBJ_tag_idx != zBJ_probe_idx")
  zBJPostTagCuts.Add("zBJ_has_avoidant_Bjet", "zBJ_n_avoidant_Bjet > 0")
  zBJPostTagCuts.Add("zBJ_Z_mass_window",     "zBJ_pair_mass > 81 && zBJ_pair_mass < 101")

  #---------------------------------------------------------

  ptbins  = [10.0, 20.0, 30.0, 40.0, 50.0, 70.0, 100.0, 200.0, 9999.0]
  etabinsmu = [0.0, 0.9, 1.2, 2.1, 2.4]
  etabinsel = [-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]

  nodeToPlot = a.Apply([flagCuts, gjsonVars, gjsonCuts, tVars, eandmuVars, lVars])

  # # Solution to cleanJets() problem:
  # #       The analyzer .Apply() calls the analyzer .Define().  This .Define() calls self._collectionOrg.CollectionDefCheck(var, newNode).
  # #  This method executes this line: if re.search(r"\b" + re.escape(c+'s') + r"\b", action_str) and (c+'s' not in self._builtCollections):
  # #                                       print ('MAKING %ss for %s'%(c,action_str))
  # #  Apparently somethings get discarded from this _collectionOrg?
  # #  Instead force the .Apply() from the ActiveNode because the node .Apply() is better.

  newNode = a.ActiveNode.Apply(jVars)
  a.SetActiveNode(newNode)
  if isSig:
      a.Apply([recoGenVars])
  a.Apply([jCuts])
  a.Apply(tTagCuts)
  a.Apply(tagDefVars)
  zbj = a
  ttbar = a
  ttbar.Apply(postTagCuts, metVars, metCuts)
  ttbar.Apply(tagProbeUniquenessCuts)
  zbj.Apply(zBJTagDefVars)
  zbj.Apply(zBJPostTagCuts)
  a_loose = ttbar
  a_tight = a_loose.Cut("probe_tight","probe_isTight")
  allColumns = a.GetColumnNames()

  checkpoint = a.GetActiveNode()

  a.setActiveNode(checkpoint)
  a.Cut("ElectronCut", "has_el_mu")
  hDen_el = a.DataFrame.Histo2d(("hDen_el", "Electron fake rate denominator;p_{T} [GeV];#eta",len(pt_bins)-1, ROOT.std.vector('double')(pt_bins),len(etabinsel)-1, ROOT.std.vector('double')(etabinsel)),"lep_pt","lep_eta")

  h_all = a_loose.Histo2D(("h_all", "All probes", len(ptbins)-1, ptbins, len(etabins)-1, etabins), "probe_pt", "probe_eta")
  h_tight = a_tight.Histo2D(("h_tight", "Tight probes", len(ptbins)-1, ptbins, len(etabins)-1, etabins), "probe_pt", "probe_eta")
  columns = []

  za_loose = zbj
  za_tight = za_loose.Cut("probe_tight","probe_isTight")

  zh_all = za_loose.Histo2D(("zh_all", "All probes", len(ptbins)-1, ptbins, len(etabins)-1, etabins), "probe_pt", "probe_eta")
  zh_tight = za_tight.Histo2D(("zh_tight", "Tight probes", len(ptbins)-1, ptbins, len(etabins)-1, etabins), "probe_pt", "probe_eta")
  columns = []


  for col in allColumns:
     if ("P4" in col) or ("cleanedJets" in col) or ("cleanFatJets" in col) or ("cleanMets" in col) or ("Dummy" in col): continue
     if ("LHE" in col) and ("Weight" not in col) and (col != "LHE_HT") and (col != "LHE_Vpt") and (col != "gcHTCorr_WjetLHE"): continue
     if col.startswith("Muon") and ("_tightId" not in col) and ("_isPF" not in col) and ("tunep" not in col) and ("genPartFlav" not in col): continue
     if col.startswith("Electron") and ("genPartFlav" not in col): continue
     if col.startswith("Jet") and ("rawFactor" not in col): continue
     if col.startswith("FatJet") and ("rawFactor" not in col): continue
     if col.startswith("PPS") or col.startswith("Proton") or col.startswith("L1_"): continue
     if col.startswith("Gen") or col.startswith("Soft") or col.startswith("fixed"): continue
     if col.startswith("Sub")  or col.startswith("Calo") or col.startswith("Chs"): continue
     if col.startswith("Corr") or col.startswith("Fsr") or col.startswith("Iso") or col.startswith("Tau"): continue
     if col.startswith("SV") or col.startswith("Photon") or col.startswith("Low"): continue
     if col.startswith("HLT") or col.startswith("HT") or col.startswith("boosted") or col.startswith("Deep"): continue
     if col.startswith("Flag") or col == "Bprime_gen_info" or col == "t_gen_info" or col == "W_gen_info" or col == "metxyoutput": continue
     if col == "assignleps" or col == "pnetoutput" or col == "t_output" or col == "Bprime_output" or col.startswith("Other"): continue
     if col.startswith("PS") or col.startswith("Tk") or col.startswith("Trig"): continue
     if col.startswith("nCorr") or col.startswith("nFsr"): continue
     if col.startswith("nGen") or col.startswith("nIso") or col.startswith("nLow"): continue
     if col.startswith("nOther") or col.startswith("nPS") or col.startswith("nPhoton"): continue
     if col.startswith("nSV") or col.startswith("nSub") or col.startswith("nTau") or col.startswith("nTrig"): continue
     if col.startswith("nboosted"): continue
     if col == "tauBUG": continue
     if col == "Matching": continue
     if col == "ObjectList": continue
     if col == "manual": continue
     if col.startswith("BeamSpot"): continue
     if col.startswith("Lepton"): continue
     if col.startswith("iLepton"): continue
     if col.startswith("MET"): continue
     if col.startswith("RawMET"): continue

     columns.append(col)


  finalFile = sample + era + "_" + year + "_" + str(testNum1) + ".root"
  if not isMC:
    finalFile = sample + era + ver + "_" + year + "_" + str(testNum1) + ".root";

  mode = 'RECREATE'
  if jesvar != "Nominal":
    mode = 'UPDATE'
  #print('\n(1)\n')
  #sys.setprofile(trace_calls)
  a.Snapshot(columns, finalFile, "Events_"+jesvar, lazy=False, openOption=mode, saveRunChain=True)
  #print('\n(2)\n')

  outFile = TFile.Open(finalFile, "UPDATE")

  h_all.GetValue().SetName("ttbar_h_all")
  h_tight.GetValue().SetName("ttbar_h_tight")
  h_all.GetValue().Write()
  h_tight.GetValue().Write()

  zh_all.GetValue().SetName("zbj_h_all")
  zh_tight.GetValue().SetName("zbj_h_tight")
  zh_all.GetValue().Write()
  zh_tight.GetValue().Write()

  outFile.Close()

  if jesvar == "Nominal":
    print("Cut statistics:")
    rep = a.DataFrame.Report()
    rep.Print()

  print("--------- Analysis End ---------")

  a.Close()

if not isMC:
  analyze("Nominal")
else:
  analyze("Nominal")
  #TODO fix why this not work?  shifts = ["Nominal","JECup","JECdn","JERup","JERdn"]
  #for shift in shifts:
  #  analyze(shift)

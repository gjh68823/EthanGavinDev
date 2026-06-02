import os 

class sample:
    def __init__(self, prefix, xsec, year, textlist, samplename): #, color
        self.prefix = prefix
        self.year = year
        self.textlist = textlist
        self.samplename = samplename
        self.xsec = xsec # in pb

# Update the following block (Bprime), we need our Bprime samples (copy from Timber repo)
Bprime_M1000_2022 = sample("Bprime_M1000_2022", 1.0, "2022", "Bprime_M1000_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1000_2022EE = sample("Bprime_M1000_2022EE", 1.0, "2022EE", "Bprime_M1000_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1000_2023 = sample("Bprime_M1000_2023", 1.0, "2023", "Bprime_M1000_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1000_2023BPix = sample("Bprime_M1000_2023BPix", 1.0, "2023BPix", "Bprime_M1000_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1300_2022 = sample("Bprime_M1300_2022", 1.0, "2022", "Bprime_M1300_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1300_2022EE = sample("Bprime_M1300_2022EE", 1.0, "2022EE", "Bprime_M1300_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1300_2023 = sample("Bprime_M1300_2023", 1.0, "2023", "Bprime_M1300_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1300_2023BPix = sample("Bprime_M1300_2023BPix", 1.0, "2023BPix", "Bprime_M1300_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1600_2022 = sample("Bprime_M1600_2022", 1.0, "2022", "Bprime_M1600_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1600_2022EE = sample("Bprime_M1600_2022EE", 1.0, "2022EE", "Bprime_M1600_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1600_2023 = sample("Bprime_M1600_2023", 1.0, "2023", "Bprime_M1600_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1600_2023BPix = sample("Bprime_M1600_2023BPix", 1.0, "2023BPix", "Bprime_M1600_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M700_2022 = sample("Bprime_M700_2022", 1.0, "2022", "Bprime_M700_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M700_2022EE = sample("Bprime_M700_2022EE", 1.0, "2022EE", "Bprime_M700_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M700_2023 = sample("Bprime_M700_2023", 1.0, "2023", "Bprime_M700_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M700_2023BPix = sample("Bprime_M700_2023BPix", 1.0, "2023BPix", "Bprime_M700_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M400_2022 = sample("Bprime_M400_2022", 1.0, "2022", "Bprime_M400_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M400_2022EE = sample("Bprime_M400_2022EE", 1.0, "2022EE", "Bprime_M400_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M400_2023 = sample("Bprime_M400_2023", 1.0, "2023", "Bprime_M400_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M400_2023BPix = sample("Bprime_M400_2023BPix", 1.0, "2023BPix", "Bprime_M400_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

SingleElecRun2022C = sample("SingleElecRun2022C", 1.0, "2022", "SingleElecRun2022C2022NanoList.txt", "/EGamma/Run2022C-22Sep2023-v1/NANOAOD")
SingleElecRun2022D = sample("SingleElecRun2022D", 1.0, "2022", "SingleElecRun2022D2022NanoList.txt", "/EGamma/Run2022D-22Sep2023-v1/NANOAOD")
SingleElecRun2022EEE  = sample("SingleElecRun2022EEE", 1.0, "2022EE", "SingleElecRun2022EEE2022EENanoList.txt", "/EGamma/Run2022E-22Sep2023-v1/NANOAOD")
SingleElecRun2022EEF  = sample("SingleElecRun2022EEF", 1.0, "2022EE", "SingleElecRun2022EEF2022EENanoList.txt", "/EGamma/Run2022F-22Sep2023-v1/NANOAOD")
SingleElecRun2022EEG  = sample("SingleElecRun2022EEG", 1.0, "2022EE", "SingleElecRun2022EEG2022EENanoList.txt", "/EGamma/Run2022G-22Sep2023-v2/NANOAOD")
SingleElecRun2023C01  = sample("SingleElecRun2023C01", 1.0, "2023", "SingleElecRun2023C012023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023C02  = sample("SingleElecRun2023C02", 1.0, "2023", "SingleElecRun2023C022023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2023C03  = sample("SingleElecRun2023C03", 1.0, "2023", "SingleElecRun2023C032023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleElecRun2023C04  = sample("SingleElecRun2023C04", 1.0, "2023", "SingleElecRun2023C042023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD")
SingleElecRun2023C11  = sample("SingleElecRun2023C11", 1.0, "2023", "SingleElecRun2023C112023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023C12  = sample("SingleElecRun2023C12", 1.0, "2023", "SingleElecRun2023C122023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2023C13  = sample("SingleElecRun2023C13", 1.0, "2023", "SingleElecRun2023C132023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleElecRun2023C14  = sample("SingleElecRun2023C14", 1.0, "2023", "SingleElecRun2023C142023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD")
SingleElecRun2023BPixD01  = sample("SingleElecRun2023BPixD01", 1.0, "2023BPix", "SingleElecRun2023BPixD012023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023BPixD02  = sample("SingleElecRun2023BPixD02", 1.0, "2023BPix", "SingleElecRun2023BPixD022023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2023BPixD11  = sample("SingleElecRun2023BPixD11", 1.0, "2023BPix", "SingleElecRun2023BPixD112023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023BPixD12  = sample("SingleElecRun2023BPixD12", 1.0, "2023BPix", "SingleElecRun2023BPixD122023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2024C0 = sample("SingleElecRun2024C0", 1.0, "2024", "SingleElecRun2024C0NanoList.txt","/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024D0 = sample("SingleElecRun2024D0", 1.0, "2024", "SingleElecRun2024D0NanoList.txt","/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024E0 = sample("SingleElecRun2024E0", 1.0, "2024", "SingleElecRun2024E0NanoList.txt","/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024F0 = sample("SingleElecRun2024F0", 1.0, "2024", "SingleElecRun2024F0NanoList.txt","/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024G0 = sample("SingleElecRun2024G0", 1.0, "2024", "SingleElecRun2024G0NanoList.txt","/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD")
SingleElecRun2024H0 = sample("SingleElecRun2024H0", 1.0, "2024", "SingleElecRun2024H0NanoList.txt","/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD")
SingleElecRun2024I01 = sample("SingleElecRun2024I01", 1.0, "2024", "SingleElecRun2024I01NanoList.txt","/EGamma0/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024I02 = sample("SingleElecRun2024I02", 1.0, "2024", "SingleElecRun2024I02NanoList.txt","/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
SingleElecRun2024C1 = sample("SingleElecRun2024C1", 1.0, "2024", "SingleElecRun2024C1NanoList.txt","/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024D1 = sample("SingleElecRun2024D1", 1.0, "2024", "SingleElecRun2024D1NanoList.txt","/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024E1 = sample("SingleElecRun2024E1", 1.0, "2024", "SingleElecRun2024E1NanoList.txt","/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024F1 = sample("SingleElecRun2024F1", 1.0, "2024", "SingleElecRun2024F1NanoList.txt","/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024G1 = sample("SingleElecRun2024G1", 1.0, "2024", "SingleElecRun2024G1NanoList.txt","/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD")
SingleElecRun2024H1 = sample("SingleElecRun2024H1", 1.0, "2024", "SingleElecRun2024H1NanoList.txt","/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024I11 = sample("SingleElecRun2024I11", 1.0, "2024", "SingleElecRun2024I11NanoList.txt","/EGamma1/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024I12 = sample("SingleElecRun2024I12", 1.0, "2024", "SingleElecRun2024I12NanoList.txt","/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")

SingleMuonRun2022C = sample("SingleMuonRun2022C", 1.0, "2022", "SingleMuonRun2022C2022NanoList.txt", "/Muon/Run2022C-22Sep2023-v1/NANOAOD")
SingleMuonRun2022D = sample("SingleMuonRun2022D", 1.0, "2022", "SingleMuonRun2022D2022NanoList.txt", "/Muon/Run2022D-22Sep2023-v1/NANOAOD")
SingleMuonRun2022EEE  = sample("SingleMuonRun2022EEE", 1.0, "2022EE", "SingleMuonRun2022EEE2022EENanoList.txt", "/Muon/Run2022E-22Sep2023-v1/NANOAOD")
SingleMuonRun2022EEF  = sample("SingleMuonRun2022EEF", 1.0, "2022EE", "SingleMuonRun2022EEF2022EENanoList.txt", "/Muon/Run2022F-22Sep2023-v2/NANOAOD")
SingleMuonRun2022EEG  = sample("SingleMuonRun2022EEG", 1.0, "2022EE", "SingleMuonRun2022EEG2022EENanoList.txt", "/Muon/Run2022G-22Sep2023-v1/NANOAOD")
SingleMuonRun2023C01  = sample("SingleMuonRun2023C01", 1.0, "2023", "SingleMuonRun2023C012023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023C02  = sample("SingleMuonRun2023C02", 1.0, "2023", "SingleMuonRun2023C022023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2023C03  = sample("SingleMuonRun2023C03", 1.0, "2023", "SingleMuonRun2023C032023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleMuonRun2023C04  = sample("SingleMuonRun2023C04", 1.0, "2023", "SingleMuonRun2023C042023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD")
SingleMuonRun2023C11  = sample("SingleMuonRun2023C11", 1.0, "2023", "SingleMuonRun2023C112023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023C12  = sample("SingleMuonRun2023C12", 1.0, "2023", "SingleMuonRun2023C122023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2023C13  = sample("SingleMuonRun2023C13", 1.0, "2023", "SingleMuonRun2023C132023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleMuonRun2023C14  = sample("SingleMuonRun2023C14", 1.0, "2023", "SingleMuonRun2023C142023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD")
SingleMuonRun2023BPixD01  = sample("SingleMuonRun2023BPixD01", 1.0, "2023BPix", "SingleMuonRun2023BPixD012023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023BPixD02  = sample("SingleMuonRun2023BPixD02", 1.0, "2023BPix", "SingleMuonRun2023BPixD022023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2023BPixD11  = sample("SingleMuonRun2023BPixD11", 1.0, "2023BPix", "SingleMuonRun2023BPixD112023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023BPixD12  = sample("SingleMuonRun2023BPixD12", 1.0, "2023BPix", "SingleMuonRun2023BPixD122023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2024C0 = sample("SingleMuonRun2024C0", 1.0, "2024", "SingleMuonRun2024C0NanoList.txt","/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024D0 = sample("SingleMuonRun2024D0", 1.0, "2024", "SingleMuonRun2024D0NanoList.txt","/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024E0 = sample("SingleMuonRun2024E0", 1.0, "2024", "SingleMuonRun2024E0NanoList.txt","/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024F0 = sample("SingleMuonRun2024F0", 1.0, "2024", "SingleMuonRun2024F0NanoList.txt","/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024G0 = sample("SingleMuonRun2024G0", 1.0, "2024", "SingleMuonRun2024G0NanoList.txt","/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024H0 = sample("SingleMuonRun2024H0", 1.0, "2024", "SingleMuonRun2024H0NanoList.txt","/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024I01 = sample("SingleMuonRun2024I01", 1.0, "2024", "SingleMuonRun2024I01NanoList.txt","/Muon0/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024I02 = sample("SingleMuonRun2024I02", 1.0, "2024", "SingleMuonRun2024I02NanoList.txt","/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
SingleMuonRun2024C1 = sample("SingleMuonRun2024C1", 1.0, "2024", "SingleMuonRun2024C1NanoList.txt","/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024D1 = sample("SingleMuonRun2024D1", 1.0, "2024", "SingleMuonRun2024D1NanoList.txt","/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024E1 = sample("SingleMuonRun2024E1", 1.0, "2024", "SingleMuonRun2024E1NanoList.txt","/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024F1 = sample("SingleMuonRun2024F1", 1.0, "2024", "SingleMuonRun2024F1NanoList.txt","/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024G1 = sample("SingleMuonRun2024G1", 1.0, "2024", "SingleMuonRun2024G1NanoList.txt","/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD")
SingleMuonRun2024H1 = sample("SingleMuonRun2024H1", 1.0, "2024", "SingleMuonRun2024H1NanoList.txt","/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD")
SingleMuonRun2024I11 = sample("SingleMuonRun2024I11", 1.0, "2024", "SingleMuonRun2024I11NanoList.txt","/Muon1/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024I12 = sample("SingleMuonRun2024I12", 1.0, "2024", "SingleMuonRun2024I12NanoList.txt","/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")

MuonEGRun2022C = sample("MuonEGRun2022C", 1.0, "2022", "MuonEGRun2022C2022NanoList.txt", "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD")
MuonEGRun2022D = sample("MuonEGRun2022D", 1.0, "2022", "MuonEGRun2022D2022NanoList.txt", "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD")
MuonEGRun2022EEE  = sample("MuonEGRun2022EEE", 1.0, "2022EE", "MuonEGRun2022EEE2022EENanoList.txt", "/MuonEG/Run2022E-22Sep2023-v1/NANOAOD")
MuonEGRun2022EEF  = sample("MuonEGRun2022EEF", 1.0, "2022EE", "MuonEGRun2022EEF2022EENanoList.txt", "/MuonEG/Run2022F-22Sep2023-v1/NANOAOD")
MuonEGRun2022EEG  = sample("MuonEGRun2022EEG", 1.0, "2022EE", "MuonEGRun2022EEG2022EENanoList.txt", "/MuonEG/Run2022G-22Sep2023-v1/NANOAOD")
MuonEGRun2023C01  = sample("MuonEGRun2023C01", 1.0, "2023", "MuonEGRun2023C012023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v1-v1/NANOAOD")
MuonEGRun2023C02  = sample("MuonEGRun2023C02", 1.0, "2023", "MuonEGRun2023C022023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v2-v1/NANOAOD")
MuonEGRun2023C03  = sample("MuonEGRun2023C03", 1.0, "2023", "MuonEGRun2023C032023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v3-v1/NANOAOD")
MuonEGRun2023C04  = sample("MuonEGRun2023C04", 1.0, "2023", "MuonEGRun2023C042023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD")
MuonEGRun2023BPixD01  = sample("MuonEGRun2023BPixD01", 1.0, "2023BPix", "MuonEGRun2023BPixD012023BPixNanoList.txt", "/MuonEG/Run2023D-22Sep2023_v1-v1/NANOAOD")
MuonEGRun2023BPixD02  = sample("MuonEGRun2023BPixD02", 1.0, "2023BPix", "MuonEGRun2023BPixD022023BPixNanoList.txt", "/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD")

TauRun2022C = sample("TauRun2022C", 1.0, "2022", "TauRun2022C2022NanoList.txt", "/Tau/Run2022C-22Sep2023-v1/NANOAOD")
TauRun2022D = sample("TauRun2022D", 1.0, "2022", "TauRun2022D2022NanoList.txt", "/Tau/Run2022D-22Sep2023-v1/NANOAOD")
TauRun2022EEE  = sample("TauRun2022EEE", 1.0, "2022EE", "TauRun2022EEE2022EENanoList.txt", "/Tau/Run2022E-22Sep2023-v1/NANOAOD")
TauRun2022EEF  = sample("TauRun2022EEF", 1.0, "2022EE", "TauRun2022EEF2022EENanoList.txt", "/Tau/Run2022F-22Sep2023-v1/NANOAOD")
TauRun2022EEG  = sample("TauRun2022EEG", 1.0, "2022EE", "TauRun2022EEG2022EENanoList.txt", "/Tau/Run2022G-22Sep2023-v1/NANOAOD")
TauRun2023C01  = sample("TauRun2023C01", 1.0, "2023", "TauRun2023C012023NanoList.txt", "/Tau/Run2023C-22Sep2023_v1-v2/NANOAOD")
TauRun2023C02  = sample("TauRun2023C02", 1.0, "2023", "TauRun2023C022023NanoList.txt", "/Tau/Run2023C-22Sep2023_v2-v1/NANOAOD")
TauRun2023C03  = sample("TauRun2023C03", 1.0, "2023", "TauRun2023C032023NanoList.txt", "/Tau/Run2023C-22Sep2023_v3-v1/NANOAOD")
TauRun2023C04  = sample("TauRun2023C04", 1.0, "2023", "TauRun2023C042023NanoList.txt", "/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD")
TauRun2023BPixD01  = sample("TauRun2023BPixD01", 1.0, "2023BPix", "TauRun2023BPixD012023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v1-v1/NANOAOD")
TauRun2023BPixD02  = sample("TauRun2023BPixD02", 1.0, "2023BPix", "TauRun2023BPixD022023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD")

NonpromptSingleElecRun2022C = sample("NonpromptSingleElecRun2022C", 1.0, "2022", "SingleElecRun2022C2022NanoList.txt", "/EGamma/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptSingleElecRun2022D = sample("NonpromptSingleElecRun2022D", 1.0, "2022", "SingleElecRun2022D2022NanoList.txt", "/EGamma/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptSingleElecRun2022EEE  = sample("NonpromptSingleElecRun2022EEE", 1.0, "2022EE", "SingleElecRun2022EEE2022EENanoList.txt", "/EGamma/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptSingleElecRun2022EEF  = sample("NonpromptSingleElecRun2022EEF", 1.0, "2022EE", "SingleElecRun2022EEF2022EENanoList.txt", "/EGamma/Run2022F-22Sep2023-v1/NANOAOD")
NonpromptSingleElecRun2022EEG  = sample("NonpromptSingleElecRun2022EEG", 1.0, "2022EE", "SingleElecRun2022EEG2022EENanoList.txt", "/EGamma/Run2022G-22Sep2023-v2/NANOAOD")
NonpromptSingleElecRun2023C01  = sample("NonpromptSingleElecRun2023C01", 1.0, "2023", "SingleElecRun2023C012023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleElecRun2023C02  = sample("NonpromptSingleElecRun2023C02", 1.0, "2023", "SingleElecRun2023C022023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleElecRun2023C03  = sample("NonpromptSingleElecRun2023C03", 1.0, "2023", "SingleElecRun2023C032023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptSingleElecRun2023C04  = sample("NonpromptSingleElecRun2023C04", 1.0, "2023", "SingleElecRun2023C042023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptSingleElecRun2023C11  = sample("NonpromptSingleElecRun2023C11", 1.0, "2023", "SingleElecRun2023C112023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleElecRun2023C12  = sample("NonpromptSingleElecRun2023C12", 1.0, "2023", "SingleElecRun2023C122023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleElecRun2023C13  = sample("NonpromptSingleElecRun2023C13", 1.0, "2023", "SingleElecRun2023C132023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptSingleElecRun2023C14  = sample("NonpromptSingleElecRun2023C14", 1.0, "2023", "SingleElecRun2023C142023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD01  = sample("NonpromptSingleElecRun2023BPixD01", 1.0, "2023BPix", "SingleElecRun2023BPixD012023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD02  = sample("NonpromptSingleElecRun2023BPixD02", 1.0, "2023BPix", "SingleElecRun2023BPixD022023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD11  = sample("NonpromptSingleElecRun2023BPixD11", 1.0, "2023BPix", "SingleElecRun2023BPixD112023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD12  = sample("NonpromptSingleElecRun2023BPixD12", 1.0, "2023BPix", "SingleElecRun2023BPixD122023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v2-v1/NANOAOD")

NonpromptSingleMuonRun2022C = sample("NonpromptSingleMuonRun2022C", 1.0, "2022", "SingleMuonRun2022C2022NanoList.txt", "/Muon/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptSingleMuonRun2022D = sample("NonpromptSingleMuonRun2022D", 1.0, "2022", "SingleMuonRun2022D2022NanoList.txt", "/Muon/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptSingleMuonRun2022EEE  = sample("NonpromptSingleMuonRun2022EEE", 1.0, "2022EE", "SingleMuonRun2022EEE2022EENanoList.txt", "/Muon/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptSingleMuonRun2022EEF  = sample("NonpromptSingleMuonRun2022EEF", 1.0, "2022EE", "SingleMuonRun2022EEF2022EENanoList.txt", "/Muon/Run2022F-22Sep2023-v2/NANOAOD")
NonpromptSingleMuonRun2022EEG  = sample("NonpromptSingleMuonRun2022EEG", 1.0, "2022EE", "SingleMuonRun2022EEG2022EENanoList.txt", "/Muon/Run2022G-22Sep2023-v1/NANOAOD")
NonpromptSingleMuonRun2023C01  = sample("NonpromptSingleMuonRun2023C01", 1.0, "2023", "SingleMuonRun2023C012023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleMuonRun2023C02  = sample("NonpromptSingleMuonRun2023C02", 1.0, "2023", "SingleMuonRun2023C022023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleMuonRun2023C03  = sample("NonpromptSingleMuonRun2023C03", 1.0, "2023", "SingleMuonRun2023C032023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptSingleMuonRun2023C04  = sample("NonpromptSingleMuonRun2023C04", 1.0, "2023", "SingleMuonRun2023C042023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptSingleMuonRun2023C11  = sample("NonpromptSingleMuonRun2023C11", 1.0, "2023", "SingleMuonRun2023C112023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleMuonRun2023C12  = sample("NonpromptSingleMuonRun2023C12", 1.0, "2023", "SingleMuonRun2023C122023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleMuonRun2023C13  = sample("NonpromptSingleMuonRun2023C13", 1.0, "2023", "SingleMuonRun2023C132023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptSingleMuonRun2023C14  = sample("NonpromptSingleMuonRun2023C14", 1.0, "2023", "SingleMuonRun2023C142023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD")
NonpromptSingleMuonRun2023BPixD01  = sample("NonpromptSingleMuonRun2023BPixD01", 1.0, "2023BPix", "SingleMuonRun2023BPixD012023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleMuonRun2023BPixD02  = sample("NonpromptSingleMuonRun2023BPixD02", 1.0, "2023BPix", "SingleMuonRun2023BPixD022023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleMuonRun2023BPixD11  = sample("NonpromptSingleMuonRun2023BPixD11", 1.0, "2023BPix", "SingleMuonRun2023BPixD112023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleMuonRun2023BPixD12  = sample("NonpromptSingleMuonRun2023BPixD12", 1.0, "2023BPix", "SingleMuonRun2023BPixD122023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD")

NonpromptMuonEGRun2022C = sample("NonpromptMuonEGRun2022C", 1.0, "2022", "MuonEGRun2022C2022NanoList.txt", "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022D = sample("NonpromptMuonEGRun2022D", 1.0, "2022", "MuonEGRun2022D2022NanoList.txt", "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022EEE  = sample("NonpromptMuonEGRun2022EEE", 1.0, "2022EE", "MuonEGRun2022EEE2022EENanoList.txt", "/MuonEG/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022EEF  = sample("NonpromptMuonEGRun2022EEF", 1.0, "2022EE", "MuonEGRun2022EEF2022EENanoList.txt", "/MuonEG/Run2022F-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022EEG  = sample("NonpromptMuonEGRun2022EEG", 1.0, "2022EE", "MuonEGRun2022EEG2022EENanoList.txt", "/MuonEG/Run2022G-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2023C01  = sample("NonpromptMuonEGRun2023C01", 1.0, "2023", "MuonEGRun2023C012023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptMuonEGRun2023C02  = sample("NonpromptMuonEGRun2023C02", 1.0, "2023", "MuonEGRun2023C022023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptMuonEGRun2023C03  = sample("NonpromptMuonEGRun2023C03", 1.0, "2023", "MuonEGRun2023C032023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptMuonEGRun2023C04  = sample("NonpromptMuonEGRun2023C04", 1.0, "2023", "MuonEGRun2023C042023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptMuonEGRun2023BPixD01  = sample("NonpromptMuonEGRun2023BPixD01", 1.0, "2023BPix", "MuonEGRun2023BPixD012023BPixNanoList.txt", "/MuonEG/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptMuonEGRun2023BPixD02  = sample("NonpromptMuonEGRun2023BPixD02", 1.0, "2023BPix", "MuonEGRun2023BPixD022023BPixNanoList.txt", "/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD")

NonpromptTauRun2022C = sample("NonpromptTauRun2022C", 1.0, "2022", "TauRun2022C2022NanoList.txt", "/Tau/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022D = sample("NonpromptTauRun2022D", 1.0, "2022", "TauRun2022D2022NanoList.txt", "/Tau/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022EEE  = sample("NonpromptTauRun2022EEE", 1.0, "2022EE", "TauRun2022EEE2022EENanoList.txt", "/Tau/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022EEF  = sample("NonpromptTauRun2022EEF", 1.0, "2022EE", "TauRun2022EEF2022EENanoList.txt", "/Tau/Run2022F-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022EEG  = sample("NonpromptTauRun2022EEG", 1.0, "2022EE", "TauRun2022EEG2022EENanoList.txt", "/Tau/Run2022G-22Sep2023-v1/NANOAOD")
NonpromptTauRun2023C01  = sample("NonpromptTauRun2023C01", 1.0, "2023", "TauRun2023C012023NanoList.txt", "/Tau/Run2023C-22Sep2023_v1-v2/NANOAOD")
NonpromptTauRun2023C02  = sample("NonpromptTauRun2023C02", 1.0, "2023", "TauRun2023C022023NanoList.txt", "/Tau/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptTauRun2023C03  = sample("NonpromptTauRun2023C03", 1.0, "2023", "TauRun2023C032023NanoList.txt", "/Tau/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptTauRun2023C04  = sample("NonpromptTauRun2023C04", 1.0, "2023", "TauRun2023C042023NanoList.txt", "/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptTauRun2023BPixD01  = sample("NonpromptTauRun2023BPixD01", 1.0, "2023BPix", "TauRun2023BPixD012023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptTauRun2023BPixD02  = sample("NonpromptTauRun2023BPixD02", 1.0, "2023BPix", "TauRun2023BPixD022023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD")

# diboson 3L and 4L
WZ3L2022 = sample("WZ3L2022", 4.924, "2022", "WZ3L2022NanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZ3L2022ext = sample("WZ3L2022ext", 4.924, "2022", "WZ3L2022extNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM")
WZ3L2022EE = sample("WZ3L2022EE", 4.924, "2022EE", "WZ3L2022EENanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZ3L2022EEext = sample("WZ3L2022EEext", 4.924, "2022EE", "WZ3L2022EEextNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WZ3L2023 = sample("WZ3L2023", 4.924, "2023", "WZ3L2023NanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WZ3L2023ext = sample("WZ3L2023ext", 4.924, "2023", "WZ3L2023extNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15_ext1-v2/NANOAODSIM")
WZ3L2023BPix = sample("WZ3L2023BPix", 4.924, "2023BPix", "WZ3L2023BPixNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WZ3L2023BPixext = sample("WZ3L2023BPixext", 4.924, "2023BPix", "WZ3L2023BPixextNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM")
ZZ4L2022 = sample("ZZ4L2022", 1.39, "2022", "ZZ4L2022NanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZ4L2022ext = sample("ZZ4L2022ext", 1.39, "2022", "ZZ4L2022extNanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
ZZ4L2022EE = sample("ZZ4L2022EE", 1.39, "2022EE", "ZZ4L2022EENanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZ4L2022EEext = sample("ZZ4L2022EEext", 1.39, "2022EE", "ZZ4L2022EEextNanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
ZZ4L2023 = sample("ZZ4L2023", 1.39, "2023", "ZZ4L2023NanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
ZZ4L2023BPix = sample("ZZ4L2023BPix", 1.39, "2023BPix", "ZZ4L2023BPixNanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")

# xsec from H+ -> WA preapp
VHnonbb2022     = sample("VHnonbb2022", 1.0132, "2022", "VHnonbb2022.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM")
VHnonbb2022EE   = sample("VHnonbb2022EE", 1.0132, "2022EE", "VHnonbb2022EE.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM")
VHnonbb2023     = sample("VHnonbb2023", 1.0132, "2023", "VHnonbb2023.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
VHnonbb2023BPix = sample("VHnonbb2023BPix", 1.0132, "2023BPix", "VHnonbb2023BPix.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# triboson
WWW2022     = sample("WWW2022", 0.2328, "2022", "WWW2022.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWW2022EE   = sample("WWW2022EE", 0.2328, "2022EE", "WWW2022EE.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWW2023     = sample("WWW2023", 0.2328, "2023", "WWW2023.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WWW2023BPix = sample("WWW2023BPix", 0.2328, "2023BPix", "WWW2023BPix.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WWZ2022     = sample("WWZ2022", 0.1851, "2022", "WWZ2022.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZ2022EE   = sample("WWZ2022EE", 0.1851, "2022EE", "WWZ2022EE.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZ2023     = sample("WWZ2023", 0.1851, "2023", "WWZ2023.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WWZ2023BPix = sample("WWZ2023BPix", 0.1851, "2023BPix", "WWZ2023BPix.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WWZ4L2022     = sample("WWZ4L2022", 0.002244, "2022", "WWZ4L2022.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZ4L2022EE   = sample("WWZ4L2022EE", 0.002244, "2022EE", "WWZ4L2022EE.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZ4L2023     = sample("WWZ4L2023", 0.002244, "2023", "WWZ4L2023.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZ4L2023BPix = sample("WWZ4L2023BPix", 0.002244, "2023BPix", "WWZ4L2023BPix.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

WZZ2022     = sample("WZZ2022", 0.06206, "2022", "WZZ2022.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZZ2022EE   = sample("WZZ2022EE", 0.06206, "2022EE", "WZZ2022EE.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZZ2023     = sample("WZZ2023", 0.06206, "2023", "WZZ2023.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WZZ2023BPix = sample("WZZ2023BPix", 0.06206, "2023BPix", "WZZ2023BPix.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
ZZZ2022     = sample("ZZZ2022", 0.01591, "2022", "ZZZ2022.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZZ2022EE   = sample("ZZZ2022EE", 0.01591, "2022EE", "ZZZ2022EE.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZZ2023     = sample("ZZZ2023", 0.01591, "2023", "ZZZ2023.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
ZZZ2023BPix = sample("ZZZ2023BPix", 0.01591, "2023BPix", "ZZZ2023BPix.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")

# 4 bosons
WWZZ3L2022     = sample("WWZZ3L2022", 0.0004888, "2022", "WWZZ3L2022NanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZZ3L2022EE   = sample("WWZZ3L2022EE", 0.0004888, "2022EE", "WWZZ3L2022EENanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZZ3L2023     = sample("WWZZ3L2023", 0.0004888, "2023", "WWZZ3L2023NanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZZ3L2023BPix = sample("WWZZ3L2023BPix", 0.0004888, "2023BPix", "WWZZ3L2023BPixNanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WWZZ4L2022     = sample("WWZZ4L2022", 0.0004888, "2022", "WWZZ4L2022NanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZZ4L2022EE   = sample("WWZZ4L2022EE", 0.0004888, "2022EE", "WWZZ4L2022EENanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZZ4L2023     = sample("WWZZ4L2023", 0.0004888, "2023", "WWZZ4L2023NanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZZ4L2023BPix = sample("WWZZ4L2023BPix", 0.0004888, "2023BPix", "WWZZ4L2023BPixNanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# Photon conversions
ZG2J2022     = sample("ZG2J2022", 0.1136, "2022", "ZG2J2022NanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_withDipoleRecoil_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZG2J2022EE   = sample("ZG2J2022EE", 0.1136, "2022EE", "ZG2J2022EENanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_withDipoleRecoil_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
ZG2J2023     = sample("ZG2J2023", 0.1136, "2023", "ZG2J2023NanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
ZG2J2023BPix = sample("ZG2J2023BPix", 0.1136, "2023BPix", "ZG2J2023BPixNanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTG1Jpt102022     = sample("TTG1Jpt102022", 4.216, "2022", "TTG1Jpt102022NanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM")
TTG1Jpt102022EE   = sample("TTG1Jpt102022EE", 4.216, "2022EE", "TTG1Jpt102022EENanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM")
TTG1Jpt102023     = sample("TTG1Jpt102023", 4.216, "2023", "TTG1Jpt102023NanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTG1Jpt102023BPix = sample("TTG1Jpt102023BPix", 4.216, "2023BPix", "TTG1Jpt102023BPixNanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTG1Jpt1002022     = sample("TTG1Jpt1002022", 0.4114, "2022", "TTG1Jpt1002022NanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
TTG1Jpt1002022EE   = sample("TTG1Jpt1002022EE", 0.4114, "2022EE", "TTG1Jpt1002022EENanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTG1Jpt1002023     = sample("TTG1Jpt1002023", 0.4114, "2023", "TTG1Jpt1002023NanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTG1Jpt1002023BPix = sample("TTG1Jpt1002023BPix", 0.4114, "2023BPix", "TTG1Jpt1002023BPixNanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTG1Jpt2002022     = sample("TTG1Jpt2002022", 0.1284, "2022", "TTG1Jpt2002022NanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
TTG1Jpt2002022EE   = sample("TTG1Jpt2002022EE", 0.1284, "2022EE", "TTG1Jpt2002022EENanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTG1Jpt2002023     = sample("TTG1Jpt2002023", 0.1284, "2023", "TTG1Jpt2002023NanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTG1Jpt2002023BPix = sample("TTG1Jpt2002023BPix", 0.1284, "2023BPix", "TTG1Jpt2002023BPixNanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# t+Z/y
TZQB2022     = sample("TZQB2022", 0.07968, "2022", "TZQB2022NanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TZQB2022EE   = sample("TZQB2022EE", 0.07968, "2022EE", "TZQB2022EENanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TZQB2023     = sample("TZQB2023", 0.07968, "2023", "TZQB2023NanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TZQB2023BPix = sample("TZQB2023BPix", 0.07968, "2023BPix", "TZQB2023BPixNanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v3/NANOAODSIM")
3.873
TGQB2022     = sample("TGQB2022", 0.07968, "2022", "TGQB2022NanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TGQB2022EE   = sample("TGQB2022EE", 0.07968, "2022EE", "TGQB2022EENanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TGQB2023     = sample("TGQB2023", 0.07968, "2023", "TGQB2023NanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TGQB2023BPix = sample("TGQB2023BPix", 0.07968, "2023BPix", "TGQB2023BPixNanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# tt+X
TTHnonB2022 = sample("TTHnonB2022", 0.570*(1.0-0.5824), "2022", "TTHnonB2022NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM")
TTHnonB2022EE = sample("TTHnonB2022EE", 0.570*(1.0-0.05824), "2022EE", "TTHnonB2022EENanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTHnonB2023 = sample("TTHnonB2023", 0.570*(1.0-0.05824), "2023", "TTHnonB2023NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTHnonB2023BPix = sample("TTHnonB2023BPix", 0.570*(1.0-0.05824), "2023BPix", "TTHnonB2023BPixNanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")

TTWl2022 = sample("TTWl2022", 0.2505, "2022", "TTWl2022NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-mg35x_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWl2022EE = sample("TTWl2022EE", 0.2505, "2022EE", "TTWl2022EENanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-mg35x_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWl2023 = sample("TTWl2023", 0.2505, "2023", "TTWl2023NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-mg35x_130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWl2023BPix = sample("TTWl2023BPix", 0.2505, "2023BPix", "TTWl2023BPixNanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-mg35x_130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

TTZM42022 = sample("TTZM42022", 0.03949, "2022", "TTZM42022NanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZM42022EE = sample("TTZM42022EE", 0.03949, "2022EE", "TTZM42022EENanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTZM42023 = sample("TTZM42023",  0.03949,"2023", "TTZM42023NanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTZM42023BPix = sample("TTZM42023BPix", 0.03949, "2023BPix", "TTZM42023BPixNanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZM502022 = sample("TTZM502022", 0.08646, "2022", "TTZM502022NanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZM502022EE = sample("TTZM502022EE", 0.08646, "2022EE", "TTZM502022EENanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTZM502023 = sample("TTZM502023", 0.08646, "2023", "TTZM502023NanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTZM502023BPix = sample("TTZM502023BPix", 0.08646, "2023BPix", "TTZM502023BPixNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZM502022ext = sample("TTZM502022ext", 0.08646, "2022", "TTZM502022extNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM")
TTZM502022EEext = sample("TTZM502022EEext", 0.08646, "2022EE", "TTZM502022EEextNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
TTZM502023ext = sample("TTZM502023ext", 0.08646, "2023", "TTZM502023extNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15_ext1-v2/NANOAODSIM")
TTZM502023BPixext = sample("TTZM502023BPixext", 0.08646, "2023BPix", "TTZM502023BPixextNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM")

# tt + XX
TTWH2022     = sample("TTWH2022", 0.001252, "2022", "TTWH2022.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWH2022EE   = sample("TTWH2022EE", 0.001252, "2022EE", "TTWH2022EE.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWH2023     = sample("TTWH2023", 0.001252, "2023", "TTWH2023.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
TTWH2023BPix = sample("TTWH2023BPix", 0.001252, "2023BPix", "TTWH2023BPix.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTWW2022     = sample("TTWW2022", 0.008203, "2022", "TTWW2022.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWW2022EE   = sample("TTWW2022EE", 0.008203, "2022EE", "TTWW2022EE.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWW2023     = sample("TTWW2023", 0.008203, "2023", "TTWW2023.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWW2023BPix = sample("TTWW2023BPix", 0.008203, "2023BPix", "TTWW2023BPix.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTWZ2022     = sample("TTWZ2022", 0.002715, "2022", "TTWZ2022.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWZ2022EE   = sample("TTWZ2022EE", 0.002715, "2022EE", "TTWZ2022EE.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWZ2023     = sample("TTWZ2023", 0.002715, "2023", "TTWZ2023.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWZ2023BPix = sample("TTWZ2023BPix", 0.002715, "2023BPix", "TTWZ2023BPix.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZH2022     = sample("TTZH2022", 0.001288, "2022", "TTZH2022.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZH2022EE   = sample("TTZH2022EE", 0.001288, "2022EE", "TTZH2022EE.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTZH2023     = sample("TTZH2023", 0.001288, "2023", "TTZH2023.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
TTZH2023BPix = sample("TTZH2023BPix", 0.001288, "2023BPix", "TTZH2023BPix.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZZ2022     = sample("TTZZ2022", 0.001579, "2022", "TTZZ2022NanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZZ2022EE   = sample("TTZZ2022EE", 0.001579, "2022EE", "TTZZ2022EENanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTZZ2023     = sample("TTZZ2023", 0.001579, "2023", "TTZZ2023NanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM")
TTZZ2023BPix = sample("TTZZ2023BPix", 0.001579, "2023BPix", "TTZZ2023BPixNanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTTT2022     = sample("TTTT2022", 0.009652, "2022", "TTTT2022NanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTTT2022EE   = sample("TTTT2022EE", 0.009652, "2022EE", "TTTT2022EENanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM")
TTTT2023     = sample("TTTT2023", 0.009652, "2023", "TTTT2023NanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTTT2023BPix = sample("TTTT2023BPix", 0.009652, "2023BPix", "TTTT2023BPixNanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

samples_test = {
    "SingleElecRun2022C":      SingleElecRun2022C,
}

samples_data = {
    "SingleElecRun2022C":      SingleElecRun2022C,      
    "SingleElecRun2022D":      SingleElecRun2022D,      
    "SingleElecRun2022EEE":    SingleElecRun2022EEE,    
    "SingleElecRun2022EEF":    SingleElecRun2022EEF,    
    "SingleElecRun2022EEG":    SingleElecRun2022EEG,    
    "SingleElecRun2023C01":    SingleElecRun2023C01,    
    "SingleElecRun2023C02":    SingleElecRun2023C02,    
    "SingleElecRun2023C03":    SingleElecRun2023C03,    
    "SingleElecRun2023C04":    SingleElecRun2023C04,    
    "SingleElecRun2023C11":    SingleElecRun2023C11,    
    "SingleElecRun2023C12":    SingleElecRun2023C12,    
    "SingleElecRun2023C13":    SingleElecRun2023C13,    
    "SingleElecRun2023C14":    SingleElecRun2023C14,    
    "SingleElecRun2023BPixD01":SingleElecRun2023BPixD01,
    "SingleElecRun2023BPixD02":SingleElecRun2023BPixD02,
    "SingleElecRun2023BPixD11":SingleElecRun2023BPixD11,
    "SingleElecRun2023BPixD12":SingleElecRun2023BPixD12,
    "SingleMuonRun2022C":      SingleMuonRun2022C,      
    "SingleMuonRun2022D":      SingleMuonRun2022D,      
    "SingleMuonRun2022EEE":    SingleMuonRun2022EEE,    
    "SingleMuonRun2022EEF":    SingleMuonRun2022EEF,    
    "SingleMuonRun2022EEG":    SingleMuonRun2022EEG,    
    "SingleMuonRun2023C01":    SingleMuonRun2023C01,    
    "SingleMuonRun2023C02":    SingleMuonRun2023C02,    
    "SingleMuonRun2023C03":    SingleMuonRun2023C03,    
    "SingleMuonRun2023C04":    SingleMuonRun2023C04,    
    "SingleMuonRun2023C11":    SingleMuonRun2023C11,    
    "SingleMuonRun2023C12":    SingleMuonRun2023C12,    
    "SingleMuonRun2023C13":    SingleMuonRun2023C13,    
    "SingleMuonRun2023C14":    SingleMuonRun2023C14,    
    "SingleMuonRun2023BPixD01":SingleMuonRun2023BPixD01,
    "SingleMuonRun2023BPixD02":SingleMuonRun2023BPixD02,
    "SingleMuonRun2023BPixD11":SingleMuonRun2023BPixD11,
    "SingleMuonRun2023BPixD12":SingleMuonRun2023BPixD12,
    "MuonEGRun2022C":      MuonEGRun2022C,
    "MuonEGRun2022D":      MuonEGRun2022D,
    "MuonEGRun2022EEE":    MuonEGRun2022EEE,
    "MuonEGRun2022EEF":    MuonEGRun2022EEF,
    "MuonEGRun2022EEG":    MuonEGRun2022EEG,
    "MuonEGRun2023C01":    MuonEGRun2023C01,
    "MuonEGRun2023C02":    MuonEGRun2023C02,
    "MuonEGRun2023C03":    MuonEGRun2023C03,
    "MuonEGRun2023C04":    MuonEGRun2023C04,
    "MuonEGRun2023BPixD01":MuonEGRun2023BPixD01,
    "MuonEGRun2023BPixD02":MuonEGRun2023BPixD02,
    "TauRun2022C":      TauRun2022C,
    "TauRun2022D":      TauRun2022D,
    "TauRun2022EEE":    TauRun2022EEE,
    "TauRun2022EEF":    TauRun2022EEF,
    "TauRun2022EEG":    TauRun2022EEG,
    "TauRun2023C01":    TauRun2023C01,
    "TauRun2023C02":    TauRun2023C02,
    "TauRun2023C03":    TauRun2023C03,
    "TauRun2023C04":    TauRun2023C04,
    "TauRun2023BPixD01":TauRun2023BPixD01,
    "TauRun2023BPixD02":TauRun2023BPixD02,
}

samples_nonprompt = {
    "NonpromptSingleElecRun2022C":      NonpromptSingleElecRun2022C,      
    "NonpromptSingleElecRun2022D":      NonpromptSingleElecRun2022D,      
    "NonpromptSingleElecRun2022EEE":    NonpromptSingleElecRun2022EEE,    
    "NonpromptSingleElecRun2022EEF":    NonpromptSingleElecRun2022EEF,    
    "NonpromptSingleElecRun2022EEG":    NonpromptSingleElecRun2022EEG,    
    "NonpromptSingleElecRun2023C01":    NonpromptSingleElecRun2023C01,    
    "NonpromptSingleElecRun2023C02":    NonpromptSingleElecRun2023C02,    
    "NonpromptSingleElecRun2023C03":    NonpromptSingleElecRun2023C03,    
    "NonpromptSingleElecRun2023C04":    NonpromptSingleElecRun2023C04,    
    "NonpromptSingleElecRun2023C11":    NonpromptSingleElecRun2023C11,    
    "NonpromptSingleElecRun2023C12":    NonpromptSingleElecRun2023C12,    
    "NonpromptSingleElecRun2023C13":    NonpromptSingleElecRun2023C13,    
    "NonpromptSingleElecRun2023C14":    NonpromptSingleElecRun2023C14,    
    "NonpromptSingleElecRun2023BPixD01":NonpromptSingleElecRun2023BPixD01,
    "NonpromptSingleElecRun2023BPixD02":NonpromptSingleElecRun2023BPixD02,
    "NonpromptSingleElecRun2023BPixD11":NonpromptSingleElecRun2023BPixD11,
    "NonpromptSingleElecRun2023BPixD12":NonpromptSingleElecRun2023BPixD12,
    "NonpromptSingleMuonRun2022C":      NonpromptSingleMuonRun2022C,      
    "NonpromptSingleMuonRun2022D":      NonpromptSingleMuonRun2022D,      
    "NonpromptSingleMuonRun2022EEE":    NonpromptSingleMuonRun2022EEE,    
    "NonpromptSingleMuonRun2022EEF":    NonpromptSingleMuonRun2022EEF,    
    "NonpromptSingleMuonRun2022EEG":    NonpromptSingleMuonRun2022EEG,    
    "NonpromptSingleMuonRun2023C01":    NonpromptSingleMuonRun2023C01,    
    "NonpromptSingleMuonRun2023C02":    NonpromptSingleMuonRun2023C02,    
    "NonpromptSingleMuonRun2023C03":    NonpromptSingleMuonRun2023C03,    
    "NonpromptSingleMuonRun2023C04":    NonpromptSingleMuonRun2023C04,    
    "NonpromptSingleMuonRun2023C11":    NonpromptSingleMuonRun2023C11,    
    "NonpromptSingleMuonRun2023C12":    NonpromptSingleMuonRun2023C12,    
    "NonpromptSingleMuonRun2023C13":    NonpromptSingleMuonRun2023C13,    
    "NonpromptSingleMuonRun2023C14":    NonpromptSingleMuonRun2023C14,    
    "NonpromptSingleMuonRun2023BPixD01":NonpromptSingleMuonRun2023BPixD01,
    "NonpromptSingleMuonRun2023BPixD02":NonpromptSingleMuonRun2023BPixD02,
    "NonpromptSingleMuonRun2023BPixD11":NonpromptSingleMuonRun2023BPixD11,
    "NonpromptSingleMuonRun2023BPixD12":NonpromptSingleMuonRun2023BPixD12,
    "NonpromptMuonEGRun2022C":      NonpromptMuonEGRun2022C,
    "NonpromptMuonEGRun2022D":      NonpromptMuonEGRun2022D,
    "NonpromptMuonEGRun2022EEE":    NonpromptMuonEGRun2022EEE,
    "NonpromptMuonEGRun2022EEF":    NonpromptMuonEGRun2022EEF,
    "NonpromptMuonEGRun2022EEG":    NonpromptMuonEGRun2022EEG,
    "NonpromptMuonEGRun2023C01":    NonpromptMuonEGRun2023C01,
    "NonpromptMuonEGRun2023C02":    NonpromptMuonEGRun2023C02,
    "NonpromptMuonEGRun2023C03":    NonpromptMuonEGRun2023C03,
    "NonpromptMuonEGRun2023C04":    NonpromptMuonEGRun2023C04,
    "NonpromptMuonEGRun2023BPixD01":NonpromptMuonEGRun2023BPixD01,
    "NonpromptMuonEGRun2023BPixD02":NonpromptMuonEGRun2023BPixD02,
    "NonpromptTauRun2022C":      NonpromptTauRun2022C,
    "NonpromptTauRun2022D":      NonpromptTauRun2022D,
    "NonpromptTauRun2022EEE":    NonpromptTauRun2022EEE,
    "NonpromptTauRun2022EEF":    NonpromptTauRun2022EEF,
    "NonpromptTauRun2022EEG":    NonpromptTauRun2022EEG,
    "NonpromptTauRun2023C01":    NonpromptTauRun2023C01,
    "NonpromptTauRun2023C02":    NonpromptTauRun2023C02,
    "NonpromptTauRun2023C03":    NonpromptTauRun2023C03,
    "NonpromptTauRun2023C04":    NonpromptTauRun2023C04,
    "NonpromptTauRun2023BPixD01":NonpromptTauRun2023BPixD01,
    "NonpromptTauRun2023BPixD02":NonpromptTauRun2023BPixD02,
}

samples_signal={
    "Bprime_M1000_2022":    Bprime_M1000_2022,    
    "Bprime_M1000_2022EE":  Bprime_M1000_2022EE,  
    "Bprime_M1000_2023":    Bprime_M1000_2023,    
    "Bprime_M1000_2023BPix":Bprime_M1000_2023BPix,
    "Bprime_M1300_2022":    Bprime_M1300_2022,    
    "Bprime_M1300_2022EE":  Bprime_M1300_2022EE,  
    "Bprime_M1300_2023":    Bprime_M1300_2023,    
    "Bprime_M1300_2023BPix":Bprime_M1300_2023BPix,
    "Bprime_M1600_2022":    Bprime_M1600_2022,    
    "Bprime_M1600_2022EE":  Bprime_M1600_2022EE,  
    "Bprime_M1600_2023":    Bprime_M1600_2023,    
    "Bprime_M1600_2023BPix":Bprime_M1600_2023BPix,
    "Bprime_M700_2022":    Bprime_M700_2022,    
    "Bprime_M700_2022EE":  Bprime_M700_2022EE,  
    "Bprime_M700_2023":    Bprime_M700_2023,    
    "Bprime_M700_2023BPix":Bprime_M700_2023BPix,
    "Bprime_M400_2022":     Bprime_M400_2022,
    "Bprime_M400_2022EE":   Bprime_M400_2022EE,
    "Bprime_M400_2023":     Bprime_M400_2023,
    "Bprime_M400_2023BPix": Bprime_M400_2023BPix,
}

samples_mc = {
    "Bprime_M1000_2022":    Bprime_M1000_2022,    
    "Bprime_M1000_2022EE":  Bprime_M1000_2022EE,  
    "Bprime_M1000_2023":    Bprime_M1000_2023,    
    "Bprime_M1000_2023BPix":Bprime_M1000_2023BPix,
    "Bprime_M1300_2022":    Bprime_M1300_2022,    
    "Bprime_M1300_2022EE":  Bprime_M1300_2022EE,  
    "Bprime_M1300_2023":    Bprime_M1300_2023,    
    "Bprime_M1300_2023BPix":Bprime_M1300_2023BPix,
    "Bprime_M1600_2022":    Bprime_M1600_2022,    
    "Bprime_M1600_2022EE":  Bprime_M1600_2022EE,  
    "Bprime_M1600_2023":    Bprime_M1600_2023,    
    "Bprime_M1600_2023BPix":Bprime_M1600_2023BPix,
    "Bprime_M700_2022":    Bprime_M700_2022,    
    "Bprime_M700_2022EE":  Bprime_M700_2022EE,  
    "Bprime_M700_2023":    Bprime_M700_2023,    
    "Bprime_M700_2023BPix":Bprime_M700_2023BPix,
    "Bprime_M400_2022":     Bprime_M400_2022,
    "Bprime_M400_2022EE":   Bprime_M400_2022EE,
    "Bprime_M400_2023":     Bprime_M400_2023,
    "Bprime_M400_2023BPix": Bprime_M400_2023BPix,
    "WZ3L2022":       WZ3L2022,
    "WZ3L2022ext":    WZ3L2022ext,
    "WZ3L2022EE":     WZ3L2022EE,
    "WZ3L2022EEext":  WZ3L2022EEext,
    "WZ3L2023":       WZ3L2023,
    "WZ3L2023ext":    WZ3L2023ext,
    "WZ3L2023BPix":   WZ3L2023BPix,
    "WZ3L2023BPixext":WZ3L2023BPixext,
    "ZZ4L2022":       ZZ4L2022,
    "ZZ4L2022ext":    ZZ4L2022ext,
    "ZZ4L2022EE":     ZZ4L2022EE,
    "ZZ4L2022EEext":  ZZ4L2022EEext,
    "ZZ4L2023":       ZZ4L2023,
    "ZZ4L2023BPix":   ZZ4L2023BPix,
    "WWW2022"     :     WWW2022     ,
    "WWW2022EE"   :     WWW2022EE   ,
    "WWW2023"     :     WWW2023     ,
    "WWW2023BPix" :     WWW2023BPix ,
    "WWZ2022"     :     WWZ2022     ,
    "WWZ2022EE"   :     WWZ2022EE   ,
    "WWZ2023"     :     WWZ2023     ,
    "WWZ2023BPix" :     WWZ2023BPix ,
    "WZZ2022"     :     WZZ2022     ,
    "WZZ2022EE"   :     WZZ2022EE   ,
    "WZZ2023"     :     WZZ2023     ,
    "WZZ2023BPix" :     WZZ2023BPix ,
    "ZZZ2022"     :     ZZZ2022     ,
    "ZZZ2022EE"   :     ZZZ2022EE   ,
    "ZZZ2023"     :     ZZZ2023     ,
    "ZZZ2023BPix" :     ZZZ2023BPix ,
    "WWZZ4L2022":     WWZZ4L2022,
    "WWZZ4L2022EE":   WWZZ4L2022EE,
    "WWZZ4L2023":     WWZZ4L2023,
    "WWZZ4L2023BPix": WWZZ4L2023BPix,
    "VHnonbb2022": VHnonbb2022,
    "VHnonbb2022EE": VHnonbb2022EE,
    "VHnonbb2023": VHnonbb2023,
    "VHnonbb2023BPix": VHnonbb2023BPix,
    "ZG2J2022"           : ZG2J2022,
    "ZG2J2022EE"         : ZG2J2022EE,
    "ZG2J2023"           : ZG2J2023,
    "ZG2J2023BPix"       : ZG2J2023BPix,
    "TTG1Jpt102022"      : TTG1Jpt102022,
    "TTG1Jpt102022EE"    : TTG1Jpt102022EE,   
    "TTG1Jpt102023"      : TTG1Jpt102023, 
    "TTG1Jpt102023BPix"  : TTG1Jpt102023BPix, 
    "TTG1Jpt1002022"     : TTG1Jpt1002022,
    "TTG1Jpt1002022EE"   : TTG1Jpt1002022EE, 
    "TTG1Jpt1002023"     : TTG1Jpt1002023,
    "TTG1Jpt1002023BPix" : TTG1Jpt1002023BPix, 
    "TTG1Jpt2002022"     : TTG1Jpt2002022,
    "TTG1Jpt2002022EE"   : TTG1Jpt2002022EE, 
    "TTG1Jpt2002023"     : TTG1Jpt2002023,
    "TTG1Jpt2002023BPix" : TTG1Jpt2002023BPix, 
    "TTHnonB2022":    TTHnonB2022,    
    "TTHnonB2022EE":  TTHnonB2022EE,  
    "TTHnonB2023":    TTHnonB2023,    
    "TTHnonB2023BPix":TTHnonB2023BPix,
    "TTWl2022":         TTWl2022,         
    "TTWl2022EE":       TTWl2022EE,       
    "TTWl2023":         TTWl2023,         
    "TTWl2023BPix":     TTWl2023BPix,     
    "TTZM42022":       TTZM42022,       
    "TTZM42022EE":     TTZM42022EE,     
    "TTZM42023":       TTZM42023,       
    "TTZM42023BPix":   TTZM42023BPix,   
    "TTZM502022":    TTZM502022,    
    "TTZM502022EE":  TTZM502022EE,  
    "TTZM502023":    TTZM502023,    
    "TTZM502023BPix":TTZM502023BPix,
    "TTZM502022ext":    TTZM502022ext,  
    "TTZM502022EEext":  TTZM502022EEext,
    "TTZM502023ext":    TTZM502023ext,
    "TTZM502023BPixext":TTZM502023BPixext,
    "TTWH2022"     : TTWH2022     ,
    "TTWH2022EE"   : TTWH2022EE  ,
    "TTWH2023"     : TTWH2023    ,
    "TTWH2023BPix" : TTWH2023BPix,
    "TTWW2022"     : TTWW2022    ,
    "TTWW2022EE"   : TTWW2022EE  ,
    "TTWW2023"     : TTWW2023    ,
    "TTWW2023BPix" : TTWW2023BPix,
    "TTWZ2022"     : TTWZ2022    ,
    "TTWZ2022EE"   : TTWZ2022EE  ,
    "TTWZ2023"     : TTWZ2023    ,
    "TTWZ2023BPix" : TTWZ2023BPix,
    "TTZH2022"     : TTZH2022    ,
    "TTZH2022EE"   : TTZH2022EE  ,
    "TTZH2023"     : TTZH2023    ,
    "TTZH2023BPix" : TTZH2023BPix,
    "TTZZ2022"     : TTZZ2022    ,
    "TTZZ2022EE"   : TTZZ2022EE  ,
    "TTZZ2023"     : TTZZ2023    ,
    "TTZZ2023BPix" : TTZZ2023BPix,
    "TTTT2022"     : TTTT2022    ,
    "TTTT2022EE"   : TTTT2022EE  ,
    "TTTT2023"     : TTTT2023    ,
    "TTTT2023BPix" : TTTT2023BPix,
    "TZQB2022" : TZQB2022,
    "TZQB2022EE" : TZQB2022EE,
    "TZQB2023" : TZQB2023,
    "TZQB2023BPix" : TZQB2023BPix,
    "TGQB2022" : TGQB2022,
    "TGQB2022EE" : TGQB2022EE,
    "TGQB2023" : TGQB2023,
    "TGQB2023BPix" : TGQB2023BPix,
}

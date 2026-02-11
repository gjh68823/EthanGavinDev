import os

list = {
    'Bprime_M1000_2022EE':'/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM',
    'Bprime_M1000_2022':'/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM',
    'Bprime_M1000_2023BPix':'/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM',
    'Bprime_M1000_2023':'/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM',
    'Bprime_M1300_2022EE':'/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM',
    'Bprime_M1300_2022':'/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM',
    'Bprime_M1300_2023BPix':'/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM',
    'Bprime_M1300_2023':'/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM',
    'Bprime_M1600_2022EE':'/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM',
    'Bprime_M1600_2022':'/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM',
    'Bprime_M1600_2023BPix':'/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM',
    'Bprime_M1600_2023':'/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM',
    'Bprime_M700_2022EE':'/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM',
    'Bprime_M700_2022':'/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM',
    'Bprime_M700_2023BPix':'/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM',
    'Bprime_M700_2023':'/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM',
    'Bprime_M400_2022EE':'/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM',
    'Bprime_M400_2022':'/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM',
    'Bprime_M400_2023BPix':'/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM',
    'Bprime_M400_2023':'/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM',
    }


for item in list.keys():
    query = 'dasgoclient --query="file dataset='+list[item]+'" > NanoList/'+item+'NanoList.txt'
    os.system(query)

    with open(os.path.abspath('NanoList/'+item+'NanoList.txt'),'r') as rootlist:
        rootfiles = [''.join(["root://cmsxrootd.fnal.gov/", line.strip(), "\n"]) for line in rootlist.readlines()]

    with open(os.path.abspath('NanoList/'+item+'NanoList.txt'),'w') as rootlist:
        rootlist.writelines(rootfiles)

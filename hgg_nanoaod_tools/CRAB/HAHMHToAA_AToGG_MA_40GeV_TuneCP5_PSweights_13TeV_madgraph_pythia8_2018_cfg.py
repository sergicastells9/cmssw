# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename HAHMHToAA_AToGG_MA_40GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:HAHMHToAA_AToGG_MA_40GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root --conditions 102X_upgrade2018_realistic_v15 --step NANO --filein dbs:/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM --era Run2_2018,run2_nanoAOD_102Xv1 --mc -n -1 --no_exec --nThreads 1
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.Eras.Modifier_run2_nanoAOD_102Xv1_cff import run2_nanoAOD_102Xv1

process = cms.Process('NANO',Run2_2018,run2_nanoAOD_102Xv1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/015C226B-38AC-2B45-B78C-35091B0905BF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/180588A4-5082-B246-A015-10D254C5DCD1.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/18D9C809-F3D8-EB45-AF6F-3CAB9B7D2B24.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/1DE6CDA4-C803-0747-8483-95E635F03939.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/33AC5962-8683-A041-9184-E3765D3F46A3.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/44AACEE1-33F4-B34B-AFA6-006A2762F69C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/4B45E09A-EE0C-E14B-8940-73CD9BC505E0.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/602D3DAB-7E1C-B64D-9541-C4F040BC83BE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/67E4648B-2025-B84D-B6F7-73EA45E687B4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/95754480-6A85-654B-89EA-460BE5CA7234.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/9BC96B4B-A92A-B74F-875B-7BF4FA00FADF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/ACC41FEE-28F8-7545-944A-7F3984F8D8BB.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/AF0F5421-E395-6842-AA69-7F7F5BD94FE4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/CAB6825D-C5DF-D643-AD70-0A9591BE215A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/D3577E58-EB21-7840-94B5-F738C11F2512.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/D59FFCC8-5647-3843-8E35-660E79ABB775.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/D887F405-7162-3E4F-85C5-728356B9C3AF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/E2F2B2E7-EA97-554F-82FE-E4F9CCFBFEE7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/F3F1308B-3484-1A45-A75D-7191F0B4ADA9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-40GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/FF931C66-FC98-3945-8767-A99C1A7054F7.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:HAHMHToAA_AToGG_MA_40GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v15', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

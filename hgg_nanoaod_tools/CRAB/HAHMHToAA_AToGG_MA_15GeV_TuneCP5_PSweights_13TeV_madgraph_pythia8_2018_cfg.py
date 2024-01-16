# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename HAHMHToAA_AToGG_MA_15GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:HAHMHToAA_AToGG_MA_15GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root --conditions 102X_upgrade2018_realistic_v15 --step NANO --filein dbs:/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM --era Run2_2018,run2_nanoAOD_102Xv1 --mc -n -1 --no_exec --nThreads 1
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
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/10A392D9-7B9A-B042-B72F-E0013FFEF891.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/21CE983C-8F46-254F-AEFA-DEA9AF2511C8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/3A229160-09DE-5545-9938-30486DDAC7AA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/3B2535EE-E622-314C-8605-7DC5974DE9A4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/41E68BF4-350A-9341-A9A4-6ECCCE47BA15.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/61A5DE8B-2ABE-2044-BDD2-237F83113D8A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/677464D6-B136-C54F-A265-1526E896D2FE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/7D86811E-C6E6-EC42-884F-E2054ED4DAFD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/8560372E-3C98-0448-A9EE-5BC87CEE153E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/8E9E7C40-AF75-FC4D-A6F5-93FBCC1BEA27.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/9A4E6446-E5B0-B142-9801-12091C3BA77A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/BE519A93-7136-5148-A245-02A990F2B807.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/BFE97C07-FD70-F74A-9EEE-D69552EBDB68.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/CFE3ECF6-29F7-9C4E-A35E-93ADD3FE55D6.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/DFB30F52-B403-9A47-B783-01C21F6D738C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-15GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/F4CD46BD-D0B5-0843-BFE6-948A248BE1CC.root'
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
    fileName = cms.untracked.string('file:HAHMHToAA_AToGG_MA_15GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root'),
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

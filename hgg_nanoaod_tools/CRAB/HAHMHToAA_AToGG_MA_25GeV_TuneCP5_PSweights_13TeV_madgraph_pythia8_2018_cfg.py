# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename HAHMHToAA_AToGG_MA_25GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:HAHMHToAA_AToGG_MA_25GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root --conditions 102X_upgrade2018_realistic_v15 --step NANO --filein dbs:/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM --era Run2_2018,run2_nanoAOD_102Xv1 --mc -n -1 --no_exec --nThreads 1
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
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/021BD9E4-DDC5-574C-BE7F-EC72D12C26C9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/1334A49D-68F1-6149-87F8-0B5502036365.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/1E3D2131-5438-184C-ADFB-3ED110BA36E5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/2565620F-3DF5-4F46-AC51-6AA06B352285.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/325B07D6-572C-1F47-9932-6E52F0E4A944.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/46AA4097-AE19-A64E-9688-FA246459667C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/53F4AA8A-E02D-C04E-8E5F-2BD1362C1B58.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/5ECA1B62-15A3-2244-B097-A243D3EC67DD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/77C2E9B4-D490-4544-92B5-F22611BE40E0.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/A8172972-6E18-D245-8A1F-8122F096A048.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/B95E1B69-EC43-C84D-A732-38EDCB14C418.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/B966887C-2FC8-7546-AE24-976DE59CA3E2.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/B9B68421-B8C9-6D49-86CD-162C0F39289F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/E2FB745B-9BDB-5742-8415-4A77DAF4EA47.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/ED46E87D-465D-6A4F-A27E-8283C91F0A15.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-25GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/F34B1E01-6493-D64D-ADA1-1852943A1252.root'
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
    fileName = cms.untracked.string('file:HAHMHToAA_AToGG_MA_25GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root'),
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

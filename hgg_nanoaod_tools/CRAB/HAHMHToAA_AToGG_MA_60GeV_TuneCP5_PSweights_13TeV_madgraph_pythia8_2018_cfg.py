# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename HAHMHToAA_AToGG_MA_60GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:HAHMHToAA_AToGG_MA_60GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root --conditions 102X_upgrade2018_realistic_v15 --step NANO --filein dbs:/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM --era Run2_2018,run2_nanoAOD_102Xv1 --mc -n -1 --no_exec --nThreads 1
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
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/1362B753-9147-4E40-B694-9834AFC085BD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/16D3FB5A-D39A-2041-A834-B6D9A7DD6D9E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/1C0F4718-53C4-6646-A8BE-BD26E1711EB5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/268C473E-66F9-E64F-8ECC-CC81BDEF486E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/35D7F0A0-063D-F648-B6AE-7F02A8E4570B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/39510FC3-993A-B84F-8EA7-833B4A3B5839.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/4CE79504-C5A1-DB40-A22B-3E709DA050B1.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/53B60B3F-9227-A24D-949D-58D7DE0E42A3.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/689A398E-8D19-F748-B84A-808D9BE4E131.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/6B796D06-C546-8A4F-8498-EB4D2AFA53BA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/8503A2F5-BED8-5949-B843-8EE694C53E35.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/8B135368-FB2D-C742-9B28-95F9D4F132A4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/8EF8E60E-8D5F-D849-B8DC-A96A844ADE3B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/908607AA-24BD-C949-AA2D-2CF064E1FAA6.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/98C96DA4-B9A3-684F-A053-AA621B32B01A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/A567C5C5-8796-9249-9813-A3234CB25A84.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/B7FA3B7D-981F-2A45-8137-BEF4700AD85D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/C15D6B87-68E8-C045-88E2-9E4774256710.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/C365E8D9-B9D4-5E41-8AEA-FD5F233E2226.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/C5852F8C-52BE-D346-81A4-EFF543960CEE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/CE9B9393-EBC4-2B4D-B473-F7025C817A65.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/D19C4FDF-238A-CD4D-8590-DCAC3E3748C0.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/D5320A0E-1CDD-354A-A683-1227EDB2318B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/D5CF600B-4B9B-5B42-B144-B72C1EDF72F9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-60GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/E38BC5B4-75E4-EF4E-B943-DEEDB81B84C4.root'
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
    fileName = cms.untracked.string('file:HAHMHToAA_AToGG_MA_60GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root'),
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

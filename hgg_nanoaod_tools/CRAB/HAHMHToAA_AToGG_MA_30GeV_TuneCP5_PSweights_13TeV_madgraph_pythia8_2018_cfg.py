# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename HAHMHToAA_AToGG_MA_30GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:HAHMHToAA_AToGG_MA_30GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root --conditions 102X_upgrade2018_realistic_v15 --step NANO --filein dbs:/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM --era Run2_2018,run2_nanoAOD_102Xv1 --mc -n -1 --no_exec --nThreads 1
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
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/094FFC67-9083-B546-AE0F-7E5AD557A441.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/0AA7AF6F-8F43-B74F-AEA2-5FF7C7C827F0.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/0BBC3C88-E475-A545-B9A2-9934A3BCC79B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/135AB4D5-621C-FE41-856E-787357F6F0B5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/14D9A99C-3276-5044-937F-0183046EB4FE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/22C1D67A-AA67-F441-9908-041901FD63B9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/24F64F9F-7338-5F44-BE4B-5714FA6D7D94.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/2E6D1C2A-7E49-4643-B969-38CE3B81E87A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/321CD4AF-20C0-1940-9B4A-D93F04718EBD.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/4F1B45C4-8E20-0846-8578-F4327371AB9A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/7635048F-8C85-8440-B25A-DB0B5CDC5364.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/785C3367-7A0C-6E47-9A51-C16F5437958D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/88C77B3C-3DB9-1347-80D8-C0082FBDCDDF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/92BD3943-C117-0F43-A865-2D928A9A8808.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/AAB845DC-F342-2C42-82AA-23C969951A7B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/B2F6F749-205A-B444-93D6-354F43C70855.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/B3E4E1E6-443F-2044-B9B9-BDC9A0D404FF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/C2F6847D-C07E-8945-B0AE-B709E0759B04.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/CB2E7E06-4120-124F-B39C-A5FB0FADF016.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/CCCC1229-E7EE-F145-9D77-716C3DB81D42.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/CF3C99AD-C425-AE48-B21A-9ED900B2D554.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/E1979B6A-832C-494D-8858-E55929E5A49B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/F1BC1757-203D-024A-A570-399EF3C4D72F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/HAHMHToAA_AToGG_MA-30GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/250000/F20B956E-26E8-E444-809B-64C6F5260C4C.root'
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
    fileName = cms.untracked.string('file:HAHMHToAA_AToGG_MA_30GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018.root'),
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

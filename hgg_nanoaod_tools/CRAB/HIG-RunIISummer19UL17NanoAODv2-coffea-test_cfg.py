# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename HIG-RunIISummer19UL17NanoAODv2-coffea-test_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:HIG-RunIISummer19UL17NanoAODv2-00001.root --conditions 106X_mc2017_realistic_v7 --step NANO --filein dbs:/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM --era Run2_2017,run2_nanoAOD_106Xv1 --no_exec --mc -n -1
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2017_cff import Run2_2017
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv1_cff import run2_nanoAOD_106Xv1

process = cms.Process('NANO',Run2_2017,run2_nanoAOD_106Xv1)

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
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/1F74B36B-6A1D-494A-9725-CFD24771D0AE.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/3A5C6A65-631B-A845-AB7F-E96067441E1E.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/47833876-4524-224D-92CF-E6A9EAA0429D.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/5520649B-F125-5640-A5A7-654CCFA00DC1.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/5B6D790E-CAAB-524C-8B9E-9AB489BFC3DD.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7B131CFE-94D6-0E43-94A8-590C2E448621.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/AAA70B67-DC32-5A49-B92B-1C9E977EA46C.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C6BE06DD-78C1-3847-BFE6-EC0CEDED7B02.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/CD66920F-B317-2344-BE5F-9E925C047F77.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/280000/6123E990-F6D9-844C-9120-06AA4894D089.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/280000/62854D58-2728-C74D-A0F3-554A1827E62C.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/280000/A1955DEE-7FE2-C646-AEBE-62FED8C5596C.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/07315A32-54D5-9D44-8C21-33E8BE21A93B.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/0BF4272C-A9E0-0C40-A6DE-04FB5B983384.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/1249005B-EFEE-BF45-9F7A-4EC233DB919F.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/18F53634-1E3B-C648-AD97-EB7A3ACC2618.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/1ACC3930-0BBC-C34A-BE05-873EE52E8B6D.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/1BC82F95-E06F-0D49-983C-E9840363368B.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/21DFB473-9EAD-C449-9255-886CBE0E80C9.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/26B2C113-50C1-864E-8BBF-6F94FA1B9D4D.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/2C3267A3-CEFF-9E42-8B76-83E32993F545.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/2E39A178-31DE-4F48-836A-F3530E1781AE.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/32379F39-DDBD-134D-9A57-1BF37CC49A02.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/3DD8BE42-2354-824E-B36C-A84459D66595.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/4FB7CF4E-925E-4B47-8200-1A4B559D60AE.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/65DC742E-141D-3A45-9780-84C9807B505C.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/6DB97D3C-5936-AF46-A9F8-756CA6D1541F.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/820D45D4-2A92-FF41-9FF5-4BEAD2B4B9F8.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/884CA9F0-CEDB-4C4C-84AF-92CC6239F601.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/8B03C272-7452-1641-8E63-EF70869BE586.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/8D031E7B-7B48-324A-8BB8-4105FCD8786E.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/91E9FA90-E784-DD44-A1DF-870ED98F1D36.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/9527C0BA-1B13-AE4F-847E-EBD5F323DC0E.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/9B401F4A-D980-F545-8F51-6B4618FEF4D6.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/A2EE0E6B-E25F-784C-AB12-4463B2EC9054.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/AA4437B6-35C6-3A4D-AEB4-B5A7915BC718.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/B2E447B1-7F53-5348-8C1B-8F62B6288CF5.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/B7C8FF96-5A49-3B4B-837C-EC70582FC5C9.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/B9DAFB5C-656B-3C41-BA18-25B2284BC5C3.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/C3CA8070-875A-484B-ACBF-0B33E94F596F.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/C9C7DC23-FEED-6740-ABC5-DE0E7750FCFD.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/CA0665AF-378F-AB4E-892A-50BE59C2AEBF.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/E1639FCC-E923-F24E-A676-F8AC5E55F0D1.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/E69B34C5-AECE-4E42-9904-573AE2A1068E.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/E9F8AA1D-13A8-6147-AE34-5462D61C5C6E.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/F1523BDE-2291-6046-A0E9-B4858171C214.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/F26681AD-074D-B84E-9CF1-38ABD35D2EF1.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/F3E62D3C-3EB6-254A-90EA-6AD3B6A3545D.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/F4B3BEC6-398F-4C42-8065-E55736A6C8B1.root', 
        '/store/mc/RunIISummer19UL17MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/F925DBD2-CF5B-8546-B106-9B152ECE352C.root'
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

#process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
process.NANOAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:HIG-RunIISummer19UL17NanoAODv2-00001.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mc2017_realistic_v7', '')

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

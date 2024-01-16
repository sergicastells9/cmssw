
from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.workArea          =  'MNConversion_crab'
config.General.requestName	     =  'MNConversion_HAHMHToAA_AToGG_MA_35GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018'
config.General.transferLogs	     =  True
config.General.transferOutputs   =  True

config.section_('JobType')
config.JobType.pluginName        = 'Analysis'
config.JobType.numCores          = 1

# Name of the CMSSW configuration file
config.JobType.psetName          = 'HAHMHToAA_AToGG_MA_35GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_2018_cfg.py'
config.JobType.priority          = 30
config.JobType.maxMemoryMB       = 2500

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset         = '/HAHMHToAA_AToGG_MA-35GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'Automatic'
config.Data.lumiMask             = ''
# config.Data.unitsPerJob          = 1
config.Data.totalUnits           = -1
config.Data.publication          = False
config.Data.outLFNDirBase        = '/store/user/castells/outputs/Signal_MC_2018'

# This string is used to construct the output dataset name
config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite          = 'T3_US_NotreDame'
    
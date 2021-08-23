from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName       = 'ReReco-Run2017B-DoubleEG-UL2017_MiniAODv1_NanoAODv2_cfg'
config.General.transferLogs      = True
config.General.transferOutputs   = True

config.section_('JobType')
config.JobType.pluginName        = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName          = 'ReReco-Run2017B-DoubleEG-UL2017_MiniAODv1_NanoAODv2_cfg.py'
config.JobType.priority          = 30

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset         = '/DoubleEG/Run2017B-UL2017_MiniAODv2-v1/MINIAOD'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'Automatic'
config.Data.lumiMask             = ''
#config.Data.unitsPerJob          = 10
config.Data.totalUnits           = -1
config.Data.publication          = True
config.Data.outputDatasetTag     = 'CRAB3_ReReco-Run2017B-DoubleEG-UL2017_MiniAODv1_NanoAODv2'

# This string is used to construct the output dataset name
config.Data.outLFNDirBase        = '/store/user/gallim/HggNano/'

config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite          = 'T3_CH_PSI'

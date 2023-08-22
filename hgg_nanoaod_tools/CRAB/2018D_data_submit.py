
from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.workArea          =  'MNConversion_crab'
config.General.requestName	     =  'MNConversion_2018D_data'
config.General.transferLogs	     =  True
config.General.transferOutputs   =  True

config.section_('JobType')
config.JobType.pluginName        = 'Analysis'
config.JobType.numCores          = 8
config.JobType.maxMemoryMB       = 20000

# Name of the CMSSW configuration file
config.JobType.psetName          = '2018D_data_cfg.py'
config.JobType.priority          = 30

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset         = '/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'Automatic'
config.Data.lumiMask             = ''
#config.Data.unitsPerJob         = 30
config.Data.totalUnits           = -1
config.Data.publication          = False
config.Data.outLFNDirBase        = '/store/user/castells/outputs/MNConversion_2018D_final/'

# This string is used to construct the output dataset name
config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite          = 'T3_US_NotreDame'
    
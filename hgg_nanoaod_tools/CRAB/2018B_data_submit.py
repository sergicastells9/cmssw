
from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.workArea          =  'MNConversion_crab'
config.General.requestName	     =  'MNConversion_2018B_data'
config.General.transferLogs	     =  True
config.General.transferOutputs   =  True

config.section_('JobType')
config.JobType.pluginName        = 'Analysis'
config.JobType.numCores          = 8
config.JobType.maxMemoryMB       = 20000

# Name of the CMSSW configuration file
config.JobType.psetName          = '2018B_data_cfg.py'
config.JobType.priority          = 30

config.section_('Data')
# This string determines the primary dataset of the newly-produced outputs.
config.Data.inputDataset         = '/EGamma/Run2018B-UL2018_MiniAODv2-v1/MINIAOD'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'Automatic'
config.Data.lumiMask             = ''
#config.Data.unitsPerJob         = 30
config.Data.totalUnits           = -1
config.Data.publication          = False
config.Data.outLFNDirBase        = '/hadoop/users/scastel2/outputs/MNConversion_2018B/'

# This string is used to construct the output dataset name
config.section_('Site')
# Where the output files will be transmitted to
config.Site.storageSite          = 'T3_CH_CERNBOX'
    
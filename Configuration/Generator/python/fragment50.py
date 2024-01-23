import FWCore.ParameterSet.Config as cms

# link to card:
# https://github.com/cms-sw/genproductions/tree/248a8c57ea32ea412635044ded74eeb7d84edfbd/bin/MadGraph5_aMCatNLO/cards/production/13p6TeV/hToaaTo4gamma_ma_AMASS_GeV_MLM_4f_max1j

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    nEvents = cms.untracked.uint32(5000),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
    args = cms.vstring('/eos/user/c/castells/H4g/Gridpacks/hToaaTo4gamma_ma_50_GeV_MLM_4f_max1j_el8_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz')
)

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
              maxEventsToPrint = cms.untracked.int32(1),
              pythiaPylistVerbosity = cms.untracked.int32(1),
              filterEfficiency = cms.untracked.double(1.0),
              pythiaHepMCVerbosity = cms.untracked.bool(False),
              comEnergy = cms.double(13600.),
              PythiaParameters = cms.PSet(
                pythia8CommonSettingsBlock,
                pythia8CP5SettingsBlock,
                pythia8PSweightsSettingsBlock,
                processParameters = cms.vstring(
                  'JetMatching:setMad = off',
                  'JetMatching:scheme = 1',
                  'JetMatching:merge = on',
                  'JetMatching:jetAlgorithm = 2',
                  'JetMatching:etaJetMax = 5.',
                  'JetMatching:coneRadius = 1.',
                  'JetMatching:slowJetPower = 1',
                  'JetMatching:qCut = 30.', 
                  'JetMatching:nQmatch = 4', 
                  'JetMatching:nJetMax = 1', 
                  'JetMatching:doShowerKt = off',
                ),
                parameterSets = cms.vstring(
                  'pythia8CommonSettings',
                  'pythia8CP5Settings',
                  'pythia8PSweightsSettings',
                  'processParameters'
                )
              )
            )

ProductionFilterSequence = cms.Sequence(generator)

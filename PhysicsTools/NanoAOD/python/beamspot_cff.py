import FWCore.ParameterSet.Config as cms
from  PhysicsTools.NanoAOD.common_cff import *
from PhysicsTools.NanoAOD.nano_eras_cff import *


##################### Tables for final output and docs ##########################
beamSpotTable = cms.EDProducer("SimpleBeamspotFlatTableProducer",
    src = cms.InputTag("offlineBeamSpot"),
    name = cms.string("BeamSpot"),
    doc = cms.string("offlineBeamSpot, the offline reconstructed beamspot"),
    singleton = cms.bool(True),  # there's always exactly one MET per event
    extension = cms.bool(False), # this is the main table for the MET
    variables = cms.PSet(
       type = Var("type()","int8",doc="BeamSpot type (Unknown = -1, Fake = 0, LHC = 1, Tracker = 2)"),
       x = Var("position().x()",float,doc="BeamSpot center, x coordinate (cm)",precision=-1),
       y = Var("position().y()",float,doc="BeamSpot center, y coordinate (cm)",precision=-1),
       z = Var("position().z()",float,doc="BeamSpot center, z coordinate (cm)",precision=-1),
       xError = Var("x0Error()",float,doc="Error on BeamSpot center, x coordinate (cm)",precision=-1),
       yError = Var("y0Error()",float,doc="Error on BeamSpot center, y coordinate (cm)",precision=-1),
       zError = Var("z0Error()",float,doc="Error on BeamSpot center, z coordinate (cm)",precision=-1),
       sigmaZ = Var("sigmaZ()",float,doc="Width of BeamSpot in z (cm)",precision=-1),
       sigmaZError = Var("sigmaZ0Error()",float,doc="Error on width of BeamSpot in z (cm)",precision=-1),
       dxdz = Var("dxdz()",float,doc="BeamSpot dxdz",precision=-1),
       dydz = Var("dydz()",float,doc="BeamSpot dydz",precision=-1),
       dxdyError = Var("dxdzError()",float,doc="Error on BeamSpot dxdz",precision=-1),
       dydzError = Var("dydzError()",float,doc="Error on BeamSpot dydz",precision=-1),
       beamWidthX = Var("BeamWidthX()",float,doc="Beam width, x coordinate (cm)",precision=-1),
       beamWidthY = Var("BeamWidthY()",float,doc="Beam width, y coordinate (cm)",precision=-1),
       beamWidthError = Var("BeamWidthXError()",float,doc="Error on beam width, assumed that error_x == error_y, cm",precision=-1),
       emittance_x = Var("emittanceX()",float,doc="Beam emittance, x coordinate",precision=-1),
       emittance_y = Var("emittanceY()",float,doc="Beam emittance, y coordinate",precision=-1),
       betaStar = Var("betaStar()",float,doc="Beam beta-star",precision=-1),
    ),
)

beamSpotTables = cms.Sequence( beamSpotTable )


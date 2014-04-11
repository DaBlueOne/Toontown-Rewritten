from toontown.toonbase import ToontownGlobals
from HoodAI import HoodAI
from toontown.safezone import ButterflyGlobals
from toontown.safezone.DistributedButterflyAI import DistributedButterflyAI
from toontown.toon import NPCToons
from toontown.election.DistributedElectionEventAI import DistributedElectionEventAI
from toontown.building.HQBuildingAI import HQBuildingAI
from toontown.toon import NPCToons

class TTHoodAI(HoodAI):
    HOOD = ToontownGlobals.ToontownCentral
    
    def createSafeZone(self):
        HoodAI.createSafeZone(self)
        self.spawnObjects()
        self.butterflies = []
        # TODO: Re-enable butterflies. RIP, you will be missed.
        #self.createButterflies()
        
        #beginhack disable election props
        #self.spawnElection()
        #endhack

        #TODO: in reality this should be done by the buildingMgr
        hqBlock = 20
        hqZone = self.HOOD - self.HOOD % 100 + 500 + hqBlock
        self.hqBuilding = HQBuildingAI(self.air, self.HOOD, hqZone, hqBlock)
        #beginhack FLIPPY IN TTC
        flippy = NPCToons.createNPC(self.air, 2001, NPCToons.NPCToonDict[2001], self.HOOD, 3)
        print flippy
        #endhack
    
    def spawnElection(self):
        event = self.air.doFind('ElectionEvent')
        if event is None:
            event = DistributedElectionEventAI(self.air)
            event.generateWithRequired(self.HOOD)
        event.b_setState('Intro')
    
    def createButterflies(self):
        playground = ButterflyGlobals.TTC
        for area in range(ButterflyGlobals.NUM_BUTTERFLY_AREAS[playground]):
            for b in range(ButterflyGlobals.NUM_BUTTERFLIES[playground]):
                butterfly = DistributedButterflyAI(self.air)
                butterfly.setArea(playground, area)
                butterfly.setState(0, 0, 0, 1, 1)
                butterfly.generateWithRequired(self.HOOD)
                self.butterflies.append(butterfly)

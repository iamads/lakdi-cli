from player import Player
class Bot(Player):

    def __init__(self,mycards , trump):
        super(Player, self).init(mycards, trump)

    def move(self, currentcards):
        if len(currentcards) == 0:
            return self.makefirstmove()
        else:
            return self.makecountermove(currentcards)

    def makefirstmove(self):
        return self.mycards.pop()

    def makecountermove(self, currentcards):
        # cards belonging to same suit as of current round
        suitofround = currentcards[0][0]
        validcards = [i for i in self.mycards if i[0] == suitofround]  # validcards I have for this round
        # has anyone thrown trump in this round
        istrumpthere = [self.prioritytable(i[2])
                        for i in currentcards if i[0] == self.trump]
        istrumpthere.append(0)
        print "validcards",len(validcards)
        print "istrumpthere",len(istrumpthere)
        if len(validcards) > 0 and len(istrumpthere) == 0:
            #print "daphne"
            return validcards.pop()
        elif len(validcards) > 0 and len(istrumpthere) > 0:
            #print "velma"
            return validcards.pop(0)
        else:
            #print "fred"
            if self.prioritytable(self.mytrumps[-1]) > max(istrumpthere):
                #print "shaggy"
                return self.mycards.pop(self.mytrumps.pop())
            else:
                #print "scooby"
                return self.mycards.pop(validcards.pop())

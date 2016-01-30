from players import *
from utility import *
class Bot(Players):

    def __init__(self,mycards , trump):
        self.mycards = mycards
        self.trump = trump
        self.sortmycardsandtrumps()
        self.utility = Utility()

    def move(self, player,  currentcards):
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
        if len(validcards) > 0 and len(istrumpthere) == 0:# throw the biggest card if no trump
            #print "daphne"
            tothrow = self.utility.largest_card(validcards)
            self.mycards.remove(tothrow)
            return tothrow
        elif len(validcards) > 0 and len(istrumpthere) > 0:     # throw smallest card if have valid cards and if there is trump
            #print "velma"
            tothrow = self.utility.smallest_card(validcards)
            self.mycards.remove(tothrow)
            return tothrow
        else:
            #print "fred"
            if self.utility.prioritytable(self.mytrumps[-1].split("_")[1]) > max(istrumpthere):
                #print "shaggy"
                tothrow = self.mytrumps.pop()       # throw the bigger trump not biggest
                self.mycards.remove(tothrow)
                return tothrow
            else:
                #print "scooby"
                tothrow = self.mycards.pop()        # throw smallest card if trump thrown is bigger than bots biggest trump and no valid card
                return tothrow

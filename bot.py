class Bot(object):

    def __init__(self, mycards, trump):
        self.mycards = mycards
        self.trump = trump
        self.sortmycardsandtrumps()

    def move(self, currentcards):
        if len(currentcards) == 0:
            return self.makefirstmove()
        else:
            return self.makecountermove(currentcards)

    def prioritytable(self, numeral):
        if numeral == "A":
            return 13
        elif numeral == "K":
            return 12
        elif numeral == "Q":
            return 11
        elif numeral == "J":
            return 10
        elif numeral == "10":
            return 9
        elif numeral == "9":
            return 8
        elif numeral == "8":
            return 7
        elif numeral == "7":
            return 6
        elif numeral == "6":
            return 5
        elif numeral == "5":
            return 4
        elif numeral == "4":
            return 3
        elif numeral == "3":
            return 2
        elif numeral == "3":
            return 1
        # return prioritytable[numeral]

    def sortmycardsandtrumps(self):
        self.mycards.sort(key=lambda x: self.prioritytable(x[2]))
        self.mytrumps = [i for i in self.mycards if i[0] == self.trump]

    def makefirstmove(self):
        return self.mycards.pop()

    def makecountermove(self, currentcards):
        # cards belonging to same suit as of current round
        suitofround = currentcards[0][2]
        validcards = [self.prioritytable(i[2]) for i in self.mycards if i[
                                    0] == suitofround]  # validcards I have for this round
        # has anyone thrown trump in this round
        istrumpthere = [self.prioritytable(i[2])
                        for i in currentcards if i[0] == self.trump]
        istrumpthere.append(0)
        if len(validcards) > 0 and len(istrumpthere) == 0:
            return validcards.pop()
        elif len(validcards) > 0 and len(istrumpthere) > 0:
            return validcards.pop(0)
        else:
            if self.prioritytable(self.mytrumps[-1]) > max(istrumpthere):
                return self.mycards.pop(self.mytrumps.pop())
            else:
                return self.mycards.pop()

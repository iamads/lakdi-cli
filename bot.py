class Bot(object):

    def __init__(self, mycards, trump):
        self.mycards = mycards.sort(key=lambda x: self.prioritytable(x[2]))
        self.trump = trump
        self.mytrumps = [i for i in self.mycards if i[2] == self.trump]

    def move(self, currentcards):
        if len(currentcards) == 0:
            self.makefirstmove(self.mycards)
        else:
            self.makecountermove(currentcards)

    def prioritytable(self, numeral):
        # prioritytable = {
        #     "A": 13,
        #     "K": 12,
        #     "Q": 11,
        #     "J": 10,
        #     "10": 9,
        #     "9": 8,
        #     "8": 7,
        #     "7": 6,
        #     "6": 5,
        #     "5": 4,
        #     "4": 3,
        #     "3": 2,
        #     "2": 1
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

    def makefirstmove(self, cards):
        return self.mycards.pop()

     def makecountermove(self, currentcards):
        # cards belonging to same suit as of current round
        suitofround = currentcards[0][2]
        validcards = [self.prioritytable(i[2]) for i in self.mycards if i[
                                    0] == suitofround]  # validcards I have for this round
        # has anyone thrown trump in this round
        istrumpthere = [self.prioritytable(i[2])
                        for i in currentcards if i[0] == self.trump]
        if len(validcards) > 0 and len(istrumpthere) == 0:
            return validcards.pop()
        elif len(validcards) > 0 and len(istrumpthere) > 0:
            return validcards.pop(0)
        else:
            if self.prioritytable(self.mytrumps[-1]) > max(istrumpthere):
                return self.mycards.pop(self.mytrumps.pop())
            else:
                return self.mycards.pop()

from pick import pick
class Players(object):

    def __init__(self,  mycards, trump):
        self.mycards = mycards
        self.trump = trump
        self.sortmycardsandtrumps()

    def sortmycardsandtrumps(self):
        self.mycards.sort(key=lambda x: self.prioritytable(x.split("_")[1]))
        self.mytrumps = [i for i in self.mycards if i[0] == self.trump]

    def move(self,player,currentroundcards):         # Add current cards for validity checking
        title = player + " Choose your card. current round = " + " ".join(currentroundcards)
        # Need to add get valid cards and only show those as options
        option,index = pick(self.mycards, title)
        return option

    def prioritytable(self, numeral):       # Should be a separate composition
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
        elif numeral == "2":
            return 1
        # return prioritytable[numeral]


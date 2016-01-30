class Utility(object):
    
    def prioritytable(self,numeral):
        priority = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        return priority.index(numeral)
    
    def largest_card(self, cards):
        cards.sort(key=lambda x: self.prioritytable(x.split("_")[1]))
        return cards.pop()
        
    def smallest_card(self,cards):
        cards.sort(key=lambda x: self.priority(x.split("_")[1]))
        return cards.pop(0)    
    
    
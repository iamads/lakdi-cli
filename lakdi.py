from bot import *
from players import *
from pick import pick
cards = [
    "h_A",
    "h_K",
    "h_Q",
    "h_J",
    "h_10",
    "h_9",
    "h_8",
    "h_7",
    "h_6",
    "h_5",
    "h_4",
    "h_3",
    "h_2",
    "c_A",
    "c_K",
    "c_Q",
    "c_J",
    "c_10",
    "c_9",
    "c_8",
    "c_7",
    "c_6",
    "c_5",
    "c_4",
    "c_3",
    "c_2",
    "d_A",
    "d_K",
    "d_Q",
    "d_J",
    "d_10",
    "d_9",
    "d_8",
    "d_7",
    "d_6",
    "d_5",
    "d_4",
    "d_3",
    "d_2",
    "s_A",
    "s_K",
    "s_Q",
    "s_J",
    "s_10",
    "s_9",
    "s_8",
    "s_7",
    "s_6",
    "s_5",
    "s_4",
    "s_3",
     "s_2"]
players = ["player1", "player2", "player3", "player4"]
player_cards = {"player1": [], "player2": [], "player3": [], "player4": []}
playertypes = {"player1": False, "player2": False, "player3": False,
               "player4": False}  # True for human player else false
playerinstance = {}
trump = "s"  # Needs to be variable
predictedscore = {"player1": 0, "player2": 0, "player3": 0, "player4": 0}
currentscore = {"player1": 0, "player2": 0, "player3": 0, "player4": 0}
currentround = []


def getcountofplayers():
    n = input()
    if n > 4:
        print "Number of players cannot be more than 4."
        return getcountofplayers()
    elif n < 1:
        print "Number of players cannot be less than 1."
        return getcountofplayers()
    else:
        return n


def assignplayertypes(n):
    if n == 1:
        playertypes["player1"] = True
    elif n == 2:
        playertypes["player1"] = playertypes["player2"] = True
    elif n == 3:
        playertypes["player2"] = playertypes[
            "player3"] = playertypes["player1"] = True
    elif n == 4:
        playertypes["player1"] = playertypes["player2"] = playertypes[
            "player3"] = playertypes["player4"] = True


def distributecards():
    # use this distribution for now randomise later
    player_cards["player1"] = [
        "d_6",
        "d_10",
        "d_7",
        "h_7",
        "c_K",
        "s_5",
        "h_5",
        "c_8",
        "h_A",
        "h_9",
        "d_2",
        "c_4",
     "d_8"]
    player_cards["player2"] = [
        "d_3",
        "d_9",
        "s_7",
        "s_4",
        "h_2",
        "d_4",
        "d_K",
        "c_3",
        "d_Q",
        "h_Q",
        "s_9",
        "c_10",
     "c_2"]
    player_cards["player3"] = [
        "h_6",
        "h_8",
        "s_6",
        "d_J",
        "h_J",
        "h_10",
        "c_J",
        "s_Q",
        "c_6",
        "c_A",
        "s_8",
        "s_3",
     "h_K"]
    player_cards["player4"] = [
        "s_10",
        "s_2",
        "c_9",
        "s_K",
        "c_5",
        "s_J",
        "h_4",
        "c_Q",
        "d_5",
        "s_A",
        "c_7",
        "h_3",
     "d_A"]
    for player in players:
        if playertypes[player]:
            playerinstance[player] = Players(player_cards[player],trump)
        else:
            playerinstance[player] = Bot(player_cards[player],trump)


def showcards(player):
    print player, "cards are", player_cards[player]


def showcardsandgetprediction():
    for player in players:
        if playertypes[player]:
            showcards(player)
            predictedscore[player] = input()
            # Add confirmation for predicted score
        else:
            predictedscore[player] = 3  # this needs to be decided by the bot
            print player, "predicted ", predictedscore[player]


def biggest_same_suit(cards):
    priority = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    cards.sort(key=lambda x: priority.index(x.split("_")[1]))
    return cards.pop()


def findwinner(currentcards):
    trumpsincurrentround = [i for i in currentcards if i[0]==trump]
    if len(trumpsincurrentround) > 0:
        # Return biggest card of all trumps
        return players[currentcards.index(biggest_same_suit(trumpsincurrentround))]
    else:
        samesuitasfirstcard = [i for i  in currentcards if i[0]== currentcards[0][0]]
        print currentcards
        return players[currentcards.index(biggest_same_suit(samesuitasfirstcard))]

def runchance():
    currentroundcards = []
    for player in players:
        currentroundcards.append(playermakemove(player,currentroundcards))
    winner = findwinner(currentroundcards)
    return winner


def playermakemove(player,currentroundcards):
    return playerinstance[player].move(player,currentroundcards)


def rotatetheplayers(winner):
    global players
    startfromhere= players.index(winner)
    players = players[startfromhere:] + players[:startfromhere]


def startgame():
    numplayers = getcountofplayers()
    assignplayertypes(numplayers)
    distributecards()
    showcardsandgetprediction()
    for i in xrange(13):
        winner = runchance()
        currentscore[winner] += 1
        print winner , " won this round."
        rotatetheplayers(winner)
        raw_input(">Go ahead")

startgame()

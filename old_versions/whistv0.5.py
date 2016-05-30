##Input the number of players and asks for the names
playerlist = []
def howManyPlayers():
    while True:
        try:
            no_players = int(input('Enter number of players(3-6): '))
        except ValueError:
            print('Enter a number between 3 and 6): ')
            continue
        if no_players not in range(3, 7):
            print('BETWEEN 3 AND 6 I SAID!')
        else:
            break
    while len(playerlist) != no_players:
        name = input('Enter player name: ')
        playerlist.append(name)
    print('And the players are: ', end='')
    print(*playerlist, sep=', ')
        


##bids = len(playerlist)
##print(bids)

##Points added when you win + bids won
base_score = 5

##threePlayersRounds[1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1]

## Player biddings. Added max players (6). Handling the number of players when calling them in roundx()
## Need to figure out the max bidding to use with the other rounds (2,3,4,etc)
class Players():
    def player1bid():
        global p1bid
        while True:
            try:
                p1bid = int(input(playerlist[0] + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p1bid > 1:
                print("You can't bid more than 1.")
            else:
                break
    def player2bid():
        global p2bid
        while True:
            try:
                p2bid = int(input(playerlist[1] + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p2bid > 1:
                print("You can't bid more than 1.")
            else:
                break
    def player3bid():
        global p3bid
        while True:
            try:
                p3bid = int(input(playerlist[2] + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p3bid > 1:
                print("You can't bid more than 1.")
            else:
                break
    def player4bid():
        global p4bid
        while True:
            try:
                p4bid = int(input(playerlist[3] + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p4bid > 1:
                print("You can't bid more than 1.")
            else:
                break
    def player5bid():
        global p5bid
        while True:
            try:
                p5bid = int(input(playerlist[4] + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p5bid > 1:
                print("You can't bid more than 1.")
            else:
                break
    def player6bid():
        global p6bid
        while True:
            try:
                p6bid = int(input(playerlist[5] + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p6bid > 1:
                print("You can't bid more than 1.")
            else:
                break
        


##Game starts. Based on number of players, when playerlist ends, the error is passed
def round1():
    print('Round 1. Bid.')
    try:
        Players.player1bid()
        Players.player2bid()
        Players.player3bid()
        Players.player4bid()
        Players.player5bid()
        Players.player6bid()
    except IndexError:
        pass
    try:
        print(playerlist[0] + ' bid: ' + str(p1bid))
        print(playerlist[1] + ' bid: ' + str(p2bid))
        print(playerlist[2] + ' bid: ' + str(p3bid))
        print(playerlist[3] + ' bid: ' + str(p4bid))
        print(playerlist[4] + ' bid: ' + str(p5bid))
        print(playerlist[5] + ' bid: ' + str(p6bid))
    except IndexError:
        pass

## First version of roundx. Keeping it in case i need something
## I think it was better to separate the player bidding from the rounds
## Still trying to figure how to call rounds without adding all of them separately
def round2():
##    global p1bid, p2bid, p3bid, p4bid, p5bid, p6bid
    print('Round 2. Bid.')
    
    while True:
        try:
            p2bid = int(input(playerlist[1] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p2bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        try:
            p3bid = int(input(playerlist[2] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p3bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        try:
            p4bid = int(input(playerlist[3] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p4bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        try:
            p5bid = int(input(playerlist[4] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p5bid > 1:
            print("You can't bid more than 1.")
            continue
        else:
            break
    if (p2bid + p3bid + p4bid + p5bid) == 0:
        p1bid = 0    
    elif (p2bid + p3bid + p4bid + p5bid) == 1:
        p1bid = 1 
    else:
        while True:
            try:
                p1bid = int(input(playerlist[0] + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p1bid > 1:
                print("You can't bid more than 1.")
            else:
                break
       
    print(playerlist[1] + ' bid: ' + str(p2bid))
    print(playerlist[2] + ' bid: ' + str(p3bid))
    print(playerlist[3] + ' bid: ' + str(p4bid))
    print(playerlist[4] + ' bid: ' + str(p5bid))
    print(playerlist[0] + ' bid: ' + str(p1bid))


## Score calculation. Would like to improve
## Right now there's a def scorex for every roundx
## Might make it like i did with the player biddings
def score1():
    global p1score, p2score, p3score, p4score, p5score
    print('Round 1. Insert results.')
    while True:
        try:
            p1result = int(input(playerlist[0] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p1result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
    while True:
        if p1result == 1:
            p2result = 0
            p3result = 0
            p4result = 0
            p5result = 0
            break
        try:
            p2result = int(input(playerlist[1] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p2result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
    while True:
        if p1result or p2result == 1:
            p3result = 0
            p4result = 0
            p5result = 0
            break
        try:
            p3result = int(input(playerlist[2] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p3result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
    while True:
        if p1result or p2result or p3result == 1:
            p4result = 0
            p5result = 0
            break
        try:
            p4result = int(input(playerlist[3] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p4result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
    while True:
        if p1result or p2result or p3result or p4result == 1:
            p5result = 0
            break
        try:
            p5result = int(input(playerlist[4] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p5result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
    try:
        if p1result == p1bid:
            p1score = base_score + p1result
        else:
            p1score = -1
        if p2result == p2bid:
            p2score = base_score + p2result
        else:
            p2score = -1
        if p3result == p3bid:
            p3score = base_score + p3result
        else:
            p3score = -1
        if p4result == p4bid:
            p4score = base_score + p4result
        else:
            p4score = -1       
        if p5result == p5bid:
            p5score = base_score + p5result
        else:
            p5score = -1
    except NameError:
        pass
    try:
        print('Score after round 1')
        print(playerlist[0] + ": " + str(p1score))
        print(playerlist[1] + ": " + str(p2score))
        print(playerlist[2] + ": " + str(p3score))
        print(playerlist[3] + ": " + str(p4score))
        print(playerlist[4] + ": " + str(p5score))
    except IndexError:
        pass

def score2():
    global p1score, p2score, p3score, p4score, p5score
    print('Round 2. Insert results.')
    while True:
        try:
            p1result = int(input(playerlist[0] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p1result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
    while True:
        if p1result == 1:
            p2result = 0
            p3result = 0
            p4result = 0
            p5result = 0
            break
        try:
            p2result = int(input(playerlist[1] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p2result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
    while True:
        if p1result or p2result == 1:
            p3result = 0
            p4result = 0
            p5result = 0
            break
        try:
            p3result = int(input(playerlist[2] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p3result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
    while True:
        if p1result or p2result or p3result == 1:
            p4result = 0
            p5result = 0
            break
        try:
            p4result = int(input(playerlist[3] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p4result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
    while True:
        if p1result or p2result or p3result or p4result == 1:
            p5result = 0
            break
        try:
            p5result = int(input(playerlist[4] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p5result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
        
    if p1result == p1bid:
        p1score = p1score + base_score + p1result
    elif p1result < p1bid:
        p1score = p1score - (p1bid - p1result)
    else:
        p1score = p1score - (p1result - p1bid)
    if p2result == p2bid:
        p2score = p2score + base_score + p2result
    elif p2result < p2bid:
        p2score = p2score - (p2bid - p2result)
    else:
        p2score = p2score - (p2result - p2bid)
    if p3result == p3bid:
        p3score = p3score + base_score + p3result
    elif p3result < p3bid:
        p3score = p3score - (p3bid - p3result)
    else:
        p3score = p3score - (p3result - p3bid)
    if p4result == p4bid:
        p4score = p4score + base_score + p4result
    elif p4result < p4bid:
        p4score = p4score - (p4bid - p4result)
    else:
        p4score = p4score - (p4result - p4bid)
    if p5result == p5bid:
        p5score = p5score + base_score + p5result
    elif p5result < p5bid:
        p5score = p5score - (p5bid - p5result)
    else:
        p5score = p5score - (p5result - p5bid)
        
    print('Score after round 2')
    print(playerlist[0] + ": " + str(p1score))
    print(playerlist[1] + ": " + str(p2score))
    print(playerlist[2] + ": " + str(p3score))
    print(playerlist[3] + ": " + str(p4score))
    print(playerlist[4] + ": " + str(p5score))

## starting the game
howManyPlayers()

round1()
score1()
wait = input("PRESS ENTER TO CONTINUE.")
round2()
score2()

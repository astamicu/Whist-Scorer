playerlist = []
def players():   
    while len(playerlist) != 5:
        name = input('Enter player name: ')
        playerlist.append(name)
    print('And the players are: ', end='')
    print(*playerlist, sep=', ')


start_score = 0
base_score = 5
p = 0


def howManyRounds():
    global rounds, x, k
    rounds = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 7, 6, 5, 4, 3
              , 2, 1, 1, 1, 1, 1]
    k = len(rounds) # k = 27
    x = iter(rounds)
    print(rounds)


class Players():
    def player1bid():
        global p1bid
        while True:
            try:
                p1bid = int(input(playerlist[0] + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p1bid > z:
                print("You can't bid more than " + str(z))
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
            if p2bid > z:
                print("You can't bid more than " + str(z))
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
            if p3bid > z:
                print("You can't bid more than " + str(z))
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
            if p4bid > z:
                print("You can't bid more than " + str(z))
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
            if p5bid > z:
                print("You can't bid more than " + str(z))
            else:
                break


def playersOrder():
    if k % 1 == :
        Players.player1bid()
        Players.player2bid()
        Players.player3bid()
        Players.player4bid()
        Players.player5bid()
        print(playerlist[0] + ' bid: ' + str(p1bid))
        print(playerlist[1] + ' bid: ' + str(p2bid))
        print(playerlist[2] + ' bid: ' + str(p3bid))
        print(playerlist[3] + ' bid: ' + str(p4bid))
        print(playerlist[4] + ' bid: ' + str(p5bid))

        
def increaseRounds():
    global z, p
    z = next(x)
    print('Cards to divide: ' + str(z))
    p = p + 1
    print('p = ' + str(p))

def roundNumber():
    playersOrder()
##    print('Round ' + str(p) + '. Bid.')
##    if len(playerlist) == 3 and (p == 1 or p == 4 or p == 7 or p == 10 or p == 13
##                                 or p == 16 or p == 19 or p == 22):
##        try:
##            Players.player1bid()
##            Players.player2bid()
##            Players.player3bid()
##            Players.player4bid()
##            Players.player5bid()
##            Players.player6bid()
##        except IndexError:
##            pass
##        try:
##            print(playerlist[0] + ' bid: ' + str(p1bid))
##            print(playerlist[1] + ' bid: ' + str(p2bid))
##            print(playerlist[2] + ' bid: ' + str(p3bid))
##            print(playerlist[3] + ' bid: ' + str(p4bid))
##            print(playerlist[4] + ' bid: ' + str(p5bid))
##            print(playerlist[5] + ' bid: ' + str(p6bid))
##        except IndexError:
##            pass
##    elif len(playerlist) == 3 and (p == 2 or p == 5 or p == 8 or p == 11 or p == 14
##                                 or p == 17 or p == 20 or p == 23):
##        try: 
##            Players.player2bid()
##            Players.player3bid()
##            Players.player4bid()
##            Players.player5bid()
##            Players.player6bid()
##            Players.player1bid()
##        except IndexError:
##            pass
##        try:
##            print(playerlist[1] + ' bid: ' + str(p2bid))
##            print(playerlist[2] + ' bid: ' + str(p3bid))
##            print(playerlist[3] + ' bid: ' + str(p4bid))
##            print(playerlist[4] + ' bid: ' + str(p5bid))
##            print(playerlist[5] + ' bid: ' + str(p6bid))
##            print(playerlist[0] + ' bid: ' + str(p1bid))
##        except IndexError:
##            pass
##    elif len(playerlist) == 3 and (p == 3 or p == 6 or p == 9 or p == 12 or p == 15
##                                 or p == 18 or p == 21 or p == 24):
##        try: 
##            Players.player3bid()
##            Players.player1bid()
##            Players.player2bid()
##            Players.player4bid()
##            Players.player5bid()
##            Players.player6bid()
##            
##        except IndexError:
##            pass
##        try:
##            print(playerlist[2] + ' bid: ' + str(p3bid))
##            print(playerlist[3] + ' bid: ' + str(p4bid))
##            print(playerlist[4] + ' bid: ' + str(p5bid))
##            print(playerlist[5] + ' bid: ' + str(p6bid))
##            print(playerlist[0] + ' bid: ' + str(p1bid))
##            print(playerlist[1] + ' bid: ' + str(p2bid))
##        except IndexError:
##            pass

## Score calculation. Would like to improve
## Right now there's a def scorex for every roundx
## Might make it like i did with the player biddings
def scoring():
    global p1score, p2score, p3score, p4score, p5score, p6score
    print('Round ' + str(p) + '. Insert results.')
    while True:
        try:
            p1result = int(input(playerlist[0] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p1result > z:
            print("You couldn't bid more than " + str(z))
            continue
        else:
            break
    while True:
        if p1result == z:
            p2result = 0
            p3result = 0
            p4result = 0
            p5result = 0
            p6result = 0
            break
        try:
            p2result = int(input(playerlist[1] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p2result > z:
            print("You couldn't bid more than" + str(z))
            continue
        else:
            break
    while True:
        if p1result or p2result == z:
            p3result = 0
            p4result = 0
            p5result = 0
            p6result = 0
            break
        try:
            p3result = int(input(playerlist[2] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p3result > z:
            print("You couldn't bid more than" + str(z))
            continue
        else:
            break
    while True:
        if p1result or p2result or p3result == z:
            p4result = 0
            p5result = 0
            p6result = 0
            break
        try:
            p4result = int(input(playerlist[3] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p4result > z:
            print("You couldn't bid more than" + str(z))
            continue
        else:
            break
    while True:
        if p1result or p2result or p3result or p4result == z:
            p5result = 0
            p6result = 0
            break
        try:
            p5result = int(input(playerlist[4] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p5result > z:
            print("You couldn't bid more than" + str(z))
            continue
        else:
            break
    while True:
        if p1result or p2result or p3result or p4result or p5result == z:
            p6result = 0
            break
        try:
            p5result = int(input(playerlist[4] + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p5result > z:
            print("You couldn't bid more than" + str(z))
            continue
        else:
            break
    try:
        if p == 1:
            if p1result == p1bid:
                p1score = base_score + p1result
            else:
                p1score = start_score - p1bid
            if p2result == p2bid:
                p2score = base_score + p2result
            else:
                p2score = start_score - p2bid
            if p3result == p3bid:
                p3score = base_score + p3result
            else:
                p3score = start_score - p3bid
            if p4result == p4bid:
                p4score = base_score + p4result
            else:
                p4score = start_score - p4bid       
            if p5result == p5bid:
                p5score = base_score + p5result
            else:
                p5score = start_score - p5bid
            if p6result == p6bid:
                p6score = base_score + p6result
            else:
                p6score = start_score - p6bid
        else:
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
    except NameError:
        pass
    try:
        print('Score after round ' + str(p))
        print(playerlist[0] + ": " + str(p1score))
        print(playerlist[1] + ": " + str(p2score))
        print(playerlist[2] + ": " + str(p3score))
        print(playerlist[3] + ": " + str(p4score))
        print(playerlist[4] + ": " + str(p5score))
        print(playerlist[5] + ": " + str(p6score))
    except IndexError:
        pass


## starting the game
players()
howManyRounds()

while p != k:
    increaseRounds()
    roundNumber()
    scoring()
    wait = input("PRESS ENTER TO CONTINUE.")
else:
    print('Game Over')


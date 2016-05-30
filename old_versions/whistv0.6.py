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
start_score = 0
base_score = 5
p = 0


def howManyRounds():
    global rundele, x, k
    if len(playerlist) == 3:
        rundele = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1]
        k = len(rundele)
        print('Number of rounds: ' + str(k))
    elif len(playerlist) == 4:
        rundele = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1]
        k = len(rundele)
        print('Number of rounds: ' + str(k))
    elif len(playerlist) == 5:
        rundele = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]
        k = len(rundele)
        print('Number of rounds: ' + str(k))
    else:
        rundele = [1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1]
        k = len(rundele)
        print('Number of rounds: ' + str(k))
    x = iter(rundele)
    print(rundele)


    
                              


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
    def player6bid():
        global p6bid
        while True:
            try:
                p6bid = int(input(playerlist[5] + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p6bid > z:
                print("You can't bid more than " + str(z))
            else:
                break



##Game starts. Based on number of players, when playerlist ends, the error is passed


##def increaseRounds():
##    global z
##    try:
##        z = next(x)
##    except StopIteration:
##        return z
##    print(z)
def increaseRounds():
    global z, p
    z = next(x)
    print('Cards to divide: ' + str(z))
    p = p + 1
    print('p = ' + str(p))

def roundNumberThree():
    print('Round ' + str(p) + '. Bid.')
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
howManyPlayers()
howManyRounds()

while p != k:
    increaseRounds()
    roundNumberThree()
    scoring()
    wait = input("PRESS ENTER TO CONTINUE.")
else:
    print('Game Over')


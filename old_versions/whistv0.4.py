##players = []
##def howManyPlayers():
##    while True:
##        try:
##            no_players = int(input('Enter number of players(3-6): '))
##        except ValueError:
##            print('Enter a number between 3 and 6): ')
##            continue
##        if no_players not in range(3, 7):
##            print('BETWEEN 3 AND 6 I SAID!')
##        else:
##            break
##    while len(players) != no_players:
##        name = input('Enter player name: ')
##        players.append(name)
##        
##howManyPlayers()
##print('And the players are: ', end='')
##print(*players, sep=', ')
##
##bids = len(players)
##print(bids)

p1 = 'a'
p2 = 'b'
p3 = 'c'
p4 = 'd'
p5 = 'e'

base_score = 5

pbid = []

def round1():
    global p1bid, p2bid, p3bid, p4bid, p5bid
    print('Round 1. Bid.')
    while True:
        try:
            p1bid = int(input(p1 + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p1bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        try:
            p2bid = int(input(p2 + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p2bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        try:
            p3bid = int(input(p3 + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p3bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        try:
            p4bid = int(input(p4 + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p4bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        if (p1bid + p2bid + p3bid + p4bid) == 0:
            p5bid = 0
            break
        elif (p1bid + p2bid + p3bid + p4bid) == 1:
            p5bid = 1
            break
        else:
            while True:
                try:
                    p5bid = int(input(p5 + ': '))
                except ValueError:
                    print("Insert a number.")
                    continue
                if p5bid > 1:
                    print("You can't bid more than 1.")
                    continue
                else:
                    break
        break
    print(p1 + ' bid: ' + str(p1bid))
    print(p2 + ' bid: ' + str(p2bid))
    print(p3 + ' bid: ' + str(p3bid))
    print(p4 + ' bid: ' + str(p4bid))
    print(p5 + ' bid: ' + str(p5bid))

def round2():
    global p1bid, p2bid, p3bid, p4bid, p5bid
    print('Round 2. Bid.')
    
    while True:
        try:
            p2bid = int(input(p2 + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p2bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        try:
            p3bid = int(input(p3 + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p3bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        try:
            p4bid = int(input(p4 + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p4bid > 1:
            print("You can't bid more than 1.")
        else:
            break
    while True:
        try:
            p5bid = int(input(p5 + ': '))
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
                p1bid = int(input(p1 + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if p1bid > 1:
                print("You can't bid more than 1.")
            else:
                break
       
    print(p2 + ' bid: ' + str(p2bid))
    print(p3 + ' bid: ' + str(p3bid))
    print(p4 + ' bid: ' + str(p4bid))
    print(p5 + ' bid: ' + str(p5bid))
    print(p1 + ' bid: ' + str(p1bid))

def score1():
    global p1score, p2score, p3score, p4score, p5score
    print('Round 1. Insert results.')
    while True:
        try:
            p1result = int(input(p1 + ': '))
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
            p2result = int(input(p2 + ': '))
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
            p3result = int(input(p3 + ': '))
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
            p4result = int(input(p4 + ': '))
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
            p5result = int(input(p5 + ': '))
        except ValueError:
            print("Insert a number.")
            continue
        if p5result > 1:
            print("You couldn't bid more than 1.")
            continue
        else:
            break
        
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
        
    print('Score after round 1')
    print(p1 + ": " + str(p1score))
    print(p2 + ": " + str(p2score))
    print(p3 + ": " + str(p3score))
    print(p4 + ": " + str(p4score))
    print(p5 + ": " + str(p5score))

def score2():
    global p1score, p2score, p3score, p4score, p5score
    print('Round 2. Insert results.')
    while True:
        try:
            p1result = int(input(p1 + ': '))
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
            p2result = int(input(p2 + ': '))
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
            p3result = int(input(p3 + ': '))
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
            p4result = int(input(p4 + ': '))
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
            p5result = int(input(p5 + ': '))
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
    print(p1 + ": " + str(p1score))
    print(p2 + ": " + str(p2score))
    print(p3 + ": " + str(p3score))
    print(p4 + ": " + str(p4score))
    print(p5 + ": " + str(p5score))

round1()
score1()
wait = input("PRESS ENTER TO CONTINUE.")
round2()
score2()

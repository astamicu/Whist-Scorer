from operator import add

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


start_score = 0
base_score = 5
p = 0
i = 0
bidList = []
resultList = []
scoreList = []
finalScores = [0, 0, 0, 0, 0]




def howManyRounds():
    roundList = []
    for val in playerlist:
        roundList.append(1)
    roundList.extend(range(2, 8))
    for val in playerlist:
        roundList.append(8)
    roundList.extend(reversed(range(2, 8)))
    for val in playerlist:
        roundList.append(1)
    print(roundList)
    global rounds, x, k
    rounds = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 7, 6, 5, 4, 3
              , 2, 1, 1, 1, 1, 1]
    k = len(roundList) # k = 27
    x = iter(roundList)
    print(rounds)

    
def changeOrder():
    global i, playerlist
    for val in playerlist:
##        print(val)
        i += 1
        if i >= len(playerlist) + 1:
##            print(playerlist)
            playerlist += [playerlist.pop(0)]
##            print(playerlist)
            break

def player():
    global i, playerlist, bidList
    print('Place your bids.')
    plist = iter(playerlist)
    lastPlayer = playerlist[-1]
##    print(lastPlayer)
    for val in playerlist:
        cine = next(plist)
        if cine == lastPlayer and z == 1 == sum(bidList):
            bidList.append(1)
            break
        elif cine == lastPlayer and z - sum(bidList) >= 0:
            print(cine + ", you can't bid " + str(z - sum(bidList)))
        elif cine == lastPlayer:
            print(cine + ", you can bid whatever you want.")
        while True:
            try:
                pbid = int(input(cine + ': '))
##                print(pbid)
            except ValueError:
                print("Insert a number.")
                continue
            if pbid > z:
                print("You can't bid more than " + str(z))
                continue
            if cine == lastPlayer and pbid == z - sum(bidList): 
                print("You can't bid " + str(pbid))
                continue
            else:
                bidList.append(pbid)
                break
        i += 1
    print(bidList)
    bidList[:] = []
        

def scoring():
    global i, bidList, playerlist, resultList, finalScores, presult
    pscore = 0
    maxbid = z
    print('Round ' + str(p) + '. Insert results.')
    plist = iter(playerlist)
    for val in playerlist:
        cine = next(plist)
        while sum(resultList) < z:
            #if sum(resultList) < z:
            print('Z-ul: ' + str(z))
            print('Suma result: ' + str(sum(resultList)))
            try:
                presult = int(input(cine + ': '))
            except ValueError:
                print("Insert a number.")
                continue
            if presult > z:
                print("You couldn't bid more than " + str(z))
                continue
            if presult > maxbid:
                print("The bids can't be bigger than " + str(z))
                continue
            else:
                resultList.append(presult)
                maxbid = z - sum(resultList)
##                    print(presult)
##                    print(resultList)
                break
        else:
            if len(resultList) < 5:
                resultList.append(0)
##                print(resultList)
            else:
                break





##                if sum(resultList) != z:
##                    resultList.append(presult)
##                    print(presult)
##                    print(resultList)
##                elif len(resultList) < 5:
##                    resultList.append(0)
##                    print(presult)
##                    print(resultList)
##                else:
##                    break

    print(resultList)
    blist = iter(bidList)
    rlist = iter(resultList)
    for val in bidList:
        theBid = next(blist)
        theResult = next(rlist)
##        print(theBid)
##        print(theResult)
        if theBid == theResult:
            pscore = base_score + theResult
            scoreList.append(pscore)
        else:
            pscore = start_score - theBid
            scoreList.append(pscore)
    print(scoreList)
    finalScores = list(map(add, scoreList, finalScores))
    bidList[:] = []
    resultList[:] = []
    scoreList[:] = []
    print(finalScores)
        
     
    
##    try:
##        if p == 1:
##            if presult == pbid:
##                pscore = base_score + presult
##            else:
##                p1score = start_score - p1bid
##        else:
##            if p1result == p1bid:
##                p1score = p1score + base_score + p1result
##            elif p1result < p1bid:
##                p1score = p1score - (p1bid - p1result)
##            else:
##                p1score = p1score - (p1result - p1bid)
##    except NameError:
##        pass

    
    

    
##        try:
##            print('Score after round ' + str(p))
##            print(cine + ": " + str(pscore))
##            print(playerlist[1] + ": " + str(p2score))
##            print(playerlist[2] + ": " + str(p3score))
##            print(playerlist[3] + ": " + str(p4score))
##            print(playerlist[4] + ": " + str(p5score))
##            print(playerlist[5] + ": " + str(p6score))
##        except IndexError:
##            pass



        
def increaseRounds():
    global z, p
    z = next(x)
    print('Cards to divide: ' + str(z))
    p = p + 1
##    print('p = ' + str(p))



## Score calculation. Would like to improve
## Right now there's a def scorex for every roundx
## Might make it like i did with the player biddings
def scoring234():
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


#### starting the game
howManyPlayers()
##allThePlayers()
howManyRounds()
##
##while p != k:
##    increaseRounds()
##    player()
####    roundNumber()
##    scoring()
##    changeOrder()
##    wait = input("PRESS ENTER TO CONTINUE.")
##else:
##    print('Game Over')


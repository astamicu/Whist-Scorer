from operator import add

playerList = []
p = 0
i = 0
bidList = []
resultList = []
scoreList = []
finalScores = [0, 0, 0, 0, 0]


def howManyPlayers():
    while True:
        try:
            number_of_players = int(input('Enter number of players(3-6): '))
        except ValueError:
            print('Enter a number between 3 and 6): ')
            continue
        if number_of_players not in range(3, 7):
            print('BETWEEN 3 AND 6 I SAID!')
        else:
            break
    while len(playerList) != number_of_players:
        name = input('Enter player name: ')
        if name not in playerList:
            playerList.append(name)
        else:
            print('Player name already exists. Please enter another name')
    print('And the players are: ', end='')
    print(*playerList, sep=', ')


def howManyRounds():
    roundList = []
    for val in playerList:
        roundList.append(1)
    roundList.extend(range(2, 8))
    for val in playerList:
        roundList.append(8)
    roundList.extend(reversed(range(2, 8)))
    for val in playerList:
        roundList.append(1)
    print("Number of rounds: " + str(len(roundList)))
    global x, k
    k = len(roundList) 
    x = iter(roundList)


def increaseRounds():
    global z, p
    z = next(x)
    print('Cards to divide: ' + str(z))
    p = p + 1

    
def changeOrder():
    global i, playerList
    for val in playerList:
        i += 1
        if i >= len(playerList) + 1:
            playerList += [playerList.pop(0)]
            break


def player():
    global i, bidList
    print('Round ' + str(p) + ' bids:')
    plist = iter(playerList)
    lastPlayer = playerList[-1]
    for val in playerList:
        cine = next(plist)
        if cine == lastPlayer and z == 1 == sum(bidList):
            bidList.append(1)
            print(cine + ", you are obligated to bid 1")
            break
        elif cine == lastPlayer and z - sum(bidList) >= 0:
            print(cine + ", you can't bid " + str(z - sum(bidList)))
        while True:
            try:
                pbid = int(input(cine + ': '))
            except ValueError:
                print("Insert a number")
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

    print("\n")
    fmt = '{:<15}{}'
    print(fmt.format('Player', 'Bid'))
    for i, (player, bid) in enumerate(zip(playerList, bidList)):
        print(fmt.format(player, bid))
    print("\n")
        

def scoring():
    global i, bidList, resultList, finalScores, presult
    start_score = 0
    base_score = 5
    pscore = 0
    maxbid = z
    print('Round ' + str(p) + ' results:')
    plist = iter(playerList)
    lastPlayer = playerList[-1]
    for val in playerList:
        cine = next(plist)
        if cine == lastPlayer and sum(resultList) != z:
            resultList.append(z - sum(resultList))
            print(cine + ", you made " + str(resultList[-1]) + ' for sure')
        while sum(resultList) < z:
            try:
                presult = int(input(cine + ': '))
            except ValueError:
                print("Insert a number")
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
                break
        else:
            if len(resultList) < len(playerList):
                resultList.append(0)
            else:
                break

    print("\n")
    fmt = '{:<15}{:<15}{}'
    print(fmt.format('Player', 'Bid', 'Result'))
    for i, (player, bid, result) in enumerate(zip(playerList, bidList, resultList)):
        print(fmt.format(player, bid, result))
        
    blist = iter(bidList)
    rlist = iter(resultList)
    for val in bidList:
        theBid = next(blist)
        theResult = next(rlist)
        if p == 1:
            if theResult == theBid:
                pscore = base_score + theResult
                scoreList.append(pscore)
            else:
                pscore = start_score - theBid
                scoreList.append(pscore)
        else:
            if theResult == theBid:
                pscore = base_score + theResult
                scoreList.append(pscore)
            elif theResult < theBid:
                pscore = theResult - theBid
                scoreList.append(pscore)
            else:
                pscore = theBid - theResult
                scoreList.append(pscore)

    finalScores = list(map(add, scoreList, finalScores))
    
    print("\n")
    fmt = '{:<15}{:<15}{}'
    print(fmt.format('Player', 'Round score', 'Final Score'))
    for i, (player, score, final) in enumerate(zip(playerList, scoreList, finalScores)):
        print(fmt.format(player, score, final))
    print("\n")

    bidList[:] = []
    resultList[:] = []
    scoreList[:] = []

    
howManyPlayers()
howManyRounds()
while p != k:
    increaseRounds()
    player()
    scoring()
    changeOrder()
    wait = input("Press enter if you're ready for next round.")
else:
    print("\n")
    print('Game Over')
    fmt = '{:<15}{}'
    print(fmt.format('Player', 'Final Score'))
    for i, (player, final) in enumerate(zip(playerList, finalScores)):
        print(fmt.format(player, final))

#this function will calculate the X and O score of the current board state.
import sys


def calculateScore(currentState, playerName):

    XScore = 0
    OScore = 0

    for i in range (0,5):
        for j in range (0,5):
            if currentState[i][j] == 'X':
                XScore = XScore + (int)(boardValuesMatrix[i][j])
            elif currentState[i][j] == 'O':
                OScore = OScore + (int)(boardValuesMatrix[i][j])

    #Decide who is the player and who is the opponent

    if playerName == 1:
       playerScore = XScore
       opponentScore = OScore
    elif playerName == 0:
       playerScore = OScore
       opponentScore = XScore

    #print(playerName, playerScore, opponentScore)

    return(playerScore, opponentScore)


#this function will check if the next move of X is a raid or sneak

def checkRaidX(i, j, currentState):

    tempraid = 0

    if i-1 >= 0:
        if currentState[i-1][j] == 'X':
            tempraid = 1

    if i+1 <= 4:
        if currentState[i+1][j] == 'X':
            tempraid = 1

    if j-1 >= 0:
        if currentState[i][j-1] == 'X':
            tempraid = 1

    if j+1 <= 4:
        if currentState[i][j+1] == 'X':
            tempraid = 1

    return tempraid

#this function will check if the next move of O is raid or sneak

def checkRaidO(i, j, currentState):

    tempraid = 0

    if i-1 >= 0:
        if currentState[i-1][j] == 'O':
            tempraid = 1


    if i+1 <= 4:
        if currentState[i+1][j] == 'O':
            tempraid = 1


    if j-1 >= 0:
        if currentState[i][j-1] == 'O':
            tempraid = 1


    if j+1 <= 4:
        if currentState[i][j+1] == 'O':
            tempraid = 1


    return tempraid


def greedyBestFirstSearch(playerName, currentState):



    OScore = 0
    XScore = 0
    tempi = 0
    tempj = 0
    playerScore = 0
    opponentScore = 0

    #calculate the current player and opponent score

    (playerScore, opponentScore) = calculateScore(currentState, playerName)

    tempOpponentScore = opponentScore

    #Calculate the initial evaluation function

    eval = playerScore - opponentScore
    #print(eval)

    tempcheck = eval


    #Now, go through each and every empty position on the board and calculate evaluation function for each

    for i in range(0,5):
        for j in range(0,5):
            max = playerScore + int(boardValuesMatrix[i][j])
            raid = 0
            tempeval = 0
            tempOpponentScore = opponentScore
            tempCurrentState = [x[:] for x in currentState]
            if currentState[i][j] == '*':
                if playerName == 1:

                    raid = checkRaidX(i,j,currentState)

                    if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'O':
                                max = max + (int)(boardValuesMatrix[i-1][j])
                                tempCurrentState[i-1][j] = 'X'
                                tempOpponentScore = tempOpponentScore - int(boardValuesMatrix[i-1][j])

                        if i+1 <= 4:
                            if currentState[i+1][j] == 'O':
                                max = max + (int)(boardValuesMatrix[i+1][j])
                                tempCurrentState[i+1][j] = 'X'
                                tempOpponentScore = tempOpponentScore - int(boardValuesMatrix[i+1][j])


                        if j-1 >= 0:
                            if currentState[i][j-1] == 'O':
                                max = max + (int)(boardValuesMatrix[i][j-1])
                                tempCurrentState[i][j-1] = 'X'
                                tempOpponentScore = tempOpponentScore - int(boardValuesMatrix[i][j-1])

                        if j+1 <= 4:
                            if currentState[i][j+1] == 'O':
                                max = max + (int)(boardValuesMatrix[i][j+1])
                                tempCurrentState[i][j+1] = 'X'
                                tempOpponentScore = tempOpponentScore - int(boardValuesMatrix[i][j+1])

                        tempeval = max - tempOpponentScore
                        if tempeval > tempcheck:
                            tempcheck = tempeval
                            tempi = i
                            tempj = j
                            finalOpponentScore = tempOpponentScore
                            tempCurrent = [x[:] for x in tempCurrentState]


                    elif raid == 0:
                        tempeval = max - tempOpponentScore
                        if tempeval > tempcheck:
                            tempcheck = tempeval
                            finalOpponentScore = tempOpponentScore
                            tempi = i
                            tempj = j
                            tempCurrent = [x[:] for x in tempCurrentState]

                elif playerName == 0:

                     raid = checkRaidO(i, j, currentState)

                     if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'X':
                                max = max + (int)(boardValuesMatrix[i-1][j])
                                tempCurrentState[i-1][j] = 'O'
                                tempOpponentScore = tempOpponentScore - int(boardValuesMatrix[i-1][j])


                        if i+1 <= 4:
                            if currentState[i+1][j] == 'X':
                                max = max + (int)(boardValuesMatrix[i+1][j])
                                tempCurrentState[i+1][j] = 'O'
                                tempOpponentScore = tempOpponentScore - int(boardValuesMatrix[i+1][j])

                        if j-1 >= 0:
                            if currentState[i][j-1] == 'X':
                                max = max + (int)(boardValuesMatrix[i][j-1])
                                tempCurrentState[i][j-1] = 'O'
                                tempOpponentScore = tempOpponentScore - int(boardValuesMatrix[i][j-1])

                        if j+1 <= 4:
                            if currentState[i][j+1] == 'X':
                                max = max + (int)(boardValuesMatrix[i][j+1])
                                tempCurrentState[i][j+1] = 'O'
                                tempOpponentScore = tempOpponentScore - int(boardValuesMatrix[i][j+1])


                        tempeval = max - tempOpponentScore
                        if tempeval > tempcheck:
                            tempcheck = tempeval
                            tempi = i
                            tempj = j
                            finalOpponentScore = tempOpponentScore
                            tempCurrent = [x[:] for x in tempCurrentState]

                     elif raid == 0:
                        tempeval = max - tempOpponentScore
                        if tempeval > tempcheck:
                            tempcheck = tempeval
                            finalOpponentScore = tempOpponentScore
                            tempi = i
                            tempj = j
                            tempCurrent = [x[:] for x in tempCurrentState]

    #print(tempi)
    #print(tempj)

    currentState = [x[:] for x in tempCurrent]

    #tempi and tempj store the position of next best move.

    return(tempi, tempj, currentState)




def calculateUtility(boardState, playerName):
    XScore = 0
    OScore = 0
    playerScore = 0
    opponentScore = 0
    leaf = 0

    for i in range (0,5):
        for j in range (0,5):
            if boardState[i][j] == 'X':
                XScore = XScore + (int)(boardValuesMatrix[i][j])
            elif boardState[i][j] == 'O':
                OScore = OScore + (int)(boardValuesMatrix[i][j])

    if playerName == 1:
        playerScore = XScore
        opponentScore = OScore
    elif playerName == 0:
        playerScore = OScore
        opponentScore = XScore



    leaf = int(playerScore - opponentScore)
    return leaf

def numberToAlphabets(i,j):
    if i == 0:
        x = 1
    elif i == 1:
        x = 2
    elif i == 2:
        x = 3
    elif i == 3:
        x = 4
    elif i == 4:
        x = 5

    if j == 0:
        y = 'A'
    elif j == 1:
        y = 'B'
    elif j == 2:
        y = 'C'
    elif j == 3:
        y = 'D'
    elif j == 4:
        y = 'E'

    return x,y

#this function will print traverse_log for miniMax

def traverseLog(i, j, logDepth, logUtility):

    if logUtility == float('inf'):
        logUtility = 'Infinity'
    elif logUtility == -float('inf'):
        logUtility = '-Infinity'


    if i == float('inf'):
        if j == float('inf'):
            #print('root', logDepth, logUtility)
            
            append = open('traverse_log.txt', 'a')
            append.write('root,' + str(logDepth) + ',' + str(logUtility) +'\n')



    else:
        (x,y) = numberToAlphabets(i,j)
        #print(str(x),y,logDepth,logUtility)
        append = open('traverse_log.txt', 'a')
        append.write(str(y)+str(x)+','+str(logDepth) +',' + str(logUtility)+'\n')

def traverseLogAlphaBeta(i, j, logDepth, logUtility, alpha, beta):

    if logUtility == float('inf'):
        logUtility = 'Infinity'
    elif logUtility == -float('inf'):
        logUtility = '-Infinity'


    if alpha == float('inf'):
        alpha = 'Infinity'
    elif alpha == -float('inf'):
        alpha = '-Infinity'


    if beta == float('inf'):
        beta = 'Infinity'
    elif beta == -float('inf'):
        beta = '-Infinity'

    if i == float('inf'):
        if j == float('inf'):
            #print('root', logDepth, logUtility, alpha, beta)

            append = open('traverse_log.txt', 'a')
            append.write('root,' + str(logDepth) + ',' + str(logUtility) + ',' + str(alpha) + ',' + str(beta)+'\n')
            append.close()


    else:
        (x,y) = numberToAlphabets(i,j)
        #print(str(x),y,logDepth,logUtility,alpha,beta)

        append = open('traverse_log.txt', 'a')
        append.write(str(y)+str(x)+','+str(logDepth)+','+str(logUtility)+','+str(alpha)+','+str(beta)+'\n')
        append.close()

def miniMax(printTraverse, currentStateMatrix, boardValuesMatrix, playerTag, cutoffDepth, depth, constantplayerName, selfPosi, selfPosj):

    #tempi and tempj will store the position of next best move

    tempi = -99
    tempj = -99

    childEvaluation = 0




    if depth == int(cutoffDepth):

        leafUtility = calculateUtility(currentStateMatrix, constantplayerName)
        if printTraverse == 1:
            traverseLog(selfPosi, selfPosj, depth, leafUtility)
        return leafUtility, tempi, tempj



    playerName = playerTag

    if depth%2 == 0:
        utility = -float('inf')
    else:
        utility = float('inf')


    if printTraverse == 1:
        traverseLog(selfPosi, selfPosj, depth, utility)

    for i in range (0,5):
        for j in range(0,5):
            tempCurrentState = [x[:] for x in currentStateMatrix]
            raid= 0
            if playerName == 1:
                opponentName = 0
                if currentStateMatrix[i][j] == '*':
                    raid = checkRaidX(i, j, currentStateMatrix)

                    if raid == 1:
                        if i-1 >= 0:
                            if currentStateMatrix[i-1][j] == 'O':
                                tempCurrentState[i-1][j] = 'X'


                        if i+1 <= 4:
                            if currentStateMatrix[i+1][j] == 'O':
                                tempCurrentState[i+1][j] = 'X'



                        if j-1 >= 0:
                            if currentStateMatrix[i][j-1] == 'O':
                                tempCurrentState[i][j-1] = 'X'


                        if j+1 <= 4:
                            if currentStateMatrix[i][j+1] == 'O':
                                tempCurrentState[i][j+1] = 'X'

                        tempCurrentState[i][j] = 'X'
                        (childEvaluation, x, y) = miniMax(printTraverse, tempCurrentState, boardValuesMatrix, opponentName, cutoffDepth, depth+1, constantplayerName, i, j)

                    elif raid == 0:
                        tempCurrentState[i][j] = 'X'
                        (childEvaluation, x, y) = miniMax(printTraverse, tempCurrentState, boardValuesMatrix, opponentName, cutoffDepth, depth+1, constantplayerName, i, j)

                    if depth%2 == 0:
                        if childEvaluation > utility:
                            utility = childEvaluation
                            if depth == 0:
                                tempi = i
                                tempj = j
                    else:
                        if childEvaluation < utility:
                            utility = childEvaluation
                            if depth == 0:
                                tempi = i
                                tempj = j

                    if printTraverse == 1:
                        traverseLog(selfPosi, selfPosj, depth, utility)


            elif playerName == 0:
                opponentName = 1
                if currentStateMatrix[i][j] == '*':
                    raid = checkRaidO(i, j, currentStateMatrix)

                    if raid == 1:
                        if i-1 >= 0:
                            if currentStateMatrix[i-1][j] == 'X':
                                tempCurrentState[i-1][j] = 'O'


                        if i+1 <= 4:
                            if currentStateMatrix[i+1][j] == 'X':
                                tempCurrentState[i+1][j] = 'O'



                        if j-1 >= 0:
                            if currentStateMatrix[i][j-1] == 'X':
                                tempCurrentState[i][j-1] = 'O'


                        if j+1 <= 4:
                            if currentStateMatrix[i][j+1] == 'X':
                                tempCurrentState[i][j+1] = 'O'

                        tempCurrentState[i][j] = 'O'

                        (childEvaluation, x, y) = miniMax(printTraverse, tempCurrentState, boardValuesMatrix, opponentName, cutoffDepth, depth+1, constantplayerName, i, j)

                    elif raid == 0:
                        tempCurrentState[i][j] = 'O'

                        (childEvaluation, x, y) = miniMax(printTraverse, tempCurrentState, boardValuesMatrix, opponentName, cutoffDepth, depth+1, constantplayerName, i, j)

                    if depth%2 == 0:
                        if childEvaluation > utility:
                            utility = childEvaluation
                            if depth == 0:
                                tempi = i
                                tempj = j
                    else:
                        if childEvaluation < utility:
                            utility = childEvaluation
                            if depth == 0:
                                tempi = i
                                tempj = j

                    if printTraverse == 1:
                        traverseLog(selfPosi, selfPosj, depth, utility)


    return utility, tempi, tempj



def alphaBeta(printTraverse, alpha, beta, currentStateMatrix, boardValuesMatrix, playerTag, cutoffDepth, depth, constantplayerName, selfPosi, selfPosj):



    tempi = -99
    tempj = -99

    tempAlpha = alpha
    tempBeta = beta

    if depth == int(cutoffDepth):

        leafUtility = calculateUtility(currentStateMatrix, constantplayerName)

        if printTraverse==1:
            traverseLogAlphaBeta(selfPosi, selfPosj, depth, leafUtility, alpha, beta)

        return tempAlpha, tempBeta, leafUtility, tempi, tempj


    playerName = playerTag


    if depth%2 == 0:
        utility = -float('inf')
    else:
        utility = float('inf')

    if printTraverse == 1:
        traverseLogAlphaBeta(selfPosi, selfPosj, depth, utility, alpha, beta)

    for i in range (0,5):
        for j in range(0,5):
            tempCurrentState = [x[:] for x in currentStateMatrix]
            raid= 0
            if playerName == 1:
                opponentName = 0
                if currentStateMatrix[i][j] == '*':
                    raid = checkRaidX(i, j, currentStateMatrix)

                    if raid == 1:
                        if i-1 >= 0:
                            if currentStateMatrix[i-1][j] == 'O':
                                tempCurrentState[i-1][j] = 'X'


                        if i+1 <= 4:
                            if currentStateMatrix[i+1][j] == 'O':
                                tempCurrentState[i+1][j] = 'X'



                        if j-1 >= 0:
                            if currentStateMatrix[i][j-1] == 'O':
                                tempCurrentState[i][j-1] = 'X'


                        if j+1 <= 4:
                            if currentStateMatrix[i][j+1] == 'O':
                                tempCurrentState[i][j+1] = 'X'

                        tempCurrentState[i][j] = 'X'
                        (tempAlpha, tempBeta, childEvaluation, x, y) = alphaBeta(printTraverse, alpha, beta, tempCurrentState, boardValuesMatrix, opponentName, cutoffDepth, depth+1, constantplayerName, i, j)

                    elif raid == 0:
                        tempCurrentState[i][j] = 'X'
                        (tempAlpha, tempBeta, childEvaluation, x, y) = alphaBeta(printTraverse, alpha, beta, tempCurrentState, boardValuesMatrix, opponentName, cutoffDepth, depth+1, constantplayerName, i, j)



                    if depth%2 == 0:
                        if childEvaluation > tempAlpha:
                            alpha = childEvaluation
                            utility = childEvaluation
                            if depth == 0:
                                 tempi = i
                                 tempj = j
                    else:
                        if childEvaluation < tempBeta:
                            #print('hurray',tempBeta)
                            utility = childEvaluation
                            beta = childEvaluation
                            if depth == 0:
                                tempi = i
                                tempj = j

                    if alpha>=beta:
                        if printTraverse == 1:
                            traverseLogAlphaBeta(selfPosi, selfPosj, depth, utility, tempAlpha, tempBeta)

                        return(alpha, beta, utility, tempi, tempj)
                    else:
                        if printTraverse == 1:
                            traverseLogAlphaBeta(selfPosi, selfPosj, depth, utility, alpha, beta)






            elif playerName == 0:
                opponentName = 1
                if currentStateMatrix[i][j] == '*':
                    raid = checkRaidO(i, j, currentStateMatrix)

                    if raid == 1:
                        if i-1 >= 0:
                            if currentStateMatrix[i-1][j] == 'X':
                                tempCurrentState[i-1][j] = 'O'


                        if i+1 <= 4:
                            if currentStateMatrix[i+1][j] == 'X':
                                tempCurrentState[i+1][j] = 'O'



                        if j-1 >= 0:
                            if currentStateMatrix[i][j-1] == 'X':
                                tempCurrentState[i][j-1] = 'O'


                        if j+1 <= 4:
                            if currentStateMatrix[i][j+1] == 'X':
                                tempCurrentState[i][j+1] = 'O'

                        tempCurrentState[i][j] = 'O'

                        (tempAlpha, tempBeta, childEvaluation, x, y) = alphaBeta(printTraverse,alpha, beta, tempCurrentState, boardValuesMatrix, opponentName, cutoffDepth, depth+1, constantplayerName, i, j)

                    elif raid == 0:
                        tempCurrentState[i][j] = 'O'

                        (tempAlpha, tempBeta, childEvaluation, x, y) = alphaBeta(printTraverse,alpha, beta, tempCurrentState, boardValuesMatrix, opponentName, cutoffDepth, depth+1, constantplayerName, i, j)



                    if depth%2 == 0:
                        if childEvaluation > tempAlpha:
                            alpha = childEvaluation
                            utility = childEvaluation
                            if depth == 0:
                                 tempi = i
                                 tempj = j
                    else:
                        if childEvaluation < tempBeta:

                            utility = childEvaluation
                            beta = childEvaluation
                            if depth == 0:
                                tempi = i
                                tempj = j

                    if alpha>=beta:
                        if printTraverse == 1:
                            traverseLogAlphaBeta(selfPosi, selfPosj, depth, utility, tempAlpha, tempBeta)

                        return(alpha, beta, utility, tempi, tempj)
                    else:
                        if printTraverse == 1:
                            traverseLogAlphaBeta(selfPosi, selfPosj, depth, utility, alpha, beta)







    return alpha, beta, utility, tempi, tempj


def simulateGame(printTraverse, emptySpaces, boardValuesMatrix, playerCondition, currentState, firstPlayer, secondPlayer, firstAlgorithmTag, secondAlgorithmTag, firstCutoff, secondCutoff):



    if emptySpaces != 0:

        if playerCondition == 1:

            constantPlayer = firstPlayer
            playerCondition = 0
            if firstAlgorithmTag == 1:

                (i,j, currentState) = greedyBestFirstSearch(firstPlayer, currentState)

                if firstPlayer == 1:
                    currentState[i][j] = 'X'


                elif firstPlayer == 0:
                    currentState[i][j] = 'O'



                append = open('trace_state.txt', 'a')
                for i in range (0,5):
                    for j in range (0,5):
                        append.write(currentState[i][j])
                        if j == 4:
                            append.write('\n')
                append.close()
                #print(currentState)
                emptySpaces = emptySpaces-1
                simulateGame(printTraverse, emptySpaces, boardValuesMatrix, playerCondition, currentState, firstPlayer, secondPlayer, firstAlgorithmTag, secondAlgorithmTag, firstCutoff, secondCutoff)

            elif firstAlgorithmTag  == 2:


                depth = 0
                selfPositioni = float('inf')
                selfPositionj = float('inf')
                saveFile = open('traverse_log.txt', 'w')
                saveFile.write('Node,Depth,Value \n')
                saveFile.close()
                if int(emptySpaces) < int(firstCutoff):
                    firstCutoff = emptySpaces
                (rootUtility, i, j) = miniMax(printTraverse, currentState, boardValuesMatrix, firstPlayer, firstCutoff, depth, constantPlayer, selfPositioni, selfPositionj)

                #print(rootUtility, i, j)

                if firstPlayer == 1:
                    currentState[i][j] = 'X'
                    raid = checkRaidX(i,j,currentState)
                    if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'O':
                                currentState[i-1][j] = 'X'


                        if i+1 <= 4:
                            if currentState[i+1][j] == 'O':
                                currentState[i+1][j] = 'X'



                        if j-1 >= 0:
                            if currentState[i][j-1] == 'O':
                                currentState[i][j-1] = 'X'


                        if j+1 <= 4:
                            if currentState[i][j+1] == 'O':
                                currentState[i][j+1] = 'X'

                elif firstPlayer == 0:
                    currentState[i][j] = 'O'
                    raid = checkRaidO(i,j,currentState)
                    if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'X':
                                currentState[i-1][j] = 'O'


                        if i+1 <= 4:
                            if currentState[i+1][j] == 'X':
                                currentState[i+1][j] = 'O'



                        if j-1 >= 0:
                            if currentState[i][j-1] == 'X':
                                currentState[i][j-1] = 'O'


                        if j+1 <= 4:
                            if currentState[i][j+1] == 'X':
                                currentState[i][j+1] = 'O'


                append = open('trace_state.txt', 'a')
                for i in range (0,5):
                    for j in range (0,5):
                        append.write(currentState[i][j])
                        if j == 4:
                            append.write('\n')

                append.close()

                #print(currentState)
                emptySpaces = emptySpaces-1

                simulateGame(printTraverse, emptySpaces, boardValuesMatrix, playerCondition, currentState, firstPlayer, secondPlayer, firstAlgorithmTag, secondAlgorithmTag, firstCutoff, secondCutoff)

            elif firstAlgorithmTag == 3:



                a = -float('inf')
                b = float('inf')
                depth = 0
                selfPositioni = float('inf')
                selfPositionj = float('inf')

                saveFile = open('traverse_log.txt', 'w')
                saveFile.write('Node,Depth,Value,Alpha,Beta \n')
                saveFile.close()
                if int(emptySpaces) < int(firstCutoff):
                    firstCutoff = emptySpaces
                (a, b, rootUtility, i, j) = alphaBeta(printTraverse, a,b,currentState,boardValuesMatrix,firstPlayer,firstCutoff,depth,constantPlayer,selfPositioni,selfPositionj)


                if firstPlayer == 1:
                    currentState[i][j] = 'X'
                    raid = checkRaidX(i,j,currentState)
                    if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'O':
                                currentState[i-1][j] = 'X'


                        if i+1 <= 4:
                            if currentState[i+1][j] == 'O':
                                currentState[i+1][j] = 'X'



                        if j-1 >= 0:
                            if currentState[i][j-1] == 'O':
                                currentState[i][j-1] = 'X'


                        if j+1 <= 4:
                            if currentState[i][j+1] == 'O':
                                currentState[i][j+1] = 'X'

                elif firstPlayer == 0:
                    currentState[i][j] = 'O'
                    raid = checkRaidO(i,j,currentState)
                    if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'X':
                                currentState[i-1][j] = 'O'


                        if i+1 <= 4:
                            if currentState[i+1][j] == 'X':
                                currentState[i+1][j] = 'O'



                        if j-1 >= 0:
                            if currentState[i][j-1] == 'X':
                                currentState[i][j-1] = 'O'


                        if j+1 <= 4:
                            if currentState[i][j+1] == 'X':
                                currentState[i][j+1] = 'O'


                append = open('trace_state.txt', 'a')
                for i in range (0,5):
                    for j in range (0,5):
                        append.write(currentState[i][j])
                        if j == 4:
                            append.write('\n')

                append.close()
                #print(currentState)
                emptySpaces = emptySpaces-1
                simulateGame(printTraverse, emptySpaces, boardValuesMatrix, playerCondition, currentState, firstPlayer, secondPlayer, firstAlgorithmTag, secondAlgorithmTag, firstCutoff, secondCutoff)


        else:

            constantPlayer = secondPlayer
            playerCondition = 1

            if secondAlgorithmTag == 1:
                #print('yay')
                (i,j, currentState) = greedyBestFirstSearch(secondPlayer, currentState)

                if secondPlayer == 1:
                    currentState[i][j] = 'X'


                elif secondPlayer == 0:
                    currentState[i][j] = 'O'


                append = open('trace_state.txt', 'a')
                for i in range (0,5):
                    for j in range (0,5):
                        append.write(currentState[i][j])
                        if j == 4:
                            append.write('\n')
                append.close()
                #print(currentState)


                emptySpaces = emptySpaces-1
                simulateGame(printTraverse, emptySpaces, boardValuesMatrix, playerCondition, currentState, firstPlayer, secondPlayer, firstAlgorithmTag, secondAlgorithmTag, firstCutoff, secondCutoff)

            elif secondAlgorithmTag  == 2:



                depth = 0
                selfPositioni = float('inf')
                selfPositionj = float('inf')
                #saveFile = open('traverse_log.txt', 'w')
                #saveFile.write('Node,Depth,Value \n')
                #saveFile.close()
                #print(emptySpaces)
                #print(secondCutoff)

                if int(emptySpaces) < int(secondCutoff):
                    secondCutoff = emptySpaces
                (rootUtility, i, j) = miniMax(printTraverse, currentState, boardValuesMatrix, secondPlayer, secondCutoff, depth, constantPlayer, selfPositioni, selfPositionj)

                #print(rootUtility, i, j)

                if secondPlayer == 1:
                    currentState[i][j] = 'X'
                    raid = checkRaidX(i,j,currentState)
                    if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'O':
                                currentState[i-1][j] = 'X'


                        if i+1 <= 4:
                            if currentState[i+1][j] == 'O':
                                currentState[i+1][j] = 'X'



                        if j-1 >= 0:
                            if currentState[i][j-1] == 'O':
                                currentState[i][j-1] = 'X'


                        if j+1 <= 4:
                            if currentState[i][j+1] == 'O':
                                currentState[i][j+1] = 'X'

                elif secondPlayer == 0:
                    currentState[i][j] = 'O'
                    raid = checkRaidO(i,j,currentState)
                    if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'X':
                                currentState[i-1][j] = 'O'


                        if i+1 <= 4:
                            if currentState[i+1][j] == 'X':
                                currentState[i+1][j] = 'O'



                        if j-1 >= 0:
                            if currentState[i][j-1] == 'X':
                                currentState[i][j-1] = 'O'


                        if j+1 <= 4:
                            if currentState[i][j+1] == 'X':
                                currentState[i][j+1] = 'O'

                append = open('trace_state.txt', 'a')
                for i in range (0,5):
                    for j in range (0,5):
                        append.write(currentState[i][j])
                        if j == 4:
                            append.write('\n')

                append.close()

                #print(currentState)

                emptySpaces = emptySpaces-1
                simulateGame(printTraverse, emptySpaces, boardValuesMatrix, playerCondition, currentState, firstPlayer, secondPlayer, firstAlgorithmTag, secondAlgorithmTag, firstCutoff, secondCutoff)


            elif secondAlgorithmTag == 3:


                a = -float('inf')
                b = float('inf')
                depth = 0
                selfPositioni = float('inf')
                selfPositionj = float('inf')

                #saveFile = open('traverse_log.txt', 'w')
                #saveFile.write('Node,Depth,Value,Alpha,Beta \n')
                #saveFile.close()
                #print('hurray')


                if int(emptySpaces) < int(secondCutoff):
                    secondCutoff = emptySpaces


                (a, b, rootUtility, i, j) = alphaBeta(printTraverse, a,b,currentState,boardValuesMatrix,secondPlayer,secondCutoff,depth,constantPlayer,selfPositioni,selfPositionj)


                if secondPlayer == 1:
                    currentState[i][j] = 'X'
                    raid = checkRaidX(i,j,currentState)
                    if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'O':
                                currentState[i-1][j] = 'X'


                        if i+1 <= 4:
                            if currentState[i+1][j] == 'O':
                                currentState[i+1][j] = 'X'



                        if j-1 >= 0:
                            if currentState[i][j-1] == 'O':
                                currentState[i][j-1] = 'X'


                        if j+1 <= 4:
                            if currentState[i][j+1] == 'O':
                                currentState[i][j+1] = 'X'



                elif secondPlayer == 0:
                    currentState[i][j] = 'O'
                    raid = checkRaidO(i,j,currentState)
                    if raid == 1:
                        if i-1 >= 0:
                            if currentState[i-1][j] == 'X':
                                currentState[i-1][j] = 'O'


                        if i+1 <= 4:
                            if currentState[i+1][j] == 'X':
                                currentState[i+1][j] = 'O'



                        if j-1 >= 0:
                            if currentState[i][j-1] == 'X':
                                currentState[i][j-1] = 'O'


                        if j+1 <= 4:
                            if currentState[i][j+1] == 'X':
                                currentState[i][j+1] = 'O'


                append = open('trace_state.txt', 'a')
                for i in range (0,5):
                    for j in range (0,5):
                        append.write(currentState[i][j])
                        if j == 4:
                            append.write('\n')

                append.close()
                #print(currentState)
                emptySpaces = emptySpaces-1
                simulateGame(printTraverse, emptySpaces,boardValuesMatrix, playerCondition, currentState, firstPlayer, secondPlayer, firstAlgorithmTag, secondAlgorithmTag, firstCutoff, secondCutoff)

    else:



        with open('trace_state.txt', 'rb+') as f:
                f.seek(0,2)
                size=f.tell()
                f.truncate(size-1)
        return 0


algorithmTag = 0
playerTag = 0

filename = sys.argv[-1]

f = open(filename)

#check for number of liens in the input files to find out whether we simply need to predict next move or simulate the whole game

with open(filename) as f1:
    for i, l in enumerate(f1):
        pass
lines = str(i+1)


#check for the first line in the input.txt
#that will tell you which algorithm you need to use

if lines == str(13):

    printTraverse = 1

    emptySpaces = 0

    algorithm = f.readline()

    if algorithm.startswith('1'):
        #print('We will be using the Greedy Best First Search\n')
        algorithmTag = 1
    elif algorithm.startswith('2'):
        #print('We will be using Minimax\n')
        algorithmTag = 2
    elif algorithm.startswith('3'):
        #print('We will be using alpha beta pruning')
        algorithmTag = 3

    #check for the second line to find out whose turn is it next

    player = f.readline()

    if player.startswith('X'):
        #print('Player 1 is X\n')
        playerTag = 1

    if player.startswith('O'):
        #print('Player 1 is O\n')
        playerTag = 0

    constantPlayer = playerTag

    #check for the third line to get the cut-off depth (1 for best first search and 2 for the rest)

    cutoff = f.readline()

    cutoffDepth = int(cutoff)

    #print('cutoff is', cutoffDepth)


    #now create 2 matrices, one to store the board values and another to store the current state of the board.

    boardValuesMatrix = []
    currentStateMatrix = []

    #now read the next five lines and store them each in the boardValuesMatrix

    for i in range(0, 5):
        boardList = f.readline()
        boardValuesMatrix.append(boardList.split())

    #repeat the same for next five lines and store them in currentStateMatrix. we cannot use .split() since the values aren't separated by space

    for i in range(0, 5):
        l = list(f.readline().strip())
        currentStateMatrix.append(l)

    #print(boardValuesMatrix)
    #print(currentStateMatrix)

    for i in range (0,5):
        for j in range (0,5):
            if currentStateMatrix[i][j] == '*':
                emptySpaces = emptySpaces + 1

    if int(emptySpaces) < int(cutoffDepth):
        cutoffDepth = emptySpaces

    #print('updated cutoff', cutoffDepth)

    if emptySpaces != 0:

        if algorithmTag == 1:
            (i,j, currentState) = greedyBestFirstSearch(playerTag, currentStateMatrix)

            currentStateMatrix = [x[:] for x in currentState]

            if playerTag == 1:
                    currentStateMatrix[i][j] = 'X'
            elif playerTag == 0:
                    currentStateMatrix[i][j] = 'O'

            saveFile = open('next_state.txt', 'w')
            saveFile.close()

            append = open('next_state.txt', 'a')
            for i in range (0,5):
                for j in range (0,5):
                    append.write(currentStateMatrix[i][j])
                    if j == 4:
                        append.write('\n')
            append.close()

            with open('next_state.txt', 'rb+') as f:
                f.seek(0,2)

                size=f.tell()
                f.truncate(size-1)

        elif algorithmTag == 2:
            depth = 0
            selfPositioni = float('inf')
            selfPositionj = float('inf')
            saveFile = open('traverse_log.txt', 'w')
            saveFile.write('Node,Depth,Value\n')
            saveFile.close()
            (rootUtility, i, j) = miniMax(printTraverse, currentStateMatrix, boardValuesMatrix, playerTag, cutoffDepth, depth, constantPlayer, selfPositioni, selfPositionj)

            #print(rootUtility, i, j)

            if playerTag == 1:
                currentStateMatrix[i][j] = 'X'
                raid = checkRaidX(i,j,currentStateMatrix)
                if raid == 1:
                    if i-1 >= 0:
                        if currentStateMatrix[i-1][j] == 'O':
                            currentStateMatrix[i-1][j] = 'X'


                    if i+1 <= 4:
                        if currentStateMatrix[i+1][j] == 'O':
                            currentStateMatrix[i+1][j] = 'X'



                    if j-1 >= 0:
                        if currentStateMatrix[i][j-1] == 'O':
                            currentStateMatrix[i][j-1] = 'X'


                    if j+1 <= 4:
                        if currentStateMatrix[i][j+1] == 'O':
                            currentStateMatrix[i][j+1] = 'X'

            elif playerTag == 0:
                currentStateMatrix[i][j] = 'O'
                raid = checkRaidO(i,j,currentStateMatrix)
                if raid == 1:
                    if i-1 >= 0:
                        if currentStateMatrix[i-1][j] == 'X':
                            currentStateMatrix[i-1][j] = 'O'


                    if i+1 <= 4:
                        if currentStateMatrix[i+1][j] == 'X':
                            currentStateMatrix[i+1][j] = 'O'



                    if j-1 >= 0:
                        if currentStateMatrix[i][j-1] == 'X':
                            currentStateMatrix[i][j-1] = 'O'


                    if j+1 <= 4:
                        if currentStateMatrix[i][j+1] == 'X':
                            currentStateMatrix[i][j+1] = 'O'


            saveFile = open('next_state.txt', 'w')
            saveFile.close()



            append = open('next_state.txt', 'a')
            for i in range (0,5):
                for j in range (0,5):
                    append.write(currentStateMatrix[i][j])
                    if j == 4:
                        append.write('\n')

        # we now need to remove the final blank line from the text file.

            with open('traverse_log.txt', 'rb+') as r:
                for l in r:
                    l.strip('\n')

            with open('traverse_log.txt', 'rb+') as f:
                f.seek(0,2)
                size=f.tell()
                f.truncate(size-1)


        elif algorithmTag == 3:
            a = -float('inf')
            b = float('inf')
            depth = 0
            selfPositioni = float('inf')
            selfPositionj = float('inf')

            saveFile = open('traverse_log.txt', 'w')
            saveFile.write('Node,Depth,Value,Alpha,Beta\n')
            saveFile.close()
            (a, b, rootUtility, i, j) = alphaBeta(printTraverse, a,b,currentStateMatrix,boardValuesMatrix,playerTag,cutoffDepth,depth,constantPlayer,selfPositioni,selfPositionj)


            if playerTag == 1:
                currentStateMatrix[i][j] = 'X'
                raid = checkRaidX(i,j,currentStateMatrix)
                if raid == 1:
                    if i-1 >= 0:
                        if currentStateMatrix[i-1][j] == 'O':
                            currentStateMatrix[i-1][j] = 'X'


                    if i+1 <= 4:
                        if currentStateMatrix[i+1][j] == 'O':
                            currentStateMatrix[i+1][j] = 'X'



                    if j-1 >= 0:
                        if currentStateMatrix[i][j-1] == 'O':
                            currentStateMatrix[i][j-1] = 'X'


                    if j+1 <= 4:
                        if currentStateMatrix[i][j+1] == 'O':
                            currentStateMatrix[i][j+1] = 'X'

            elif playerTag == 0:
                currentStateMatrix[i][j] = 'O'
                raid = checkRaidO(i,j,currentStateMatrix)
                if raid == 1:
                    if i-1 >= 0:
                        if currentStateMatrix[i-1][j] == 'X':
                            currentStateMatrix[i-1][j] = 'O'


                    if i+1 <= 4:
                        if currentStateMatrix[i+1][j] == 'X':
                            currentStateMatrix[i+1][j] = 'O'



                    if j-1 >= 0:
                        if currentStateMatrix[i][j-1] == 'X':
                            currentStateMatrix[i][j-1] = 'O'


                    if j+1 <= 4:
                        if currentStateMatrix[i][j+1] == 'X':
                            currentStateMatrix[i][j+1] = 'O'


            saveFile = open('next_state.txt', 'w')
            saveFile.close()



            append = open('next_state.txt', 'a')
            for i in range (0,5):
                for j in range (0,5):
                    append.write(currentStateMatrix[i][j])
                    if j == 4:
                        append.write('\n')

            with open('traverse_log.txt', 'rb+') as f:
                f.seek(0,2)
                size=f.tell()
                f.truncate(size-1)

            with open('traverse_log.txt', 'rb+') as r:
                for l in r:
                    l.strip('\n')

    else:
        #print('Board is full')

        saveFile = open('next_state.txt', 'w')
        saveFile.close()

        append = open('next_state.txt', 'a')
        for i in range (0,5):
            for j in range (0,5):
                append.write(currentStateMatrix[i][j])
                if j == 4:
                    append.write('\n')

else:

    printTraverse = 0

    battleSimulation = f.readline()


    firstPlayer = f.readline()

    if firstPlayer.startswith('X'):
        #print('Player 1 is X\n')
        firstPlayerTag = 1

    if firstPlayer.startswith('O'):
        #print('Player 1 is O\n')
        firstPlayerTag = 0

    #print(firstPlayer)

    firstPlayerAlgorithm = f.readline()

    if firstPlayerAlgorithm.startswith('1'):
        #print('We will be using the Greedy Best First Search for player 1\n')
        firstPlayerAlgorithmTag = 1
    elif firstPlayerAlgorithm.startswith('2'):
        #print('We will be using Minimax for player 1\n')
        firstPlayerAlgorithmTag  = 2
    elif firstPlayerAlgorithm.startswith('3'):
        #print('We will be using alpha beta pruning for player 1\n')
        firstPlayerAlgorithmTag = 3


    firstPlayerCutOff = f.readline()

    secondPlayer = f.readline()

    if secondPlayer.startswith('X'):
        #print('Player 2 is X\n')
        secondPlayerTag = 1

    if secondPlayer.startswith('O'):
        #print('Player 2 is O\n')
        secondPlayerTag = 0

    secondPlayerAlgorithm = f.readline()

    if secondPlayerAlgorithm.startswith('1'):
        #print('We will be using the Greedy Best First Search for player 2\n')
        secondPlayerAlgorithmTag = 1
    elif secondPlayerAlgorithm.startswith('2'):
        #print('We will be using Minimax for player 2\n')
        secondPlayerAlgorithmTag  = 2
    elif secondPlayerAlgorithm.startswith('3'):
        #print('We will be using alpha beta pruning for player 2\n')
        secondPlayerAlgorithmTag = 3

    secondPlayerCutoff = f.readline()

    #now create 2 matrices, one to store the board values and another to store the current state of the board.

    boardValuesMatrix = []
    currentStateMatrix = []

    #now read the next five lines and store them each in the boardValuesMatrix

    for i in range(0, 5):
        boardList = f.readline()
        boardValuesMatrix.append(boardList.split())

    #repeat the same for next five lines and store them in currentStateMatrix. we cannot use .split() since the values aren't separated by space

    for i in range(0, 5):
        l = list(f.readline().strip())
        currentStateMatrix.append(l)

    #print(boardValuesMatrix)
    #print(currentStateMatrix)

    emptySpaces = 0


    for i in range (0,5):
        for j in range (0,5):
            if currentStateMatrix[i][j] == '*':
                emptySpaces = emptySpaces + 1

    #print('empty', emptySpaces)

    #print(firstPlayerAlgorithm)

    playerCondition = 1

    saveFile = open('trace_state.txt', 'w')
    saveFile.close()

    d = simulateGame(printTraverse, emptySpaces, boardValuesMatrix, playerCondition, currentStateMatrix, firstPlayerTag, secondPlayerTag, firstPlayerAlgorithmTag, secondPlayerAlgorithmTag, firstPlayerCutOff, secondPlayerCutoff)





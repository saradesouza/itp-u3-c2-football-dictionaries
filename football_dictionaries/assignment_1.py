from squads_data import SQUADS_DATA

squad_keys = ['number','position','name','date_of_birth','caps','club','country','club_country','year']



def players_as_dictionaries(vanillalist):
    
    footballerDictOne = {}
    
    for i in range(0, len(vanillalist[0])):
        # print(squad_keys[i],SQUADS_DATA[0][i])
        footballerDictOne[squad_keys[i]] = vanillalist[0][i]
    
    footballerDictTwo = {}
    
    for i in range(0, len(vanillalist[1])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictTwo[squad_keys[i]] = vanillalist[1][i]
    
    footballerDictThree = {}
    
    for i in range(0, len(vanillalist[2])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictThree[squad_keys[i]] = vanillalist[2][i]
    
    footballerDictFour = {}
    
    for i in range(0, len(vanillalist[3])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictFour[squad_keys[i]] = vanillalist[3][i]
    
    footballerDictFive = {}
    
    for i in range(0, len(vanillalist[4])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictFive[squad_keys[i]] = vanillalist[4][i]
    
    footballerDictSix = {}
    
    for i in range(0, len(vanillalist[5])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictSix[squad_keys[i]] = vanillalist[5][i]
    
    footballerDictSeven = {}
    
    for i in range(0, len(vanillalist[6])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictSeven[squad_keys[i]] = vanillalist[6][i]
    
    footballerDictEight = {}
    
    for i in range(0, len(vanillalist[7])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictEight[squad_keys[i]] = vanillalist[7][i]
    
    footballerDictNine = {}
    
    for i in range(0, len(vanillalist[8])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictNine[squad_keys[i]] = vanillalist[8][i]
    
    footballerDictTen = {}
    
    for i in range(0, len(vanillalist[9])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictTen[squad_keys[i]] = vanillalist[9][i]
    
    footballerDictEleven = {}
    
    for i in range(0, len(vanillalist[10])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictEleven[squad_keys[i]] = vanillalist[10][i]
    
    footballerDictTwelve = {}
    
    for i in range(0, len(vanillalist[11])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictTwelve[squad_keys[i]] = vanillalist[11][i]
    
    footballerDictThirteen = {}
    
    for i in range(0, len(vanillalist[12])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictThirteen[squad_keys[i]] = vanillalist[12][i]
    
    footballerDictFourteen = {}
    
    for i in range(0, len(vanillalist[13])):
        # print(squad_keys[i],SQUADS_DATA[1][i])
        footballerDictFourteen[squad_keys[i]] = vanillalist[13][i]
    
    
    # for i in range(0, len(SQUADS_DATA)):
    #     for j in range(0, len(SQUADS_DATA[0])):
    #         print(squad_keys[j],SQUADS_DATA[i][j])
    #         footballerDict[squad_keys[j]] = SQUADS_DATA[i][j]
            # footballerDict.update({squad_keys[j]:SQUADS_DATA[i][j]})
    
    # footballerOne.update({squad_keys[0]:SQUADS_DATA[0][0]})
    # footballerOne.update({squad_keys[1]:SQUADS_DATA[0][1]})
    
    playerList = [footballerDictOne,footballerDictTwo,footballerDictThree,footballerDictFour,footballerDictFive,footballerDictSix,footballerDictSeven,footballerDictEight,footballerDictNine,footballerDictTen,footballerDictEleven,footballerDictTwelve,footballerDictThirteen,footballerDictFourteen]
    
    # print(playerList)
    return playerList

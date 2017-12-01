from squads_data import SQUADS_DATA

squad_keys = ['number','position','name','date_of_birth','caps','club','country','club_country','year']

footballerDict = {}

for i in range(0, len(SQUADS_DATA)):
    for j in range(0, len(SQUADS_DATA[i])):
        print(squad_keys[j],SQUADS_DATA[i][j])
        footballerDict[squad_keys[j]] = SQUADS_DATA[i][j]
        # footballerDict.update({squad_keys[j]:SQUADS_DATA[i][j]})

# footballerOne.update({squad_keys[0]:SQUADS_DATA[0][0]})
# footballerOne.update({squad_keys[1]:SQUADS_DATA[0][1]})

playerList = [footballerDict]

print(playerList)

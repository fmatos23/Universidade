def getTeam():
    teams = []
    team = input("equipa: ")
    while True:
        team = input("equipa: ")
        if team in teams:
            continue
        if team == "":
            if len(teams) < 2:
                continue
            break
        teams.append(team)
    return teams

def allmatches(lst):
    newList = []
    for team1 in lst:
        for team2 in lst:
            if team1 != team2:
                newList.append((team1, team2))
    return newList

def getResult(matches):
    result = dict()
    for match in matches:
        equipa1, equipa2 = match
        golo1 = int(input(f"numero de golos do {equipa1}: "))
        golo2 = int(input(f"numero de golos do {equipa2}: "))
        result[match] = (golo1, golo2)
    return result

print(getResult([("slb", "scp")]))

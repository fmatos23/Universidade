def allMatches(lst):
    newList = []
    for team1 in lst:
        for team2 in lst:
            if team1 != team2:
                newList.append((team1, team2))

    return newList

print(allMatches(["FCP", "SCP", "SLB"]))


def countdigits(String):
    count = 0
    for i in String:
        if i.isdigit():
            count += 1
    return count


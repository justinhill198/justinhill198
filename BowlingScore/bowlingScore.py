total = 0
frame = 0
throws = [10,10,10,10,10,10,10,10,10,10,10,10]
thrownum = 0
while frame <= 9:
    currthrow = throws[thrownum]
    if throws[thrownum]  == 10:
        total = total + currthrow + sum(throws[thrownum+1:thrownum+3])
        thrownum += 1
        frame += 1
        continue
    elif currthrow + throws[thrownum+1] == 10:
        total += 10 + throws[thrownum+2]
        thrownum += 2
        frame += 1
        continue
    else:
        total += currthrow + throws[thrownum+1]
        thrownum += 2
        frame += 1
        continue
print(throws, "\nThe total score is: " +  str(total))

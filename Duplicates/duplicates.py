
list = []
list_len = len(list)
dupes=[]
for i in range(list_len):
    a = i + 1
    for b in range(a, list_len):
        if list[i] == list[b] and list[i] not in dupes:
            dupes.append(list[i])
dupes.sort()
print(dupes)

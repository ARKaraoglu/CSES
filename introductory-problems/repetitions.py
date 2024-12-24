dna = input().strip()

seqDict = {}

for seq in dna:
    if seq not in seqDict:
        seqDict[f"{seq}"] = 1
    else:
        seqDict[f"{seq}"] += 1
print(max(seqDict.values()))



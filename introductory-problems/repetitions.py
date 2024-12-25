dna = input().strip()

sequenceLengthList = []

longestSeqLength = 1
currentSeqChar = dna[0]
for x in range(1, len(dna)):
    if currentSeqChar == dna[x]:
        longestSeqLength += 1
    else:
        if longestSeqLength not in sequenceLengthList:
            sequenceLengthList.append(longestSeqLength)
        currentSeqChar = dna[x]
        longestSeqLength = 1

if len(sequenceLengthList) == 0:
    print(longestSeqLength)
elif max(sequenceLengthList) < longestSeqLength:
    print(longestSeqLength)
else:
    print(max(sequenceLengthList))


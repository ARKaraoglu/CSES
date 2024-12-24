num = int(input())
numList = [int(x) for x in input().split()]

sortedNumList = sorted(numList)

numChecker = 1
for x in range(0, num - 1):
    if sortedNumList[x] != numChecker:
        print(numChecker)
        break
    else:
        numChecker += 1
        continue

if num == sortedNumList[len(sortedNumList) - 1] + 1:
    print(num)




n = [int(x) for x in input().split()][0]

answerString = f"{n}"
while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(n * 3 + 1)
    answerString += f" {n}"

print(answerString)

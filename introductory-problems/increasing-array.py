listSize = int(input().strip())
numbers = [int(x) for x in input().split()]

counter = 0

for x in range(1, listSize):
    if numbers[x] < numbers[x - 1]:
        difference = numbers[x - 1] - numbers[x]
        numbers[x] += difference
        counter += difference

print(counter)

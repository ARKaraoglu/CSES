num = int(input())

permutations = ""
if num == 1:
    print("1")
    quit()
elif num <= 3:
    print("NO SOLUTION")
    quit()
elif num == 4:
    print("2 4 1 3")
    quit()

for x in range(1, num + 1, 2):
    print(f"{x} ", end= " ")
for x in range(2, num + 1, 2):
    print(f"{x} ", end = " ")


# SOLUTION 2 USING LIST AND JOIN
# num = int(input())
#
# permutations = []
# if num == 1:
#     print("1")
#     quit()
# elif num <= 3:
#     print("NO SOLUTION")
#     quit()
# elif num == 4:
#     print("2 4 1 3")
#     quit()
#
# for x in range(1, num + 1, 2):
#     permutations.append(f"{x} ")
# for x in range(2, num + 1, 2):
#     permutations.append(f"{x} ")
#
# print("".join(permutations))

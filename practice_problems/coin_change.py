# N is the value to be given change for
# M is the number of different coin values you can give change with
# C is the array of the different coin values

# C = [2, 6, 3, 5]
# N = 10
# [2, 2, 2, 2, 2]
# [2, 2, 6]
# [2, 2, 3, 3]
# [5, 5]
# [2, 3, 5]
# if N % C[i] == 0
C = [2, 6, 3, 5]
N = 10

total_ways = 0
for i in range(0, len(C)):
    if N % C[i] == 0:
        total_ways += 1
        for j in range(i+1, len(C)):
            left_over =
            x = j
            while x > i:



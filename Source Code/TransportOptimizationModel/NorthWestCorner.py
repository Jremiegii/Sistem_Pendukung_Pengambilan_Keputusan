grid = [[8, 5, 6], [15, 10, 12], [3, 9, 10]]  # table
supply = [120, 80, 80]  # supply
demand = [150, 70, 60]  # demand

startR = 0  # start row
startC = 0  # start col
ans = 0
solution_matrix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

# loop runs until it reaches the bottom right corner
while startR != len(grid) and startC != len(grid[0]):
    # if demand is greater than supply
    if supply[startR] <= demand[startC]:
        ans += supply[startR] * grid[startR][startC]
        # subtract the value of supply from the demand
        demand[startC] -= supply[startR]
        solution_matrix[startR][startC] = 1
        startR += 1
    # if supply is greater than demand
    else:
        ans += demand[startC] * grid[startR][startC]
        # subtract the value of demand from the supply
        supply[startR] -= demand[startC]
        solution_matrix[startR][startC] = 1
        startC += 1

print("The initial feasible basic solution is :", ans)
print("\n")
print("The solution matrix is:")
for row in solution_matrix:
    # Bernilai 1 jika terdapat alokasi dan bernilai 0 jika tidak memiliki alokasi
    print(row)

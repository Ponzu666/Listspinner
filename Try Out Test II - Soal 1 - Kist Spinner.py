def counterClockwise(x):
    return [[x[y][z] for y in range(len(x))] for z in range(len(x[0])-1,-1,-1)]

x = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
print(counterClockwise(x))
#belum bisa dalam bentuk 3 line outputnya
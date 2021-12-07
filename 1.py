import random as rng
data1 = [[rng.randint(0,10) for x in range(10)] for x in range (4)]
print(data1)

urut = data1.copy()
for x in range(len(urut)):
    for y in range(len(urut[x])):
        for z in range(y+1,len(urut[x])):
            if urut[x][y] > urut[x][z]:
                ubah2 = urut[x][y]
                urut[x][y] = urut[x][z]
                urut[x][z] = ubah2
print('list setelah diurut :', urut)
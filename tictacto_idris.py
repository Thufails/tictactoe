papan = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
henti = 0
kondisi = True

while kondisi:
    print(papan[0][0],'|', papan[0][1],'|', papan[0][2])
    print(papan[1][0],'|', papan[1][1],'|', papan[1][2])
    print(papan[2][0],'|', papan[2][1],'|', papan[2][2])

    print("1. X\n""2. O")
    selectmenu = int(input("Pilih simbol: "))

    if selectmenu == 1:
        place = int(input("Pilih urutan (1-9): "))
        print("="*25)
        baris = (place - 1) // 3
        kolom = (place - 1) % 3

        if papan[baris][kolom] == "X" or papan[baris][kolom] == "O":
            print("Kotak telah diisi, pilih kotak lain!!!")
            pass
        else:
            papan[baris][kolom] = "X"
            henti += 1

    elif selectmenu == 2:
        place = int(input("Pilih urutan (1-9): "))
        print("="*25)
        baris = (place - 1) // 3
        kolom = (place - 1) % 3
        if papan[baris][kolom] == "X" or papan[baris][kolom] == "O":
            print("Kotak telah diisi!!!")
            pass
        else:
            papan[baris][kolom] = "O"
            henti += 1

    else:
        print("Pilih menu yang disediakan ya!!")
        print("="*25)

    for elemen in papan:
        if " " not in elemen:
            kondisi = False
        else:
            kondisi = True
if kondisi == False:
    print(papan[0][0],'|', papan[0][1],'|', papan[0][2])
    print(papan[1][0],'|', papan[1][1],'|', papan[1][2])
    print(papan[2][0],'|', papan[2][1],'|', papan[2][2])
    print(""*5+"Program Selesai"+""*5)
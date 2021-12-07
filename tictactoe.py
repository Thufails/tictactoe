board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
henti = 0
play = True

while True:
    if henti < 9:
        print("{}|{}|{}" .format(board[0][0], board[0][1], board[0][2]))
        print("{}|{}|{}" .format(board[1][0], board[1][1], board[1][2]))
        print("{}|{}|{}" .format(board[2][0], board[2][1], board[2][2]))

        print("1. X\n""2. O")
        selectmenu = int(input("Pilih simbol: "))

        if selectmenu == 1:
            place = int(input("Pilih urutan (1-9): "))
            print("="*25)
            baris = (place - 1) // 3
            kolom = (place - 1) % 3

            if board[baris][kolom] == "X" or board[baris][kolom] == "O":
                print("Kotak telah diisi, pilih kotak lain!!!")
                pass
            else:
                board[baris][kolom] = "X"
                henti += 1

        elif selectmenu == 2:
            place = int(input("Pilih urutan (1-9): "))
            print("="*25)
            baris = (place - 1) // 3
            kolom = (place - 1) % 3
            if board[baris][kolom] == "X" or board[baris][kolom] == "O":
                print("Kotak telah diisi!!!")
                pass
            else:
                board[baris][kolom] = "O"
                henti += 1

        else:
            print("Pilih menu yang disediakan ya!!")
            print("="*25)
    else:
        print("{}|{}|{}" .format(board[0][0], board[0][1], board[0][2]))
        print("{}|{}|{}" .format(board[1][0], board[1][1], board[1][2]))
        print("{}|{}|{}" .format(board[2][0], board[2][1], board[2][2]))
        break
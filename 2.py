tictacto = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

berhenti = 0

while True:
    if berhenti < 9:
        print(tictacto[0][0],'|', tictacto[0][1],'|', tictacto[0][2])
        print(tictacto[1][0],'|', tictacto[1][1],'|', tictacto[1][2])
        print(tictacto[2][0],'|', tictacto[2][1],'|', tictacto[2][2])
        print('1. X\n' '2. O' )
        choice= int(input('Pilih Simbol dari (1/2)'))

        if choice == 1:
            choice2 = int(input('Pilihlah kotak antara 1-9 : '))
            print("=================================")
            row = (choice2 - 1) // 3
            column = (choice2 - 1) % 3
            tictacto[row][column] = "X"
            berhenti += 1
        elif choice == 2:
            choice2 = int(input('Pilihlah kotak antara 1-9 : '))
            print("=================================")
            row = (choice2 - 1) // 3
            column = (choice2 - 1) % 3
            tictacto[row][column] = "O"
            berhenti += 1
        else:
            print('pilih sesuai pilihan')
    else:
        print(tictacto[0][0],'|', tictacto[0][1],'|', tictacto[0][2])
        print(tictacto[1][0],'|', tictacto[1][1],'|', tictacto[1][2])
        print(tictacto[2][0],'|', tictacto[2][1],'|', tictacto[2][2])
        print("permainan selesai")
        break 



    



############################### SUDOKU GAME ##################################

# It's simple SUDOKU game with define board for player  
# No random boards
# If you want play give a row and col numer then give a right number 



from colorama import Fore, Style 

#clear screen FUNCTION - necesseary to avoid bords multiplication during game

def clear_screen():
    import os
    os.system('clear')

#GLOBAL LIST with orgin board - app use it to compare player result 

board_orgin = [[9, 8, 4, 5, 3, 1, 6, 7, 2],
              [6, 1, 3, 8, 2, 7, 5, 4, 9],
              [2, 5, 7, 6, 4, 9, 8, 3, 1],
              [3, 7, 8, 9, 6, 2, 4, 1, 5],
              [5, 6, 1, 3, 7, 4, 9, 2, 8],
              [4, 2, 9, 1, 8, 5, 7, 6, 3],
              [8, 3, 2, 4, 9, 6, 1, 5, 7],
              [7, 4, 5, 2, 1, 8, 3, 9, 6],
              [1, 9, 6, 7, 5, 3, 2, 8, 4]]  

#GLOBAL LIST with player board 

board_player = [[9, 8, " ", 5, 3, 1, 6, 7, " "],
                [6, 1, 3, 8, 2, 7, 5, 4, " "],
                [" ", 5, 7, 6, 4, 9, 8, 3, 1],
                [3, 7, 8, 9, 6, 2, 4, 1, 5],
                [5, 6, 1, 3, 7, " ", 9, 2, 8],
                [" ", 2, 9, " ", 8, 5, 7, 6, 3],
                [8, 3, 2, 4, 9, 6, 1, 5, 7],
                [7, 4, 5, 2, 1, " ", 3, 9, 6],
                [1, 9, " ", 7, 5, 3, 2, 8, " "]]

#FUNCTION wich prints a color player-board for player-board list 

def kolorki():
    print("")
    print(Fore.RED + " -------------------------------")   
    print(Fore.RED +" |", Fore.GREEN, *board_player[0][0:3],
        Fore.RED +" |", Fore.WHITE, *board_player[0][3:6], 
        Fore.RED +" |", Fore.GREEN, *board_player[0][6:9], Fore.RED +" | ")

    print(Fore.RED +" |", Fore.GREEN, *board_player[1][0:3],
        Fore.RED +" |", Fore.WHITE, *board_player[1][3:6], 
        Fore.RED +" |", Fore.GREEN, *board_player[1][6:9], Fore.RED +" | ")

    print(Fore.RED +" |", Fore.GREEN, *board_player[2][0:3],
        Fore.RED +" |", Fore.WHITE, *board_player[2][3:6], 
        Fore.RED +" |", Fore.GREEN, *board_player[2][6:9], Fore.RED +" | ")
    print(Fore.RED + " -------------------------------") 

    print(Fore.RED +" |", Fore.GREEN, *board_player[3][0:3],
        Fore.RED +" |", Fore.WHITE, *board_player[3][3:6], 
        Fore.RED +" |", Fore.GREEN, *board_player[3][6:9], Fore.RED +" | ")

    print(Fore.RED +" |", Fore.GREEN, *board_player[4][0:3],
        Fore.RED +" |", Fore.WHITE, *board_player[4][3:6], 
        Fore.RED +" |", Fore.GREEN, *board_player[4][6:9], Fore.RED +" | ")

    print(Fore.RED +" |", Fore.GREEN, *board_player[5][0:3],
        Fore.RED +" |", Fore.WHITE, *board_player[5][3:6], 
        Fore.RED +" |", Fore.GREEN, *board_player[5][6:9], Fore.RED +" | ")
    print(Fore.RED + " -------------------------------") 

    print(Fore.RED +" |", Fore.GREEN, *board_player[6][0:3],
        Fore.RED +" |", Fore.WHITE, *board_player[6][3:6], 
        Fore.RED +" |", Fore.GREEN, *board_player[6][6:9], Fore.RED +" | ")

    print(Fore.RED +" |", Fore.GREEN, *board_player[7][0:3],
        Fore.RED +" |", Fore.WHITE, *board_player[7][3:6], 
        Fore.RED +" |", Fore.GREEN, *board_player[7][6:9], Fore.RED +" | ")

    print(Fore.RED +" |", Fore.GREEN, *board_player[8][0:3],
        Fore.RED +" |", Fore.WHITE, *board_player[8][3:6], 
        Fore.RED +" |", Fore.GREEN, *board_player[8][6:9], Fore.RED +" | ")
    print(Fore.RED + " -------------------------------") 
    print(Style.RESET_ALL)

#FUNCTION input number - this is a loop, allows players inputs.   

def input_numbers():

    i = 10
    while i != 0:
        i = i - 1
        print(" ")
        print("SUDOKU")
        
        kolorki()

        print("\nRozwiąż sudoku!\n")

        x = int(input('Wiersz: '))
        
        while (x) < 1 or (x) > 9:
            x = int(input('Wiersz: '))
        
        y = int(input('Kolumna: '))
        while y < 1 or y > 9:
            y = int(input('Kolumna: '))

        z = int(input('Liczba: '))
        while z < 1 or z > 9:
            z = int(input('Liczba: '))
        
        board_player[int(x)-1][int(y)-1] = int(z)
        
        clear_screen()

    if board_orgin == board_player:
        print(Fore.GREEN + "\nYou win\n")
    else:
        print(Fore.RED + "\nGame over\n")

#MAIN function 

def main():
    input_numbers()

main()
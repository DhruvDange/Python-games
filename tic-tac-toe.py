import time
player_no = 1
played_pos = [] 
available_pos = [1,2,3,4,5,6,7,8,9]
grid = {'7':' ','8':' ','9':' ','4':' ','5':' ','6':' ','1':' ', '2':' ','3':' '}


def rules():
    print("Welcome to tic-tac-toe!!")
    time.sleep(2)
    print("Decide your position by typing on your numpad!")
    print("The grid is numbered as follows:")
    print(" 7 | 8 | 9 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 1 | 2 | 3 ")
    print("Press the corresponding no to make your move!!")
    time.sleep(3)
    print("LETS PLAY!!!!")


def get_player_input():
    
    global played_pos, available_pos
    within_range = False
    pos = 'word'

    while pos.isdigit() == False or within_range == False:

        pos = input("Enter position index (between 1 & 9): ")

        if pos.isdigit() == False:
            print("Input not a number..please enetr again")
        if pos.isdigit() == True:
            if int(pos) in available_pos:
                if pos not in played_pos:
                    played_pos.append(pos)
                    within_range = True
                else:
                    print("Position already played...please enter again")
            else:
                within_range = False
                print("Number not in acceptable range")

    return pos

def player_select(turn):
    global player_no
    selected_pos = 'word'
    if player_no  == 1:
        print("Player 1 please enter your position: ")
        selected_pos = get_player_input()
        display_grid(selected_pos, 1, turn)
        player_no += 1
    else:
        print("Player 2 please enter your position: ")
        selected_pos = get_player_input()
        display_grid(selected_pos, 2, turn)
        player_no -= 1

    
def display_grid(selected_pos, player, turn):
    global available_pos, grid

    for pos in available_pos:
        if pos == int(selected_pos):
            if player == 1:
                grid[selected_pos] = 'X'
            elif player == 2:
                grid[selected_pos] = 'O'

    print(f" {grid['7']} | {grid['8']} | {grid['9']} ")
    print(f"---|---|---")
    print(f" {grid['4']} | {grid['5']} | {grid['6']} ")
    print(f"---|---|---")
    print(f" {grid['1']} | {grid['2']} | {grid['3']} ")
    check_winner(turn)

def check_winner(turn):

    global grid
    won = 0

    if grid['1'] == grid['2'] and grid['2'] == grid['3']:
        if grid['1'] != ' ':
            print(f"Game Over! Player {(player_no)} wins!!")
            won = 1
    elif grid['4'] == grid['5'] and grid['5'] == grid['6']:
        if grid['4'] != ' ':
            print(f"Game Over! Player {(player_no)} wins!!")
            won = 1
    elif grid['7'] == grid['8'] and grid['8'] == grid['9']:
        if grid['7'] != ' ':
            print(f"Game Over! Player {(player_no)} wins!!")
            won = 1
    elif grid['7'] == grid['4'] and grid['4'] == grid['1']:
        if grid['7'] != ' ':
            print(f"Game Over! Player {(player_no)} wins!!")
            won = 1
    elif grid['8'] == grid['5'] and grid['5'] == grid['2']:
        if grid['8'] != ' ':
            print(f"Game Over! Player {(player_no)} wins!!")
            won = 1
    elif grid['9'] == grid['6'] and grid['6'] == grid['3']:
        if grid['9'] != ' ':
            print(f"Game Over! Player {(player_no)} wins!!")
            won = 1
    elif grid['1'] == grid['5'] and grid['5'] == grid['9']:
        if grid['1'] != ' ':
            print(f"Game Over! Player {(player_no)} wins!!")
            won = 1
    elif grid['7'] == grid['5'] and grid['5'] == grid['3']:
        if grid['7'] != ' ':
            print(f"Game Over! Player {(player_no)} wins!!")
            won = 1
    
    if won == 0 and turn == 8:
        print("Game over! DRAW")
        time.sleep(3)
        exit()
    elif won == 1:
        time.sleep(3)
        exit()

def game_run():
    rules()
    for i in range(0,9):
        player_select(i)

game_run()
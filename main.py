# Name: Chase Prasad
# Title: Connect Four

def main():
    #asks user to input height and length to be used to create board
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))
    
    #creates and prints board
    board = initialize_board(height, length)
    print_board(board)

    print("\nPlayer 1: x\nPlayer 2: o")

    #loop used to keep game running until winner or tie is determined
    while True:
        #asks player 1 to input which column they would like to place their piece
        column = int(input("\nPlayer 1: Which column would you like to choose? "))

        #inserts piece into specified column and returns row it was placed in for later use
        row = insert_chip(board, column, 'x')
        #prints board
        print_board(board)

        #checks if latest move has caused player 1 to win or tie and ends the game if so
        if check_if_winner(board, column, row, 'x'):
            print("\nPlayer 1 won the game!")
            break
        elif check_if_tie(board):
            print("\nDraw. Nobody wins.")
            break

        #same logic used for player 2, then loops back to player 1
        column = int(input("\nPlayer 2: Which column would you like to choose? "))

        row = insert_chip(board, column, 'o')
        print_board(board)

        if check_if_winner(board, column, row, 'o'):
            print("\nPlayer 2 won the game!")
            break
        elif check_if_tie(board):
            print("\nDraw. Nobody wins.")
            break

#prints board
def print_board(board):
    for i in board:
        for j in i:
            print(j, end=' ')
        print()

#creates board with specified number of rows and columns
def initialize_board(num_rows, num_cols):
    return [['-'] * num_cols for i in range(num_rows)]

#inserts player chip into open row in column on board
def insert_chip(board, col, chip_type):
    for i in range(len(board) - 1, -1, -1):
        if board[i][col] == '-':
            board[i][col] = chip_type
            return i

#checks if latest move has determined a winner
def check_if_winner(board, col, row, chip_type):
    #count variable used to count 4 in a row to determine win
    count = 0

    #checks for win vertically
    for c in range(col - 3, col + 4):
        if 0 <= c < len(board[0]) and board[row][c] == chip_type:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0

    #resets count variable for next check
    count = 0

    #checks for win horizontally
    for r in range(row - 3, row + 4):
        if 0 <= r < len(board) and board[r][col] == chip_type:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
    
    return False

#checks if any space is left in board, if not meaning there is a tie
def check_if_tie(board):
    if any('-' in i for i in board):
        return False
    
    return True

if __name__ == "__main__":
    main()
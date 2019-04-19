import game, math, random, time
from game import Game

# Agente1: fav1 = nlinhas4(1) – nlinhas4(2)
# Agente2: fav2 = 100*fav1 + nlinhas3(1) – nlinhas3(2)
# Agente3: fav3 = 100*fav1 + central(1) – central(2)
# Agente4: fav4 = 5*fav2 + fav3 

def Agente1(game):
    return game.nlinhas4(1) - game.nlinhas4(2)

def Agente2(game):
    fav1 = game.nlinhas4(1) - game.nlinhas4(2)
    return 100*fav1 + game.nlinhas3(1) - game.nlinhas3(2)

def Agente3(game):
    fav1 =  game.nlinhas4(1) - game.nlinhas4(2)
    return 100*fav1 + game.central(1) - game.central(2)

def Agente4(game):
    fav1 = game.nlinhas4(1) - game.nlinhas4(2)
    fav2 = 100*fav1 + game.nlinhas3(1) - game.nlinhas3(2)
    fav3 = 100*fav1 + game.central(1) - game.central(2)
    return 5*fav2 + fav3

#INICIO: alínea d)

def minimax(game, depth, alpha, beta, maximizingPlayer, agent):

    if (depth == 0 or game.winning_move(1) or game.winning_move(2)) and agent == 1:
        return None, None, Agente1(game)

    if (depth == 0 or game.winning_move(1) or game.winning_move(2)) and agent == 2:
        return None, None, Agente2(game)

    if (depth == 0 or game.winning_move(1) or game.winning_move(2)) and agent == 3:
        return None, None, Agente3(game)

    if (depth == 0 or game.winning_move(1) or game.winning_move(2)) and agent == 4:
        return None, None, Agente4(game)
        
    valid_locations = game.get_valid_locations()
    
    if maximizingPlayer:
        value = -math.inf
        children = game.children(1)

        column = random.choice(valid_locations)
        row = game.is_valid_position(column)

        for child in children:

            new_score = minimax(child[0], depth - 1, alpha, beta, False, agent)

            if new_score[2] > value:
                value = new_score[2]
                column = child[2]
                row = child[1]

            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return column, row, value

    else:
        value = math.inf
        children = game.children(2)

        column = random.choice(valid_locations)
        row = game.is_valid_position(column)

        for child in children:
            new_score = minimax(child[0], depth - 1, alpha, beta, True, agent)
            if new_score[2] < value:
                value = new_score[2]
                column = child[2]
                row = child[1]
            beta = min(beta, value)
            if beta <= alpha:
                break
        return column, row, value

#FIM: alínea d)

def player_player(game):

    moves = 0

    while not game.game_over and moves != 42:
        if game.turn == 0:
            col = int(input("Player 1 Make your Selection (0-6):"))
            row = game.is_valid_position(col)

            if row != -1:
                game.drop_piece(row, col, 1)
                if game.winning_move(1):
                    print("______________________")
                    print(game.board)
                    print("______________________")
                    print("PALYER 1 Wins! Congrats!")
                    game.game_over = True
                    break

        else:
            col = int(input("Player 2 Make your Selection (0-6):"))
            row = game.is_valid_position(col)

            if row != -1:
                game.drop_piece(row, col, 2)
                if game.winning_move(2):
                    print("______________________")
                    print(game.board)
                    print("______________________")
                    print("PALYER 2 Wins! Congrats!")
                    game.game_over = True
                    break

        print(game.board)

        game.turn += 1
        game.turn = game.turn % 2
        moves += 1

def player_vs_AI(game):

    moves = 0
    
    while not game.game_over and moves != 42:

        if game.turn == 0:
            
            column, row, minimax_score = minimax(game, 5, -math.inf, math.inf, True, 3)

            #row = game.is_valid_position(column)
            if row != -1:
                game.drop_piece(row, column, 1)
                if game.winning_move(1):
                    print("______________________")
                    print(game.board)
                    print("______________________")
                    print("PLAYER 1 Wins! Congrats!")
                    game.game_over = True
                    break

        else:
            col = int(input("Player 2 Make your Selection (0-6):"))
            row = game.is_valid_position(col)

            if row != -1:
                game.drop_piece(row, col, 2)
                if game.winning_move(2):
                    print("______________________")
                    print(game.board)
                    print("______________________")
                    print("PLAYER 2 Wins! Congrats!")
                    game.game_over = True
                    break

        print("______________________")
        print(game.board)
        print("______________________")

        game.turn += 1
        game.turn = game.turn % 2
        moves += 1

def ai_vs_ai(game):

    moves = 0

    while not game.game_over and moves != 42:

        if game.turn == 0:
            
            column, row, minimax_score = minimax(game, 7, -math.inf, math.inf, True, 3)
            #row = game.is_valid_position(column)

            if row != -1:
                #time.sleep(1)
                game.drop_piece(row, column, 1)
                if game.winning_move(1):
                    print("______________________")
                    print(game.board)
                    print("______________________")
                    print("PLAYER 1 Wins! Congrats!")
                    game.game_over = True
                    break

        else:
            column, row, minimax_score = minimax(game, 7, -math.inf, math.inf, True, 4)
            
            #row = game.is_valid_position(column)
            
            if row != -1:
                #time.sleep(1)
                game.drop_piece(row, column, 2)
                if game.winning_move(2):
                    print("______________________")
                    print(game.board)
                    print("______________________")
                    print("PLAYER 2 Wins! Congrats!")
                    game.game_over = True
                    break

        print("______________________")
        print(game.board)
        print("______________________")

        game.turn += 1
        game.turn = game.turn % 2
        moves += 1

def main():
    game = Game()
    print("Please choose an option:")
    print("1: Player vs Player")
    print("2: Player vs AI")
    print("3: AI vs AI")
    opt = int(input())

    if opt == 1:
        player_player(game)
    if opt == 2:
        player_vs_AI(game)
    if opt == 3: 
        ai_vs_ai(game)

if __name__ == "__main__":
    main()
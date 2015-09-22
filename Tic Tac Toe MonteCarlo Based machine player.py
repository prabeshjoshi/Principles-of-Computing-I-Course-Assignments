"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator

NTRIALS = 20        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    

EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4


def mc_trial(board, player):
    """This function takes a current board and the next player to move. 
    The function should play a game starting with the given player by 
    making random moves, alternating between players.
    The function should return when the game is over."""
   
    empty = list(board.get_empty_squares())
    while board.check_win() == None :
        ranpos = random.choice(empty)
        board.move(ranpos[0],ranpos[1], player)
        player = provided.switch_player(player)
                 
def mc_update_scores(scores, board, player):
    """This function takes a grid of scores (a list of lists) with
    the same dimensions as the Tic-Tac-Toe board, 
    a board from a completed game, and which player the machine player is. """
    dimen = board.get_dim()
    player2 = provided.switch_player(player)
    
    if board.check_win() == player:
        for row in range(dimen):
            for col in range(dimen):
                if board.square(row, col) == player:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == player2:
                    scores[row][col] -= SCORE_OTHER
    
    elif board.check_win() == player2:
        for row in range(dimen):
            for col in range(dimen):
                if board.square(row, col) == player2:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == player:
                    scores[row][col] -= SCORE_OTHER     
    
    
def get_best_move(board, scores):
    """  The function should find all of the empty squares
    with the maximum score 
    and randomly return one of them as a (row, column) tuple."""
    score_list= []
    dimen = board.get_dim()
    for square in board.get_empty_squares():
        score_list.append(scores[square[0]][square[1]])
        

    if not len(score_list) == 0:
        maxscore = max(score_list)
        best_moves = []                    
        for row in range(dimen):
            for col in range(dimen):
                if scores[row][col] == maxscore:
                    if board.square(row, col) == EMPTY:
                        best_moves.append((row,col))
                    
        return random.choice(best_moves)

def mc_move(board, player, trials):
    """ The function should use the Monte Carlo simulation described above
    to return a move for the machine player in the form of a (row, column) tuple."""
    dimen = board.get_dim()
    scores = [[0 for _ in range(dimen)]
                for _ in range(dimen)]
                                   
    for _ in range(trials):
        clone = board.clone()
        mc_trial(clone, player)
        mc_update_scores(scores, clone, player)
   
        
    return get_best_move(board, scores)
    
    

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

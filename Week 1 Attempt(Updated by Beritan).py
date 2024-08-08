import random

class Card:
    def __init__(self, symbol):
        self.symbol = symbol
        self.is_matched = False

    def reveal(self):
        return self.symbol if self.is_matched else "*"

    def hide(self):
        return "*" if not self.is_matched else self.symbol


class GameBoard:
    def __init__(self, board_size=6):
        self._board_size = board_size
        self._grid_of_cards = self._setup_board()

    def _setup_board(self):
        symbols = [chr(i) for i in range(65, 65 + (self._board_size * self._board_size) // 2)]
        symbols *= 2 #tried retyping by Anne
        random.shuffle(symbols)

        board = []
        for i in range(self._board_size):
            row = []
            for j in range(self._board_size):
                row.append(Card(symbols.pop()))
            board.append(row)
        return board

    def display(self):                      #Added by Kevin. This is to show the current state of the board.
        for row in self._grid_of_cards:
            print(" ".join(card.reveal() for card in row))


class MemoryGame:
    def __init__(self):                     #Changed by Kevin. Removed "moves_counter" and "matched_pairs" since they're unused parameters.
        self.game_board = GameBoard()
        self.moves_counter = 0
        self.matched_pairs = []

    def flip_card(self, row, col):
        card = self.game_board._grid_of_cards[row][col]
        print (f"Card at ({row}, {col}) : {card.reveal()}")
        return card

    def check_match(self, first_card, second_card):
        if first_card.symbol == second_card.symbol:
            first_card.is_matched = True
            second_card.is_matched = True
            self.matched_pairs.append((first_card, second_card))
            return True
        return False

    def update_board(self):
        self.game_board.display()

    def display_end_game_message(self):
        print("Congratulations!")

    def play(self):
        while len(self.matched_pairs) < (self.game_board._board_size * self.game_board._board_size) // 2:
            self.update_board()
            try:
                row1, col1 = map(int, input("Enter the first card (row col): ").split())
                first_card = self.flip_card(row1, col1)

                row2, col2 = map(int, input("Enter the second card (row col): ").split())
                second_card = self.flip_card(row2, col2)

                self.moves_counter += 1
                
                if not self.check_match(first_card, second_card):
                    print("No match. Try again.")
                else:
                    print("Match!")
                      
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column numbers.")
        
        self.update_board()
        self.display_end_game_message()

if __name__ == "__main__":  #Added by Kevin. This is to run the game.
    game = MemoryGame()
    game.play()

MemoryGame.display_end_game_message()
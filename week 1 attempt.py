class Card:
    def __init__(self, symbol):
        self.symbol = symbol
        self.is_matched = False

    def reveal(self): 
        return self.symbol

    def hide(self):
        return "*"


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


class MemoryGame:
	def __init__(self):
		self.game_board = GameBoard()
		self.moves_counter = 0
		self.matched_pairs = []

	def flip_card(self, row, col):
		card = self.game_board._grid_of_cards[row][col]
		print(f"Card at ({row}, {col}) : {card.reveal()}")
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
		while len(self.matched_pairs) < (self.game_board_size * self.game_board.board_size) // 2:
			self.update_board()
            try:
				row1, col1 = map(int, input("Enter the first card (row col): ").split())
                first_card = self.flip_card(row1, col1)
                row2, col2 = map(int, input("Enter the second card (row col): ").split())
                second_card = self.flip_card(row2, col2)

                self.moves_counter +=1

                if not self-check_match(first_card, second_card):
	                print(“No match. Try again.”)
                else:
	                print("Match!")
					
            except ValueError:
                print("Invalid input. Please enter row and column numbers.")

		self.dislay_end_game_message()

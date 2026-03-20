import os
import random
from typing import List, Generator


class Board:
    def __init__(self):
        self.cells = [" " for i in range(1, 10)]

    def display(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.cells[i]} | {self.cells[i + 1]} | {self.cells[i + 2]} ")
            if i < 6:
                print("-----------")
        print("\n")

    def update(self, position, symbol):
        if self.cells[position - 1] not in ["X", "O"]:
            self.cells[position - 1] = symbol

    def available_moves(self) -> List[int]:
        return [i + 1 for i, v in enumerate(self.cells) if v not in ("X", "O")]


class Player:
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol

    def make_move(self, board: Board) -> int:
        while True:
            raw = input(f"{self.name} ({self.symbol}), ваш хід (1-9): ").strip()
            try:
                move = int(raw)
            except ValueError:
                print("Введіть число від 1 до 9.")
                continue
            if move not in range(1, 10):
                print("Введіть число від 1 до 9.")
                continue
            if move not in board.available_moves():
                print("Ця клітинка вже зайнята. Спробуйте ще раз.")
                continue
            return move


class BotPlayer(Player):
    def __init__(self, name: str, symbol: str, *, seed: int | None = None) -> None:
        super().__init__(name, symbol)
        self._rng = random.Random(seed)

    def make_move(self, board: Board) -> int:
        moves = board.available_moves()
        return self._rng.choice(moves)


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player", "X"), Player("Bot", "O")]
        self.current_player_index = 0

    def player_turn(self) -> Generator[Player, None, None]:
        while True:
            yield self.players[self.current_player_index]
            self.current_player_index = (self.current_player_index + 1) % 2

    def check_winner(self):
        win_coords = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонталі
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикалі
            (0, 4, 8), (2, 4, 6)  # діагоналі
        ]
        for a, b, c in win_coords:
            for player_sign in ["X", "O"]:
                if self.board.cells[a] == self.board.cells[b] == self.board.cells[c] == player_sign:
                    return True
        return False


def start_game():
    game = Game()
    turn_gen = game.player_turn()

    for _ in range(9):
        print("--- Гра в хрестики-нулики ---")
        game.board.display()
        current_player = next(turn_gen)
        move = current_player.make_move(game.board)
        game.board.update(move, current_player.symbol)

        if game.check_winner():
            game.board.display()
            print(f"Переможець: {current_player.name} ({current_player.symbol})")
            return

        os.system("cls")

    print("Нічия.")


if __name__ == "__main__":
    start_game()
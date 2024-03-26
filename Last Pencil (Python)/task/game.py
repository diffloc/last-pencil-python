from typing import NoReturn


class Pencils:
    def __init__(self) -> None:
        self.num_pencils = 0

    def print_pencils(self) -> None:
        print("|" * self.num_pencils)

    def set_num_pencils(self, num_pencils: int) -> None:
        self.num_pencils = num_pencils

    def remove_pencils(self, num_removed: int) -> None:
        self.num_pencils -= num_removed

    def choose_num_pencils(self) -> None:
        print("How many pencils would you like to use:")
        while True:
            try:
                num_pencils = int(input())
                if num_pencils <= 0:
                    print("The number of pencils should be positive")
                    continue
                self.num_pencils = num_pencils
                break
            except ValueError:
                print("The number of pencils should be numeric")


class Players:
    def __init__(self) -> None:
        self.players = ("John", "Jack")
        self.current_player = ""
        self.is_bot_turn = False

    def switch_player(self) -> None:
        self.current_player = "Jack" if self.current_player == "John" else "John"
        self.is_bot_turn = not self.is_bot_turn

    def choose_player_one(self) -> None:
        while True:
            print(f"Who will be the first ({self.players[0]}, {self.players[1]}):")
            player_name = input()
            if player_name in self.players:
                self.current_player = player_name
                self.is_bot_turn = (player_name == "Jack")
                break
            else:
                print(f"Choose between '{self.players[0]}' and '{self.players[1]}'")


def bot_move(pencils) -> int:
    remainder = pencils.num_pencils % 4
    if remainder == 0:
        return 3
    elif remainder == 1:
        return 1
    else:
        return remainder - 1


def start_game(pencils, players) -> None:
    while pencils.num_pencils > 0:
        pencils.print_pencils()
        if players.is_bot_turn:
            move = bot_move(pencils)
            print(f"{players.current_player}'s turn:\n{move}")
            pencils.remove_pencils(move)
        else:
            print(f"{players.current_player}'s turn:")
            while True:
                try:
                    move = int(input())
                    if move < 1 or move > 3:
                        raise ValueError
                    if move > pencils.num_pencils:
                        print("Too many pencils were taken")
                        continue
                    if 1 <= move <= 3 and move <= pencils.num_pencils:
                        pencils.remove_pencils(move)
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    print("Possible values: '1', '2', or '3'")
        players.switch_player()
    print(f"{players.current_player} won!")


def initialize_game() -> None:
    pencils = Pencils()
    players = Players()
    pencils.choose_num_pencils()
    players.choose_player_one()
    start_game(pencils, players)


def main() -> NoReturn:
    initialize_game()


if __name__ == "__main__":
    main()

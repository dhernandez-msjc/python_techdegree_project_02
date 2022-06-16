def display_title() -> None:
    pass


def display_main_menu() -> None:
    pass


def display_players() -> None:
    pass


def display_team_list(players: list) -> None:
    print("Players on Team: ")
    for player in players:
        print(f"    {player['name']}")
    print()

    print("Guardians: ")
    for player in players:
        for guardian in player["guardians"]:
            print(f"    {guardian}")
    print()


def run_menu() -> None:
    pass
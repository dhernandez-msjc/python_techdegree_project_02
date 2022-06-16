def display_title() -> None:
    pass


def display_main_menu() -> None:
    pass


def display_players() -> None:
    pass


def display_team_list(players: dict) -> None:
    number_of_experienced = len(players['experienced_players'])
    number_of_inexperienced = len(players['inexperienced_players'])

    print(f"Total players      : {number_of_experienced + number_of_inexperienced}")
    print(f"Total Experienced  : {number_of_experienced}")
    print(f"Total Inexperienced: {number_of_inexperienced}\n")

    print("Players on Team: ")
    print(f"    Experienced: {', '.join([player['name'] for player in players['experienced_players']])}")

    print("  Inexperienced:")
    print(f"-- {', '.join([player['name'] for player in players['experienced_players']])}")
    for player in players['inexperienced_players']:
        print(f"        {player['name']}")
    print()

    print("Guardians: ")
    for player in players['experienced_players']:
        print(f"    {', '.join(player['guardians'])}")
    print()


def run_menu() -> None:
    pass
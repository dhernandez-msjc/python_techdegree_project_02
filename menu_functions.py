from team_balancing import PLAYERS_PER_TEAM


def display_title() -> None:
    print("BASKETBALL TEAM STATS TOOL\n")


def display_main_menu() -> None:
    print("1. Display Team Stats")
    print("2. Exit")
    print()

def calculate_average_height(players: dict) -> float:
    average_height = 0
    for player_type in ['experienced_players', 'inexperienced_players']:
        for player in players[player_type]:
            average_height += player['height']
    return average_height / PLAYERS_PER_TEAM


def get_player_names(player_type: str, players: dict) -> str:
    """
    Joins a list of player names of specified player type (in-/experienced),
    and returns information as a string.
    :param player_type: experienced, or inexperienced players.
    :param players: the dictionary of players to extract names from.
    :return: string representing concatenation of player names.
    """
    return ', '.join([player['name'] for player in players[player_type]])


def get_player_guardians(player_type: str, players: dict) -> str:
    """

    :param player_type:
    :param players:
    :return:
    """
    guardians = []
    for player in players[player_type]:
        for guardian in player['guardians']:
            guardians.append(guardian)
    return ", ".join(guardians)


def display_team_info(team: str, players: dict) -> None:
    number_of_experienced = len(players['experienced_players'])
    number_of_inexperienced = len(players['inexperienced_players'])

    print("=========================")
    print(f"Team: {team}")
    print("=========================")
    print(f"Total players      : {number_of_experienced + number_of_inexperienced:4.0f}")
    print(f"Total Experienced  : {number_of_experienced:4.0f}")
    print(f"Total Inexperienced: {number_of_inexperienced:4.0f}")
    print(f"Average height     : {calculate_average_height(players):4.1f}")
    print("=========================\n")

    print("Players on Team: ")
    print(f"    Experienced: {get_player_names('experienced_players', players)}")
    print(f"  Inexperienced: {get_player_names('inexperienced_players', players)}\n")

    print("Guardians: ")
    print(f"    Experienced: {get_player_guardians('experienced_players', players)}")
    print(f"  Inexperienced: {get_player_guardians('inexperienced_players', players)}\n")


def run_menu(team_data: dict) -> None:
    display_title()

    while True:
        display_main_menu()
        user_input = int(input("Enter Menu Selection:  "))

        if user_input == 1:
            print("1. Panthers")
            print("2. Bandits")
            print("3. Warriors")

            team = user_input = int(input("Enter Team Selection:  "))
            if user_input == 1:
                team = "Panthers"
            elif user_input == 2:
                team = "Bandits"
            elif user_input == 3:
                team = "Warriors"

            display_team_info(team, team_data[team])
            input("Press Enter to continue ...")

        elif user_input == 2:
            break


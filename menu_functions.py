from constants import TEAMS
from team_balancing import PLAYERS_PER_TEAM

MENU_OPTIONS = ["Display Team Stats", "Exit"]


def display_title() -> None:
    """
    Displays the main title in a clean format
    :return: None
    """
    TITLE = "BASKETBALL TEAM STATS TOOL"
    BORDER = "=" * (2 * len(TITLE))

    print(BORDER)
    print(f"{TITLE:^{len(BORDER)}}")
    print(BORDER)


def display_main_menu() -> None:
    """
    Displays the main menu in a clean format.
    :return: None
    """
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    for index, menu_item in enumerate(MENU_OPTIONS, 1):
        print(f'{index}. {menu_item}')
    print("~~~~~~~~~~~~~~~~~~~~~~~")


def display_team_options() -> None:
    """
    Display Team Selection Options in a clean format.
    :return: None
    """
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    for index, team_name in enumerate(TEAMS, 1):
        print(f'{index}. {team_name}')
    print("~~~~~~~~~~~~~~~~~~~~~~~")


def calculate_average_height(players: dict) -> float:
    """
    Calculates the average height of all players on a team and returns
    the value as a float.
    :param players: dictionary of players to extract heights from.
    :return: a float representing the average height of players on team.
    """
    average_height = 0
    for player_experience in ['experienced_players', 'inexperienced_players']:
        for player in players[player_experience]:
            average_height += player['height']
    return average_height / PLAYERS_PER_TEAM


def get_player_names(player_experience: str, players: dict) -> str:
    """
    Joins a list of player names of specified player type (in-/experienced),
    and returns information as a string.
    :param player_experience: experienced, or inexperienced players.
    :param players: the dictionary of players to extract names from.
    :return: string representing concatenation of player names.
    """
    return ', '.join([player['name'] for player in players[player_experience]])


def get_player_guardians(player_experience: str, players: dict) -> str:
    """
    Concatenates the list of player guardians of a given player
    experience type
    :param player_experience: experienced, or inexperienced players.
    :param players: dictionary of players to extract guardians from.
    :return: string representing concatenation of player guardians.
    """
    guardians = []
    for player in players[player_experience]:
        for guardian in player['guardians']:
            guardians.append(guardian)
    return ", ".join(guardians)


def display_team_info(team_name: str, players: dict) -> None:
    """
    Displays selected team information from a given dictionary of team players.
    :param team_name: String representing the name of the team.
    :param players: Dictionary of team players.
    :return: None
    """
    number_of_experienced = len(players['experienced_players'])
    number_of_inexperienced = len(players['inexperienced_players'])

    print("=========================")
    print(f"Team: {team_name}")
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


def validated_user_input() -> bool:
    pass


def run_menu(team_data: dict) -> None:
    """
    Runs main menu program.
    :param team_data: dictionary of team data.
    :return: None
    """
    display_title()

    while True:
        display_main_menu()
        # TODO needs to have error handling
        user_input = int(input("Enter Menu Selection:  "))
        print()

        if user_input == 1:
            display_team_options()
            team = user_input = int(input("Enter Team Selection:  "))
            print()

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


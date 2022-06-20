from constants import PLAYERS, TEAMS

# Determine the number of teams, players and players per team.
NUMBER_OF_TEAMS = len(TEAMS)
TOTAL_PLAYERS = len(PLAYERS)
PLAYERS_PER_TEAM = TOTAL_PLAYERS // NUMBER_OF_TEAMS


def split_by_player_experience(players: list) -> (list, list):
    """
    Splits the players into two sets of lists, experienced and
    the other for inexperienced players.
    :param players: The players list to analyze.
    :return: tuple of lists representing the list of experienced
    and inexperienced players.
    """
    experienced_players = []
    inexperienced_players = []

    for player in players:
        if player['experience']:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    return experienced_players, inexperienced_players


def create_balanced_teams(players: list) -> dict:
    """
    Takes in a list of players and creates a balanced team of experienced and
    inexperienced players.
    :param players: the list of players to create a balanced team from.
    :return: A dictionary of balanced teams.
    """
    balanced_teams = {}
    experienced_players, inexperienced_players = split_by_player_experience(players)

    for team in TEAMS:
        balanced_teams[team] = {"experienced_players": [], "inexperienced_players": []}

    while experienced_players:
        for team, team_players in balanced_teams.items():
            team_players['experienced_players'].append(experienced_players.pop())

    while inexperienced_players:
        for team, team_players in balanced_teams.items():
            team_players['inexperienced_players'].append(inexperienced_players.pop())

    return balanced_teams

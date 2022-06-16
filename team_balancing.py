from constants import TEAMS
from constants import PLAYERS

# Determine the number of teams, players and players per team.
NUMBER_OF_TEAMS = len(TEAMS)
TOTAL_PLAYERS = len(PLAYERS)
PLAYERS_PER_TEAM = TOTAL_PLAYERS // NUMBER_OF_TEAMS


def split_by_player_experience(players: list) -> (list, list):
    experienced_players = []
    inexperienced_players = []

    for player in players:
        if player['experience']:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    return experienced_players, inexperienced_players


def create_balanced_teams(players: list) -> dict:
    balanced_teams = {}
    experienced_players, inexperienced_players = split_by_player_experience(players)

    for team in TEAMS:
        balanced_teams[team] = []

    while experienced_players:
        for team, team_players in balanced_teams.items():
            team_players.append(experienced_players.pop())

    while inexperienced_players:
        for team, team_players in balanced_teams.items():
            team_players.append(inexperienced_players.pop())

    return balanced_teams

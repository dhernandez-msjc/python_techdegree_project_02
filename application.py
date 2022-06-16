import constants
from data_cleaning import clean_data
from team_balancing import create_balanced_teams
import menu_functions


def main():
    cleaned_data = clean_data(constants.PLAYERS)
    balanced_teams = create_balanced_teams(cleaned_data)

    menu_functions.display_team_list(balanced_teams['Panthers'])
    # menu_functions.display_team_list(balanced_teams['Bandits'])


if __name__ == '__main__':
    main()

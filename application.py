from constants import PLAYERS
from data_cleaning import clean_data
from team_balancing import create_balanced_teams
import menu_functions


def main() -> None:
    cleaned_data = clean_data(PLAYERS)
    balanced_teams = create_balanced_teams(cleaned_data)
    menu_functions.run_menu(balanced_teams)


if __name__ == '__main__':
    main()

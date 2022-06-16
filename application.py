import constants
from data_cleaning import clean_data
from team_balancing import create_balanced_teams


def main():
    cleaned_data = clean_data(constants.PLAYERS)
    balanced_teams = create_balanced_teams(cleaned_data)

    print(balanced_teams)


if __name__ == '__main__':
    main()

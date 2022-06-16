import constants
from data_cleaning import clean_data


def main():
    cleaned_data = clean_data(constants.PLAYERS)
    print(cleaned_data)

    print(len(cleaned_data)//len(constants.TEAMS))


if __name__ == '__main__':
    main()

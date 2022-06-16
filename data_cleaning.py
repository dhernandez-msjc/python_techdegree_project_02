def clean_data(data: list) -> list:
    """
    Function takes in a list of data to be cleaned and returns
    a cleaned list of data.
    :param data: list of data to be cleaned.
    :return: list of cleaned data.
    """
    cleaned_data = []

    for player in data:
        player_data = {"name": player["name"],
                       "guardians": clean_guardians(player),
                       "experience": convert_experience(player),
                       "height": convert_height(player)
                       }
        cleaned_data.append(player_data)
    return cleaned_data


def clean_guardians(player: dict) -> list:
    """
    Cleans guardian list by removing " and "
    :param player: The player data to be cleaned
    :return: names of guardians as a list of strings
    """
    return player["guardians"].split(" and ")


def convert_experience(player: dict) -> bool:
    """
    Converts the experience field of the player data
    into a boolean value.
    :param player: The player data to be cleaned
    :return: boolean value representing experience
    """
    return player["experience"] == "YES"


def convert_height(player: dict) -> int:
    """
    Converts player's height from a string into an int.
    :param player: The player data to be cleaned
    :return: the player's height in inches as an int
    """
    return int(player["height"].split()[0])

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
                       "guardians": player["guardians"],
                       "experience": convert_experience(player),
                       "height": convert_height(player)
                       }
        cleaned_data.append(player_data)
    return cleaned_data


def convert_experience(player: dict) -> bool:
    return player["experience"] == "YES"


def convert_height(player: dict) -> int:
    return int(player["height"].split()[0])


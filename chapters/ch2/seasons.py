def season(season_name):
    season_name = season_name.lower()
    if season_name == 'winter':
        season_related_word = 'snow'
        return season_related_word
    elif season_name == 'spring':
        season_related_word = 'flowers'
        return season_related_word
    elif season_name == 'summer':
        season_related_word = 'beach'
        return season_related_word
    elif season_name == 'fall' or season_name == 'autumn':
        season_related_word = 'leaves'
        return season_related_word
    else:
        return "I don't know this season"


def challenge_2():
    season_name = input('Please enter a season: ')
    result = season(season_name)
    print(result)


if __name__ == '__main__':
    challenge_2()

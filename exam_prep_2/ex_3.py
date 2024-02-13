from collections import defaultdict


def sort_players(kvp):
    return -len(kvp[1]), kvp[0]


def team_lineup(*args):
    country_players = defaultdict(lambda: [])
    for player_name, country in args:
        country_players[country].append(player_name)

    result = ""

    sorted_players = sorted(country_players.items(), key=sort_players)
    for country, players in sorted_players:
        result += f"{country}:\n"
        for player_name in players:
            result += f"  -{player_name}\n"
    return result[:-1]




print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")
)
)

#challenge 1

class Player:
    def __init__(self, player_info):
        self.__dict__.update(player_info)


player_data = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}

player_instance = Player(player_data)
print(player_instance.name) 

#challenge 2

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}


player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)


print(player_kevin)
print(player_jason)
print(player_kyrie)

#challenge 3

players_list = [
    {"name": "Kevin Durant", "age": 34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age": 24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age": 32, "position": "Point Guard", "team": "Brooklyn Nets"},
    
]

new_team = [Player(player_info) for player_info in players_list]

#ninja bonus

class Player:
    def __init__(self, player_info):
        self.__dict__.update(player_info)

    @classmethod
    def get_team(cls, team_list):
        return [cls(player_info) for player_info in team_list]

new_team = Player.get_team(players_list)
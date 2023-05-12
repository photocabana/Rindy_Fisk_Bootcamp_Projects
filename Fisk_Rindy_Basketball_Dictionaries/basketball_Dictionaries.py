#Challenge 1: Update the Constructor
#Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
class Player:
    def __init__(self, player_roster):
        self.name = player_roster["name"]
        self.age = player_roster["age"]
        self.position = player_roster["position"]
        self.team = player_roster["team"]

    @classmethod 
    def get_team(cls, team_list):
        rocket_team=[]
        for basketball_team in team_list:
            rocket_team.append(cls(basketball_team))
        print(rocket_team)
        return rocket_team

#Challenge 2: Create instances using individual player dictionaries.
#Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.
kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    }
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
print(kevin)

player_jason = Player(jason)
print(jason)

player_kyrie = Player(kyrie)
print(kyrie)


#Challenge 3: Make a list of Player instances from a list of dictionaries
#Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]


# ... (class definition and large list of players here)
new_team = []
# Write your for loop here to populate the new_team variable with Player objects

def populate_new_team():
    for player in players:
        new_team.append(player)
    return new_team

print(populate_new_team())



# NINJA BONUS: Add a get_team(cls, team_list) @class method
# Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!

Player.get_team(players)

# Set up a new file and add the Player class with the given constructor

# Challenge 1: Update the constructor to accept a dictionary (player) as an argument and set the attributes using the dictionary

# Complete challenge 2: Create 3 instances of the Player class using the given dictionaries

# Complete challenge 3: Populate a new list with Player instances from the list of players.

# Ninja Bonus: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
class User:
    #Attributes
    def __init__(self, first_name, Last_name, email, age):
        self.first_name = first_name
        self.last_name = Last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards member: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")

    def enroll(self):
        
        if self.is_rewards_member:
            print("User already a member")
            return self
        
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        
        if self.gold_card_points < amount:
            "You don't have enough points."
        return self
        
        #self.gold_card_points -= amount
        self.gold_card_points = self.gold_card_points - amount
        


my_user = User("Rindy", "Fisk","rinnn16@hotmail.com", 40)
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(100)
my_user.display_info()


my_user = User("Rindy", "Fisk", "rinnn16@hotmail.com", 40)
my_user.display_info()

user2 = User("Michael", "Fisk", "vinnarrk@hotmail.com", 40)
user3 = User("Donald", "Cook", "wouldYouLike2no@fake.com", 59)

my_user.spend_points(50)
user2.enroll()
user2.spend_points(80)

my_user.display_info()
user2.display_info()
user3.display_info()
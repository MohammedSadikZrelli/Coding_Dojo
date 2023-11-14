class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self  
    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("Enrolled successfully!")
        else:
            print("User already a member.")
        return self  

    def spend_points(self, amount):
        if not self.is_rewards_member:
            print("User is not a rewards member. Enroll first.")
        elif amount <= 0:
            print("Amount should be a positive number.")
        elif amount > self.gold_card_points:
            print("Insufficient points.")
        else:
            self.gold_card_points -= amount
            print(f"Spend successful! Remaining points: {self.gold_card_points}")
        return self 

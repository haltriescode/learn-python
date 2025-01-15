# creating class

# class User:
#    pass 

# adding attributes
# user_1 = User()
# user_1.id = "001"
# user_1.username = "haltriescode"

# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.name = "jack"

# constructor
# part of class blueprint

# class Car:
#    def __init__ (self, seats):
    #initialize
#        self.seats = seats

# class User:
#    def __init__(self,user_id, username):
#        self.id = user_id
#        self.username = username

#User_1 = User("001","angela")

#print(User_1.username)

# ADDING METHODS
#class AnotherCar:
#    def enter_race_mode():
#        self.seats = 2

#my_car.enter_race_mode()

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.followers)
print(user_2.followers)
print(user_2.following)



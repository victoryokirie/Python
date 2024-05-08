class Users:
    def __init__(self, user_id, user_name): #this is the init function/constructor
        self.id = user_id
        self.uname = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1

timmy = Users("001", "Timmy")
james = Users("002", "James")



timmy.follow(james)
print(timmy.following)
print(james.followers)
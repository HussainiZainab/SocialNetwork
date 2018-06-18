## Made by: Zainab Hussaini
## My Social Network


class User:
    def __init__(self, firstName, lastName, username, bio, userID):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.bio = bio
        self.userID = userID
        self.friends = []
        self.posts = []
        

    def addFriend (self,username):
        self.friends.append(username)

##    def unFriend():
##
##
    def viewNewsFeed (self, friends):
     for Friend in self.friends:
       print (friends.posts)





if __name__== "__main__":
    firstName = "Zainab"
    lastName = "Hussaini"
    username = "ZainabHussaini"
    bio = "Welcome to my timeline."
    userID = 0000

    Zainab = User(firstName, lastName, username, bio, userID)
    lucy = User("Lucy", "Lucille", "Lucygoosy", "I like geese", "0123")
    print (Zainab.firstName)
    print (lucy.firstName)

    Zainab.addFriend("lucygoosy")
    print(Zainab.friends)
    lucy.posts.append("This Is My Friend")
    print(lucy.posts)

    Zainab = User(firstName, lastName, username, bio, userID)
    Sara = User("Sara", "Brown", "SaraBrown", "Welcome", "2222")
    print (Zainab.firstName)
    print (Sara.firstName)
    
    Zainab.addFriend("SaraBrown")
    print(Zainab.friends)
    Sara.posts.append("Another Friend")
    print(Sara.posts)

Zainab.viewNewsFeed(username)

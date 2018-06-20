class User:
    def __init__(self, username):
        self.username = username
        self.firstName = " "
        self.lastName = " "
        self.bio = " "
        self.friends = []
        self.posts = []
        self.userID = " "

    def addFriend(self, person):
        self.friends.append(person)

    def removeFriend(self, person):
        self.friends.remove(person)
        
    def addFirstName(self, firstName):
        self.firstName = firstName
    def addLastName(self, lastName):
        self.lastName = lastName
    def addBio(self, bio):
        self.bio = bio
                
    def addPost(self, post):
        self.posts.append(post)

    def showUsernames(self):
        for friend in self.friends:
            print (friend.username)
            
    def viewNewsFeed(self):
         for friend in self.friends:
            print (friend.posts)
            
    def createUserID(self, num):
        self.userID = num
            
    def createPost(self, content):
        myPost = post(content)
        self.post.append(myPost)
        myPost.createPostID(len(posts))

    def createPostID(self):
        self.postID = len(self.posts)

    def addComment(self, comment):
        self.comments.append(comment)

        
    
class Post:
    def __init__(self, content):
        self.content = content
        self.postID = " "
        self.comments = []
        
    def createPostID(self, num):
        self.postID = num

class Network:
    def __init__(self):
        self.users = []

    def createUser(self, username):
        myUser = User(username)
        self.users.append(myUser)
        myUser.createUserID(len(self.users))

        print ("*Usercreated")

if __name__ == "__main__":

####    username = "ZainabHussaini"
####
####    Zainab = User("ZainabHussaini")
####    Lucy = User("Lucygoosy")
####    Sara = User("SaraBrown")
####
####    Zainab.addFriend(Lucy)
####    Zainab.addFriend(Sara)
####
####    Lucy.posts.append("This is my friend")
####    Sara.posts.append("Another friend")
####
####    Zainab.viewNewsFeed()
####    Zainab.showUsernames()
####    Zainab.addPost("Hello")
####    
####    Zainab.removeFriend(Sara)
####    Zainab.showUsernames()
####   
####    Zainab.addFirstName("Zainab")
####    Zainab.addLastName("Husssaini")
####    Zainab.addBio("Welcome")

    network = Network()
    network.createUser("ZainabHussaini")
    



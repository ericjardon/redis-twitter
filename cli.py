import app as api
from redis import Redis
import time

db = Redis(host="localhost", port=6379, db=0)
tl = db.pubsub()  # pubsub object for the user's timeline


def subscribeAll(currentUser):
    following = app.getFollowing(currentUser)
    for account in following:
        # subscribe to every following account
        api.followUser(currentUser, account)


#Create a new tweet and publish it on the correspondant channel
def createTweet(user, msg):
    db.publish(user + ":channel", msg)


# Suscribe current instance to a channel
def subscribe(user):
    print(tl.subscribe(user + ":channel"))


# Notify a channel about a new follower
def notify(user, follower):
    tl.publish(user + ":channel", " started following you")


def startMenu():
    """Either register or login"""

    print("\nWelcome to Twitter!")
    exit = False
    while not exit:
        print("\nMain Menu")
        print(
            "1) Login to your account\n2) Register a new account\n3) Exit Twitter"
        )
        i = input("Selection: ")

        if i == "3":
            print("Bye!")
            return

        if i == "1":
            print("LOGIN\n")
            login = True
            while login:
                user = input("Your username: ")
                password = input("Your password: ")
                if api.login(user, password):
                    return userMenu(user)
                else:
                    print("Wrong username/password.")
                    login = input("Try again? y/n")
                    if login == "n":
                        break
                    elif login == "y":
                        login = True
                    else:
                        return

        if i == "2":  # register new user
            print("\nRegister")
            login = True
            while login:
                user = input("Create username: ")
                password = input("Create password: ")
                if api.registerUser(user, password):
                    return userMenu(user)
                else:
                    print("The username already exists")
                    login = input("Try again? y/n")
                    if login == "n":
                        break
                    elif login == "y":
                        login = True
                    else:
                        return


def userMenu(currentUser):

    print("Welcome to Twitter-Redis")

    exit = False

    while not exit:
        print(
            "Type 1 to follow somebody, 2 to tweet something, 3 to see your timeline or 4 to exit"
        )
        option = input("Selection: ")

        if option == "1":
            print("Option 1")
            userToFollow = input(
                "Type the username of who you want to follow: ")
            print(subscribe(userToFollow))
            if api.followUser(currentUser, userToFollow):
                subscribe(userToFollow)
                print("You started following: ", userToFollow)

        elif option == "2":
            msg = input("Tweet something: ")
            for i in range(5):
                createTweet(currentUser, msg)
                time.sleep(3)

        elif option == "3":
            currentlyFollowing = db.smembers(currentUser + ":following")
            for user in currentlyFollowing:
                subscribe(user.decode("UTF-8"))

                msg = tl.get_message()
                if msg['type'] == 'message':
                    print(msg['data'])

        elif option == "4":
            print("Bye!")
            break

    # print("welcome,", currentUser)

    # subscribeAll(currentUser)
    # pass


startMenu()
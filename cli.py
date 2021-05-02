import app as api
from redis import Redis
import time

db = Redis(host="localhost", port=6379, db=0)

### PUBLISH-SUBSCRIBE ACTIONS


# Subscribe to all the channles the user follows
def subscribeAll(currentUser, tl):
    print("Subscribing to all...")
    following = api.getFollowing(currentUser)
    for account in following:
        print(account.decode("utf-8"))
        subscribe(tl, account.decode("utf-8"))


# Publish a tweet ito the given channel
def publishTweet(user, msg):
    return db.publish(user + ":channel", msg)


# Suscribe current instance to a channel
def subscribe(tl, user):
    print("Subscribed to channel", user + ":channel")
    return tl.subscribe(user + ":channel")


# Notify a channel about a new follower
def notify(user, follower):
    tl.publish(user + ":channel", " started following you")


def fetchTweets(tl):
    print("---TIMELINE---")
    # a None value is returned from get_message() since the message was already handled.
    msg = tl.get_message()
    while msg is not None:
        if msg["type"] == "message":
            print(msg["data"].decode("utf-8"))
        msg = tl.get_message()


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

        if i == "1":  # Log in
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

        if i == "2":  # Register new user
            print("\REGISTER")
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
    tl = db.pubsub()  # pubsub object for the user's timeline
    subscribeAll(currentUser, tl)  # subscribe to all currently following users
    subscribe(tl, currentUser)  # subscribe to your own channel
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
            if api.followUser(currentUser, userToFollow):
                subscribe(tl, userToFollow)
                print("You started following: ", userToFollow)

        elif option == "2":
            msg = input("Tweet something: ")
            publishTweet(currentUser, msg)  # publishes to their own channel

        elif option == "3":
            fetchTweets(tl)

        elif option == "4":
            print("Bye!")
            break

    # print("welcome,", currentUser)

    # subscribeAll(currentUser)
    # pass


startMenu()
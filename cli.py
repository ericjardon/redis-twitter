import app as api
from redis import Redis

conn = Redis(host="localhost", port=6379, db=0)


def startMenu():
    """Either register or login"""

    print("\nWelcome to Twitter!")
    exit = False
    while not exit:
        print("\nMain Menu")
        print("1) Login to your account\n2) Register a new account\n3) Exit Twitter")
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
                api.helloWorld()
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

        if i == "2":
            return userMenu("new user")

        pass


def userMenu(currentUser):
    """For logged in users
    1) Follow somebody
    2) Tweet something
    3) Log out"""
    print("welcome,", currentUser)
    tl = r.pubsub()  # pubsub object for the user's timeline

    pass

def subscribeAll(currentUser):
    following = app.getFollowing(currentUser)

# Suscribe current instance to a channel
def subscribe(user):
    return db.suscribe(user + ":channel")


# Notify a channel about a new follower
def notify(user, follower):
    return db.publish(user + ":channel", " started following you")


startMenu()
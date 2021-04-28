from redis import Redis

db = Redis(host="localhost", port=6379, db=0)


# Utility functions for user
def seeUsers():
    return db.hgetall("users")


def existUser(user):
    """Receives: a username string
    Returns: a boolean whether user exists in table"""
    return db.hexists("users", user)


# User registration
def registerUser(user, password):
    return db.hset("users", user, password)


# User login
def login(user, password):
    print("Logging in...", user, password)

    if existUser(user):
        print("User exists")
        return password == db.hget("users", user).decode("UTF-8")

    print("User does not exist")
    return False


# Follow a user
def followUser(user, userToFollow):
    # the user's channel subscribes to toFollow channel
    db.sadd(user + ":following", userToFollow)
    db.sadd(userToFollow + ":followers", user)


def unfollowUser(user, userToUnfollow):
    return db.srem(user + ":following", userToUnfollow)


# Suscribe current instance to a channel
def subscribe(user):
    return db.suscribe(user + ":channel")


# Notify a channel about a new follower
def notify(user, follower):
    return db.publish(user + ":channel", " started following you")


# Tweet a messages (list)
def createTweet(user, msg):
    return db.publish(user + ":channel", msg)


def helloWorld():
    print("APP SAYS: Hello, World!")


# See the messages in your timeline

# registerUser(user, password)
# if login(user, password):
#     currentUser = user
#     print("Welcome ", currentUser)
# else:
#     print("Incorrect password or user")

# print(registerUser("bryanmon", "chelas123"))

# solo confirmar si la password ingresada es igual a la existente en redis
# si sí, todo cool, si no, lanzar excepción o algo a´si

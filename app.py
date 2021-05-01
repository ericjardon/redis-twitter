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
    if existUser(user):
        print("User already exists. Registration failed")
        return 0
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
    a = db.sadd(user + ":following", userToFollow)
    b = db.sadd(userToFollow + ":followers", user)
    print("followUser", user, userToFollow, "result:", a, "and", b)


def unfollowUser(user, userToUnfollow):
    a = db.srem(userToUnfollow + ":following", userToUnfollow)
    b = db.srem(user + ":followers", userToUnfollow)
    print("unfollowUser", user, userToUnfollow, "result:", a, "and", b)


# Return the set of accounts that user follows
def getFollowing(user):
    return db.smembers(user + ":following")


# Tweet a messages (list)
# def createTweet(user, msg):
#     return db.publish(user + ":channel", msg)

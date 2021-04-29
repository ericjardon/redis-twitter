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


# Tweet a messages (list)
def createTweet(user, msg):
    return db.publish(user + ":channel", msg)

# Return the set of following users of a user
def getFollowing(user):
    return db.smembers(user+':following')


getFollowing('Ein')

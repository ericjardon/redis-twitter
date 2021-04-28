from redis import Redis

db = Redis(host="localhost", port=6379, db=0)

# User registration
def registerUser(user, password):
    return db.hset("users", user, password)

def seeUsers():
    return db.hgetall("users")

def existUser(user):
    """Receives: a string of the username
        Returns: a boolean if it exists as a key in users table"""
    return db.hexists("users", user)  

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
    db.sadd(user+":following", userToFollow)
    db.sadd(userToFollow+":followers", user)
    

def unfollowUser(user, userToUnfollow):
    return db.srem(user+":following", userToUnfollow)

# Suscribe to a channel
def suscribe(user):
    return db.suscribe(user+":channel")

# Notify a channel the subscripiton
def notify(user, follower):
    return db.publish(user+':channel'," started following you")

# Tweet a messages (list)
def createTweet (user, msg):
    return db.publish(user+":channel", msg)


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

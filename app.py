from redis import Redis
from other import hola

db = Redis(host="localhost", port=6379, db=1)

hola()

db.set("Hello", "World")
print(db.get("Hello").decode("UTF-8"))

# User registration
def registerUser(user, password):
    return db.hset("users", user, password)


def seeUsers():
    return db.hgetall("users")


def existUser(user):
    return db.hexists("users", user)  # regresa bool


def login(user, password):
    if existUser(user):
        print("User exists")
        return password == db.hget("users", user).decode("UTF-8")

    print("User does not exist")
    return False


# User login
user = "bryanmon"
password = "chelas123"
# registerUser(user, password)
if login(user, password):
    currentUser = user
    print("Welcome ", currentUser)
else:
    print("Incorrect password or user")

# print(registerUser("bryanmon", "chelas123"))

# solo confirmar si la password ingresada es igual a la existente en redis
# si sí, todo cool, si no, lanzar excepción o algo a´si

# Follow a new user

# Tweet a messages

# See the messages in your timeline

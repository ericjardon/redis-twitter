import app as app

from redis import Redis
r = Redis(host="localhost", port=6379, db=0)

currentUser = None
def menu():
  exit = False
  loginConfirmed = False
  while not exit:
    print("Welcome to Twitter")
    loginRegisterOption=input("Type 1 to login, type 2 to register: ")
    
    while not loginConfirmed:
      if loginRegisterOption == "1":
          username = input("Please type your username: ")
          password = input("Please type your password: ")
          
          if app.login(username, password):
              currentUser = username
              loginConfirmed= True
              print("Welcome ", currentUser)
              timeline = r.pubsub()


          else:
              print("Wrong username or password please try again")

    # option= input("Please enter an option: ")
    # print("")
    # if option == "1":
    #   stri = ""
      
    #   print("Note: If you want to load your own Automata please copy-paste it in test1.txt")
    #   print("---------------------------")
    #   #Ask user for string
    #   stri= input("Enter the String you want to evaluate: ")
    #   print("")
    #   #Evaluate string with User string
    #   evaluatedString = evaluateString("q0",stri)
    #   print("Final set of states", evaluatedString)
    #   print("")

    #   print("List of final states in the automata", finalStates)
    #   print("")
    #    #Evaluate states form evaluatedString() and run isFinalState()
    #   if isFinalState(evaluatedString):
    #     print("The string is accepted")
    #   else:
    #     print("The string is not accepted")
     
    #   print("")
    
      
    # elif option == "2":
    #     exit = True
    # else:
    #   print("Please enter a valid option :(")


def validation(user, password):
    if login(user, password):
        currentUser = user
        return true
    else:
        return false


menu()




#print -> Welcome to twitter
#input -> Type 1 to register , type 2 to login

#Option 1
#input-> Select a username
#if existUser
#select another username
#else
#input -> select password
#registerUser(username, password)
#currentUser=username
#print -> Successful registration

# Option 2
#input -> Username
#input -> Password
# login (username, password)
# if true
#currentUser=username
#print -> Successful login

#After login or registration

#print -> Pls select an action
#input -> 1 Feed, 2 Follow, 3 Tweet, 4 My tweets

#Option 1
#

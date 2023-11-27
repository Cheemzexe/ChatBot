
##############
#   Imports  #
##############
import pwinput  # used to sanitise password
import time     # 
import webbrowser
import csv
import sys
###############
#   SECURITY  #
###############
def security(): #This function requires a username and password input.
    username = input("Please enter your username\n")
    password = (pwinput.pwinput(prompt=("Please enter your password \n")))
    with open("Username_Password.txt","r") as txt: #opens username&password txt file.
        data = txt.read()
        data = data.split()
        password = password.strip() #encrypts the password into astrixs
    if username == data[0] and password == data[1]:
     return True
    else:
     return False
###############
#LOCATION MENU#
###############
def location(): #asks the user to choose between 4 choices of location
    reply = "0"
    while reply != "1" and reply != "2" and reply != "3" and reply != "4": #user must reply with 1,2,3,4 to proceed

      print("+-----------------------------------------+")
      print("|    Restaurant Location                  |")
      print("|    Choose an option:                    |")
      print("|     1   Havant                          |")
      print("|     2   Portsmouth                      |")
      print("|     3   Southampton                     |")
      print("|     4   Brighton                        |")
      print("+-----------------------------------------+")

      reply = input("Please enter a valid option (1-4)\n")
      if reply == "1":
        return "HAVANT"
      elif reply == "2":
        return "PORTSMOUTH"
      elif reply == "3":
        return "SOUTHAMPTON"
      elif reply == "4":
        return "BRIGHTON"
      else:  
        print("")
        print("Invalid Option Please Try Again(1-4)") #error message
        print("")
###############
#FOODTYPE MENU#
###############
def foodtype(): #asks the user to choose between 3 choices of food types
    reply = "0"
    while reply != "1" and reply != "2" and reply != "3": #user must reply with 1,2,3 to proceed

      print("+-----------------------------------------+")
      print("|    FOOD TYPE LIST                       |")
      print("|    Choose an option:                    |")
      print("|     1   Indian                          |")  
      print("|     2   Chinese                         |")
      print("|     3   FastFood                        |")
      print("+-----------------------------------------+")

      reply = input("Please enter a valid option (1-3)\n")
      if reply == "1":
        return "INDIAN"
      elif reply == "2":
        return "CHINESE"
      elif reply == "3":
        return "FAST FOOD"
      else:
        print("")
        print("Invalid Option Please Try Again (1-3)") #error message
        print("")
#############
#BUDGET MENU#
#############
def budget(): #asks the user to choose between 4 choices of budget
    reply = "0"
    while reply != "1" and reply != "2" and reply != "3" and reply != "4": #user must reply with 1,2,3,4 to proceed

      print("+-----------------------------------------+")
      print("|    BUDGET MENU                          |")
      print("|    Choose an option:                    |")
      print("|     1   £5                              |")  
      print("|     2   £10                             |")
      print("|     3   £15                             |")
      print("|     4   £20                             |")
      print("+-----------------------------------------+")

      reply = input("Please enter a valid option (1-4)\n")
      if reply == "1":
        return "5"
      elif reply == "2":
        return "10"
      elif reply == "3":
        return "15"
      elif reply == "4":
        return "20"
      else:
        print("")
        print("Invalid Option Please Try Again  (1-4)") #error message
        print("")
###########
#MAIN MENU#
###########
def MainMenu():
    print("************************************\n")
    print("**WELCOME TO CHATBOT FOOD SERVICES**\n") 
    print("************************************\n")
#################
#FIND RESTAURANT#
#################
def findrestaurant():
    with open("restaurant.csv", newline="") as csvfile: #opens the csvfile
        reader = csv.DictReader(csvfile) #reads the CSV file
        for row in reader:
           if row["location"] == location and row["foodtype"] == foodtype and row["budget"] == budget:
              print("\n")
              print("**********************************") 
              print("**   Taking you there now       **") 
              print("**   Thank you for using ChatBot**") 
              print("**********************************") 
              time.sleep(3)
              url = (row["website"]) #opens the URL from the CSV file
              webbrowser.open(url, new=0, autoraise=True) 
              sys.exit(0) #closes the program

##########
#SECURITY#
##########
securityOK = security()
if securityOK == True: #if the username and password is correct program goes to the next step
    MainMenu() #presents the mainmenu
    location = location() #presents the location menu
    foodtype = foodtype() #presents the foodtype menu
    budget = budget() #presents the budget menu
    findrestaurant() #reads through the csv file finding the best restaurant which fits the criteria.
else:
    print("access denied") #if username and password are incorrect sends this error message and stops the program#


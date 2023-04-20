import random

player = input(" what is you naem travler")

print("Hello" + player )

def travel():
    miles_travled= random.randint(38,61)
    days_spent=random.randint(3,8)

    print("You've travled" + str("miles_travled") +"miles it took" + str(days_spent) + 'days')

def rest():
        health_increase = random.randint(1,6)
        days_spent = random.randint(2,6)

        print("You've gained" + str(health_increase) + "health it took" + str(days_spent) + "days")


def hunt():
    animal=100
    days_spent= random.randint(2,6)

    print("you've gained"+str(animal)+"lbs of food, and it took" + str(days_spent) + "days")


def help_function():
    commands = ["Travel", "Rest", "Hunt", "Status","Help",]
    print(commands)

def status(date,food,health,travel):


date=
health=5
food=500
days_left =336
travel_distance = 2000

player= input("You've is your name travler")
ready = input("ok," + player +"! Are you ready to start your journey along the Orgeon Trail? Yes or No")

print("you've Options are:")
help_function

travel()
rest()
hunt()
help_function()
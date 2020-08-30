import time

print(""" ____      ____      __                                     
|_  _|    |_  _|    [  |                                    
  \ \  /\  / /.---.  | |  .---.   .--.   _ .--..--.  .---.  
   \ \/  \/ // /__ \ | | / /'`\]/ .'`\ \[ `.-. .-. |/ /__ \ 
    \  /\  / | \__., | | | \__. | \__. | | | | | | || \__., 
     \/  \/   '.__.'[___]'.___.' '.__.' [___||__||__]'.__.'""")
time.sleep(1)
print(""" _        
| |       
| |_ ___  
| __/ _ \ 
| || (_) |
 \__\___/ """)
time.sleep(1)
print("""███████╗██████╗ ██╗   ██╗██╗████████╗   ██╗███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗      █████╗  ██████╗  ██████╗  ██████╗ 
██╔════╝██╔══██╗██║   ██║██║╚══██╔══╝   ██║████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██╔══██╗██╔═████╗██╔═████╗██╔═████╗
█████╗  ██████╔╝██║   ██║██║   ██║█████╗██║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝    ╚██████║██║██╔██║██║██╔██║██║██╔██║
██╔══╝  ██╔══██╗██║   ██║██║   ██║╚════╝██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗     ╚═══██║████╔╝██║████╔╝██║████╔╝██║
██║     ██║  ██║╚██████╔╝██║   ██║      ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║     █████╔╝╚██████╔╝╚██████╔╝╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝   ╚═╝      ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝     ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝ 
                                                                                                                              """)
time.sleep(1)
confirm = 2
while confirm == 2:
    print("What is your age? (years)")
    while True:
        try:
            age = int(input())
            break
        except ValueError:
            print("Please enter a number")
        continue
    print("How tall are you? (feet)")
    while True:
        try:
            height_feet = int(input())
            break
        except ValueError:
            print("Please enter a number")
        continue
    print("How tall are you? (Inches)")
    while True:
        try:
            height_inches = int(input())
            break
        except ValueError:
            print("Please enter a number")
        continue
    print("How much do you weigh? (pounds)")
    while True:
        try:
            weight = int(input())
            break
        except ValueError:
            print("Please enter a number")
        continue
    time.sleep(1)

    print("You are " + str(age) + " years old")
    print(str(height_feet) + " feet and " + str(height_inches) + " inches tall")
    print("You weigh " + str(weight) + " pounds")
    time.sleep(1)

    print("""is this info correct?
    1. Yes
    2. No
    """)
    while True:
        try:
            confirm = int(input())
            break
        except ValueError:
            print("Please enter a number")
        continue
    continue

true_height = (height_feet * 12) + height_inches

print("""Pick a Fruit
1. Apple
2. Orange
3. Banana
4. Watermelon
5. Grape
6. Pineapple""")

while True:
        try:
            fruit = int(input())
            break
        except ValueError:
            print("Please enter a number")
        continue
print("Calculating...")
time.sleep(5)
if fruit == 1:
    apple_height = 4
    apple_weight = float(.33)
    apple_age = 6
    print("You are approximately " + str(true_height/apple_height) + " Apples tall")
    print("You weigh as much as " + str(weight/apple_weight) + " apples")
    print("If an apple tree was planted the day you were born, then under ideal conditions the tree would have produced " + str(age - apple_age) + " harvests")
elif fruit == 2:
    orange_height = 4
    orange_weight = float(.26)
    orange_age = 15
    print("You are approximately " + str(true_height/orange_height) + " Oranges tall")
    print("You weigh as much as " + str(weight/orange_weight) + " oranges")
    print("If an orange tree was planted the day you were born, then under ideal conditions the tree would have produced " + str(age - orange_age) + " harvests")
elif fruit == 3:
    banana_height = 7
    banana_weight = float(.26)
    banana_age = float(.75)
    print("You are approximately " + str(true_height/banana_height) + " Bananas tall")
    print("You weigh as much as " + str(weight/banana_weight) + " bananas")
    print("If a banana tree was planted the day you were born, and then continually replanted then under ideal conditions there would have been" + str(age / banana_age) + " banana trees planted until today")
elif fruit == 4:
    watermelon_height = 16
    watermelon_weight = 20
    watermelon_age = float(.25)
    print("You are approximately " + str(true_height/watermelon_height) + " Watermelons tall")
    print("You weigh as much as " + str(weight/watermelon_weight) + " watermelons")
    print("If a watermelon was planted the day you were born, and then continually replanted under ideal conditions there would have been " + str(age/watermelon_age) + " watermelons planted until today")
elif fruit == 5:
    grape_height = float(.24)
    grape_weight = float(.013)
    grape_age = 3
    print("You are approximately " + str(true_height/grape_height) + " Grapes tall")
    print("You weigh as much as " + str(weight/grape_weight) + " grapes")
    print("If a grape vine was planted the day you were born, then under ideal conditions the vine would have produced " + str(age - grape_age) + " harvests")
elif fruit == 6:
    pineapple_height = 12
    pineapple_weight = 2
    pineapple_age = 2
    print("You are approximately " + str(true_height/pineapple_height) + " Pineapples tall")
    print("You weigh as much as " + str(weight/pineapple_weight) + " pineapples")
    print("If a pineapple plant was planted the day you were born, then continually replanted under ideal conditions there would have been " + str(age / pineapple_age) + " pineapples planted until today")
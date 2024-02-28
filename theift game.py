print("Welcome to the Parking slot!")
print("the parking slot have a costly vehicles.")
print("do you want to have a close look.")
print("don't dare to steel other vehicles.")
print("Do you want to enter the car zone or the bike zone?")

zoneChoice = input("> ")

if(zoneChoice == "car zone"):
  print("You enter the car zone.")
  print("As you walk in, you see a bmw car with fully secired techology.")
  print("You attempt to steal the car, but it produce alarms and inform to police.")
  print("Do you want to steal the car?")

  pitBullChoice = input("> ")

  if(pitBullChoice == "yes"):
    print("You are arrested.")
  elif(pitBullChoice == "no"):
    print("You decide to not steal the car.")
    print("You turn around and leave the paarking slot.")
  else:
    print("Invalid choice. Please enter yes or no.")
elif(zoneChoice == "bike zone"):
  print("You chose to go into the bike zone.")
  print("As you walk in, you see a rx 100.")
  print("you are under cctv surveillance")
  print("Do you want to have a steel the  bike?")

  vaseChoice = input("> ")

  if(vaseChoice == "yes"):
    print("you got arrested by police")
  elif(vaseChoice == "no"):
    print("You decide not to steal the bike.")
    print("You have exited from parking slot.")
  else:
    print("Invalid choice. Please enter yes or no.")
else:
  print("Invalid choice. Please enter car zone or bike zone.")

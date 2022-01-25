print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 11:
  print("You are old enough to play!")

  wants_to_play = input("Do you want to play? (Y/N) ")
  if wants_to_play == "Y":
    print("You are starting with", health, "health.")
    print("Let's play!")

    left_or_right = input("Where to go captain? Left or Right? (L/R) ")
    if left_or_right == "L":
      ans = input("Nice, you turn left and reach a river.. Do you swim across or go around? (across/around) ")

      if ans == "around":
          print("You went around and reached the other side of the river")
      elif ans == "across":
          print("You managed to get across, but you were bit by a piranha and lost 5 health.")
          health -=5

      ans = input("You notice a mansion and a river. Where ya going to? (river/mansion) ")
      if ans == "mansion":
          print("You go to the mansion and are greeted by the owner...ELON MUSK (OMH OMH OMH) you don't own 5 quatrillion DOGE and he uses his fire launcher on you... you lose 5 health....")
          health -= 5

          if health <= 0:
              print("You now have 0 health and you lose the game...")
          else:
              print("You have survived... You win!")

      else:
          print("You fell into the river and lost...!")


    else:
      print("Wrong answer! You fell down a hole and died, poor you...")

  else:
    print("Then why even bother writing this code...? Bye!")
else:
  print("You are not old enough to play...")
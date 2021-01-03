#(Easy)

team_1 = ["Mia", "Lisa", "Liam"]
team_2 = ["James", "Ty", "Ava"]

size_1 = len(team_1)
size_2 = len(team_2)

if size_1 != size_2:
  print("Teams must have the same size!")
else:
  print("Game on!")

if size_1 == 3:
  print("Rounds left: 3")
elif size_1 == 2:
  print("Rounds left: 2")
else:
  print("Final round!")

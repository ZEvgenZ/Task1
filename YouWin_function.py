from random import randrange

def game(n,m):
  random_number = randrange(n, m)
  guesses_left = 3
  while guesses_left > 0:
    print("Guess a number between %d-%d!" % (n, m))
    guess = int(input("Enter a guess:"))
    guesses_left -= 1
    if guess == random_number:
      print("You Win!")
      break
  else:
    print("Try again!")

game(1,8)


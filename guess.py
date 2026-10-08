#guess the umber between 1 to 10 using anay funtion
import random


def guess_number():
	secret_number = random.randint(1, 10)
	print("Guess the number from 1 to 10!")

	while True:
		try:
			guess = int(input("Your guess: "))
		except ValueError:
			print("Please enter a whole number.")
			continue

		if not 1 <= guess <= 10:
			print("Choose a number between 1 and 10.")
		elif guess < secret_number:
			print("Too low. Try again.")
		elif guess > secret_number:
			print("Too high. Try again.")
		else:
			print("Correct! You guessed it.")
			return


if __name__ == "__main__":
	guess_number()

import random

true = 1


def main():
    while 1:
        dice_rolls = int(input("How many dice we rollin'?\n"))
        dice_size = int(input("How many sides this puppy got?\n"))
        dice_sum = 0

        for i in range(0, dice_rolls):
            roll = random.randint(1, dice_size)
            dice_sum += roll
            print(f"You rolled a {roll}")
        print(f"You rolled a total of {dice_sum}")

        if dice_sum == dice_rolls:
            print(f"Wow you fucking suck, damn!")
        elif (dice_rolls) < dice_sum < (dice_rolls * dice_size):
            print(f"Ok, okay, {dice_sum}, still alive...")
        elif dice_sum == (dice_rolls * dice_size):  # could just do "else" instead of this whole line, figured I'd be specific just for the variable practice
            print(f"Fucking  YES MOTHERFUCKER, {dice_sum}, thats what Im TALKINABOUT BABY, WOOOOOOO!!!!")

        if input("Roll again?") == "No":
            break
        else:
            continue


if __name__ == "__main__":
    main()

#why doesn't this work

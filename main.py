import random

options = ("rock", "paper", "scissors")

winning_conditions = {"rock" : "scissors",
                      "paper" : "rock",
                      "scissors" : "paper"}

player_points = 0
computer_points = 0

is_playing = True
while is_playing:
    computer = random.choice(options)

    while True:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        if player in options:
            break
        else:
            print("Wrong input. Enter a valid choice.")

    print(f"Player:   {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It' s a tie!")
    elif winning_conditions[player] == computer:
        print("You win!")
        player_points += 1
    else:
        print("You lose!")
        computer_points += 1

    print(f"Player   points: {player_points}")
    print(f"Computer points: {computer_points}")

    if not input("Play again? (y/n): ").lower() == 'y':
        is_playing = False

    print("-" * 55)

print("Final Score:")
print(f"Player   points: {player_points}")
print(f"Computer points: {computer_points}")

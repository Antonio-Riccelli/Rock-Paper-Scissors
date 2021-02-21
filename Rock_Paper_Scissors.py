import random
import sys

player_1_list = ["Rock", "Paper", "Scissors"]
computer_list = ["Rock", "Paper", "Scissors"]


def intro():
    print("Welcome to this game of Rock, Paper, Scissors!\n\n"
          "You will be playing a match consisting of four rounds "
          "against the machine. You can play as many matches as you like.\n"
          )


def outro():
    print("\n'Then why you wasting my time? Get the hell outta here!!!'\n\n"
          "Suddenly, you are grabbed by two heavily-armed guards who "
          "knock you out and take you away. When you wake up, you "
          "find yourself in a cold jail cell, where you will "
          "probably spend the rest of your days.\n\n"
          "A cockroach waves at you and tries to "
          "engage in conversation.\n\n"
          "You really should have just played...\n")


def get_player_choice():
    player_choice = input().strip()
    player_choice = player_choice.lower().capitalize()
    player_choice = player_1_list[player_1_list.index(player_choice)]
    return player_choice


def get_computer_choice():
    computer_choice = random.choice(computer_list)
    return computer_choice


def score(player_choice, computer_choice,
          player_win_counter, computer_win_counter):
    outcome = ""
    if player_choice == computer_choice:
        outcome = "IT'S A TIE"
    elif player_choice == "Rock" and computer_choice == "Scissors":
        outcome = "YOU WIN"
        player_win_counter = player_win_counter + 1
    elif player_choice == "Papers" and computer_choice == "Rock":
        outcome = "YOU WIN"
        player_win_counter = player_win_counter + 1
    elif player_choice == "Scissors" and computer_choice == "Paper":
        outcome = "YOU WIN"
        player_win_counter = player_win_counter + 1
    else:
        outcome = "YOU LOSE"
        computer_win_counter = computer_win_counter + 1
    print(f"\nPlayer: {player_choice} ||| Computer: {computer_choice}\n"
          f"{outcome}\n"
          f"Player wins: {player_win_counter}\n"
          f"Computer wins: {computer_win_counter}\n")
    return [player_win_counter, computer_win_counter]


def round(player_win_counter, computer_win_counter):
    print("Rock Paper Scissors, go!\n"
          "You pick: ")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    match_score = score(player_choice, computer_choice,
                        player_win_counter, computer_win_counter)
    return match_score


def main():
    player_win_counter = 0
    computer_win_counter = 0
    intro()
    ready_or_not = input("Are you ready to play? Y or N\n").strip()
    while ready_or_not != "y" and ready_or_not != "n":
        ready_or_not = input("Not a valid choice. Please choose Y or N.\n"
                             ).strip()
    if ready_or_not == "n":
        outro()
        restart = input("Enter 'r' if you'd like to restart or "
                        "any other key close the program.\n").strip()
        if restart != 'r':
            sys.exit()
        else:
            main()
    match_counter = 0
    while match_counter < 4:
        wins = round(player_win_counter, computer_win_counter)
        player_win_counter = wins[0]
        computer_win_counter = wins[1]
        match_counter += 1
    print("\nGame's over!\n")
    if player_win_counter > computer_win_counter:
        print("YOU WON!\n"
              "Your comment: 'YO, ADRIAN!'\n"
              "Computer's comment: 'The horror, the horror...'\n")
    elif player_win_counter < computer_win_counter:
        print("COMPUTER WON!\n"
              "Computer's comment: 'I am your father!'\n"
              "Player's comment: 'Nooooooooooooooooo'\n")
    else:
        print("IT'S A TIE!\n"
              "Player's comment: 'The Dude abides.'\n"
              "Computer's comment: 'I'll be back.'\n")
    restart = input("Enter 'r' if you'd like to restart or "
                    "any other key close the program.\n").strip()
    if restart != 'r':
        sys.exit()
    else:
        main()


if __name__ == "__main__":
    main()

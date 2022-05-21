import random


while True:
    player_choice = input("""
        Choose your option:
        1 - rock
        2 - paper
        3 - scissors
    """)
    ai_list = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(ai_list)
    print(f"\nYou chose {player_choice}.\n")

    
    if player_choice == computer_choice:
        print(f"Both picked {player_choice}. It's a tie.")
    
    elif computer_choice == 'rock':
        if player_choice == 'scissors':
            print(f"Computer's choice: {computer_choice}. You Lose.")
        elif player_choice == 'paper':
            print(f"Computer's choice: {computer_choice}. You Win!")
    
    elif computer_choice == 'scissors':
        if player_choice == 'rock':
            print(f"Computer's choice: {computer_choice}. You Win!")
        elif player_choice == 'paper':
            print(f"Computer's choice: {computer_choice}. You Lose.")
    
    elif computer_choice == 'paper':
        if player_choice == 'rock':
            print(f"Computer's choice: {computer_choice}. You Lose.")
        elif player_choice == 'scissors':
            print(f"Computer's choice: {computer_choice}. You Win!")


    play_again = input('Play again? (y/n):')
    if play_again.lower() != 'y':
        break
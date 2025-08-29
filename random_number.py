import random;

machine_num = random.randrange(0, 11);

user_wants = input("Do you want to play a number choice game? (Yes/No): ")

if user_wants.lower() != 'yes':
    quit()

how_many_games =  input("How many games you want to play? ");

game_played = 0

while game_played<int(how_many_games):
    user_num = input("Choose a number between 0 to 10: ");
    game_played += 1;
    if int(user_num) == machine_num:
        print("Correct answer")
    else :
        print(f"Wrong ans, Your choice is {user_num} while machine choice is {machine_num}")



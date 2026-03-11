import random

user_bank = [] #holds their stashed money
current_player = 0 #which player is currently playing
dice = 6 #sides on the dice
dice_penalty = 1 #depending on dice type, penalty is bigger making it so rolling multiple times becomes more important.
rounds = 0 #increases roll points by the round number, so rolling multiple times becomes more profitable, especially with the dice penalty on larger dice.
next_player = False #decides when it is next turn
end_score = 25
game_end = False

def roll(dice): #rolls the dice
    roll = random.randint(1, dice)
    if roll == 1 or roll == 6 or roll == 12 or roll == 20: #values that will result in losing everything in the wallet. Set like this for D4, D6, D12, D20.
        result = 0 #loss
        return result
    else:
        result = roll + rounds - dice_penalty #safe
        return result

def setdice(choice):
    if choice == 4:
        return 4
    elif choice == 6:
        return 6
    elif choice == 12:
        return 12
    elif choice == 20:
        return 20
    else:
        print("invalid dice. Choose 4, 6, 12 or 20.")

def totalcalc(wallet, bank):
    total = wallet + bank
    return total
        
def roundloop(playernum):
    currentplayer += 1
    if playernum == player_count:
        currentplayer = 0


#setup
player_count = int(input("How many players: "))
for players in player_count:
    user_bank.append(0)

#game
while game_end == False:
    wallet = 0
    choice = input(f"Currently you have {wallet} in your wallet and {user_bank[current_player]} in your stash. \nDo you want to roll or stash? ")

    if choice == "roll":
        result = roll(dice)
        if result == 0: #loss
            if wallet > 0: #reset bank and next person
                next_player = True
                wallet = 0
                print('You lost all your money!')
            else:print("You would have lost your money and your turn would have ended, but you have no money in your wallet so you are safe!")
                #in case first roll was a 'lose' number
        else: #safe 
            wallet += result
            rounds += 1
            print(f"You got {result} money!")

    elif choice == "stash":
        if wallet == 0: #prevent skipping own round
            print("You have no poi nts in your wallet!")
        else:
            user_bank[current_player] += wallet
            next_player = True
            wallet = 0
            print("Stashed successfully!")

    else:print("invalid.")

    if wallet + user_bank[current_player] >= 25:
        print(f"{current_player} is the winner!")

    if next_player == True:
        print(f"Player {current_player} is next!")
        rounds = 0
        next_player = False

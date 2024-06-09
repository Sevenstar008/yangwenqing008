import numpy as np
def gesture():
    gesture_post = ['3', '2', '1']
    i = np.random.randint(3)
    player_gesture = int(gesture_post[i])
    if player_gesture == 3:
        print('Rock')
    elif player_gesture == 2:
        print('Scissors')
    else:
        print('Paper')
    return player_gesture


def lose_win(player1, player2):
    result = abs(player1 - player2)
    if result == 1:
        if player1 > player2:
            print('Congratulations! player1, you won!')
        else:
            print('Congratulations! player2, you won!')
    elif result == 2:
        if player1 > player2:
            print('Congratulations! player2, you won!')
        else:
            print('Congratulations! player1, you won!')
    else:
        print('You are equal, please try again!')


print("Player 1's turn:")
player1 = gesture()
print(" ")
print("Player 2's turn:")
player2 = gesture()
print(" ")
lose_win(player1, player2)
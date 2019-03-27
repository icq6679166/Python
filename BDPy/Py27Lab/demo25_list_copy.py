from copy import copy, deepcopy

leftHand = ['A', 'K', 'Q']
rightHand = ['J', '10', '9']
player1 = [leftHand, rightHand]
player2 = player1
player3 = copy(player1)
player4 = deepcopy(player1)
print player1, player2, player3, player4
player1.append('JOKER')
print 'stage1', player1, player2, player3, player4
leftHand[0] = '8'
print 'stage2', player1, player2, player3, player4

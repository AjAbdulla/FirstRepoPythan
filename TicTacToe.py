Tic_Tac_Toe_List = ["1","2","3","4","5","6","7","8","9"]

turn = 0 
while turn < 9:
    print(Tic_Tac_Toe_List[0] + '|'+ Tic_Tac_Toe_List[1] + '|' + Tic_Tac_Toe_List[2] + '|' )
    print('-------------')
    print(Tic_Tac_Toe_List[3] + '|'+ Tic_Tac_Toe_List[4] + '|' + Tic_Tac_Toe_List[5] + '|' )
    print('-------------')
    print(Tic_Tac_Toe_List[6] + '|'+ Tic_Tac_Toe_List[7] + '|' + Tic_Tac_Toe_List[8] + '|' )
    print('-------------')

    userTurn = input ('enter a number between 0-8 to mark index position for your turn')
    NumCoventer = int(userTurn)
    print('_____________')
    Tic_Tac_Toe_List.insert(NumCoventer, 'X')

turn+= 1
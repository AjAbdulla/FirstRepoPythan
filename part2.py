 Walt_Lee_Mour_List = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]




turn = 0
while turn < 9:
     print( Walt_Lee_Mour_List[0] + '|' + Walt_Lee_Mour_List[1] + '|' + Walt_Lee_Mour_List[2])
    print('-------')
    print( Walt_Lee_Mour_List[3] + '|' + Walt_Lee_Mour_List[4] + '|' + Walt_Lee_Mour_List[5])
    print('-------')
    print( Walt_Lee_Mour_List[6] + '|' + Walt_Lee_Mour_List[7] + '|' + Walt_Lee_Mour_List[8])
   
    userturn = input("Enter a number Between 0-8 to Mark the index postition for your Turn")
    numconverter = int(userturn)

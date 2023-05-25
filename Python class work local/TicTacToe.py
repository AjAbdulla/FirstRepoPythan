Walt_Lee_Mour_List = ["11", "12", "13", "14", "15", "16", "17", "18", "19"]


turn = 0
while turn < 19:
    print( Walt_Lee_Mour_List[10] + '|' + Walt_Lee_Mour_List[11] + '|' + Walt_Lee_Mour_List[12])
    print('-------')
    print( Walt_Lee_Mour_List[13] + '|' + Walt_Lee_Mour_List[14] + '|' + Walt_Lee_Mour_List[15])
    print('-------')
    print( Walt_Lee_Mour_List[16] + '|' + Walt_Lee_Mour_List[17] + '|' + Walt_Lee_Mour_List[18])
   
    userturn = input("Enter a number Between 10-18 to Mark the index postition for your Turn")
    numconverter = int(userturn)




    Walt_Lee_Mour_List.insert(numconverter, 'X')
    turn += 1

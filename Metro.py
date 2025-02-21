
#! Make a Metrorail  Tec. of Bangladesh

station = int(input("Enter Station Number 0-15 :  "))

if(station==0):
    print("Your Journey Has Just Begun,  Good Luck ! ")

elif(station==1):
    print("Right Now You Are in TSC & The  Next Station is DU ")

elif(station==2):
    print("Right Now You Are in DU & The  Next Station is Montronaloy ")

elif(station==3):
    print("Right Now You Are in Montronaloy & The  Next Station is Shabag ")

elif(station==4):
    print("Right Now You Are in Shabag & The  Next Station is KarwanBazar ")
elif(station==5):
    print("Right Now You Are in KarwanBazar & The  Next Station is Farmghate ")

elif(station==6):
    print("Right Now You Are in Farmghate & The  Next Station is BijoySarani ")

elif(station==7):
    print("Right Now You Are in BijoySarani & The  Next Station is Agargone ")

elif(station==8):
    print("Right Now You Are in Agargone & The  Next Station is KaziPara ")

elif(station==9):
    print("Right Now You Are in KaziPara & The  Next Station is ShewraPara ")

elif(station==10):
    print("Right Now You Are in ShewraPara & The  Next Station is Mirpur 10 ")

elif(station==11):
    print("Right Now You Are in Mirpur 10 & The  Next Station is Mirpur 11 ")

elif(station==12):
    print("Right Now You Are in Mirpur 11 & The  Next Station is Pollobi ")

elif(station==13):
    print("Right Now You Are in Pollobi & The  Next Station is Uttora South ")

elif(station==14):
    print("Right Now You Are in Uttora South & The  Next Station is Uttora Center ")

elif(station==15):
    print("Right Now You Are in Uttora Center & The  Next Station is Uttora North ")

else:
    print(" Station Dose'nt Exsist")

gate= station

if(gate == 9):
    print("The Door Will Open From The Right Please Maintain The Gap")
else:
    print("The Door Will Open From The Left Please Maintain The Gap")

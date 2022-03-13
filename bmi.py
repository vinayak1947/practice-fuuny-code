weight = float(input("enter your weight"))
Hight = float(input("enter your Hight"))

BMI = (weight/(Hight*Hight)*10000)
print("your BMI is: ",BMI)

if(BMI>0):
    if(BMI<=16):
        print("You are very underweight must eat alot lah what are you poor ah")
    elif(BMI<=18.5):
        print("You are underweight eat alot lah")
    elif(BMI<=25):
        print("Congrats! You are Healthy")
    elif(BMI<=30):
        print("You are overweight go take your ass to gym and eat healthy")
    else: 
        print("You are very overweight please stop eating and move your ass a bit")
else:
    print("enter valid details")
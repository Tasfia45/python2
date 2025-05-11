x=str(input("Do you have any medical cause? Yes or No: "))
y=int(input("Enter your attendence percentage:"))

x=x.lower()

if x=="yes":
    if y>=60:
        print("You are eligible for exam..")
    else:
        print("You are  not eligible for exam..")
elif x=="no":
    if y>=75:
          print("You are eligible for exam..")
    else:
        print("You are  not eligible for exam..")
        
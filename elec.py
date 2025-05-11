uni=int(input("Enter your consumed unit:"))

if uni<=100:
    b=uni*1.5
elif uni<=200:
    b=(100*1.5)+(uni-100)*2.5
elif uni<=300:
    b=(100*1.5)+ (100*2.5)+(uni-100)*4.0
else:
    b=(100*1.5)+(100*2.5)+(100*4)+(uni-300)*6.0
    
    print("Your electricity bill is: ",b)
    
    
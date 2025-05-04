s=float(input("Enter your selling price:"))
b=float(input("Enter your buying price:"))
if s>b:
    p=s-b
    print(f"Ypu made a profit of: {p} Taka")
elif s==b:
    print("No profit!No loss!")
    
else :
     l=b-s
     print(f"Ypu made a loss of: {l} Taka")
x=int(input("Enter the amount:"))
note1000= x//1000
print("1000Taka Note: ",note1000)
x%=1000


note500= x//500
print("500Taka Note: ",note500)
x%=500


note200= x//200
print("200Taka Note: ",note200)
x%=200


note100= x//100
print("100Taka Note: ",note100)
x%=100


note50= x//50
print("50Taka Note: ",note50)
x%=50


note20= x//20
print("20Taka Note: ",note20)
x%=20



note10= x//10
print("10Taka Note: ",note10)
x%=10


note5= x//5
print("5Taka Note: ",note5)
x%=5


note2= x//2
print("2Taka Note: ",note2)
x%=2

print("1Taka Coin:",x)
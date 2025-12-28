num = int(input("Enetr the Number : "))
rev =0
while num >0:
    digit = num%10
    rev= rev*10+ digit
    num//=10
    print("Reverse=",rev)


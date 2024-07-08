print("Welcome to tip calculator")
n= float(input("how much is the bill ?: $ "))
m= int(input("what percentage of the bill do you want to tip?: 10, 12, 15 or : "))
t=int(input("how many people do you wanna split bill with?: "))
if m==10:
    each=(((n*10)/100)+n)/t
    print(f"Each percon should  pay {each}")
elif m==12:
    each=(((n*12)/100)+n)/t
    print(f"Each percon should  pay {each}")
elif m==15:
    each=(((n*12)/100)+n)/t
    print(f"Each percon should  pay {each}")
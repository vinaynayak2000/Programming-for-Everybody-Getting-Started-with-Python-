hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter rate per hour:")
r=float(rate)
pay=0
if h <= 40 :
    pay=h*r
elif h > 40 :
    pay=40*r+(h-40)*1.5*r
print(float(pay))
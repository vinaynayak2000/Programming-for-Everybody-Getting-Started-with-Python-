def computepay(h,r):
    p=0.0
    if h <= 40 :
        p=h*r
    if h > 40 :
        p=40*r+(h-40)*1.5*r
    return p
    

hrs =float( input("Enter Hours:"))
rate=float(input("Enter rate per hour:"))
p = computepay(hrs,rate)
print("Pay",p)
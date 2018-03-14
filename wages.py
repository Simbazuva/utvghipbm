h=input("Enter hours: ")
r=input("Enter the rate per hour: ")
c = 1.5
if h>=40:
    g = h*r*c
else:
    g=h*r
print ('The payment is: $'),g

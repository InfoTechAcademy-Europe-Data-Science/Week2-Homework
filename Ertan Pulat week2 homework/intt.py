a = int(input("Enter number1:"))
b = int(input("Enter number2:"))
c = list(range(1,(a+1)))
if b>a:
    c= c[len(c)-b:len(c)]+c[0:len(c)-b]
    print(c)
else:
    c = (c[-b:len(c)]+c[0:(-b)])
    print(c)

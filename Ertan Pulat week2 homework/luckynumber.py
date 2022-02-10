luckynumber = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22}
for x in range(29):
    if x %2==0:
        luckynumber.discard(x)
        print(luckynumber)
    elif x %3==0:
        luckynumber.discard(x)
        print(luckynumber)
    elif x %4==0:
        luckynumber.discard(x)
        print(luckynumber)
    elif x %5==0:
        luckynumber.discard(x)
        print(luckynumber)
    
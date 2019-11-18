#This program takes an array whith numbers 0 to n and finds the missing numbers
b = [0,1,2,3,4,5,6,8]

def ftmn(a):
    n = len(a)
    sos = (n*(n+1))/2
    sos1 = sum(a)
    print ("The missing number is : " + str(sos-sos1))

ftmn(b)

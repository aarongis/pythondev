import sys
import math
from decimal import *

def bbp(n):
    pi=Decimal(0)
    k=0
    while k < n:
        pi+=(Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k+=1
    return pi

def bellard(n):
    pi=Decimal(0)
    k=0
    while k < n:
        pi+=(Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1)+Decimal(1)/(10*k+9)-Decimal(64)/(10*k+3)-Decimal(32)/(4*k+1)-Decimal(4)/(10*k+5)-Decimal(4)/(10*k+7)-Decimal(1)/(4*k+3))
        k+=1
        pi=pi*1/(2**6)
    return pi

def chudnovsky(n):
    pi=Decimal(0)
    k=0
    while k < n:
        pi+=(Decimal(-1)**k)*(Decimal(math.factorial(6*k))/((math.factorial(k)**3)*(math.factorial(3*k)))*(13591409+545140134*k)/(640320**(3*k)))
        k+=1
    pi=pi*Decimal(10005).sqrt()/4270934400
    pi=pi**(-1)
    return pi

def main(argv):
    if len(argv) !=2:
        sys.exit('Usage: BaileyBorweinPlouffe.py <prec> <n>')
    getcontext().prec=(int(sys.argv[1]))
    my_pi=chudnovsky(int(sys.argv[2]))
    accuracy=100*(Decimal(math.pi)-my_pi)/my_pi
    print("Pi is approximately "+str(my_pi))
    print("Accuracy with math.pi: "+str(accuracy))

if __name__=="__main__":

    main(sys.argv[1:])

from employee import *
basic=float(input("enter basic salary: "))
gross=basic+da(basic)+hra(basic)
print("Your gross salary :{:10.2f}".format(gross))
net=gross-pf(basic)-itax(gross)
print("Your net salary : {:10.2f}".format(net))
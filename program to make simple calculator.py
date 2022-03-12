print(" CHOOSE ONE OF THE OPERATORS")
A=print("A. Addition ")
B=print("B. Subtraction ")
C=print("C. Multiplication ")
D=print("D. Division ")
 
a=str(input("CHOOSE(A/B/C/D):"))
x=float(input("ENTER FIRST NUMBER:"))
y=float(input("ENTER SECOND NUMBER:"))

if a ==' A':
    d=x+y
    print("YOUR ANSWER :",d)
    
elif a =='B':
    c=x-y
    print("YOUR ANSWER :",c)

elif a=='C':
    e=x*y
    print("YOUR ANSWER :",e)
    
elif a=='D' :
    f=x/y
    print("YOUR ANSWER :",f)
    
else:
    print("INVALID")

   
    




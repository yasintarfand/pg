def zarb ():
    x=eval(input('enter number 1'))
    y=eval(input('enter number 2'))
    print(x,'*',y,'=',x*y)
def taghsim():
    x=eval(input('enter number 1'))
    y=eval(input('enter number 2'))
    if x==0 and y==0:
        print(x,'/',y,'=0')
    else:
        print(x,'/',y,'=',x/y)
def sum1():
    x=eval(input('enter number 1'))
    y=eval(input('enter number 2'))
    print(x,'+',y,'=',x+y)
def tafrigh():
    x=eval(input('enter number 1'))
    y=eval(input('enter number 2'))

z = input("enter mark exit (e)")

while (z!="e"):
    if z=='+' :
        sum1()
    elif z=='-' :
        tafrigh()
    elif z=='*':
        zarb()
    elif z=='/':
        taghsim()
    else:
        print ("eshtabah")
        z = input("enter mark exit (e)")
   

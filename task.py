# 1.Write a Python program to find the sum and product of given two numbers.

a=int(input('enter a'))
b=int(input('enter b'))
print('Sum =',a+b,'Product =',a*b)



# 2. Write a Python program to convert temperature in F to C.
# C = 5/9(F - 32)

import math
x,y,z=int(input('enter x')),int(input('enter y')),int(input('enter z'))
s =x+y+z/2
area =math.sqrt(s*(s-x)*(s-y)*(s-z))
print('s =',s,'area =',area)

# 3. Write a Python program to find area of trianlge
# area = sqrt(s (s-a)(s-b)*(s-c))
# where s = a+b+c /2


f=int(input('enter f'))
c=5/9*(f-32)
print('c=',c)


# 4.Write a python program to display the ASCII value of a given character.

char = input("Enter a character: ") 
print("The ASCII value of", char, "is", ord(char))

# 5. Write a python program to prepare the electricity bill for consumers.
# previous , current month reading. service number, units consumed & electricity charges.
# Take charges 1.50 per unit






# 6. Write a Python program to swap (exchange) values of two variables. A and B.

a=int(input('enter a'))
b=int(input('enter b'))
a,b=b,a
print('After swapping: a =',a,'b =',b)  

# 7. Write a python program to find the sum and average of given three numbers.

x,y,z=int(input('enter x')),int(input('enter y')),int(input('enter z'))
print('x =',x,'y =',y,'z =',z,'Sum =',x+y+z, 'Average =',(x+y+z)/3)

# 8. Write a python program to find the area & circumference of circle of radius r.
# area = pie * r * r circumference = 2*pie*r;

import math
r=int(input('enter radius'))
area=math.pi*r*r
circumference=2*math.pi*r   
print('Area =',area,'Circumference =',circumference)
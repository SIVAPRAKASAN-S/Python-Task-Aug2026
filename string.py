# str1="sivaprakasan S"
# print(str1[:12])

# str1="sivaprakasan S"
# print(str1[2:12])

# str1="sivaprakasan S"
# print(str1[6:])


# string concatenation

# str1="sivaprakasan S"
# str2=" is a good boy"
# str3=str1+str2
# print(str3)


# string append
# str1="sivaprakasan S"
# str1 +=" is a good boy"  
# print(str1) 

# string repitation
# str1="sivaprakasan S"
# str2=str1*6
# print(str2)

# # string slicing
# str1="welcome to python"
# print(str1[11 : 17 : 2])
# print(str1[11 : 17])
# print(str1[: : 4]) 
# print(str1[::-4])  


# print(str1[6:7:2])
# print(str1[0:11:3])
# print(str1[::4])
# print(str1[::-1])

# for loop 

# str="python programming"
# index=0
# for i in str:
#     print(str[:index])
#     index += 1


# formatting string

# name = 'siva'
# marks = 90
# print('name:%s marks:%d' % (name, marks))
# print('my name is {} and my marks is {}'.format(name, marks))
# print(f'name: {name} and marks :{marks}')

 
# str='COMPUTER SCIENCE'
# print(str*2) 
# print(str[0 : 7])


# str1="sivaprakasanS"
# print(str1.isalnum())

# str1="sivaprakasanS1234"
# print(str1.isalpha())

# str="python programming"
# print(str.islower())

# str="PYTHON PROGRAMMING"
# print(str.isupper())

# str="python programming"
# print(str.swapcase())

# str="python programming"
# print(str.title())

# str="python programming"
# print(str.upper())


# str1="sivaprakasanS"
# print(str1.count("a",0,12))

# print(ord('A'))


# print(chr(65))

# str1=int (input('enter a number :'))
# str2=''
# index=-1
# for i in range(str1):
#     str2 += str[index]
#     index-=1
#     print('this is string :',str2)



str1=input('enter a string:')
str2='aAeEiIoOuU'
v,c=0,0
for i in str2:
    if i in str1:
        v+=1
    else:
        c+=1
    print('vowels:',v)
    print('consonants:',c)

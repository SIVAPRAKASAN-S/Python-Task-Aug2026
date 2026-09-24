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
# #     index-=1
# #     print('this is string :',str2)



# str1=input('enter a string:')
# str2='aAeEiIoOuU'
# v,c=0,0
# for i in str2:
#     if i in str1:
#         v+=1
#     else:
#         c+=1
#     print('vowels:',v)
#     print('consonants:',c)



# mirror image of te string

# str1=input('enter a string:')

# mirror=str1[::-1]
# print('mirror image of the string:',mirror)

# 3.Write a program to remove all the occurences of a given 
# character in a string.


# str1=input('enter a string:')
# ch=input('enter a character to remove:')
# str2=str1.replace(ch,'')
# print('string after removing all occurrences of',ch,':',str2)


# 1. Write a porgram to count the occurances of each word
# in a given string.

# str1=input('enter any string')
# count=0
# result=str1.split()
# print(result)
# for word in result:
#     count+=1
# print('no.of word in given:',count)




# # Python String Programs - All in One

# # Input a string
# s = input("Enter a string: ")

# # 1. Print the string
# print("\n1. Original String:")
# print(s)

# # 2. Find length
# print("\n2. Length of String:")
# print(len(s))

# # 3. Count vowels
# vowels = 0

# for ch in s:
#     if ch in "aeiouAEIOU":
#         vowels += 1

# print("\n3. Number of Vowels:")
# print(vowels)

# # 4. Count consonants
# consonants = 0

# for ch in s:
#     if ch.isalpha() and ch not in "aeiouAEIOU":
#         consonants += 1

# print("\n4. Number of Consonants:")
# print(consonants)

# # 5. Count uppercase and lowercase
# uppercase = 0
# lowercase = 0

# for ch in s:
#     if ch.isupper():
#         uppercase += 1
#     elif ch.islower():
#         lowercase += 1

# print("\n5. Uppercase Letters:")
# print(uppercase)

# print("Lowercase Letters:")
# print(lowercase)

# # 6. Count digits
# digits = 0

# for ch in s:
#     if ch.isdigit():
#         digits += 1

# print("\n6. Number of Digits:")
# print(digits)

# # 7. Count spaces
# spaces = 0

# for ch in s:
#     if ch == " ":
#         spaces += 1

# print("\n7. Number of Spaces:")
# print(spaces)

# # 8. Reverse the string
# reverse = s[::-1]

# print("\n8. Reverse of String:")
# print(reverse)

# # 9. Check palindrome
# print("\n9. Palindrome Check:")

# if s == reverse:
#     print("The string is a Palindrome")
# else:
#     print("The string is Not a Palindrome")

# # 10. Convert to uppercase and lowercase
# print("\n10. Uppercase and Lowercase:")

# print("Uppercase:", s.upper())
# print("Lowercase:", s.lower())


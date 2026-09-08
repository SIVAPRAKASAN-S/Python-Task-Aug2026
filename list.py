# string = input("Enter a string: ")
# element = input("Enter the character to count: ")

# count = 0

# for ch in string:
#     if ch == element:
#         count += 1

# print("The character", element, "occurs", count, "times.")






# string = input("Enter a string: ")
# element = input("Enter the character: ")

# count = string.count(element)

# print("The character occurs", count, "times")




# mylist = [1, 2, 3, 4, 5]
# reverse_list = mylist[::-1]
# print("Original list:",mylist)
# print("Reversed list:",reverse_list)




# lst = [1, 2, 3, 2, 4, 5, 3, 6, 1 ,2,2, 7, 8, 9, 5]

# new_list = []

# for i in lst:
#     if i not in new_list:
#         new_list.append(i)

# print("List after removing duplicates:", new_list)


# lst = [5,20,70,30,102,8,1,3]

# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] > lst[j]:
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp

# print(lst)


# list1 = [1, 2, 3,5,7,8,9,10]
# list2 = [4, 5, 6]

# list1.extend(list2)

# print(list1)
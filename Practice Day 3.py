# # # # print(_doc_)
# # # # print(_doc_)

# # # # s = 'abcdefghijk'
# # # # for letter in s:
# # # #     print(letter)

# # # # # print(ord('A'))
# # # # # s='yash'
# # # # # print(s.center(10))

# # # # # for character in range(ord('A'), ord('Z')+1):
# # # # #     print(chr(character)," : ",character)

# # # # # print(chr(91),chr(92),chr(93),chr(94),chr(95),chr(96))

# # # # # # # Get input from user
# # # # # start_letter = input("Enter the starting letter: ")
# # # # # end_letter = input("Enter the ending letter: ")

# # # # # # Get the ASCII value of the start and end letters
# # # # # start_ascii = ord(start_letter)
# # # # # end_ascii = ord(end_letter)

# # # # # # Loop through the range from start to end letters
# # # # # for i in range(start_ascii, end_ascii + 1):
# # # # #     # For each letter, print the sequence from start to current letter
# # # # #     for j in range(start_ascii, i + 1):
# # # # #         print(chr(j), end=" ")
# # # # #     print()


# # # # # Get input from user
# # # # start_letter = input("Enter the starting letter: ")
# # # # end_letter = input("Enter the ending letter: ")

# # # # # Get the ASCII value of the start and end letters
# # # # start_ascii = ord(start_letter)
# # # # end_ascii = ord(end_letter)

# # # # # Loop through the range from start to end letters
# # # # for i in range(start_ascii, end_ascii + 1):
# # # #     # Construct the line to be printed by joining characters from start to current letter
# # # #     line = " ".join(chr(j) for j in range(start_ascii, i + 1))
# # # #     print(line)

# # # # for x in range(1,5):
# # # #     print("*"*x)


# # # # for x in range(5,0,-1):
# # # #     print("*"*x)


# # # # rows = int(input())
# # # # for i in range(1, rows + 1):
# # # #     print(" " * (rows - i) + "* " * i)


# # # rows = int(input())
# # # for i in range(1, rows*2):
# # #     if i <= rows:
# # #         print(" " * (rows - i) + "* " * (i))
# # #     else:
# # #         print(" " * (i - rows) + "* " * (2*rows - i))


# # user = "python"
# # for i in range(1, len(user)+1):
# #     print(user[0:i])


# # s.center(20, "*")

# # s= 'imagination'
# # s.find('i')
# # print(s.rfind('i'))


# # line = input("Enter Line : ")
# # v =counter = 0

# # for x in 'aeiou':
# #   counter = line.count(x)  # if x in line
# #   v += counter

# # print(line , ' : ', v)


# # input_string = input("Enter a string: ")
# # words_seen = set()
# # repeated_word_found = False

# # for word in input_string.split():
# #     if word in words_seen:
# #         print(f"The first repeated word is: {word}")
# #         repeated_word_found = True
# #         break
# #     else:
# #         words_seen.add(word)

# # if not repeated_word_found:
# #     print("No repeated word found.")


# # s = 'python python python python the the and and and'
# # word_list = s.split()
# # uni_list = set(word_list)

# # max = 0
# # word = ''
# # for words in uni_list:
# #   if word_list.count(words) > max:
# #     max = word_list.count(words)
# #     word = words

# # print("Max Word : ", word, ' count : ', max)

# line = 'way this done is this'

# word_list = line.split()
# word_list = word_list[::-1]
# rline = ''
# for x in word_list:
#     rline = rline + x + ' '
#     print(rline)


# string=input(("Enter a letter:")).upper()  
# if(string==string[::-1]):  
#       print("The letter is a palindrome")  
# else:  
#       print("The letter is not a palindrome")

# def num(num1,num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#     return None    

# print(num(10, 20))

# def sort_ascending(list1):
#     for i in range(len(list1)):
#         for j in range(i + 1, len(list1)):
#             if list1[i] > list1[j]:
#                 list1[i], list1[j] = list1[j], list1[i]

# list1 = [5, 3, 2, 1, 4]
# sort_ascending(list1)
# print(list1) 


# def sort_ascending(il):
#     sorted_list = []
#     while il:
#         minv = il[0]
#         for x in il:
#             if x < minv:
#                 minv = x
#         sorted_list.append(minv)
#         il.remove(minv)
#     return sorted_list

# my_list = [6,8,5,3,2]
# sorted_list = sort_ascending(my_list)
# print(sorted_list)


# def ascending(list):

#   sort = []

#   while list:
#     min_value = min(list)
#     sort.append(min_value)
#     list.remove(min_value)

#   return sort

# print(ascending([1, 0, 20, 10, 100, 0, 9]))


# def find_second_largest(arr):
#     if len(arr) < 2:
#         return "Array should contain at least two elements"
    
#     largest = second_largest = float('-inf')
    
#     for num in arr:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num
            
#     return second_largest

# # Sample Input
# arr = [7, 3, 9, 2, 8]

# # Find the second largest element
# second_largest = find_second_largest(arr)
# print("Second Largest:", second_largest)

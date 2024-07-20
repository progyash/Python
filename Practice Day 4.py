# Remove Duplicates from a List:
# Question: Write a function to remove duplicate elements from a list.

# Logic: Use a loop or convert the list to a set and back to a list.

# Sample Input: [1, 2, 2, 3, 4, 4, 5]

# Expected Output: [1, 2, 3, 4, 5]

# def remove_duplicates(input_list):
#     unique_set = set(input_list)
#     unique_list = list(unique_set)
#     return unique_list
# input_list = [1, 2, 2, 3, 4, 4, 5]
# print(remove_duplicates(input_list))

# Reverse a List:
# Question: Write a function to reverse the order of elements in a list.

# Logic: Use list slicing or a loop to reverse the elements.

# Sample Input: [1, 2, 3, 4, 5]

# Expected Output: [5, 4, 3, 2, 1]

# input_list = [1, 2, 3, 4, 5]
# reversed_list = input_list[::-1]
# print(reversed_list)

# Find Common Elements in Two Lists:
# ○ Question: Write a function to find common elements between two lists.

# ○ Logic: Use list comprehensions or a loop to compare elements.

# ○ Sample Input: [1, 2, 3, 4] and [3, 4, 5, 6]

# ○ Expected Output: [3, 4]

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# common_elements = []
# for element in list1:
#     if element in list2:
#         common_elements.append(element)
# print(common_elements)

# Calculate the Sum of List Elements:
# ○ Question: Write a function to calculate the sum of all elements in a list.

# ○ Logic: Use a loop to iterate through the list and accumulate the sum.

# ○ Sample Input: [1, 2, 3, 4, 5]

# ○ Expected Output: 15

# numbers = [1, 2, 3, 4, 5]
# total=0
# for number in numbers:
#   total += number
# print(total)

# Count Occurrences of an Element in a List:
# ○ Question: Write a function to count how many times a specific element appears in a list.

# ○ Logic: Use a loop to count occurrences.

# ○ Sample Input: [1, 2, 2, 3, 4, 2] and 2

# ○ Expected Output: 3

# input_list = [1, 2, 2, 3, 4, 2]
# element_to_count = 2
# count = 0
# for element in input_list:
#     if element == element_to_count:
#         count += 1
# print(count)

# 11. Generate a List of Prime Numbers:
# ○ Question: Write a function to generate a list of prime numbers within a given range.

# ○ Logic: Use loops and checks to find prime numbers.

# ○ Sample Input: Range: 1 to 20

# ○ Expected Output: List of Prime Numbers: [2, 3, 5, 7, 11, 13, 17, 19]

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def generate_primes(start, end):
#     prime_list = []
#     for num in range(start, end + 1):
#         if is_prime(num):
#             prime_list.append(num)
#     return prime_list
# start = 1
# end = 20
# prime_numbers = generate_primes(start, end)
# print("List of Prime Numbers:", prime_numbers)

# for number in range(2,20):
#     prime, divisor = True, 2

#     while prime and divisor ** 2 <= number:
#         if number % divisor == 0:
#             prime = False
#         divisor += 1
    
#     if (prime):
#         print(number)

# for number in range(2, 20):
#    for k in range(2, number):
#        if (number % k) == 0:
#            break
#    else:
#        print(number)

'''
l1 = [10, 20, 30, 40]
l2 = [90, 80, 80, 70]
Find average l2 list. After finding average of l2, divide every single number of l2 by 2.
if divided number is greater than add by 10 in number, if divided number is lesser than subtract by 10 in number.
after this add that number with l1 numbers.   
Expected Output :
l1 = [55, 70, 70, 105]
l2 = [45, 50, 50, 65]
'''

# # Step 1: Calculate the average of l2
# l2 = [90, 80, 80, 70]
# average_l2 = sum(l2) / len(l2)

# # Step 2 and 3: Divide each number in l2 by 2 and modify based on the comparison with average
# modified_l2 = []
# for num in l2:
#     divided_num = num / 2
#     if divided_num > average_l2:
#         modified_num = divided_num + 10
#     else:
#         modified_num = divided_num - 10
#     modified_l2.append(modified_num)

# # Step 4: Add each resulting number from modified_l2 to the corresponding number in l1
# l1 = [10, 20, 30, 40]
# result_l1 = [l1[i] + modified_l2[i] for i in range(len(l1))]

# # Printing the results
# print("l1 =", result_l1)
# print("l2 =", modified_l2)

# acc_balance = 10

# withdraw = 10000000

# acc_balance > withdraw ---> withdraw
# acc_balance < withdraw --->  Insufficient balance

# def withdraw_amount(acc_balance, withdraw):
#     if acc_balance >= withdraw:
#         remaining_balance = acc_balance - withdraw
#         return withdraw, remaining_balance
#     else:
#         return "Insufficient balance", acc_balance

# acc_balance = 10000000
# withdraw = int(input("Amount : "))

# withdraw_amount, remaining_balance = withdraw_amount(acc_balance, withdraw)
# print("Withdrawal amount:", withdraw_amount)
# print("Remaining balance:", remaining_balance)

'''Find Common Elements in Two Lists:
○ Question: Write a function to find common elements between two lists.
○ Logic: Use list comprehensions or a loop to compare elements.
○ Sample Input: [1, 2, 3, 4] and [3, 4, 5, 6]
○ Expected Output: [3, 4]
output: list of common elements in both
process: element to element comparission(in/not in)------use set
         def intersection(l1,l2)
input: 2 lists
'''

# def intersection(l1, l2):
#     common_elements = []
    
#     for element in l1:
#         if element in l2 and element not in common_elements:
#             common_elements.append(element)
    
#     return common_elements

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# print(intersection(list1, list2))

'''
Compress a String:
○ Question: Write a function to compress a string by replacing
consecutive characters with their counts.
○ Logic: Define a function that uses loops to count consecutive
characters and create the compressed string.
○
'''


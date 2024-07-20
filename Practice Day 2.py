# # # for x in range(int(input("x : ")),int(input("y : ")),int(input("z : "))):
# # #     print(x)


# # # # take 3 inputs from user --> start, condition, steps
# # # # and print number series

# # # start = int(input())
# # # condition = int(input())
# # # steps = int(input())


# # # for x in range(start, condition, steps):
# # #   print(x)


# # # start = int(input("Start : "))
# # # end = int(input("End : "))

# # # if start > end:
# # #   for x in range(start, end, -1):
# # #     print(x)
# # # else:
# # #   for x in range(start, end, 1):
# # #     print(x)


# # # for row in range(1, 5, 1):
# # #   for col in range(1, 5, 1):
# # #     print(col%2, end = ' ')
# # #   print()


# # # start = int(input("Start : "))
# # # end = int(input("End : "))
# # # for row in range(start, end+1, 1):
# # #   for col in range(1, row+1, 1):
# # #     print(col, end = ' ')
# # #   print()


# # # start = int(input("Start : "))
# # # end = int(input("End : "))
# # # for row in range(start, end-1, -1):
# # #   for col in range(1, row+1, 1):
# # #     print(col, end = ' ')
# # #   print()


# # # l = [1, 3, 7, 21, 70, 140, 5]
# # # l5 = []
# # # l7 = []
# # # for x in l:
# # #     if x % 5 == 0:
# # #         l5.append(x)
# # #     if x % 7 == 0:
# # #         l7.append(x)
# # # print(l5)
# # # print(l7)


# # # l = []

# # # while True:
# # #   user = input("Enter Value : ")

# # #   if user == '':
# # #     break
# # #   else:
# # #     l.append(user)

# # # print(l)


# # # l = []
# # # sum = 0
# # # l = []

# # # while True:
# # #   user = input("Enter Value : ")

# # #   if user == '':
# # #     break
# # #   else:
# # #     l.append(int(user))

# # # for num in l:
# # #   sum += num
# # # print(l)
# # # print(sum)


# # # numbers = [1, 2, 3, 4, 5]
# # # result = sum(numbers)
# # # print(result)


# # # l = [1, 2, 3, 'a', 'b', 'c']
# # # l_integer = []
# # # l_alphabets = []
# # # for x in l:
# # #     if type(x) == int:
# # #         l_integer.append(x)
# # #     elif type(x) == str:
# # #         l_alphabets.append(x)
# # # print(l_integer)
# # # print(l_alphabets)


# # # l = [1, 2, 3, 'a', 'b', 'c']
# # # l_integer = []
# # # l_alphabets = []
# # # for x in l:
# # #     if isinstance(x , int):
# # #         l_integer.append(x)
# # #     elif isinstance(x ,str):
# # #         l_alphabets.append(x)
# # # print(l_integer)
# # # print(l_alphabets)


# # # l = [1,2,3,4,5]
# # # n = len(l)
# # # for i in range(n):
# # #    data = sum(l[:i])
# # #    l[i] = l[i] + data
# # #    print(l)
# # # print(l)


# # # l = [1, 2, 5, 10, 40, 30, 20, 15]

# # # avg = sum(l) // len(l)
# # # print(l)
# # # for x in range(len(l)):

# # #   if l[x] > avg:
# # #     l[x] -= 5 
# # #   else:
# # #     l[x] += 10

# # # print(avg)
# # # print(l)


# # # numbers = []

# # # while True:
# # #     user_input = input("Enter a number (or just press Enter to finish): ")
# # #     if user_input == "":
# # #         break
# # #     try:
# # #         number = float(user_input)
# # #         numbers.append(number)
# # #     except ValueError:
# # #         print("Please enter a valid number.")

# # # if numbers:
# # #     max_value = max(numbers)
# # #     min_value = min(numbers)
# # #     average_value = sum(numbers) / len(numbers)
# # #     sorted_list = sorted(numbers)
    
# # #     print(f"Maximum value: {max_value}")
# # #     print(f"Minimum value: {min_value}")
# # #     print(f"Average value: {average_value}")
# # #     print("Sorted list:", sorted_list)
# # # else:
# # #     print("No numbers were entered.")


# # # s = set()

# # # while True:
# # #   data = input("Enter data : ")

# # #   if data == '':
# # #     break
# # #   else:
# # #     s.add(int(data))

# # # print("min value  : ", min(s))
# # # print("max value  : ", max(s))
# # # print("avg : ", sum(s)/ len(s))
# # # print(sorted(s))


# # # counter = 0
# # # check = 10
# # # s = [10, 10, 10, 20]
# # # for num in s:
# # #   if num == check:
# # #     counter += 1
# # # print(check, " = ", counter)


# # s = [10, 10, 10, 20]
# # s.count(10)


# # l = [10, 10, 20, 11, 22, 33, 11, 11, 10, 30]
# # unique_list = set(l)
# # for x in unique_list:
# #     print(x, " : ", l.count(x))


# # l = [10, 10, 20, 11, 22, 33, 11, 11, 10, 30]
# # unique_list = set(l)
# # dict = {}
# # for x in unique_list:
# #   # key  =   value
# #   dict[x] = l.count(x)
# # print(dict)


# # tea = coffee = banmaska = water = 0
# # while True:
# #   # print("1. Tea \t, 2. Coffee \t, 3. Banmaska \t, 4. Water \t, 0. Exit")
# #   user = int(input(" 1. Tea \t 12 \n 2. Coffee \t 25 \n 3. Banmaska \t 20 \n 4. Water \t 20 \n 0. Exit \n"))


# #   if user == 1:
# #     print("Tea selected")
# #     tea += 1
# #   elif user == 2:
# #     print("Coffee selected")
# #     coffee += 1
# #   elif user == 3:
# #     print("Ban Maska")
# #     banmaska += 1
# #   elif user == 4:
# #     print("Water selected")
# #     water += 1
# #   elif user == 0:
# #     print("Thanks for ordering...")
# #     break
# #   else:
# #     print("Bhai jara dekh ke...")

# # total_amount = (tea * 12) + (coffee * 25) + (banmaska * 20) + (water * 20)
# # print("Payble Amount : ", total_amount)


# # Initialize counters for each item
# tea = coffee = banmaska = water = 0

# # Bill number counter
# bill_number = 1

# # Main loop for switching on or off
# while True:
#     machine = input("Press 'Y' for On 'N' for Off: ").strip().upper()
#     if machine == "N":
#         print("Program turned off.")
#         break
#     elif machine == "Y":
#         while True:
#             # Print the menu
#             user = int(input(
#                 " 1. Tea \t 12 \n 2. Coffee \t 25 \n 3. Banmaska \t 20 \n 4. Water \t 20 \n 0. Exit \n"))

#             # Handle user input
#             if user == 1:
#                 quantity = int(input("How many Tea(s) do you want?: "))
#                 print(f"Tea selected: {quantity}")
#                 tea += quantity
#             elif user == 2:
#                 quantity = int(input("How many Coffee(s) do you want?: "))
#                 print(f"Coffee selected: {quantity}")
#                 coffee += quantity
#             elif user == 3:
#                 quantity = int(input("How many Ban Maska(s) do you want?: "))
#                 print(f"Ban Maska selected: {quantity}")
#                 banmaska += quantity
#             elif user == 4:
#                 quantity = int(input("How many Water(s) do you want?: "))
#                 print(f"Water selected: {quantity}")
#                 water += quantity
#             elif user == 0:
#                 print("Thanks for ordering...")
#                 break
#             else:
#                 print("Invalid choice, please select a valid option from the menu.")

#             # Ask if the user wants to continue ordering
#             continue_order = input("Do you want to order more? (Y/N): ").strip().upper()
#             if continue_order == 'N':
#                 print("Finishing order...")
#                 break
        
#         # Calculate the total amount
#         total_amount = (tea * 12) + (coffee * 25) + (banmaska * 20) + (water * 20)

#         # Print the bill
#         print("\n" + "="*30)
#         print(f"Bill Number: {bill_number}")
#         print("="*30)
#         print("Items Ordered:")
#         if tea > 0:
#             print(f"Tea \t\t {tea} x 12 \t= Rs {tea * 12}")
#         if coffee > 0:
#             print(f"Coffee \t\t {coffee} x 25 \t= Rs {coffee * 25}")
#         if banmaska > 0:
#             print(f"Ban Maska \t {banmaska} x 20 \t= Rs {banmaska * 20}")
#         if water > 0:
#             print(f"Water \t\t {water} x 20 \t= Rs {water * 20}")
#         print("="*30)
#         print(f"Total Amount to Pay: \t= Rs {total_amount}")
#         print("="*30)
#         print("Thank you for dining with us!")
#         print("="*30)

#         # Increment the bill number for the next bill
#         bill_number += 1
#     else:
#         print("Invalid choice, please enter 'Y' or 'N'.")

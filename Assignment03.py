
# # 1. DATA TYPES 

# # Q1. Find the data type of every value in a mixed list.

# mixed_list = [10, 20.5, "Python", True, None]

# for item in mixed_list:
#     print(item, type(item))


# # Q2. Convert a nested list into a tuple of tuples.

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# result = tuple(tuple(row) for row in nested_list)

# print(result)


# # Q3. Remove all duplicate values from a mixed list
# # while preserving the original order.

# mixed_list = [10, "apple", 20, "apple", 10, 30]

# unique_list = []

# for item in mixed_list:
#     if item not in unique_list:
#         unique_list.append(item)

# print(unique_list)



# # 2. Operators
# # Q4. Check whether a number is a power of 2 using operators.

# num = int(input("Enter a number: "))

# if num > 0 and (num & (num - 1)) == 0:
#     print("Power of 2")
# else:
#     print("Not a power of 2")


# # Q5. Swap two numbers using bitwise XOR.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Before swapping:", a, b)

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print("After swapping:", a, b)


# # Q6. Find whether a number is divisible by both 4 and 6 using logical operators.

# num = int(input("Enter a number: "))

# if num % 4 == 0 and num % 6 == 0:
#     print("Divisible by both 4 and 6")
# else:
#     print("Not divisible by both")


# # Q7. Calculate the total electricity bill using different unit rates.

# units = float(input("Enter electricity units: "))

# if units < 0:
#     print("Invalid units")
# elif units <= 100:
#     bill = units * 1.5
#     print("Electricity Bill:", bill)
# elif units <= 200:
#     bill = (100 * 1.5) + (units - 100) * 2.5
#     print("Electricity Bill:", bill)
# else:
#     bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4
#     print("Electricity Bill:", bill)



# # 3. Conditional Statements
# # Q8. Check whether three sides can form a triangle.

# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and b+c > a:
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")


# # Q9. Determine the type of triangle (Equilateral, Isosceles, Scalene).

# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a <= 0 or b <= 0 or c <= 0 or a+b <= c or a+c <= b or b+c <= a:
#     print("Invalid Triangle")
# elif a == b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")


# # Q10. Create a simple ATM menu (Withdraw, Deposit, Balance).

# balance = 5000

# while True:
#     print("\n1. Withdraw")
#     print("2. Deposit")
#     print("3. Balance")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         amount = float(input("Enter amount: "))
#         if 0 < amount <= balance:
#             balance -= amount
#             print("Withdrawal Successful")
#         else:
#             print("Invalid amount or insufficient balance")

#     elif choice == 2:
#         amount = float(input("Enter amount: "))
#         if amount > 0:
#             balance += amount
#             print("Deposit Successful")
#         else:
#             print("Invalid amount")

#     elif choice == 3:
#         print("Balance:", balance)

#     elif choice == 4:
#         print("Thank You")
#         break

#     else:
#         print("Invalid Choice")


# # Q11. Calculate income tax based on different tax slabs.

# income = float(input("Enter annual income: "))

# if income < 0:
#     print("Invalid income")
# elif income <= 300000:
#     tax = 0
# elif income <= 700000:
#     tax = (income - 300000) * 0.05
# elif income <= 1000000:
#     tax = 20000 + (income - 700000) * 0.10
# elif income <= 1200000:
#     tax = 50000 + (income - 1000000) * 0.15
# elif income <= 1500000:
#     tax = 80000 + (income - 1200000) * 0.20
# else:
#     tax = 140000 + (income - 1500000) * 0.30

# if income >= 0:
#     print("Income Tax:", tax)


# # Q12. Create a menu-driven calculator using if-elif.

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter choice: "))

# if choice == 1:
#     print("Result:", a + b)
# elif choice == 2:
#     print("Result:", a - b)
# elif choice == 3:
#     print("Result:", a * b)
# elif choice == 4:
#     if b != 0:
#         print("Result:", a / b)
#     else:
#         print("Cannot divide by zero")
# else:
#     print("Invalid Choice")



# # 4. Loops
# # Q13. Print all prime numbers between 1 and n.

# n = int(input("Enter n: "))

# for num in range(2, n + 1):
#     prime = True

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num, end=" ")

# print()


# # Q14. Find the factorial of a number using a loop.

# num = int(input("Enter a number: "))

# fact = 1

# if num < 0:
#     print("Factorial not defined")
# else:
#     for i in range(1, num + 1):
#         fact *= i

#     print("Factorial:", fact)


# # Q15. Print the Fibonacci series up to n terms.

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# print()


# # Q16. Check whether a number is an Armstrong number.

# num = int(input("Enter a number: "))

# if num < 0:
#     print("Not Armstrong Number")
# else:
#     digits = str(num)
#     power = len(digits)
#     total = 0

#     for digit in digits:
#         total += int(digit) ** power

#     if total == num:
#         print("Armstrong Number")
#     else:
#         print("Not Armstrong Number")


# # Q17. Reverse a number and check if it is a palindrome.

# num = int(input("Enter a number: "))

# original = num
# reverse = 0

# if num < 0:
#     print("Enter a positive number")
# else:
#     while num > 0:
#         digit = num % 10
#         reverse = reverse * 10 + digit
#         num = num // 10

#     print("Reverse:", reverse)

#     if original == reverse:
#         print("Palindrome Number")
#     else:
#         print("Not Palindrome")


# # Q18. Find the Greatest Common Divisor (GCD) of two numbers.

# a = abs(int(input("Enter first number: ")))
# b = abs(int(input("Enter second number: ")))

# x = a
# y = b

# while y != 0:
#     x, y = y, x % y

# print("GCD:", x)



# # 5. Functions
# # Q19. Write a function to check if a string is a palindrome.

# def palindrome(text):
#     return text == text[::-1]

# text = input("Enter a string: ")

# if palindrome(text):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # Q20. Write a function to count vowels and consonants in a string.

# def count_vowels_consonants(text):
#     vowels = 0
#     consonants = 0

#     for ch in text.lower():
#         if ch.isalpha():
#             if ch in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1

#     return vowels, consonants

# text = input("Enter a string: ")

# v, c = count_vowels_consonants(text)

# print("Vowels:", v)
# print("Consonants:", c)


# # Q21. Create a function to calculate simple and compound interest.

# def interest(p, r, t):
#     si = (p * r * t) / 100
#     ci = p * (1 + r / 100) ** t - p
#     return si, ci

# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time: "))

# if p >= 0 and r >= 0 and t >= 0:
#     si, ci = interest(p, r, t)
#     print("Simple Interest:", si)
#     print("Compound Interest:", ci)
# else:
#     print("Invalid values")


# # Q22. Write a function to return all factors of a number.

# def factors(num):
#     result = []

#     for i in range(1, abs(num) + 1):
#         if num % i == 0:
#             result.append(i)

#     return result

# num = int(input("Enter a non-zero number: "))

# if num == 0:
#     print("Zero has infinitely many factors")
# else:
#     print("Factors:", factors(num))


# # Q23. Write a function to find the second-largest number in a list.

# def second_largest(numbers):
#     unique = []

#     for num in numbers:
#         if num not in unique:
#             unique.append(num)

#     if len(unique) < 2:
#         return None

#     unique.sort()
#     return unique[-2]

# numbers = [10, 50, 30, 20, 40]

# print("Second Largest:", second_largest(numbers))



# # 6. Lists 
# # Q24. Merge two lists without duplicates.

# list1 = [10, 20, 30]
# list2 = [20, 30, 40]

# result = []

# for item in list1 + list2:
#     if item not in result:
#         result.append(item)

# print("Merged List:", result)


# # Q25. Find the second-largest and second-smallest elements.

# numbers = [10, 20, 30, 40, 50]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# unique.sort()

# if len(unique) >= 2:
#     print("Second Smallest:", unique[1])
#     print("Second Largest:", unique[-2])
# else:
#     print("Not enough distinct elements")


# # Q26. Rotate a list to the left by k positions.

# numbers = [1, 2, 3, 4, 5]

# k = int(input("Enter rotation count: "))

# if numbers:
#     k = k % len(numbers)
#     result = numbers[k:] + numbers[:k]
# else:
#     result = []

# print("Rotated List:", result)


# # Q27. Separate even and odd numbers into two lists.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even Numbers:", even)
# print("Odd Numbers:", odd)


# # Q28. Find the common elements between two lists.

# list1 = [10, 20, 30, 40]
# list2 = [30, 40, 50, 60]

# common = []

# for num in list1:
#     if num in list2 and num not in common:
#         common.append(num)

# print("Common Elements:", common)



# # 7. Tuples & Sets
# # Q29. Count the frequency of each element in a tuple.

# my_tuple = (10, 20, 10, 30, 20, 10)

# frequency = {}

# for item in my_tuple:
#     frequency[item] = frequency.get(item, 0) + 1

# print("Frequency:", frequency)


# # Q30. Find the union, intersection, and difference of two sets.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print("Union:", set1.union(set2))
# print("Intersection:", set1.intersection(set2))
# print("Difference:", set1.difference(set2))


# # Q31. Check whether one set is a subset of another.

# set1 = {1, 2}
# set2 = {1, 2, 3, 4}

# if set1.issubset(set2):
#     print("First set is a subset")
# else:
#     print("First set is not a subset")


# # 8. Dictionaries
# # Q32. Count the frequency of words in a sentence.

# sentence = input("Enter a sentence: ").lower()

# words = sentence.split()
# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print("Word Frequency:", frequency)


# # Q33. Create a dictionary from two lists (keys and values).

# keys = ["name", "age", "city"]
# values = ["Bhumika", 21, "Jalgaon"]

# result = dict(zip(keys, values))

# print("Dictionary:", result)


# # Q34. Sort a dictionary by its values.

# my_dict = {
#     "Apple": 50,
#     "Banana": 20,
#     "Mango": 80,
#     "Orange": 40
# }

# result = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# print("Sorted Dictionary:", result)



# # 9. File Handling
# # Q35. Read a text file and count the number of lines, words, and characters.

# filename = input("Enter file name: ")

# try:
#     with open(filename, "r") as file:
#         content = file.read()

#     lines = len(content.splitlines())
#     words = len(content.split())
#     characters = len(content)

#     print("Lines:", lines)
#     print("Words:", words)
#     print("Characters:", characters)

# except FileNotFoundError:
#     print("File not found")


# # Q36. Copy only the even-numbered lines from one file to another.

# source = input("Enter source file name: ")
# destination = input("Enter destination file name: ")

# try:
#     with open(source, "r") as file:
#         lines = file.readlines()

#     with open(destination, "w") as file:
#         for i, line in enumerate(lines, start=1):
#             if i % 2 == 0:
#                 file.write(line)

#     print("Even-numbered lines copied successfully")

# except FileNotFoundError:
#     print("Source file not found")


# # 10. Exception Handling
# # Q37. Handle invalid integer input using try-except.

# try:
#     num = int(input("Enter an integer: "))
#     print("Number:", num)

# except ValueError:
#     print("Invalid input! Please enter an integer.")


# # Q38. Handle file-not-found errors while reading a file.

# filename = input("Enter file name: ")

# try:
#     with open(filename, "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("Error: File not found")

# except OSError as error:
#     print("File error:", error)



# # 11. Modules
# # Q39. Create a random password generator using the random and string modules

# import random
# import string

# length = int(input("Enter password length: "))

# if length <= 0:
#     print("Enter a positive length")
# else:
#     characters = string.ascii_letters + string.digits + string.punctuation

#     password = ""

#     for i in range(length):
#         password += random.choice(characters)

#     print("Generated Password:", password)

# # Q40. Use the datetime module to calculate the number of days between two dates.

# from datetime import datetime

# date1 = input("Enter first date (DD-MM-YYYY): ")
# date2 = input("Enter second date (DD-MM-YYYY): ")

# try:
#     d1 = datetime.strptime(date1, "%d-%m-%Y")
#     d2 = datetime.strptime(date2, "%d-%m-%Y")

#     difference = abs((d2 - d1).days)

#     print("Number of Days:", difference)

# except ValueError:
#     print("Invalid date format")



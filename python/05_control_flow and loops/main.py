# numbers = [123, 45, 6]
# sums = []
# for num in numbers:
#     digit_sum = 0
#     for digit in str(num):
#         digit_sum += int(digit)
#     sums.append(digit_sum)

# print(sums)


# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# Write a program to find all prime numbers between 10 and 50 using a for loop.

# for num in range(10, 51):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break   
#         else:
#             print(num, "is a prime number")
			
# Set of friends for two people
friends_1 = {"Alice", "Bob", "Charlie", "David"}
friends_2 = {"Charlie", "David", "Eve", "Frank"}

# Find mutual friends using the intersection function
mutual_friends = friends_1.intersection(friends_2)

# Print mutual friends
print(mutual_friends)
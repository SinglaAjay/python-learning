# # Method 1: Using slicing (most Pythonic)
# string = input("Enter a string: ")
# reversed_string = string[::-1]
# print(f"Original string: {string}")
# print(f"Reversed string: {reversed_string}")
# print(f"A count: {string.count('a')}")

# movie1= input("Enter the first movie name: ")
# movie2= input("Enter the second movie name: ")  
# movie3= input("Enter the third movie name: ")

# list_of_movies = [movie1, movie2, movie3]

# print(list_of_movies)



# number_list = [1, 2, 3, 2, 2]

# reversed_list = number_list[::-1]

# if number_list == reversed_list:
#     print("The list is a palindrome.")
# else:    print("The list is not a palindrome.")
# # Diamond pattern
# n = 4
# for i in range(n):
#     print(' ' * (n - i - 1) + '*' * (2 * i + 1))
# for i in range(n - 2, -1, -1):
#     print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# print(number_list.count(2))
# print(number_list.index(2))  # Get first index of element
# print(max(number_list))  # Get maximum value
# print(min(number_list))  # Get minimum value
# print(sum(number_list))  # Get sum of all elements
# print(len(number_list))  # Get list length
# number_list.sort()  # Sort in place
# print(sorted(number_list))  # Return sorted copy
# number_list.append(4)  # Add element to end
# number_list.remove(1)  # Remove first occurrence
# number_list.pop()  # Remove and return last element
# number_list.reverse()  # Reverse in place
# print(2 in number_list)  # Check if element exists


# dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print(dict1['name'])  # Access value by key
# dict1['age'] = 31  # Update value
# print(dict1)



# dict2 = {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}


# list_of_dicts = ["Python", "Java", "C++", "Java", "Python"]

# unique_languages = set(list_of_dicts)
# print(unique_languages)

marks=[]

math_marks = int(input("Enter math marks: "))
marks.append(math_marks)
science_marks = int(input("Enter science marks: "))
marks.append(science_marks)
english_marks = int(input("Enter english marks: "))
marks.append(english_marks)

print(marks)

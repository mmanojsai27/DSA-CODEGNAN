'''
#Question 1: Student Marks Manager 
marks = []
#Use a loop to accept three marks from the user. 
for i in range(3):
    mark = int(input("Enter Marks: "))
# Add each entered mark to a list using append().
    marks.append(mark)

print("Marks:",marks)

#Insert 90 at the beginning using insert(). 
marks.insert(0,90)
#print("Marks:",marks)

#Add 75 and 85 together using extend().
marks.extend([75,85])
     print("Marks:",marks)

#Use a condition to check for 75, then remove it using remove()
if 75 in marks:
    marks.remove(75)
     print(marks)
#Remove the final mark using pop() and display the removed value
removed = marks.pop()
print("Marks:",marks)
print("Removed:", removed)

# Display the final list and its length using len().
print("Final List: ", marks)
print(f' The Length of the marks is: {len(marks)}')

'''

'''
#Question 2: Number List Analyser

numbers = [20, 10, 30, 20, 40, 20]

#Requirement 1: Sort the list in ascending order using sort().
numbers.sort()
print(numbers)
'''

'''
ans = "Python is easy"
print(ans [::-1])
#==================================================

answers = "I love python"
words = answers.split()
print(words)
words.reverse()
print(f'Reversed Answers => {words}')


answers = "I love python"
words = answers.split()
print(words)
result = ""

for word in words:
    result = word + " " + result
    
print(result.strip())
'''

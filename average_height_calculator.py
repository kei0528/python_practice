# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

array_length = 0
height_sum = 0

for height in student_heights :
  array_length += 1
  height_sum += height
  
height_average = round(height_sum / array_length)

print(height_average)
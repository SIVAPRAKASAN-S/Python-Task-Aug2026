
# 1. Line Chart

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.title("Simple Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()


# 2. Bar Chart

import matplotlib.pyplot as plt

students = ["Siva", "Arun", "Kumar", "Ravi"]
marks = [85, 90, 75, 80]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

# 3. Pie Chart

import matplotlib.pyplot as plt

subjects = ["Python", "Java", "HTML", "CSS"]
marks = [40, 30, 20, 10]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")

plt.title("Subject Percentage")

plt.show()


# 4. Scatter Plot

import matplotlib.pyplot as plt

height = [150, 160, 165, 170, 175, 180]
weight = [50, 55, 60, 65, 70, 75]

plt.scatter(height, weight)

plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")

plt.show()


# 5. Histogram

import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 60, 65, 70, 70, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()


# 6. Multiple Lines

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales1 = [10, 20, 15, 25, 30]
sales2 = [15, 18, 20, 22, 28]

plt.plot(months, sales1, label="Product A")
plt.plot(months, sales2, label="Product B")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()


| Function        | Purpose       |
| --------------- | ------------- |
| `plt.plot()`    | Line chart    |
| `plt.bar()`     | Bar chart     |
| `plt.pie()`     | Pie chart     |
| `plt.scatter()` | Scatter plot  |
| `plt.hist()`    | Histogram     |
| `plt.title()`   | Add title     |
| `plt.xlabel()`  | X-axis name   |
| `plt.ylabel()`  | Y-axis name   |
| `plt.legend()`  | Show labels   |
| `plt.show()`    | Display graph |

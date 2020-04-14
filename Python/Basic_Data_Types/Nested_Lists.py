# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
c = []
d = []
for i in range(n):       
    a =[] 
    for j in range(2): 
         if j == 0:
            a.append(input()) 
         else:
            x=float(input())
            a.append(x)
            d.append(x)       
    c.append(a) 
c.sort()
d.sort()
d = list(dict.fromkeys(d))
for i in range(0,n):
        if d[1] == c[i][1]:
            print(c[i][0])


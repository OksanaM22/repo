import statistics

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
ev_grades= statistics.mean(grades[0]),statistics.mean(grades[1]),statistics.mean(grades[2]),statistics.mean(grades[3]),statistics.mean(grades[4])
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_students=list(students)
my_students.sort()
my_students_grades =dict(zip(my_students,ev_grades))
print(my_students_grades)




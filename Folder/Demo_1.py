# courses_file = open("courses.txt")
# for line in courses_file:
#     print(line)

with open("courses.txt") as courses_file: # чтобы открыть файл COURSES.txt в переменной courses_file
    for line in courses_file:
        part = line.split(",")
        print(part)

        # print(name)
        # print(score)
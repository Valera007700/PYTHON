#     Afghanistan,    AFG,    1950,     27.638
i = 0
lowest = 1000
lowestYear = ""
lowestCountry = ""
average = 0
choiceYear = int(input("Какой год ищешь?"))

with open("life-expectancy.csv") as table: # чтобы открыть файл COURSES.txt в переменной courses_file
    for line in table:
        i = i + 1
        clean_line = line.strip()
        words = clean_line.split(",")

        if i > 1:
            country = words[0]
            code = words[1]
            year = int(words[2])
            lifeExp = float(words[3]) # Тут мы ввели переменные на все 4 массива (страна, код, год, ожидание)
            if lowest > lifeExp:
                lowest = lifeExp
                lowestYear = year
                lowestCountry = country
            if choiceYear == year:
                print(f"{year} - {country} - {lifeExp}")
                average = average + lifeExp

#print(f"lowest: {lowest} - {lowestYear} - {lowestCountry}")





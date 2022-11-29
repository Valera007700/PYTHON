i = 0
#    life-expectancy.csv
#    expectancy.txt
lowest = 1000
LowestYear = ""
LowestCountry = ""
with open ("life-expectancy.csv") as table:
    for line in table:
        i = i + 1
        CleanLine = line.strip()
        words = CleanLine.split(",")
        if i > 1:
            #print(f"{i} --- {words[0]}   {words[2]}   {words[3]} ")
            if lowest > float(words[3]):
                lowest = float(words[3])
                LowestYear = words[2]
                LowestCountry = words[0]
                print(f"{LowestCountry} - {LowestYear} - {lowest}")
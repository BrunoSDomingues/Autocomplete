import csv

with open("old-newspaper.tsv", "r") as file:
    tsv = list(csv.reader(file, delimiter="\t"))
    with open("english-sentences.csv", "w+") as sen:
        sen.write("date, sentence\n")
        for row in tsv:
            if row[0] == "English":
                sen.write(f"{row[-2]}, {row[-1]}\n")
                
        
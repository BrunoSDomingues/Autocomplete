with open("english-sentences.csv", "r") as f:
    lines = [line.split(",") for line in f.readlines()[1:]]
    
with open("english-sentences-v2.csv", "w+") as f:
    f.write("date, sentence\n")
    for line in lines:
        if len(line[1].split(" ")) >= 8:
            if "\n" in line[1]:
                f.write(f"{line[0]},{line[1]}")
            else:
                f.write(f"{line[0]},{line[1]}\n")
    
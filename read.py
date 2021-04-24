def getText():
    location = str(input("/home/pi/"))
    file = open(location, "r");
    for line in file:
        split = line.split(" ")
        if (split[0].count("\t") > 1):
            holder = line.split("\n")
            print(holder[0] + " | ", end="")
        elif (split[0].count("\t") > 0):
            print(line)
        else:
            if (line != "\n"):
                print(line)

if __name__ == "__main__":
    getText()
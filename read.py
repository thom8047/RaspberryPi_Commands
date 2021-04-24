def getText():
    location = "/home/pi/" + str(input("/home/pi/"))
    file = open(location, "r");
    for line in file:
        split = line.split(" ")
        if (split[0].count("\t") > 1):
            print(line)
        elif (split[0].count("\t") > 0):
            print(line)
        else:
            print(line)

if __name__ == "__main__":
    getText()
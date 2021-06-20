def getText():
    location = "/home/pi/" + str(input("/home/pi/"))
    file = open(location, "r");
    line_num = 0
    for line in file:
        if (line_num > 15):
            user_input = str(input())
            if (user_input):
                break;

        split = line.split(" ")
        if (split[0].count("\t") > 1):
            print(line)
        elif (split[0].count("\t") > 0):
            if (line.count("use case:") < 1):
                print(line)
        else:
            if (line != "\n"):
                print(line)

        line_num += 1;


if __name__ == "__main__":
    getText()
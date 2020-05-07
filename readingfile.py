def AppendToFile(content):
    file = open("Output.txt", "a")
    file.write(content + "\r\n")
    file.close()

one = "one"
two = "two"
three = "three"

AppendToFile(one)
AppendToFile(two)

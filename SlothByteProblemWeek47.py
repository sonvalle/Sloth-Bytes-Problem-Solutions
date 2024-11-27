import re
comentString = input("Enter the comments string")


def checkValid():
    # First test remove all '/' and '*' if there characters other than '/' and '*' the awnser should be false
    slash = re.findall("/", comentString)
    star = re.findall("\*",  comentString)

    if (len(comentString) > (len(slash)+len(star))):
        return "False"

    # Second test if the length of the string is an uneven number then it must allways be false, get fucked out of range errors
    if len(comentString) % 2 != 0:
        return "False"

    # Third test the thing that I think your actually suposed to do.
    counter = 0
    counterCheck = 0
    while counter < len(comentString):
        if comentString[counter] == comentString[counter+1] and comentString[counter] == "/":
            counter += 2
        if counter == counterCheck:
            if comentString[counter] == "/" and comentString[counter+1] == "*" and comentString[counter+2] == "*" and comentString[counter+3] == "/":
                counter += 4

        if counter == counterCheck:
            return "False"
        else:
            counterCheck = counter

    return "True"


print(checkValid())

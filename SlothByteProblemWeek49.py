# Basicly after some detective work I have concluded that inverted(x) is the number that with the number that is to be inverted(y)=255


def invert(valueList):
    invertedValueList = []
    counter = 0
    while counter < 3:
        value = 255-int(valueList[counter])
        invertedValueList.append(value)
        counter += 1

    return (invertedValueList)


counter = 0
valueList = []
while counter < 3:
    value = input("Input rgb value " + str(counter) +
                  " id est number between 0 and 255:")
    valueList.append(value)
    counter += 1

print(invert(valueList))

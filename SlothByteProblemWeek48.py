num = input("Input a number")


def num_split(num):
    listOfNums = []
    lenght = len(num)
    num2 = ""
    # checks if the first thing is a - and removes the minus
    isNegative = False
    if num[0] == "-":
        isNegative = True
        for x in num:
            if x != "-":
                num2 += x
        lenght -= 1
    else:
        num2 = num

    for x in num2:
        # check if x is zero
        if x == "0":
            number = 0
            lenght = lenght-1
        else:
            counter = 1
            while counter < lenght:
                x += '0'
                counter += 1
            number = x
            lenght = lenght-1

        listOfNums.append(number)

    # add the minus if it's a negative number
    listOfNums2 = []
    if isNegative == True:
        for n in listOfNums:
            if n != 0:
                n = "-"+n
            listOfNums2.append(n)
        return listOfNums2
    else:
        return listOfNums


print(num_split(num))

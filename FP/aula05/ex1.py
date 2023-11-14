def inputFloatList():
    num = input("number: ")
    lst = []
    count = 0
    while num != "":
        num = float(num)
        lst.append(num)
        count += 1
        num = input("number: ")
    return lst, count

def countLower(lst, v):
    count = 0
    for c in lst:
        if c < v:
            count += 1
    return count

def minmax(lst):
    minimum = lst[0]
    maximum = lst[0]
    for c in lst:
        if c > maximum:
            maximum = c
        elif c < minimum:
            minimum = c
    return minimum, maximum

def main():
    input_list = inputFloatList()[0]
    minmax_val = minmax(input_list)
    minmax_avg = (minmax_val[0] + minmax_val[1])/2
    lower_count = countLower(input_list, minmax_avg)


    print("List:", input_list)
    print("MIN Value: {}\nMAX Value: {}\nAVG Value: {}".format(minmax_val[0], minmax_val[1], minmax_avg))
    print("Number of values below AVG:", lower_count)

main()
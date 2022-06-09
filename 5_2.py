def average(*args):
    sum = 0
    count = 0
    for arg in args:
        sum += arg
        count += 1
    return sum / count
    #return sum / len(args) второй вариант - с len, но не спортивно:)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]

list1 = list(filter(lambda x: x != '', list1))

print(list1)

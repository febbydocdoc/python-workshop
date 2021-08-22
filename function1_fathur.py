string = input("Type Word: ")


def lower_case(string):
    return sum(map(str.islower, string))


def upper_case(string):
    return sum(map(str.isupper, string))


lower = lower_case(string)
upper = upper_case(string)


print("Huruf Kecil = ", lower)
print("Huruf Besar = ", upper)

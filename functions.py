# cs362 - hw07
# casey nord
# spring 2021


def fizzbuzz(_input):
    # check type
    if not isinstance(_input, int):
        raise TypeError

    # print fizzbuzz
    if _input % 3 == 0 and _input % 5 == 0:
        print("FizzBuzz")
    elif _input % 3 == 0:
        print("Fizz")
    elif _input % 5 == 0:
        print("Buzz")
    else:
        print(_input)

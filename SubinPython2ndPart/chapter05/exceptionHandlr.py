def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by Zero\n")
    except TypeError:
        # print((type(a)if 'str' else type(b)))
        print("did u use string??")


print(div(1, 2))
print(div(2, 2))
print(div(1, 0))
print(div('1', 0))
print(div(0, 1))

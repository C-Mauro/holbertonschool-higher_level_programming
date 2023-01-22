#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

i = 0
result = 0
for argument in argv:
    if i != 0:
        result += int(argument)
    else:
        i += 1
print("{:d}".format(result))

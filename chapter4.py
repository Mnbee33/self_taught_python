print("--No.1--")
def square(x):
    '''
    Returns square of x
    :param x: int.
    :return: square of x
    '''
    return x ** 2
print(square(3))


print("--No.2--")
def my_print(str):
    '''
    Print string
    :param str: string
    '''
    print(str)

my_print("hello sekiro")

print("--No.3--")
def introduce(name, age, job, pet_kind="dog", pet_name="john"):
    '''
    Print introduce
    :param name: string
    :param age: int
    :param job: string
    :param pet_kind: string
    :param pet_name: string
    '''
    print("my name is " + name)
    print("I'm " + str(age) + " years old.")
    print("I'm a " + job)
    print("I have a" + pet_kind)
    print("His name is " + pet_name)

introduce("Marry", 15, "student")

print("--No.4--")
def divide(x):
    return int(x / 2)

def multiple(x):
    return int(x * 4)

result = divide(10)
result = multiple(result)
print(result)

print("--No.5--")
def toFloat(str):
    '''
    Return convert string to float
    :param str: string
    '''
    try:
        return float(str)
    except ValueError:
        return "Invalid input"

print(toFloat("10"))
print(toFloat("99.99"))
print(toFloat("abc"))

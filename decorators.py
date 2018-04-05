def outside():

    def inside():
        print('inside function called')

    print('Outside function - calling inside function!')
    inside()

outside()


def passed():
    print('passed() is called.')

def pass_to_me(f):
    print('pass_to_me() -> calling my parameter:')
    f()

pass_to_me(passed)


def return_a_function():
    def returned_function():
        print('returned_function is called!')
    return returned_function


f = return_a_function()
f()


def simple_decorator(f):
    def wrapper(x):
        print('Calling f() now:')
        f(x)
        print('f() called.')
    return wrapper

@simple_decorator
def simple(number):
    print(number)

simple(32)

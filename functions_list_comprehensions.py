def example_function(x):
    return x + 1

example_variable = 10
print(example_variable)

processed_variable = example_function(example_variable)
print(processed_variable)  # this should be 11

def complicated_func(x, y):

    def squared(z):
        return z * z

    x_squared = squared(x)
    return x_squared + y * 3

x = 5
y = 3

print(complicated_func(x, y))  # 34

# List comprehensions
xs = [0, 1, 2, 3, 4, 5]
# target x_squared_s = [0, 1, 4, 9, 16, 25]

result = []
for x in xs:
    result.append(x * x)

print(result)

result_alternative = [(x * x) for x in xs]

print(result_alternative)

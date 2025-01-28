def compose_functions(f, g): #arguments that would be replaced with functions
    def composed (x):
        return f(g(x))
    return composed
def increment (x):
    return x + 1  #adds 1 to x
def square (x):
    return x ** 2 #squares x

increment_then_square = compose_functions(square, increment) #functions as argument

result = increment_then_square(4)
print(result)  #Sample output: 25
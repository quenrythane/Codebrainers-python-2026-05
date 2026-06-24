
def pitagoras_klasycznie(a, b):
    return ((a**2 + b**2)) ** 0.5

pitagoras_lambda = lambda a, b: ((a**2 + b**2)) ** 0.5


print(pitagoras_klasycznie(6, 8))
print(pitagoras_lambda(6, 8))

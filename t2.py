import math
import numpy as np

def getnumber(index):
    rdiv = index % 2
    if rdiv == 0:
        result = math.pow(3, index) + (7 * (math.factorial(index)))
        return result
    else:
        result = math.pow(2, index) + (4 * (math.log(index)))
        return result

values = []
for i in range(10):
    actual = getnumber(i)
    values.append(actual)

x = np.array(values)
max_value_index = np.argmax(x)
mean = np.format_float_positional(np.mean(x), precision=2)

print("Indice do maior valor: {0}".format(max_value_index))
print("Média dos valores: {0}".format(mean))
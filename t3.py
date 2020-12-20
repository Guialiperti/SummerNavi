dic = {}

for i in range(1,6):
    nota = int(input("Nota Aluno {0}: ".format(i)))
    dic["aluno{0}".format(i)] = nota

max_key = max(dic, key=dic.get)
max_value = max(dic.values())
print("Aluno com a maior nota: {0}".format(max_key))
print("Nota do aluno: {0}".format(max_value))
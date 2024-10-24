#Слишком древний шифр
k= int(input('Введите число от 3 до 20 '))

result=''
for i in range(1,k):
    for j in range(i+1, k):
        if  k % (i+j) ==0:
            result += str(i)+str(j)

print(result)
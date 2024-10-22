#Changelog:
#
#


f = open("1/input.txt", "r")
array =[]
num1 = 0
num2 = 0
sum = 0

while(True):
        line = f.readline()
        if not line:
                break
        array.append(int(line))

for x in array:
        for y in array:
                sum = x + y
                if sum == 2020:
                        num1 = x
                        num2 = y
                        break
print(num1)
print(num2)
erg = num1 * num2
print(erg)
f.close()
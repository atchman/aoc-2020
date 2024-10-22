#Changelog:
#
#


f = open("1/input.txt", "r")
array =[]
num1 = 0
num2 = 0
num3 = 0
sum = 0

while(True):
        line = f.readline()
        if not line:
                break
        array.append(int(line))

for x in array:
        for y in array:
            for z in array:

                sum = x + y + z
                if sum == 2020:
                        num1 = x
                        num2 = y
                        num3 = z
                        break
print(num1)
print(num2)
print(num3)
erg = num1 * num2 * num3

print(erg)
f.close()
print("Pearson moment coefficient for numeric attributes")

n = int(input("Enter the number of data points : "))

data = []

suma, sumb, meana, meanb, prodab, vara, varb = 0, 0, 0, 0, 0, 0, 0

for i in range(n):
	temp = list(map(int, input("Enter the data point : ").split()))
	data.append(temp)
	suma += temp[0]
	sumb += temp[1]
	
meana = suma / n
meanb = sumb / n

for i in range(n):
	vara += (data[i][0] - meana) ** 2
	varb += (data[i][1] - meanb) ** 2
	prodab += (data[i][0] - meana) * (data[i][1] - meanb)
	
vara /= n
varb /= n
sda = vara ** 0.5
sdb = varb ** 0.5

corrcoff = prodab / (n * sda * sdb)

print("The correlation coefficient is : ", corrcoff)
	
	
print("Chi-Square test for nominal attributes")

ct = [[0 for i in range(3)] for j in range(3)]
print("Input the contingency table : ")
for i in range(2):
	for j in range(2):
		ct[i][j] = int(input())
tbchis = float(input("Input the chi-square table value at required level of significance : "))
ct[0][2] = ct[0][0] + ct[0][1]
ct[1][2] = ct[1][0] + ct[1][1]
ct[2][0] = ct[0][0] + ct[1][0]
ct[2][1] = ct[0][1] + ct[1][1]
ct[2][2] = ct[2][0] + ct[2][1]


print("The required contingency table is : ", ct)
chis = 0
for i in range(2):
	for j in range(2):
		ex = (ct[i][2] * ct[2][j]) / ct[2][2]
		chis += ((ct[i][j] - ex) ** 2) / ex

print("The calcuated chi-square value is : ", chis)

if chis > tbchis:
	print("The null hyphothesis can be rejected and the data is dependent")
else:
	print("The null hyphothesis cannot be rejected")


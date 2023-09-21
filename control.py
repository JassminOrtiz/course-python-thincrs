#IF ELSE OPERATOR
edad = 21

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    
#WHILE LOOP 
count = 1
while count <= 5:
    print("el contador es: ", count)
    count += 1

#FOR LOOP
frutas = ["mango", "piña", "sandia"]

for fruta in frutas:
    print("Me gusta la", fruta)

#ANOTHER FOR LOOP 
for i in range(1, 6):
    print(i)

#BREAK 
for numero in range(1, 11):
    if numero == 5:
        break
    print(numero) 
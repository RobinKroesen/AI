#Pyramide bouwen

invoer = input("hoe hoog moet de pyramide worden: ")

for i in range(int(invoer)):
    print("*"* (i+1))
for i in reversed(range(int(invoer))):
    print("*"* (i))


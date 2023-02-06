name = input("user name:" )
if name == "bob":
    print ("your in ", name)
num_1 = float(input("enter first number: "))
aqua = (input("enter symbol "))
num_2 = float(input("enter second number "))
if aqua == '+':
    print(num_1 + num_2)
elif aqua == '-':
    print(num_1 - num_2)
elif aqua == '*':
    print(num_1 * num_2)
elif aqua == '/':
    print(num_1 / num_2)
elif name == 'rip':
    for i in range(1, 11):
        print('#'*i)
elif name == 'lis':
    a= [a + b for a in'list' if a != 's' for b in 'soup' if b != 'u']
    print (a)
elif name == "byte_sis":
    print(name.__sizeof__())


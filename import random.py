name = input("user name:" )
if name == "bob":
    print ("your in ", name)
    num_1 = float(input( "enter number one: "))
    num_2 = float(input( "enter number two: "))
    res =  float(int(num_1)) + float(int(num_2))
    res_2 = num_1 * num_2
    res_3 = num_1 / num_2
    print("your result is: ", res, res_2, res_3)
elif name == 'rip':
    for i in range(1, 11):
        print('#'*i)
elif name == 'lis':
    a= [a + b for a in'list' if a != 's' for b in 'soup' if b != 'u']
    print (a)
elif name == "byte_sis":
    print(name.__sizeof__())

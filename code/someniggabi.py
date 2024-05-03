total = 0
for i in range(10):
    num = float(input("Enter a number {}:".format(i+1)))
    total += num

    average = total/10
    print("The average of the 10 numbers is = " , average) 

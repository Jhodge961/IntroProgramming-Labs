#CMPT 120
#Jason Hodge
#20 September 2018

def main():
    x = int(input("Please enter a value for X:"))
    total=0
    for i in range(1,x):
        total += (-1)**(i+1)*((1.0/(i+i+1)))

    value = 4*(1-total)
    print(value)

main()

# CMPT 120 - Lab #6
# Jason Hodge
# 25 Oct 2018
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', 'power', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
     while True:
         cmd = input("What computation do you want to perform? ").lower()
         if cmd == "quit":
             break
         else:

             try:
                 num1 = int(input("Enter the first number: "))
                 num2 = int(input("Enter the second number: "))
                 
             except:
                 print("An error has occured...")
                     
             if cmd == "add":
                result = num1 + num2
             elif cmd == "sub":
                result = num1 - num2
             elif cmd == "mult":
                result = num1 * num2
             elif cmd == "div":
                result = num1 / num2
             elif cmd == "power":
                result = num1 ** num2
             elif cmd == "quit":
                break
    
             print("The result is " + str(result) + ".\n")
 
def main():
    showIntro()
    doLoop()
    showOutro()
main()

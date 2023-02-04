import pyfiglet
from Functions import PuncPop, PuncFilePop

print("")
print(pyfiglet.figlet_format("Punctuation Remover", justify="center", width=110))
print(pyfiglet.figlet_format("Created By Shinjan", justify="center", width=110))

while True:
    
    printer = """
1. Remove Punctuations From Input
2. Remove Punctuations From File"""
    print(printer)
    print("")

    try:
        user_input = int(input("Enter Your Choice From The Above Lines In Numbers: "))
        if user_input == 1:
            print("")
            user_input1 = input("Enter The Text With Punctuation Marks: ")
            result = PuncPop(user_input1)
            print("")
            print("Your Result Is Ready!, This is your Final Result Below :)")
            print("")
            print(result)

        else:
            print("")
            user_input2 = input("Enter The Filepath (Data.txt): ")
            PuncFilePop(user_input2)
            print("")
            print("Your File Is Successfully Updated With No Punctuation Marks")

    except ValueError:
        print("")
        print("Please Enter A No. (For Example:- 1) :/")
        continue
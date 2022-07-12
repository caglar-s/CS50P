#Einstein
#Prompts the user for mass as an integer (in kilograms) and then output the equivalent number of Joules as an integer. Assume that the user will input an integer.

def main():
    m = int(input("m: "))
    c = 300000000
    print("E: ", calc(m,c))

def calc(x,y):
    return x * (y*y)

main()

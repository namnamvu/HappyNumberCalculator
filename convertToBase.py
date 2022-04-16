# Convert to binary to speed up the process of calculating
def convert_to_binary(decimal_number, b):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % b
        remainder_stack.append(remainder)
        decimal_number = decimal_number // b

    binary_digits = []
    while remainder_stack:
        # we could just reverse and join `remainder_stack` of course,
        # as it is simply a Python list, but popping off into another
        # list helps demonstrate that the only behavior we need from
        # `remainder_stack` is stack-like
        binary_digits.append(str(remainder_stack.pop()))

    return ''.join(binary_digits)

# num here is a string, b is an int
def isHappy(num, b):
    hasVisited = []
    num = convert_to_binary(int(num), b)
    
    while num != '1' and not (num in hasVisited):
        hasVisited.append(num)
        num = str(calHappy(num))
        num = convert_to_binary(int(num), b)
        
    if (num == '1'):
        return True
    return False

def calHappy(num):
    total = 0
    for digit in num:
        # change exponent yourself here if you need to by multiply another time
        total += int(digit) * int(digit)
    return total




def main():
    start = int(input("Enter a start range to test: "))
    end = int(input("Enter an end range to test: "))
    base = int(input("Enter the base you would like to convert to: "))
    # Be careful with the name of the file since if it exist in your file
    # It will rewrite information in the file
    fout = open("Data1234.txt","w")
    count = 0

    # Plus 1 at the end so that it will return the wanted range
    for j in range(start,end+1):
        if(isHappy(str(j), base)): 
            # Number of happy number find
            count += 1
            num = str(j)+ " "
            #Write to another file
            fout.write(num)

    # Range of numbers
    rangeNum = end - start + 1
    happyPercent = (count/rangeNum)*100

    print("The percentage of happy number is: ", float(happyPercent), "%")
main()


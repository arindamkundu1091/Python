# Write a python programe to convert hexadecimal to binary:
# Take the user input as a String

class NumberConversion:
    # Convert decimal to binary
    def decimalToBinary(input = '238'):
        number = int(input)
        arr = []
    
        while number > 0 :
            quotient = number%2
            result = int(quotient)
            arr.append(result)
            number = number//2

        length = len(arr)-1

        for i in range (length,-1,-1):
            print(arr[i], end="") 

    # decimalToBinary()

    # convert hexadecimal to binary 
    # it first convert hexadecimal to decimal number
    # then find the binary value of individual decimal number
    def hexadecimalToBinary(userinput = input('Enter hexadecimal numbe: ')):

        input = userinput.upper()
        hexcode = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        decimal = 0
        hexarr = []
        strlength = len(input)-1
        count = 0

        for i in range (strlength,-1,-1):
            ch = input[i]
            number = int(hexcode.index(ch))
            for j in range (0,4,+1):
                quotient = number%2
                result = int(quotient)
                hexarr.append(result)
                number = number//2
    
        length = len(hexarr)-1

        for i in range (length,-1,-1):
            print(hexarr[i], end="")    

    hexadecimalToBinary()

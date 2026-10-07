# values bigger than 9 start at ascii 65 A and go on from there

def incode_to_number(value : int):

    if value < 10:
        return str(value)

    else:
        # Prints bigg letters, -10 is so it starts at 65/A with 10
        return chr(65 + value - 10)

def decode_from_character(character : chr):

    #print(character)

    # input is checked befor using this function

    # at 65 is A in ascii
    if ord(character) < 65:
        return int(character)

    else:
        return (ord(character) - 65 + 10)

def convert_bases( ):

    global convert_bases_what_to_do
    input_number : int
    input_base   : int
    output_base  : int

    get_input_base   : bool
    get_input_number : bool
    get_output_base  : bool
    do_input_to_10   : bool
    do_output_to_10  : bool

    if convert_bases_what_to_do == "10_to_n":
        get_input_base   = False
        get_input_number = True
        get_output_base  = True
        do_input_to_10   = False
        do_output_to_10  = True
    elif convert_bases_what_to_do == "n_to_10":
        get_input_base   = True
        get_input_number = True
        get_output_base  = False
        do_input_to_10   = True
        do_output_to_10  = False
    elif convert_bases_what_to_do == "n_to_x":
        get_input_base   = True
        get_input_number = True
        get_output_base  = True
        do_input_to_10   = True
        do_output_to_10  = True


    if get_input_base:
        print("Input base:")
        input_base = input( )

        while not input_base.isdecimal( ) or int(input_base) <= 1:
            print(f"\'{input_base}\'is an invalid input, it needs to be a whole number that is bigger 1")
            print("Pls enter a valid input:")
            input_base = input( )

        input_base = int(input_base)
    else:
        input_base = 10

    if get_input_number:
        print("Input number:")
        input_number = input( )

        # used to save number's sine bc .isdecimal does not like -
        input_number_minus : bool = False

        if input_number[0] == "-":
            input_number = input_number[1:]
            input_number_minus = True
        
        while not input_number.isdecimal( ):
            print(f"\'{input_number}\' is not an valid input, it needs to be a whole number")
            print("Pls enter a valid input:")
            input_number = input( )

            if input_number[0] == "-":
                input_number = input_number[1:]
                input_number_minus = True
            else:
                input_number_minus = False
    else:
        input_number = 69

    input_number_as_list = list(input_number)

    # only to check if input_number's characters are all valid
    for character in input_number_as_list:

        #print(ord(character) < 48)
        #print(ord(character) < 65)
        #print(ord(character) > 57)

        # checks if character is valid
        if ord(character) < 48 or (ord(character) > 57 and ord(character) < 65):

            print(f"Error: input_number contains a character \'{character}\' that is not valid character")
            input( )

            return

        elif decode_from_character(character) >= input_base:

            print(f"Error: input_number contains a character \'{character}\' that is not valid with \'input_base_{input_base}\'")
            input( )

            return

    if get_output_base:
        print("Output base:")
        output_base = input( )

        while not output_base.isdecimal( ) or int(output_base) <= 1:
            print(f"\'{output_base}\' is not an valid input, it needs to be a whole number bigger than 1")
            print("Pls enter a valid input:")
            output_base = input( )

        output_base = int(output_base)
    else:
        output_base = 10

    # input_number         : str
    # input_number_as_list : [n,u,m,b,e,r]
    # input_number_minus   : true or false
    # input_base           : int and > 1
    # output_base          : int and > 1

    # to have it between decoding and incoding
    number_in_decimal = 0

    if not do_input_to_10:
        number_in_decimal = int(input_number)
    else:
        for character in range(len(input_number_as_list)):

            #print( )
            #print(character)
            #print(number[-character - 1])
            #print(decode_from_character(number[-character - 1]))
            #print(decode_from_character(number[-character - 1]) * (10 ** int(character)))

            # number[-character - 1] is multiplyer
            # int(character) is exponent
            number_in_decimal += decode_from_character(input_number_as_list[-character - 1]) * (input_base ** int(character))



    # number_in_decimal = base_10(input_number)



    # str bc you can easly add numbers behind with + operation
    output_number = ""
    number_is_zero = False

    if not do_output_to_10:
        output_number = str(number_in_decimal)
    else:
        exponent = 0
        multiplyer = 1

        while (output_base ** exponent) * multiplyer < number_in_decimal:
            
            #print(exponent, multiplyer, (base ** exponent) * multiplyer)

            if multiplyer < output_base:
                multiplyer += 1

            if multiplyer == output_base:
                multiplyer = 1
                exponent += 1

        #print(exponent, multiplyer, (base ** exponent) * multiplyer)

        buffer_number = number_in_decimal

        if buffer_number == 0:

            number_is_zero = True
            output_number += "0"

            # a simpel way to stop the while loop
            exponent = -1


        while exponent >= 0:

            #print( )
            #print(exponent, multiplyer, (base ** exponent) * multiplyer)
            #print(buffer_number)
            #print(output_number)

            if (output_base ** exponent) * multiplyer > buffer_number:
                
                if multiplyer != 1:

                    multiplyer -= 1

                elif multiplyer == 1:

                    output_number += "0"
                    exponent -= 1
                    multiplyer = output_base - 1

            elif (output_base ** exponent) * multiplyer == buffer_number:

                buffer_number = 0
                output_number += incode_to_number(multiplyer)
                exponent -= 1
            
            elif (output_base ** exponent) * multiplyer < buffer_number:

                output_number += incode_to_number(multiplyer)
                buffer_number -= (output_base ** exponent) * multiplyer
                exponent -= 1
                multiplyer = output_base - 1
                
    if not number_is_zero and output_number[0] == "0":
        output_number = output_number[1:]

    if input_number_minus:
        output_number = "-" + output_number

    print(f"Base_{input_base}({input_number}) = base_{output_base}({output_number})")
    input( )




# Program logic:

print("Made by Thomas Antal Csipa")

loop = True
convert_bases_what_to_do : str

while loop:

    print("Type:")
    print("t    : To convert from base_10 to a chosen base")
    print("f    : To convert from a chosen base to base_10")
    print("c    : To convert form a chosen base to another base")
    print("help : To get an overview of the program and how to use it")
    print("done : To end the program")

    _input = input( ).lower( )

    while _input not in ["t","f","c","done","help"]:

        print(f"\'{_input}\' is not a valid input")
        print("Pls input a valid input:")
        _input = input( ).lower( )

    print( )
    
    if _input == "done":
        loop = False

    elif _input == "t":

        convert_bases_what_to_do = "10_to_n"

    elif _input == "f":

        convert_bases_what_to_do = "n_to_10"

    elif _input == "c":

        convert_bases_what_to_do = "n_to_x"

    elif _input == "help":

        print("Made by Thomas Antal Csipa")
        print("")
        print("This program converts values from diffrent bases")
        print("When this program asks for a input or output base, then you will need to write a number with the numbers 0-9")
        print("It can be any number, so long it is more that one")
        print("The order of character values for the output are:")
        print("0-9  A-Z  [  /  ]  ^  _  `   a-z   and so on")
        print("0-9 10-36 37 38 39 40 41 42 43-69")
        print("Values bigger than 9 start at ascii 65 A and go on from there")
        print("The character values are only used if you write a number with a base bigger than 10")
        print("Or if you want to read a number with a base bigger than 10")
        print("I do not recomend haveing a to high base")

    if loop and _input != "help":

        convert_bases( )

def calculator():
    print("Welcome to the Python Operators Demonstration Program!")

    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))

    print("\nArithmetic Operations:")
    print(f"Addition: {int1} + {int2} = {int1 + int2}")
    print(f"Subtraction: {int1} - {int2} = {int1 - int2}")
    print(f"Multiplication: {int1} * {int2} = {int1 * int2}")
    print(f"Division: {int1} / {int2} = {int1 / int2}")
    print(f"Floor Division: {int1} // {int2} = {int1 // int2}")
    print(f"Modulus: {int1} % {int2} = {int1 % int2}")
    print(f"Exponentiation: {int1} ** {int2} = {int1 ** int2}")

    bool_input = input("\nEnter a boolean value (True or False): ").strip().lower() == "true"
    logical_operator = input("Enter a logical operator (and, or, not): ").strip().lower()

    if logical_operator == "and":
        print(f"Logical AND: {bool_input} and ({int1} > {int2}) = {bool_input and (int1 > int2)}")
    elif logical_operator == "or":
        print(f"Logical OR: {bool_input} or ({int1} > {int2}) = {bool_input or (int1 > int2)}")
    elif logical_operator == "not":
        print(f"Logical NOT: not {bool_input} = {not bool_input}")
    else:
        print("Invalid logical operator.")

    print("\nBitwise Operations:")
    print(f"Bitwise AND: {int1} & {int2} = {int1 & int2}")
    print(f"Bitwise OR: {int1} | {int2} = {int1 | int2}")
    print(f"Bitwise XOR: {int1} ^ {int2} = {int1 ^ int2}")
    print(f"Bitwise NOT of {int1}: ~{int1} = {~int1}")
    print(f"Left Shift {int1} by {int2} positions: {int1} << {int2} = {int1 << int2}")
    print(f"Right Shift {int1} by {int2} positions: {int1} >> {int2} = {int1 >> int2}")

    print("\nComparison Operations:")
    print(f"Equal to: {int1} == {int2} = {int1 == int2}")
    print(f"Not equal to: {int1} != {int2} = {int1 != int2}")
    print(f"Greater than: {int1} > {int2} = {int1 > int2}")
    print(f"Less than: {int1} < {int2} = {int1 < int2}")
    print(f"Greater than or equal to: {int1} >= {int2} = {int1 >= int2}")
    print(f"Less than or equal to: {int1} <= {int2} = {int1 <= int2}")

    print("\nMembership Operations:")
    sample_list = [int1, int2, int1 + int2]
    print(f"{int1} in {sample_list} = {int1 in sample_list}")
    print(f"{int1 * 2} not in {sample_list} = {int1 * 2 not in sample_list}")

    print("\nIdentity Operations:")
    a = [int1]
    b = [int1]
    print(f"a is b: {a is b}")
    print(f"a is not b: {a is not b}")
    print(f"a == b: {a == b}")

    print("\nAssignment Operations:")
    print(f"Initial value of int1: {int1}")
    int1 += int2 
    print(f"After addition assignment (int1 += int2): {int1}")

calculator()

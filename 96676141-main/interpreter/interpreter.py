user_input = input("Expression: ")

x, y, z = user_input.split(" ")

x = int(x)
z = int(z)

match y:
    case "+":
        result = (x+z)
    case "-":
        result = (x-z)
    case "*":
        result = (x*z)
    case "/":
        result = (x/z)

result = round(result,1)

formatted_result = "{:.1f}".format(result)

print(formatted_result)

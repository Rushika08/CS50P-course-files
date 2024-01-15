user_input = input("File name: ")

lower_input = str(user_input.lower().strip())

input_parts = lower_input.split(".")

string_length = len(input_parts)

if string_length>1:
    match input_parts[string_length-1]:
        case "gif" | "png":
            print("image/"+input_parts[string_length-1])
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "pdf" | "zip":
            print("application/"+input_parts[string_length-1])
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")


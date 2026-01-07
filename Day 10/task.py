# function will take a first name and a last name and change the inputs and change them to title case
# First letter capitalized in each word
def format_name(f_name,l_name):
    """Take a first and last name and format it to
    return the title case version of the name"""
    if f_name == "" or l_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name= l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


def function1(text):
    return text + text

def function2(text):
    return text.title()

formated_name = format_name(input("What is your first name?: "), input("What is your last name?: "))
print(formated_name)

output = function2(function1("hello"))
print(output)

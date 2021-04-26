from ast import literal_eval

def getType(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        return str

print(getType("10"))        # prints <class 'int'>
print(getType("12.20"))   # prints <class 'float'>
print(getType("True"))     # prints <class 'bool'>
print(getType("xyz")) 
print(getType("2+7i")) 
n = input()
print(type(n))
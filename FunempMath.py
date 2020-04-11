import math

check_int = 123
check_float = 123.4
check_string = "Check"
check_bool = True

#intblaster: Checks data type of a variable, then either returns it as a floored integer, or returns a False boolean

def intblaster(var):
    str_type = str(type(var))
    if (str_type == "<class 'int'>"):
        return var
    if (str_type == "<class 'float'>"):
        new_var = int(math.floor(var))
        return new_var
    if (str_type == "<class 'str'>"):
        try:
            new_var = int(float(var))
            return new_var
        except:
            return False
    else:
        return False
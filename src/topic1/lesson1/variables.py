if __name__ == '__main__':
    print("hello world!")
    """
    Variables and Types:
    Python is completely object oriented, and not "statically typed". 
    You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.
    """
    my_int = 1
    my_float = 1.02

    my_float = float(1.03)

    str1 = str("some string 34")
    str1 = str("some string 34")
    str1 = str("some string 3")
    str1 = str("some string 2")
    str1 = str("some string 123")
    str1 = "hello + any one wants to print lesson 1"

    print(my_float, ",", my_int, ",", str1)


def variables_task1():
    """
    The 'my_string' should contain string 'hello', my_float - 11.025, my_int - 7.
    """
    "my_string, my_float, my_int = None, None, None"

    my_string = "hello"
    my_float = 11.025
    my_int = 7.0
    return my_string, my_float, my_int

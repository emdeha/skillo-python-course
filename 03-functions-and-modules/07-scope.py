def outer_function():
    outer_var = "I'm from outer_function"

    def inner_function():
        inner_var = "I'm from inner_function"
        print("Inside inner_function:", inner_var)
        print("Inside inner_function accessing outer_var:", outer_var)

    inner_function()
    print("Outside inner_function:", outer_var)


outer_function()

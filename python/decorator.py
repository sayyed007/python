def decorated_hello(f):
    def inner():
        print("The Code is about to Run")
        f()
        print("Done with the Code")
    return inner


@decorated_hello
def hello():
    print("Hello, World!")
hello()
import math

def calculator():
    print("🔢 Python Scientific Calculator")
    print("Type an expression (e.g., 2+3, sqrt(16), log(100), sin(3.14))")
    print("Type 'q' to quit\n")

    while True:
        expr = input(">> ")

        if expr.lower() == "q":
            print("Exiting...")
            break

        try:
            # Safe eval environment with math functions
            result = eval(expr, {"__builtins__": None}, {
                "sqrt": math.sqrt,
                "log": math.log10,   # log base 10
                "ln": math.log,      # natural log
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "pi": math.pi,
                "e": math.e,
                "exp": math.exp,
                "pow": pow
            })
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()

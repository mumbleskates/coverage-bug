

def covered_function(arg):
    x = arg
    while x < 1000:
        if x < 10:
            print(x)
        else:
            # print("if uncommented, coverage works correctly in 3.8")
            break
        x += 1

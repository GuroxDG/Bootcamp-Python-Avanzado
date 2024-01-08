import traceback

def division(n1, n2):
    return n1/n2

if __name__ == "__main__":
    try:
        division(2, 0)
    except Exception as err:
        trace = traceback.format_exc()
        print("Extraer error")
        print(trace)
        print(err)

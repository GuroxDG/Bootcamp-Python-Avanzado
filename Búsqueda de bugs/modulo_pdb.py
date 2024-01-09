import pdb

def average(numbers):
    sum = 0

    for number in numbers:
        sum += number

    return round(sum / len(numbers))

def set_score(scores):
    breakpoint()
    average_ = average(scores)
    print(average_)
    match average_:

        case 10:
            print("Pasaste con 10")
            
        case 8 | 9:
            print("Pasaste el examen")
            
        case 7:
            print("Pasaste raspando")
            
        case _:
            print("Debes repetir examen")


if __name__ == "__main__":
    set_score([6, 7, 8, 6, 8, 10])
day = 22

match day:
    case 1:
        print("week day")

    case 2:
        print("week day")

    case 3:
        print("week day")

    case 4:
        print("week day")

    case 5:
        print("week day")

    case 6:
        print("weekend")

    case 7:
        print("weekend")
    
    case _:
        print("invalid number")


match day:
    case 1 | 2 | 3 | 4 | 5:
        print("week day")
    case 6 | 7 :
        print("weekend")
    case _:
        print("invalid number")
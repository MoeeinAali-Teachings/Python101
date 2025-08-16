day_number = 15

if day_number == 1:
    print("shanbe")

elif day_number == 2:
    print("1shanbe")

elif day_number == 3:
    print("2shanbe")

elif day_number == 4:
    print("3shanbe")

elif day_number == 5:
    print("4shanbe")

elif day_number == 6:
    print("5shanbe")

elif day_number == 7:
    print("jome")

else:
    print("invalid number")


print("*******************************")

match day_number:
    case 1:
        print("shanbe")

    case 2:
        print("1shanbe")

    case 3:
        print("2shanbe")

    case 4:
        print("3shanbe")

    case 5:
        print("4shanbe")

    case 6:
        print("5shanbe")

    case 7:
        print("jome")
    
    case _:
        print("invalid number")
def hello():
    day = input("What day is it?")
    match day:
        case "Monday":
            print("Happy Monday!")
        case "Tuesday":
            print("Happy Tuesday")

hello()
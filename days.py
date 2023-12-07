def find_days(day:int):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    else:
        return "Saturday"
    
def main():

        
    num = input()
    day = int(num)

    answer = find_days(day)
    print(answer)

main()




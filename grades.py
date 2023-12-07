def grade_calc(grade:int):
    if grade >= 75:
        return 'First'
    if grade >= 70 and grade <= 75:
        return 'Upper Second'
    if grade >= 60 and grade <= 70:
        return 'Second'
    if grade >= 50 and grade <=60:
        return 'Third'
    if grade >= 45 and grade <= 50:
        return 'F1 Supp'
    if grade >= 40 and grade <=45:
        return 'F2'
    else:
        return 'F3'
    
def main():
    
    num = input()
    grade = int(num)

    answer = grade_calc(grade)
    print(answer)

main()
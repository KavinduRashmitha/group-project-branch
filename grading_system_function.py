"***This is a Function to Check the Grade According to the Marks***"
def Grade(marks):
    if marks>=75:
        grade="A"
    elif marks>=65:
        grade="B"
    elif marks>=55:
        grade="C"
    elif marks>=40:
        grade="S"
    else:
        grade="F"
    return grade

n=int(input("Enter the Marks: "))
print("Your Grade =",Grade(n))
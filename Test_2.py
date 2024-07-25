num_entered = int(input("Take your num between 1-999: "))
if not (1 <= num_entered <= 999):
    print("Incorrect number. Try to use correct ones between 1-999.")
elif type(num_entered) != int:
    print("Incorrect num type. Please, check your input")
else:
    print(f"Alright! You picked: {num_entered}")
    if num_entered == 444:
        print("Perfect choice!")
    elif num_entered == 666:
        print("HELL YEAH!")
num_entered = int(input("Take your num between 1-999: "))
if num_entered <= 0 or num_entered >= 1000:
    print("Incorrect number. Try to use correct ones between 1-999.")
elif num_entered >= 1 or num_entered <= 999:
    print("Alright! You picked: ", num_entered)
    if num_entered == 444:
        print("Perfect choice!")
    if num_entered == 666:
        print("HELL YEAH!")
else:
    print("An error occured. Fuck you then")
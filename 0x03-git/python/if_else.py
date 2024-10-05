# if...else conditioning

# ask user to input their age
# then decide whether or not
# they should be allowed in a show.
age = eval(input('what is your age? '))
if age >= 18:
    print('enjoy your movie!')
elif age < 18:
    print('sorry, children below 18 are not allowed in.')

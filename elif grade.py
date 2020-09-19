SCORE_A = 90
SCORE_B = 80
SCORE_C = 70
SCORE_D = 60

def main():
    score = int(input('Enter your score: '))

    if score>=SCORE_A:
        print('Your grade is A.')
    elif score>=SCORE_B:
        print('Your grade is B.')
    elif score>=SCORE_C:
        print('Your grade is C.')
    elif score>=SCORE_D:
        print('Your grade is D.')
    else:
        print('Your grade is F.')

main()
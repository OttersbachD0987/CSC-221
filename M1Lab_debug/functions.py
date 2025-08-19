def dis_score(score):
        """
        Tell user if they passed or failed
        """
        if score >= 80:
            print("Your score is", score)
            print("You Passed!")
        else:
            print("Your score is", score)
            print("Your score is below 80!!!")
            print("You didn't pass the exam")
def menu():
    print('-'*10 + 'MENU' + '-'*10)
    print('1) Run Program')
    print('2) Exit')
    print('-'*24)

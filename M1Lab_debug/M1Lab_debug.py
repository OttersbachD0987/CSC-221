# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:51:37 2024

@author: seidih6290
"""
from functions import dis_score, menu

exam = {1: {"question": "A learner's permit usually requires supervised driving.", 
            "answer": False},
        2: {"question": "A commercial driver's license (CDL) is required for operating a large truck or bus.", 
            "answer": True},
        3: {"question": " Renewal periods for driver's licenses can vary, but it's typically more frequent than every 10 years.", 
            "answer": False},
        4: {"question": "A red traffic light always indicates that you must stop.", 
            "answer": True},
        5: {"question": "Driving with headphones on in both ears is illegal in many states.", 
            "answer": False},
        6: {"question": "Driving under the influence (DUI) is a serious offense, not a minor traffic violation.", 
            "answer": False},
        7: {"question": "A yellow diamond-shaped sign is a warning or caution sign.", 
            "answer": True},
        8: {"question":"In most states, turning right on red is allowed after a complete stop if there is no oncoming traffic.", 
            "answer": True},
        9: {"question": "The speed limit on interstate highways is usually higher than on local roads, but it can vary.", 
            "answer": False},
        10:{"question": "The legal age for obtaining a driver's license varies by state in the U.S.", 
            "answer": True}}
    
def main():
    choice = 0

    while choice != 2:
        menu()
        choice = int(input('Enter your choice: '))

        if choice == 1:
            print("start program....\n")
            # random selection of question
            correct = 0

            for q_id, ques in exam.items():
                # display quest
                print("\nQuestion", q_id)
                print("\n", ques["question"])

                # ask for answer
                ans = int(input("Enter 1 for True, or 2 for False: "))
                
                # convert answer to boolean and check if valid
                while ans != 1 and ans != 2:
                    print("Invalid answer!!!")
                    print("\nEnter answer for following question again\n")
                    print("\n", ques["question"])
                    ans = int(input("Enter 1 for True, or 2 for False: "))
                    
                # compare
                if (ans == 1) == ques["answer"]:
                    print("\nAnswer Correct!\nwell done!")
                    correct += 10
                else:
                    print("\nIncorrect\nCorrect answer is", ques["answer"])
            
            print("\nAll question answered, score displayed below\n")
            
            #score 
            dis_score(correct)
        elif choice == 2:
            print('\nTerminate Program....')
        else:
            print('INVALID Entry!!!!')
            print('Enter a valid choice')

if __name__ == "__main__":
	main()

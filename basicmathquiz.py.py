import random
def generate_question():
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    operator=random.choice(['+','-','x','/'])
    if operator=='+':
        answer=num1+num2
    elif operator=='-':
        answer=num1-num2
    elif operator=='x':
        answer=num1*num2
    elif operator=='/':
        answer=num1/num2
    return f"{num1}{operator}{num2}",answer
def math_quiz():
    score=0
    rounds=5
    print("welcome my basic math quiz")
    for i in range(rounds):
         question,correct_answer=generate_question()
         print(f"question {i+1} {question}")
         user_answer=int(input("your answer"))
         if correct_answer==user_answer:
             print("correct")
             score+=1
         else:
             print(f"wrong answer! correct answer is {correct_answer}")
    print("game over")
    print(f"your final result after {score} out of 10")
    if score==rounds:
        print("perfect")
    elif score>=rounds//2:
        print("good job")
    else:
        print("work hard")
math_quiz()
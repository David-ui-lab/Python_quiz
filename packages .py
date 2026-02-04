import random
run = True
questions  = ["What is the capital of Nepal?", "What is the square root of 16?", "What is the highest mountain in the world?"]

answers = ["Kathmandu", "4", "Mt. Everest"]

options= [["Kathmandu", "Pokhara", "Lalitpur"], ["2", "4", "8"], ["Mt. Everest", "K2", "Kanchanjunga"]]

while run:

    q = random.choice(questions)
    print(q)

    for i in range(len(questions)):
        if questions[i] == q:
            print(f"options: {options[i]}")
            answer = answers[i]
            opt = options[i]
       
    ans = input("Input the correct answer: ")

    if ans.lower() == answer.lower():
        print("Correct")
    elif ans.lower() not in opt:
        print("Try again with a valid option")
    else:
        print("Incorrect")

    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        run = False
    
    qq_dd = input("Do you want to add a question? (yes/no): ")

    if qq_dd.lower()== "yes":
        new_q = input("Enter a new question:")
        questions.append(new_q)
        new_ans = input("Enter the answer to the question:")
        answers.append(new_ans)
        new_opts = []
        new_opts = input("Enter options separated by commas:").split(",")
        options.append(new_opts)

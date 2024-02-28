questions = ("Which city has been renamed as ‘Chatrapati Sambhajinagar’?: ",
                       "How many time zones are there in Russia? : ",
                       "Where is India's Silicon Valley located? : ",
                       "How many breaths does the average human take in a day?: ",
                       "Which planet rotates on its side?: ")

options = (("A. Bangalore", "B. Chennai", "C. Aurangabad", "D. Hyderabad "),
                   ("A. 16", "B. 5", "C. 3", "D. 11"),
                   ("A. Bangalore", "B. Hyderabad", "C. Chennai", "D. Delhi"),
                   ("A. 20,000", "B. 21107", "C. 12016", "D. 17942"),
                   ("A. Mercury", "B. Uranus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

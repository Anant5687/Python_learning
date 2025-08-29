start_quiz = input("Do you want to play a quiz? ");

if start_quiz.lower() != 'yes':
    quit();
print("Lets start a quiz :)");

questions_answers = [
  { "ques": "Who was the first Prime Minister of India?", "ans": "Jawaharlal Nehru" },
  { "ques": "What is the capital city of Australia?", "ans": "Canberra" },
  { "ques": "Which planet is known as the 'Red Planet'?", "ans": "Mars" },
  { "ques": "In JavaScript, what will typeof null return?", "ans": "object" },
  { "ques": "Which company developed React.js?", "ans": "Facebook (now Meta)" },
  { "ques": "In databases, what does ACID stand for?", "ans": "Atomicity, Consistency, Isolation, Durability" },
  { "ques": "If 5 machines take 5 minutes to make 5 widgets, how long would 100 machines take to make 100 widgets?", "ans": "5 minutes" },
  { "ques": "A man has 53 socks: 21 blue, 15 black, and 17 red. How many socks must he pull out in the dark to guarantee a pair of the same color?", "ans": "4 socks" },
  { "ques": "What comes next in the sequence: 2, 6, 12, 20, ?", "ans": "30" },
  { "ques": "What is always in front of you but can’t be seen?", "ans": "The future" }
]

right_ans = 0;
wrong_ans = 0;

for ques in questions_answers:
    answer = input(f"{ques['ques']} ")

    if answer.lower() == ques['ans'].lower():
        right_ans += 1
        print("Hurrah! Correct answer :)")
    else: 
        wrong_ans += 1;
        print("Wrong Answer");

print(f"You gave {right_ans} correct answers, {wrong_ans} wrong answers, out of {len(questions_answers)} questions")
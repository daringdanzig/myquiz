# !python3
# coding: UTF-8

import random
import csv

data = {}
csv_file = open("./QUIZ.csv", "r", encoding="utf_8", errors="", newline="" )
word_quiz = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
for row in word_quiz:
    data[row['用語']] = row['意味']

for quiz_num in range(1):
    quiz_file = open('randomquiz{}.txt'.format(quiz_num + 1), 'w')
    answer_key_file = open('randomquiz_answers{}.txt'.format(quiz_num + 1), 'w')

    quiz_file.write('名前:\n\n日付:\n\n学期:\n\n')
    quiz_file.write((' ' * 28) + '四択クイズ(問題番号{})'.format(quiz_num + 1))
    quiz_file.write('\n\n')

    questions = list(data.keys())
    random.shuffle(questions)

    for question_num in range(len(questions)):
        correct_answer = data[questions[question_num]]
        wrong_answers = list(data.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quiz_file.write('{}.{}の意味を次から選びなさい。\n'.format(question_num + 1, questions[question_num]))
        for i in range(4):
            quiz_file.write('{}.{}\n'.format('ABCD'[i], answer_options[i]))

        quiz_file.write('\n')

        answer_key_file.write('{}.{}\n'.format(question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))

    quiz_file.close()
    answer_key_file.close()
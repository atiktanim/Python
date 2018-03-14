import random

Zilla = {'Chandpur': 'Ilish', 'Dhaka': 'Biriany', 'Rajshahi': 'Mango',
         'Comilla': 'Roshmalai', 'ChapaiNababganz': 'pera', 'Bogura': 'Doi',
         'Nator': 'kachagolla', 'Chittagong': 'Shutki', 'Khulna': 'Modhu',
         'Barisal': 'Guazava'
         }

# Generates 5 quiz files:
for quizNum in range(5):
    # creates the quiz and answer key files
    quizFile = open('Zillasquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('Zillasquiz_answers%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'Zilla favourite things quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # shuffle the orders of the state.
    zillaName = list(Zilla.keys())
    random.shuffle(zillaName)

    # Loop through all 10 states,making a question for each.
    for questionNum in range(10):

        correctAnswer = Zilla[zillaName[questionNum]]
        wrongAnswers = list(Zilla.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

       # Write the question and the answer options to the quiz file.

        quizFile.write('%s.What is the famous thing of %s?\n' % (questionNum + 1, zillaName[questionNum]))

        for i in range(4):
            quizFile.write('    %s. %s\n'%('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

    # Write answer key to File
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()


















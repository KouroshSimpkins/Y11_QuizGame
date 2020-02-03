import sqlite3
from random import randint

Questions = []
Answers = []
Cor_Ans = []


def data_load():

    conn = sqlite3.connect('Quiz.db')
    c = conn.cursor()

    for row in c.execute('SELECT Question FROM comp_quiz'):
        Questions.append(row)
    for row in c.execute('SELECT Correct_Ans FROM comp_quiz'):
        Cor_Ans.append(row)
    for row in c.execute('SELECT Ans_1, Ans_2, Ans_3, Ans_4 FROM comp_quiz'):
        Answers.append(row)


'''
Each list must be treated as a multidimensional array, even if they only have one value.
Only way to present the info is as below

print(Questions[0][0])
print(Cor_Ans[0][0])
print(Answers[0][0])
'''

order = randint(0, len(Questions))

if __name__ == '__main__':
    print("Multiple Choice Quiz")
    print("Please Select a connected database:")
    print()

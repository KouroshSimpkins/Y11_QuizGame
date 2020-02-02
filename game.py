import sqlite3

questions = []
Answers = []

conn = sqlite3.connect('Quiz.db')
c = conn.cursor()

for row in c.execute('SELECT Question FROM comp_quiz'):
    questions.append(row)

print(questions[0])

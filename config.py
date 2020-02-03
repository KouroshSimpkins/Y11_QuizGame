'''
This document is for configuring the database and the questions within it
At some point I will make it easier to load questions into the database.
Currently it's just easier to type out the questions.
I'd like to be able to import a preformatted text file that is then downloaded to the database, but I'm currently still building out the system.
'''

import sqlite3

conn = sqlite3.connect('Quiz.db')

c = conn.cursor()
"""
c.execute('''CREATE TABLE comp_quiz
             (Question, Correct_Ans, Ans_1, Ans_2, Ans_3, Ans_4)''')
"""

# Use the placeholder below to add more questions and answers to the quiz.
questions = [('Question','Correct Answer (number)','Answer','Answer','Answer','Answer')]

c.executemany('INSERT INTO comp_quiz VALUES (?,?,?,?,?,?)', questions)

conn.commit()
conn.close()

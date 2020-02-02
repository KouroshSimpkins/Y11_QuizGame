'''
This document is for configuring the database and the questions within it
At some point I will make it easier to load questions into the database.
Currently it's just easier to type out the questions.
I'd like to be able to import a preformatted text file that is then downloaded to the database, but I'm currently still building out the system.
'''

import sqlite3

conn = sqlite3.connect('Quiz.db')

c = conn.cursor()

c.execute('''CREATE TABLE comp_quiz
             (Question, Correct_Ans, Ans_1, Ans_2, Ans_3, Ans_4)''')

questions = [('What are computer chips usually made of?','2','Iron','Silicon','Copper','Gold'),
             ('How many bytes are in one Kilobyte?','1','1024','1000','1023','1000'),
             ('What does LAN stand for?','2','Logical Access Network','Local Area Network','Logic And Numbers','Local Access Netowrk'),
             ('What does the CPU do?','4','Stores Data','Processes Data','Controls Hardware','Performs Logic Functions'),
             ('When does RAM dump its data?','3','Never','When there is no RAM left','When the system turns off','When it is removed')]
c.executemany('INSERT INTO comp_quiz VALUES (?,?,?,?,?,?)', questions)

conn.commit()
conn.close()

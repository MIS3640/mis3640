import dbm
import random

ROSTER = ["John", "Paul", "George", "Ringo"]
GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-"]

db = dbm.open("data/db_student.db", "c")

for student in ROSTER:
    db[student] = random.choice(GRADES)

for key in db:
    print(key, db[key])


db.close()

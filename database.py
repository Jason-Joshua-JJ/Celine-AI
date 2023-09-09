import sqlite3

def create_connection():

    connection = sqlite3.connect("database.db")
    return connection

def get_questions_and_answers():

    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM QuestionsandAnswers")

    return cur.fetchall()

    #for row in cur.fetchall():
        #print(row)

#get_questions_and_answers()

def get_answer_from_database(question):
    rows = get_questions_and_answers()
    answer = ""
    #print(rows)
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
        #print(row[0])
    return answer


print(get_answer_from_database("what is the time now"))
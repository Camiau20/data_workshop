import mysql.connector
import pandas as pd
import csv



conx = mysql.connector.connect(
   host="localhost",
   user="user",
   password="password",
  database="etl"
)

mycursor = conx.cursor()


excel = "C:/etl/candidates.csv"
df = pd.read_csv(excel)
print(df)
print (len(df))


mycursor.execute("CREATE TABLE IF NOT EXISTS candidates (first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(100), application_date DATE, country VARCHAR(200), yoe INT, seniority VARCHAR(200), technology VARCHAR(200), code_challenge_score INT, technical_interview_score INT)")

query = "INSERT INTO candidates (first_name, last_name, email, application_date, country, yoe, seniority, technology, code_challenge_score, technical_interview_score) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

with open('C:/etl/candidates.csv', newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter=';')
     next(reader)  
     for row in reader:
         
         data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
         mycursor.execute(query, data)


conx.commit()
mycursor.close()
conx.close()
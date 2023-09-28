import schedule
import time
import sqlite3
import os

def next_url():
    rows = []

    if os.path.exists('../data/images_answers.db'):
        conn = sqlite3.connect('../data/images_answers.db', uri=True)
        cursor = conn.cursor()
        cursor.execute('SELECT url, answer FROM images JOIN answers ON answers.imageId = images.imageId;')
        rows = cursor.fetchall()
    else:
        print("could not source images_answers.db")


    # Get the current row from a file (or start at the beginning)
    try:
        with open('../data/current_row.txt', 'r') as f:
            current_row = int(f.read().strip())
    except:
        current_row = 0

    # If we've reached the end of the table, loop back to the beginning
    if current_row == len(rows) - 1:
        current_row = 0
    else:
        # Get the URL and answer for the current row
        current_row += 1

    # Save the current row to a file
    with open('../data/current_row.txt', 'w') as f:
        f.write(str(current_row))

# Schedule the job to run at 9am every day
schedule.every().day.at("06:00").do(next_url)
#schedule.every(5).seconds.do(next_url)

while True:
    schedule.run_pending()
    time.sleep(3600) #3600
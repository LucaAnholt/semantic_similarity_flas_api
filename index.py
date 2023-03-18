import spacy
from flask import Flask, request, jsonify
import urllib.parse
import sqlite3

app = Flask(__name__)

@app.route('/url_and_answer', methods=["GET"])
def next_url():
    conn = sqlite3.connect('images_answers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT url, answer FROM images JOIN answers ON answers.imageId = images.imageId;')
    rows = cursor.fetchall()

    # Get the current row from a file (or start at the beginning)
    try:
        with open('current_row.txt', 'r') as f:
            current_row = int(f.read().strip())
    except:
        current_row = 0

    # If we've reached the end of the table, loop back to the beginning
    if current_row >= len(rows):
        current_row = 0

    # Get the URL and answer for the current row
    url, answer = rows[current_row]
    current_row += 1

    # Save the current row to a file
    with open('current_row.txt', 'w') as f:
        f.write(str(current_row))

    return jsonify({'url': url, 'answer': answer})

@app.route('/currentImageIndex', methods=["GET"])
def current_image():
    # Get the current image index
    image_index = get_current_index()

    # Return the index and path to the image file as a JSON response
    return str(secs)

# Load the medium Spacy model
nlp = spacy.load("en_core_web_md")

@app.route("/getSemanticScore", methods=["GET"])
def get_score():
    # Get the "user_answer" and "correct_answer" query parameters
    user_answer = urllib.parse.quote(request.args.get("user_answer"))
    correct_answer = urllib.parse.quote(request.args.get("correct_answer"))
    user_answer = str(urllib.parse.unquote(user_answer).strip('"').lower())
    correct_answer = str(urllib.parse.unquote(correct_answer).strip('"').lower())
    # Compute the similarity score using the Spacy similarity method
    doc1 = nlp(user_answer)
    doc2 = nlp(correct_answer)
    similarity_score = doc1.similarity(doc2)
    
    # Return the similarity score
    return str(similarity_score)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
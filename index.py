import spacy
from flask import Flask, request
import urllib.parse
from datetime import datetime, time
import os

app = Flask(__name__)

# List of image indices (NOTE, THIS NEEDS TO BE UPDATED MANUALLY AND REFLECTS LENGTH OF SQLite DB e.g. number of images)
IMAGE_INDICES = list(range(4))

# Index of the current image
current_index = 0

def get_current_index():
    global current_index
    # Get the current time 
    x = datetime.today()
    # Define datetime for tomorrow at 9am:
    y = x.replace(day=x.day+1, hour=9, minute=0, second=0, microsecond=0)

    # If it's before the update time, return the current image index
    if x < y:
        return IMAGE_INDICES[current_index]

    # If it's after the update time, increment the index and return the new image index
    else:
        current_index = (current_index + 1) % len(IMAGE_INDICES) ##ensure cycle back if reached end of IMAGE_INDICES
        return IMAGE_INDICES[current_index]

@app.route('/CurrentImage', methods=["GET"])
def current_image():
    # Get the current image index
    image_index = get_current_index()

    # Return the index and path to the image file as a JSON response
    return str(image_index)


# Load the medium Spacy model
nlp = spacy.load("en_core_web_md")

@app.route("/GetScore", methods=["GET"])
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
    app.run(debug=True)
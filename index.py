import spacy
from flask import Flask, request
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return str("GuessInk API")

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
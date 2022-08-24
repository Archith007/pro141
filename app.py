from flask import Flask,jsonify,request
import csv

all_articles = []
liked_articles = []
unliked_articles = []
unseen_articles = []

with open("articles.csv","r",encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)

    all_articles = data[1:]

app = Flask(__name__)

@app.route('/get_article')

def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    }), 200

@app.route('/liked_article', methods=["POST"])

def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route('/unliked_article', methods=["POST"])

def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 202

@app.route('/unseen_article', methods=["POST"])

def unseen_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    unseen_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

if __name__ =="__main__":
    app.run()


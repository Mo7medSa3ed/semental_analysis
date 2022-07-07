from googletrans import Translator
from textblob import TextBlob
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/',methods=["POST"]) 
def result ():
    reviews = request.get_json()
    resultData=[]
    for review in reviews:
        text = review
        msg=''
        translator = Translator()
        res = translator.translate(text, dest='en')
        blob = TextBlob(res.text)
        if blob.sentiment.polarity > 0:
            msg= "Positive Review"
        elif blob.sentiment.polarity < 0:
            msg= "Negative Review"
        else:
            msg= "Nature Review"
        resultData.append({'text': text , 'msg':msg})    
    return jsonify(resultData)

if __name__ == '__main__':
    app.run()

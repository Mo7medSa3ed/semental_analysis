from googletrans import Translator
from textblob import TextBlob
from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=["POST"]) 
def result ():
    request_data = request.get_json()
    text = request_data['text']
    translator = Translator()
    res = translator.translate(text, dest='en')
    msg=''
    blob = TextBlob(res.text)
    if blob.sentiment.polarity > 0:
        msg= "Positive Review"
    elif blob.sentiment.polarity < 0:
        msg= "Negative Review"
    else:
        msg= "Nature Review"
    return {'msg':msg}    

if __name__ == '__main__':
    app.run()






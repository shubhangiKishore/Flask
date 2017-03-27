
from flask import Flask, render_template, request, url_for, make_response
from textblob import TextBlob

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    if request.method == 'GET':
        text = request.form['text']
        
        #va =  store(mrz, adhaar)
        return senti(text)
        
    return 

def senti(text):
    blob = TextBlob(text1)
    for sentence in blob.sentences:
        #print(sentence.sentiment.polarity)
        if(sentence.sentiment.polarity > 0):
            emotion = "Pos"
        elif (sentence.sentiment.polarity < 0):
            emotion = "Neg"
        return emotion


# Run the app :)
if __name__ == '__main__':
  app.debug = True
  app.run( )

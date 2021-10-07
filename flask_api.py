from flask import Flask,request,render_template
import pickle
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

lm=WordNetLemmatizer()

app=Flask(__name__)
rc=pickle.load(open('model.pkl','rb'))
tv=pickle.load(open('tfvect.pkl','rb'))


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    news=request.form.getlist('input_text[]')
    news=' '.join(news)
    if news.isspace():
        return render_template('index.html',predict_text="Enter Valid News")
    if len(news)<20:
        return render_template('index.html',predict_text="News too short")
    news=re.sub(r'[^\w\s]',' ',news)
    news=[lm.lemmatize(word.lower()) for word in nltk.word_tokenize(news) if lm.lemmatize(word.lower()) not in stopwords.words("english")]
    news=' '.join(news)
    print(news)
    news=tv.transform([news])
    pred=rc.predict(news)
    
    if pred==0:
        expected="Dow jones expected to be bearish tomorrow"
    else:
        expected="Dow jones expected to be bullish tomorrow"
                
    return render_template('index.html',predict_text=expected)

if __name__=='__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
from fake_news_model import check_real

app = Flask(__name__)

@app.route('/')
def home():print("")
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    news_title = request.form['news_title']
    
    # Detect if the news is real or fake
    
    if check_real(news_title):
        return render_template('real_news.html', news_title=news_title)
    else:
        return render_template('fake_news.html', news_title=news_title)

if __name__ == '__main__':
    app.run(debug=True)

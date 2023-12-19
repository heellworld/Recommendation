import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load mô hình từ file pickle
with open('ModelBERT.pkl', 'rb') as model_file:
    recommender = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Nhận dữ liệu nhập từ form
    movie_title = request.form['movie_title']
    
    # Sử dụng recommender
    result = recommender.recommend_movies(movie_title)
    
    # Trả về kết quả
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
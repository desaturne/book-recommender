from flask import Flask, render_template, request
import pickle
import numpy as np

from pathlib import Path # .pkl files not shown despite being in the same directory

# defining the base directory
BASE_DIR = Path(__file__).parent

popular_df = pickle.load(open(BASE_DIR / 'popular.pkl', 'rb'))
pt = pickle.load(open(BASE_DIR / 'pt.pkl', 'rb'))
books = pickle.load(open(BASE_DIR / 'books.pkl', 'rb'))
similarity_score = pickle.load(open(BASE_DIR / 'similarity_score.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    combined = zip(
        popular_df['Book-Title'].values,
        popular_df['Book-Author'].values,
        popular_df['Image-URL-M'].values,
        popular_df['num_ratings'].values,
        popular_df['avg_rating'].values
    )
    return render_template('index.html', books=combined)

@app.route('/recommend')
def recommend_ui():

    return render_template('recommend.html', data=None)

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    # Defensive: check if book exists in pt index
    if user_input not in pt.index:
        return render_template('recommend.html', data=None, error="Book not found! Please enter a valid book name.")

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        book_title = temp_df['Book-Title'].values[0]
        book_author = temp_df['Book-Author'].values[0]
        book_image = temp_df['Image-URL-M'].values[0]
        data.append([book_title, book_author, book_image])

    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

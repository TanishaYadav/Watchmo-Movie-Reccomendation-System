from flask import Flask, render_template, url_for, request
import utils

app = Flask(__name__)

@app.route('/home')
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        movie = request.form['movies_name']
        if movie == "":
            movie = None
        recommendation = utils.recommend(movie)
        return render_template('index.html', movies_list=utils.movies_list, movie_name=movie, recommendation = recommendation)
    else:
        return render_template('index.html', movies_list = utils.movies_list,movie_name=None )









if __name__ == "__main__":
    app.run(debug = True)
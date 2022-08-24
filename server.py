from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/')
@app.route('/play/<num>')
@app.route('/play/<num>/<color>')
def play(num=3,color='darkcyan'):
    return render_template('index.html', num_of_boxes=int(num), color_of_boxes=color)

@app.errorhandler(404)
def not_found(e):
    return f'{e}\nMake sure you follow the layout "/play/<num>/<color>"'

app.run(debug=True)
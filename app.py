from flask import Flask, html

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Productos.html')

if __name__ == '__main__':
    app.run(debug=True)

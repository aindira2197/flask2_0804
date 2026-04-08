from flask import Flask, render_template

app = Flask(__name__)

talabalar = ["Zafar", "Malika", "Ali", "Gulnora", "Bekzod"]

@app.route("/")
def index():
    talabalar.sort()
    u = len(talabalar)
    return render_template('index.html', talabalar=talabalar, u=u)

@app.route('/roy/<int:indeks>')
def url(indeks):
    t = talabalar[indeks]
    return render_template('talaba.html', t=t)

@app.route('/roy/qidiruv/<name>')
def qidiruv(name):
    if name.lower() in list(map(lambda t: t.lower(), talabalar)):
        res = name
    else:
        res = 'none'
    return render_template('find.html', res=res)

if __name__ == '__main__':
    app.run(debug=True)

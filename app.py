from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    name = "Hydman"
    age = 27
    agonys = ["膽小", "傲慢", "懶惰"]
    info = {
        "job": "工程師",
        "hobby": "打電動",
        "favorite_food": "牛肉麵",
        "favorite_color": "藍色"
    }
    return render_template('index.html', name=name, age=age, agonys=agonys, info=info)

@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        nameInput = request.form.get('name')
        return render_template("result.html", nameInput=nameInput)
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
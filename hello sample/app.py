from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1> Top ページ </h1>'


@app.route("/list")
def item_list():
    return '<h1>商品一覧ページ</h1>'


@app.route("/detail")
def item_detail():
    return '<h1>商品詳細ページ</h1>'

@app.route("/dynamic/<value>")
def dynamic_default(value):
    print(f"型:{type(value)}, 値{value}")
    return f"<h1>渡された値は「{value}」です</h1>"


@app.route("/dynamic2/<int:number>")
def dynamic_converter(number):
    print(f"型:{type(number)}, 値{number}")
    return f"<h1>渡された値は「{number}」です</h1>"


@app.route("/dynamic3/<value>/<int:number>")
def dynamic_converter_multiple(value, number):
    print(f"型:{type(value)}, 値{value}")
    print(f"型:{type(number)}, 値{number}")
    return f"<h1>渡された値は「{value}と{number}」です</h1>"


if __name__ == "__main__":
    app.run()

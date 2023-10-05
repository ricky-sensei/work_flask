from flask import Flask, render_template, url_for


class Hero():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"名前:{self.name} 年齢:{self.age}"


# インスタンス作成
app = Flask(__name__)


@app.route('/')
def show_index():
    return render_template("top.html")


@app.route('/list')
def item_list():
    return render_template('list.html')


@app.route('/detail/<int:id>')
def item_detail(id):
    return render_template('detail.html', show_id=id)


@app.route('/multiple')
def show_jinja_multiple():
    # 辞書型で渡す
    words={
        "temp":"テンプレートえんじん",
        "jinja":"じんじゃ"
    }
    return render_template('jinja/show2.html', key=words)

@app.route('/list2')
def show_jinja_list():
    hero_list = ["桃太郎", "金太郎", "うらしまたろう"]
    return render_template('jinja/show3.html', users=hero_list)


@app.route('/class')
def show_jinja_class():
    hana = Hero("花咲かじいさん", 99)
    return render_template('jinja/show4.html', user=hana)


# 制御文
# 商品クラス
class Item(object):
    """docstring for Item`."""
    def __init__(self,id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f"商品ID:{self.id} 商品名:{self.name}"
    

@app.route('/for_list')
def show_for_list():
    item_list=[Item(1, "だんご"),Item(2, "にくまん"),Item(3, "どらやき"),]
    return render_template("for_list.html", items = item_list)

if __name__ == "__main__":
    app.run()

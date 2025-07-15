from flask import Flask, request, url_for # Flask 안에 있는 request 기능을 사용

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello,kmg" # Hello,OZ라는 텍스트를 반환해주는 index 함수를 만들었고 기본 URL에 매칭한 상대

@app.route("/search")
def search():
    keyword = request.args.get('maxprice')
    return f"검색어 : {keyword}" # select * from 원두 were 종류 = keyword (브라질, 에티오피카)

@app.route("/tags")
def tags():
    keywords = request.args.getlist('tag')
    return f"태그 목록 : {keywords}"

@app.route("/shop")
def shop():
    keyword = request.args.get('keyword')
    category = request.args.get('category')
    return f"검색어 : {keyword},<br> 카테고리 : {category}"

@app.route("/filter")
def filter_items():
    filters = request.args.getlist('filter')
    return f"적용된 필터 : {filters}"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"안녕하세요, {username}님"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f" post_id : {post_id}"

@app.route("/greet/<username>/<int:age>")
def show_greet(username, age):
    return f"이름 : {username}<br>나이 : {age}"

@app.route("/hello/<username>")
def hello(username : str) -> str:
    return f"Hello, {username}"

@app.route("/calc/<int:a>/<operator>/<int:b>")
def calc(a, operator, b):
    try:
        if operator == "add":
            return f"result = {a + b}"
        elif operator == "sub":
            sub = a - b
            return f"resutl = {sub}"
        elif operator == "mul":
            mul = a * b
            return f"result = {mul}"
        elif operator == "div":
            div = a / b
            return f"result = {div}" # 0을 나누거나 3을 0으로 나누는 행위는 파이썬에서 에러로 처리합니다. -> ZeroDivisionError
        else:
            return "해당 서비스는 add(+), sub(-), mul(x), div(/)만 지원합니다."
    except ZeroDivisionError:
        return "숫자를 0으로 나눌 수 없습니다. 0이 아닌 다른 숫자를 입력하세요."
        
@app.route("/hi", endpoint = "oz_hi")
def index():
    return "Hello,kmg"

@app.route("/min/<name>", methods = ["GET"], endpoint = "hi-oz") 
def hi(name : str) -> str:
    return f"Hello, {name}"

if __name__ == '__main__':
    app.run(debug=True) # 서버를 실행하세요!

with app.test_request_context():
    print(url_for("hi-oz", name = "dldldl")) # host: 0.0.0.123/Hi/<name>
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# -----------------이 위에 부분은 복붙으로----------------
## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('HW4_onepagemall_postGet.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def order_input():
    name_receive = request.form['input_name_give']
    select_receive = request.form['input_select_give']
    address_receive = request.form['input_address_give']
    number_receive = request.form['input_number_give']
    coupon_receive = request.form['input_coupon_give']

# 2. DB에 주문(order) 정보 삽입하기
    order = {
       'input_name': name_receive,#뒤에 콤마 붙이는 것 잊지 말기
       'input_select': select_receive,
       'input_address': address_receive,
       'input_number': number_receive,
       'input_coupon': coupon_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 완료되었습니다.'})

@app.route('/orders', methods=['GET'])
def read_orders():
    #db에서 정보들 리스트 가져오기
    orders = list(db.orders.find({},{'_id':0}))#파이썬 변수 orders에 저장
    #성공 여부 확인후 주문 리스트 반환
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug=True)

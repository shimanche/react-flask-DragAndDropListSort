from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, Flask!'
  
@app.route('/getlist',methods = ['POST'])
def getItems():
  data = request.json
  items = data.get('items',[])
  
  print("items",items)
  
  return jsonify({'message': 'Items recieved'})
  

if __name__ == '__main__':
    app.run(port=8888) #mac　Sonoma使用。デフォルトの5000番はmacで使用されているのでポート番号を変更している
    # app.run(debug=True)

from flask import Flask, jsonify, request

app = Flask(__name__)

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     data = {
#         'message': 'Hello from Flask!',
#         'status': 'success'
#     }
#     return jsonify(data)

# @app.route('/api/data', methods=['POST'])
# def post_data():
#     content = request.json
#     return jsonify({
#         'received': content,
#         'message': 'Data received!'
#     })




@app.route('/api',methods=['GET'])
def hello_world():
    d={}
    d['Query'] = str(request.args['Query'])
    return jsonify(d)



# @app.route('/api', methods = ['GET'])
# def returnascii():
#     d = {}
#     inputchr = str(request.args['query'])
#     answer = str(ord(inputchr))
#     d['output'] = answer
#     return d


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


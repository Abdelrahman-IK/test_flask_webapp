from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def postJsonHandler():
    sum ={}
    try:
        content = request.get_json()
        sum['sum'] = int(content['x'])+int(content['y'])
        print(sum)
    except:
        print('Wrong Input!')
    return str(sum)


app.run(host='0.0.0.0', port=8000)
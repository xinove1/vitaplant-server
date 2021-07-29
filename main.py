from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    return 'oi'

@app.route('/api/teste/get', methods=['GET', 'POST'])
def teste_get():
    agendado = True
    if request.method == 'POST':
        request_data = request.get_json()
        humidity = request_data['humidity']
        ledR = request_data['ledR']
        ledG = request_data['ledG']
        ledB = request_data['ledB']
        #ledR = request_data['ledR']
        #if request_data:
        #    if 'humidity' in request_data:
        #        humidity = request_data['humidity']
        #    print(humidity);
        #print("humidade:" + str(humidity))
        #print("led rgb" + str(ledR) + " " + str(ledG) + " " + str(ledB))
        #print(request.headers)
        if (agendado == True):
            agendado = False
            print(request_data)
            return Response(status=201)

    else:
        instru = {
                "ledR": 0,
                "ledG": 255,
                "ledB": 0,
                "bomb": 10000
                }
        print(instru)
        return jsonify(instru)
        #return Response(status=201)
    return ("aaa");

if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request, Response, render_template, url_for, redirect

app = Flask(__name__)

NEW_ACTION = False
LED = [0, 0, 0]
HUMIDITY = 0
PUMP = 0

@app.route('/')
@app.route('/home')
def index():
    message=''
    global LED
    global HUMIDITY
    return render_template('index.html', message=message, led=LED, humidity=HUMIDITY)

@app.route('/get_form', methods=['POST'])
def get_form():
    global PUMP
    global LED
    global NEW_ACTION
    PUMP = int(request.form.get('pump')) 
    LED[0] = int(request.form.get('ledr'))
    LED[1] = int(request.form.get('ledg')) 
    LED[2] = int(request.form.get('ledb')) 
    NEW_ACTION = True
    return redirect(url_for('index'))

@app.route('/api/arduino', methods=['GET', 'POST'])
def arduino():
    global HUMIDITY
    global LED
    global NEW_ACTION
    global PUMP
    if request.method == 'POST':
        request_data = request.get_json()
        HUMIDITY = request_data['humidity']

        print("Data recebido: ")
        print(request_data)
        print()
        if (NEW_ACTION == True):
            return Response(status=201)
        else:
            LED[0] = request_data['ledR']
            LED[1] = request_data['ledG']
            LED[2] = request_data['ledB']
            return Response(status=200)
        
    else:
        instru = {
                "ledR": LED[0],
                "ledG": LED[1], 
                "ledB": LED[2],
                "bomb": PUMP
                }
        NEW_ACTION = False
        PUMP = 0
        print("Data enviado:")
        print(instru)
        print()
        return jsonify(instru)
    return ("SAIA");

if __name__ == '__main__':
    app.run()

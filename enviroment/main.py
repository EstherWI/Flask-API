from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, send
from PyQt5 import QtWidgets
import sys


app = Flask(__name__)
io = SocketIO(app)

class Paciente:
    def __init__(self, cpf, temp, freq, pressao, resp):
        self.cpf = cpf
        self.temp = temp
        self.freq = freq
        self.pressao = pressao
        self.resp = resp

p = Paciente(1,1,1,1,1)
lista = [p]

@io.on('conectPatient')
def send_message_handler(p):
    lista.append(p)
    emit('getData', p, broadcast=True)

@io.on('patients')
def message_handler(msg):
    send(lista)

@app.route('/')
def raiz():
    return 'Ola mundo'

@app.route('/doctor')
def doc():
    return render_template('doctor.html', titulo='Pacientes', patients=lista)

@app.route('/patient', methods=['GET', ])
def patient():
    return render_template('patient.html')

@app.route('/criar', methods=['POST', ])
def criar():
    cpf = request.form['cpf']
    temp = request.form['temp']
    batimentos = request.form['batimentos']
    pressao = request.form['pressao']
    resp = request.form['resp']
    paciente = Paciente(cpf, temp, batimentos, pressao, resp)
    lista.append(paciente)
    return redirect(url_for('patient'))

io.run(app, debug=True)

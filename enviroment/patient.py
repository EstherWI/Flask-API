from _typeshed import Self
import sys
from PyQt5.QtCore import Qt, QTimer
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize 

class Paciente:
    def __init__(self, cpf, temp, freq, pressao, resp):
        self.cpf = cpf
        self.temp = temp
        self.freq = freq
        self.pressao = pressao
        self.resp = resp

p = Paciente(1,1,1,1,1)
lista = [p]

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Paciente App") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Temperatura:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20) 

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

def update_patient():
    p = Paciente()
    print('Paciente:', p)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()

    # timer which repate function `display_time` every 1000ms (1s)
    timer = QTimer()
    timer.timeout.connect(update_patient)  # execute `display_time`
    timer.setInterval(1000)  # 1000ms = 1s
    timer.start()

    sys.exit(app.exec())

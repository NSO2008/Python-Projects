#import necessary modules
import sys

#Some modules that can be imported from PyQt5.QtWidgets include:
#QApplication
#QLabel
#QWidget
#QPushButton
#QLineEdit
#QComboBox
#QRadioButton
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
#This special module is used when you need to use functions with arguments
from functools import partial



def updateText(button_pressed):
    text = display.text()
    display.setText(str(text) + str(button_pressed))

def clearText():
    text = display.text()
    display.setText('')

def calculateText():
    text = display.text()
    try:
        result = eval(text)
        display.setText(str(result))
    except ZeroDivisionError:
        display.setText('∞')
    except:
        error = sys.exc_info()
        display.setText('ERROR')
        print("Here are the details of the error: ")
        print(error)
        print("The support team line is 07086018813")
        print("The support team email is obidigbondubisi71@gmail.com")


app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(100, 100, 235, 235)
window.setMaximumWidth(460)
window.setMaximumHeight(420)
window.setWindowTitle("Calculator")
general_layout = QVBoxLayout()
button_layout = QGridLayout()
display = QLineEdit()
display.setFixedHeight(35)
display.setAlignment(Qt.AlignRight)
display.setReadOnly(True)
general_layout.addWidget(display)
buttons = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '/': (0, 3),
    'C': (0, 4),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '*': (1, 3),
    '(': (1, 4),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '-': (2, 3),
    ')': (2, 4),
    '0': (3, 0),
    '00': (3, 1),
    '.': (3, 2),
    '+': (3, 3),
    '=': (3, 4),
}

for BtnText, pos in buttons.items():
    btntext = QPushButton(BtnText)
    btntext.setFixedSize(40, 40)
    if BtnText not in ['=', 'C']:
        btntext.clicked.connect(partial(updateText, BtnText))
    elif BtnText == "=":
        btntext.clicked.connect(calculateText)
    elif BtnText == "C":
        btntext.clicked.connect(clearText)
    button_layout.addWidget(btntext, pos[0], pos[1])

general_layout.addLayout(button_layout)
window.setLayout(general_layout)
window.show()
sys.exit(app.exec())

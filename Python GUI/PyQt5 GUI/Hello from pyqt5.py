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


def hello():
    who = lineEdit.text()
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello {who}")

#If your app will not accept command line arguments,
#Then put an empty list as the parameters: "[]"
#If it will then put sys.argv as the parameters
app = QApplication(sys.argv)

window_x = 100
window_y = 100
window_width = 280
window_height = 80

#Now there are different kinds of layout managers to import too!
#QHBoxLayout
#QVBoxLayout
#QGridLayout
#QFormLayout
window = QWidget()
window.setWindowTitle("Hello World!")
window.setGeometry(window_x, window_y, window_width, window_height)
window.move(60, 15)
layout_two = QVBoxLayout()
layout = QFormLayout()

btn = QPushButton("Greet")
btn.clicked.connect(hello)#Connected btn to function hello when clicked

layout_two.addWidget(btn)
lineEdit = QLineEdit("")

layout.addRow("Name: ", lineEdit)
msg = QLabel("")

layout_two.addWidget(msg)
layout_two.addLayout(layout)
window.setLayout(layout_two)

window.show()

sys.exit(app.exec())



from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QTextEdit, QVBoxLayout

app = QApplication([])

kalk_win = QWidget()
kalk_win.setWindowTitle('Калькулятор')
kalk_win.resize(250,350)
digit_text = QTextEdit()
btn_1 = QPushButton('1')
btn_2 = QPushButton('2')
btn_3 = QPushButton('3')
btn_4 = QPushButton('4')
btn_5 = QPushButton('5')
btn_6 = QPushButton('6')
btn_7 = QPushButton('7')
btn_8 = QPushButton('8')
btn_9 = QPushButton('9')
btn_CE = QPushButton('CE')
btn_plmin = QPushButton('+/-')
btn_proc = QPushButton('%')
btn_palka = QPushButton('/')
btn_koren = QPushButton('√')
btn_del = QPushButton(':')
btn_min = QPushButton('-')
btn_plus = QPushButton('+')
btn_rovn = QPushButton('=')
btn_dot = QPushButton('.')
btn_0 = QPushButton('0')



layout_disp = QHBoxLayout()
layout_disp.addWidget(digit_text)

layout_digit1 = QHBoxLayout()
layout_digit2 = QHBoxLayout()
layout_digit3 = QHBoxLayout()
layout_digit4 = QHBoxLayout()
layout_digit5 = QHBoxLayout()

layout_digit1.addWidget(btn_CE)
layout_digit1.addWidget(btn_plmin)
layout_digit1.addWidget(btn_proc)
layout_digit1.addWidget(btn_palka)

layout_digit2.addWidget(btn_7)
layout_digit2.addWidget(btn_8)
layout_digit2.addWidget(btn_9)
layout_digit2.addWidget(btn_koren)

layout_digit3.addWidget(btn_4)
layout_digit3.addWidget(btn_5)
layout_digit3.addWidget(btn_6)
layout_digit3.addWidget(btn_del)

layout_digit4.addWidget(btn_1)
layout_digit4.addWidget(btn_2)
layout_digit4.addWidget(btn_3)
layout_digit4.addWidget(btn_min)

layout_digit5.addWidget(btn_0)
layout_digit5.addWidget(btn_dot)
layout_digit5.addWidget(btn_rovn)
layout_digit5.addWidget(btn_plus)

layout_main = QVBoxLayout()
layout_main.addLayout(layout_disp)
layout_main.addLayout(layout_digit1, )
layout_main.addLayout(layout_digit2, )
layout_main.addLayout(layout_digit3, )
layout_main.addLayout(layout_digit4, ) 
layout_main.addLayout(layout_digit5, )

kalk_win.setLayout(layout_main)

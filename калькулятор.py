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
btn_umn = QPushButton('*')
btn_proc = QPushButton('%')
btn_palka = QPushButton('/')
btn_koren = QPushButton('√')
btn_del = QPushButton('/')
btn_min = QPushButton('-')
btn_plus = QPushButton('+')
btn_rovn = QPushButton('=')
btn_dot = QPushButton('.')
btn_0 = QPushButton('0')
text = ''
def click_1():
    global text
    text += '1'
    digit_text.setText(text)

def click_2():
    global text
    text += '2'
    digit_text.setText(text)

def click_3():
    global text
    text += '3'
    digit_text.setText(text)

def click_4():
    global text
    text += '4'
    digit_text.setText(text)    

def click_5():
    global text
    text += '5'
    digit_text.setText(text)

def click_6():
    global text
    text += '6'
    digit_text.setText(text)

def click_7():
    global text
    text += '7'
    digit_text.setText(text)

def click_8():
    global text
    text += '8'
    digit_text.setText(text)

def click_9():
    global text
    text += '9'
    digit_text.setText(text)

def click_0():
    global text
    text += '0'
    digit_text.setText(text)

def click_umn():
    global text
    text += '*\n'
    digit_text.setText(text)
def umn(d1,d2):
    c = d1 * d2
    return c


def click_proc():
    global text
    text = float(text)/100
    digit_text.setText(str(text))
    text = ''

# def click_palka():
#     global text
#     text += '/'
#     digit_text.setText(text)

def click_koren():
    global text
    c = pow(float(text),1/2)
    digit_text.setText(str(c))
    text = ''

def click_del():
    global text
    text += '/\n'
    digit_text.setText(text)
def delen(d1,d2):
    c = d1 / d2
    return c


def click_min():
    global text
    text += '-\n'
    digit_text.setText(text)
def visches(d1,d2):
    c = d1 - d2
    return c


def click_plus():
    global text
    text += '+\n'
    digit_text.setText(text)
def suumma(d1,d2):
    c = d1 + d2
    return c


def click_rovn():
    global text
    text += '='
    line1 = text.split('\n')
    d1 = line1[0]
    d2 = line1[1]
    znak = d1[len(d1)-1]
    d1 = d1.replace('+', '')
    d1 = d1.replace('-', '')
    d1 = d1.replace('*', '')
    d1 = d1.replace('/', '')

    d2 = d2.replace('+', '')
    d2 = d2.replace('-', '')
    d2 = d2.replace('*', '')
    d2 = d2.replace('/', '')
    d2 = d2.replace('=', '')

    
    if znak == '+':
        qqq = suumma(float(d1),float(d2))
        digit_text.setText(str(qqq))
        text = ''
    elif znak == '-':
        www = visches(float(d1),float(d2))
        digit_text.setText(str(www))
        text = '' 
    elif znak == '*':
        eee = umn(float(d1),float(d2))
        digit_text.setText(str(eee))
        text = '' 
    elif znak == '/':
        rrr = delen(float(d1),float(d2))
        digit_text.setText(str(rrr))
        text = '' 





def suumma(d1,d2):
    c = d1 + d2
    return c

def click_dot():
    global text
    text += '.'
    digit_text.setText(text)




layout_disp = QHBoxLayout()
layout_disp.addWidget(digit_text)

layout_digit1 = QHBoxLayout()
layout_digit2 = QHBoxLayout()
layout_digit3 = QHBoxLayout()
layout_digit4 = QHBoxLayout()
layout_digit5 = QHBoxLayout()

layout_digit1.addWidget(btn_CE)
layout_digit1.addWidget(btn_umn)
layout_digit1.addWidget(btn_proc)
#layout_digit1.addWidget(btn_palka)

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

btn_1.clicked.connect(click_1)
btn_2.clicked.connect(click_2)
btn_3.clicked.connect(click_3)
btn_4.clicked.connect(click_4)
btn_5.clicked.connect(click_5)
btn_6.clicked.connect(click_6)
btn_7.clicked.connect(click_7)
btn_8.clicked.connect(click_8)
btn_9.clicked.connect(click_9)
btn_0.clicked.connect(click_0)
btn_umn.clicked.connect(click_umn)
btn_proc.clicked.connect(click_proc)
# btn_palka.clicked.connect(click_palka)
btn_koren.clicked.connect(click_koren)
btn_del.clicked.connect(click_del)
btn_min.clicked.connect(click_min)
btn_plus.clicked.connect(click_plus)
btn_rovn.clicked.connect(click_rovn)
btn_dot.clicked.connect(click_dot)

# text += '1'
# digit_text.setText(text)

kalk_win.setLayout(layout_main)
kalk_win.show()
app.exec()

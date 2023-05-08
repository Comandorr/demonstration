from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, QTimer, QTime

app = QApplication([])
window = QWidget()
window.resize(400, 300)
window.show()

line_main = QVBoxLayout()

# ВИДЖЕТЫ ПЕРВОГО ЭКРАНА
s1_text1 = QLabel('Тест Руфье')
s1_text2 = QLabel('''Добро пожаловать в тест здоровья
Здесь вы сможете измерить уровень вашей сердечно-сосудистой системы
Для этого вам нужно будет замерять свой пульс
и выполнять небольшие физические нагрузки
Все нужное для этого уже есть в приложении''')
s1_knopka = QPushButton('Начать')

# ВИДЖЕТЫ ВТОРОГО ЭКРАНА
s2_text1 = QLabel('Введите свой возраст')
s2_input1 = QLineEdit()
line_h1 = QHBoxLayout()
s2_text2 = QLabel('Введите пульс в спокойном состоянии')
s2_input2 = QLineEdit()
line_h2 = QHBoxLayout()
s2_knopka = QPushButton('Далее')
s2_text3 = QLabel('Часть 1 из 2')

# ВИДЖЕТЫ ТРЕТЬЕГО ЭКРАНА
s3_timer_text = QLabel('00:00')
s3_timer_button = QPushButton('Запустить таймер')
s3_timer_button2 = QPushButton('Запустить таймер')
s3_text1 = QLabel('Введите пульс сразу после приседаний')
s3_text2 = QLabel('Введите пуль после небольшого отдыха')
s3_input1 = QLineEdit()
s3_input2 = QLineEdit()
s3_knopka = QPushButton('Узнать результат')

screen1 = [s1_text1, s1_text2, s1_knopka]
screen2 = [s2_text1, s2_input1, s2_text2, s2_input2, s2_knopka, s2_text3]
screen3 = [s3_timer_button, s3_timer_button2, s3_timer_text, s3_text1, s3_text2, s3_input1, s3_input2, s3_knopka]
screen4 = [s4_text]
for s in screen2+screen3+screen4:
	s.hide()

# ВИДЖЕТЫ ПЕРВОГО ЭКРАНА
line_main.addWidget(s1_text1, alignment = Qt.AlignCenter)
line_main.addWidget(s1_text2, alignment = Qt.AlignCenter)
line_main.addWidget(s1_knopka, alignment = Qt.AlignCenter)
# ВИДЖЕТЫ ВТОРОГО ЭКРАНА
line_h1.addWidget(s2_text1, alignment = Qt.AlignCenter)
line_h1.addWidget(s2_input1, alignment = Qt.AlignCenter)
line_h2.addWidget(s2_text2, alignment = Qt.AlignCenter)
line_h2.addWidget(s2_input2, alignment = Qt.AlignCenter)
line_main.addWidget(s2_text3, alignment = Qt.AlignCenter)
line_main.addLayout(line_h1)
line_main.addLayout(line_h2)
line_main.addWidget(s2_knopka, alignment = Qt.AlignCenter)
# ВИДЖЕТЫ ТРЕТЬЕГО ЭКРАНА
line_main.addWidget(s3_timer_text, alignment = Qt.AlignCenter)
line_main.addWidget(s3_knopka, alignment = Qt.AlignCenter)
line_h1.addWidget(s3_text1, alignment = Qt.AlignCenter)
line_h1.addWidget(s3_input1, alignment = Qt.AlignCenter)
line_h1.addWidget(s3_timer_button, alignment = Qt.AlignCenter)
line_h2.addWidget(s3_text2, alignment = Qt.AlignCenter)
line_h2.addWidget(s3_input2, alignment = Qt.AlignCenter)
line_h2.addWidget(s3_timer_button2, alignment = Qt.AlignCenter)

# ВИДЖЕТЫ ЧЕТВЕРТОГО ЭКРАНА
s4_text = QLabel('Здесь будут результаты')

count = QTime(0, 0, 10)
def time_event():
	global count
	count = count.addSecs(-1)
	s3_timer_text.setText(count.toString('mm:ss'))
	if count == QTime(0,0,0):
		timer.stop()
		count = QTime(0, 0, 10)
		s3_timer_button.show()
		s3_timer_text.hide()

timer = QTimer()
timer.timeout.connect(time_event)

def timer_start():
	global timer
	timer.start(1000)
	s3_timer_button.hide()
	s3_timer_text.show()
s3_timer_button.clicked.connect(timer_start)
s3_timer_button2.clicked.connect(timer_start)

def s1_s2():
	for s in screen1:
		s.hide()
	for s in screen2:
		s.show()
s1_knopka.clicked.connect(s1_s2)

def check(x):
	try:
		x = int(x)
		if x > 0:
			return True
		else:
			return False
	except:
		return False


def s2_s3():
	global age, p1
	age = s2_input1.text()
	p1 = s2_input2.text()
	if check(age) and check(p1):
		age = int(age)
		p1 = int(p1)
		for s in screen2:
			s.hide()
		for s in screen3:
			s.show()
	else:
		s2_text3.setText('Ошибка! Возраст и пульс должны быть больше нуля')
	s3_timer_text.hide()
s2_knopka.clicked.connect(s2_s3)

def s3_s4():
	global p2, p3
	p2 = s3_input1.text()
	p3 = s3_input2.text()
	if check(p2) and check(p3):
		p2 = int(p2)
		p3 = int(p3)
		for s in screen3:
			s.hide()
		for s in screen4:
			s.show()
	else:
		s3_text1.setText('Ошибка! Пульс должны быть больше нуля')
	s3_timer_text.hide()
s3_knopka.clicked.connect(s3_s4)

window.setLayout(line_main)
app.exec_()


from PyQt5.QtCore import Qt                        # Импортируем модуль для работы с выравниванием и другими атрибутами
from PyQt5.QtWidgets import ( 
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, 
    QGroupBox, QRadioButton,  
    QPushButton, QLabel
)
from random import shuffle as ez
from random import randint as geforgoboltus

class Question():
    def __init__(self,questionsigma,ezanswer,twowrong,threewrong,fourwrong):
        self.question = questionsigma
        self.answer1 = ezanswer
        self.wrong1 = twowrong
        self.wrong2 = threewrong
        self.wrong3 = fourwrong

question_list = list()
question_list.append(Question('Два на два','4','3','2','10'))
question_list.append(Question('50 в корне','5 на 2 в корне',"пять в корне",'пять','два на пять'))
question_list.append(Question('Семь на восемь','56','78','15','49'))
question_list.append(Question('3 в -2 степени','1/9','9','1/64','1/3'))
question_list.append(Question('4 в 3 степени','64','16','1/64','100 в корне'))
question_list.append(Question('В прямоугольном треугольнике гипотинуза равна 5 и первый катет равен 3, найти второй катет','4','16','34 в корне','я чо знаю?'))
question_list.append(Question('раскрыть скобки (a-b) в квадрате','a в квадрате - 2ab + b в квадрате','a-b','2+2','H2O+SiO3'))


# Создаем объект приложения. Это обязательная часть программы, которая запускает интерфейс.
app = QApplication([])

# === Создаем основные элементы ===

# Кнопка, которая будет использоваться для ответа на вопрос
btn_OK = QPushButton('Ответить')

# Метка с текстом вопроса
lb_Question = QLabel('Самый сложный вопрос в мире!')

# Группа для вариантов ответов
RadioGroupBox = QGroupBox("Варианты ответов")

# Радиокнопки (кнопки для выбора одного из вариантов ответа)
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

# === Создаем макет для размещения кнопок с ответами ===

# Горизонтальный макет для двух вертикальных столбцов
layout_ans1 = QHBoxLayout()   

# Два вертикальных макета для размещения кнопок по столбцам
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

# Добавляем первые два ответа в первый столбец
layout_ans2.addWidget(rbtn_1)  
layout_ans2.addWidget(rbtn_2)

# Добавляем оставшиеся два ответа во второй столбец
layout_ans3.addWidget(rbtn_3)  
layout_ans3.addWidget(rbtn_4)

# Объединяем оба столбца в общий горизонтальный макет
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

# Устанавливаем макет для группы вариантов ответов
RadioGroupBox.setLayout(layout_ans1)

# === Создаем панель для отображения результата ===

# Группа для результата теста
AnsGroupBox = QGroupBox("Результат теста")

# Метка для вывода текста "правильно" или "неправильно"
lb_Result = QLabel('прав ты или нет?')

# Метка для вывода правильного ответа
lb_Correct = QLabel('ответ будет тут!')

# Создаем вертикальный макет для панели результата
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))  # Располагаем метку результата сверху
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)  # Располагаем метку ответа по центру

# Устанавливаем макет для группы результата
AnsGroupBox.setLayout(layout_res)

# === Размещаем виджеты в окне ===

# Создаем строку для вопроса
layout_line1 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))  # Центрируем текст вопроса

# Создаем строку для размещения панелей (варианты ответов или результат)
layout_line2 = QHBoxLayout()
layout_line2.addWidget(RadioGroupBox)  # Добавляем группу с вариантами ответов
layout_line2.addWidget(AnsGroupBox)  # Добавляем группу с результатом
AnsGroupBox.hide()

# Создаем строку для кнопки "Ответить"
layout_line3 = QHBoxLayout()
layout_line3.addStretch(1)  # Добавляем отступ слева
layout_line3.addWidget(btn_OK, stretch=2)  # Центрируем и увеличиваем кнопку
layout_line3.addStretch(1)  # Добавляем отступ справа

# Создаем общий вертикальный макет для всего окна
layout_card = QVBoxLayout()

# Добавляем строки в общий макет с разным "весом" (stretch)
layout_card.addLayout(layout_line1, stretch=2)  # Вопрос
layout_card.addLayout(layout_line2, stretch=200)  # Панели
layout_card.addStretch(1)  # Отступ
layout_card.addLayout(layout_line3, stretch=1)  # Кнопка
layout_card.addStretch(1)  # Еще отступ

# Устанавливаем расстояние между элементами
layout_card.setSpacing(5)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def start_test():
    if btn_OK.text() == "Ответить":
        show_result()
    else:
        show_answer()

def show_result():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    btn_OK.setText('Следуйщий вопрос')

def show_answer():
    btn_OK.setText('Ответить')
    AnsGroupBox.hide()
    RadioGroupBox.show()

def ask(q: Question):
    ez(answers)
    answers[0].setText(q.answer1)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.answer1)
    show_answer()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Статистика:\nВсего вопросов:', window.total, '\nПравильных ответов:',window.score)
        print('Результат',(window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Бездарь")

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def next_question():
    print('Статистика:\nВсего вопросов:', window.total, '\nПравильных ответов:',window.score)
    window.total += 1
    cur_question = geforgoboltus(0,len(question_list) -1)
    ask(question_list[cur_question])

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

# === Создаем окно приложения ===

btn_OK.clicked.connect(click_OK)

# Создаем объект окна
window = QWidget()
window.total = 0
window.score = 0
window.resize(500, 300)

# Устанавливаем макет для окна
window.setLayout(layout_card)

# Устанавливаем заголовок окна
window.setWindowTitle('Memory Card')

next_question()
# Показываем окно
window.show()

# Запускаем приложение (здесь программа переходит в "бесконечный" цикл ожидания событий)
app.exec_()
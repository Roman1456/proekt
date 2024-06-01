from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500,600)

img_lbl1 = QLabel("katinka")
img_lbl2 = QLabel("katinka")
img_lbl3 = QLabel("katinka")
img_lbl4 = QLabel("katinka")
img_lbl5 = QLabel("katinka")
img_lbl6 = QLabel("katinka")
img_lbl7 = QLabel("katinka")
img_lbl8 = QLabel("katinka")
img_lbl9 = QLabel("katinka")
img_lbl10 = QLabel("katinka")
img_lbl11 = QLabel("katinka")
img_lbl12 = QLabel("katinka")
img_lbl13 = QLabel("katinka")

answer_lbl_1 = QLabel("15 L")
answer_lbl_2 = QLabel("25 L")
answer_lbl_3 = QLabel("25 L")
answer_lbl_4 = QLabel("30 L")
answer_lbl_5 = QLabel("50 L")
answer_lbl_6 = QLabel("100 L")
answer_lbl_7 = QLabel("150 L")
answer_lbl_8 = QLabel("180 L")
answer_lbl_9 = QLabel("220 L")
answer_lbl_10 = QLabel("250 L")
answer_lbl_11 = QLabel("250 L")
answer_lbl_12 = QLabel("300 L")
answer_lbl_13 = QLabel("1L = 1,5 грн.")

qest_btn1 = QPushButton("Купити")
qest_btn2 = QPushButton("Купити")
qest_btn3 = QPushButton("Купити")
qest_btn4 = QPushButton("Купити")
qest_btn5 = QPushButton("Купити")
qest_btn6 = QPushButton("Купити")
qest_btn7 = QPushButton("Купити")
qest_btn8 = QPushButton("Купити")
qest_btn9 = QPushButton("Купити")
qest_btn10 = QPushButton("Купити")
qest_btn11 = QPushButton("Купити")
qest_btn12 = QPushButton("Купити")
qest_btn13 = QPushButton("Купити")

mine_line = QVBoxLayout()



h1 = QHBoxLayout()

v1 = QVBoxLayout()
v1.addWidget(img_lbl1)
v1.addWidget(answer_lbl_1)
v1.addWidget(qest_btn1)
h1.addLayout(v1)

v2 = QVBoxLayout()
v2.addWidget(img_lbl2)
v2.addWidget(answer_lbl_2)
v2.addWidget(qest_btn2)
h1.addLayout(v2)

v3 = QVBoxLayout()
v3.addWidget(img_lbl3)
v3.addWidget(answer_lbl_3)
v3.addWidget(qest_btn3)
h1.addLayout(v3)

mine_line.addLayout(h1)






h2 = QHBoxLayout()
v1 = QVBoxLayout()
v1.addWidget(img_lbl4)
v1.addWidget(answer_lbl_4)
v1.addWidget(qest_btn4)
h2.addLayout(v1)

v2 = QVBoxLayout()
v2.addWidget(img_lbl5)
v2.addWidget(answer_lbl_5)
v2.addWidget(qest_btn5)
h2.addLayout(v2)

v3 = QVBoxLayout()
v3 = QVBoxLayout()
v3.addWidget(img_lbl6)
v3.addWidget(answer_lbl_6)
v3.addWidget(qest_btn6)
h2.addLayout(v3)

mine_line.addLayout(h2)





h3 = QHBoxLayout()
v1 = QVBoxLayout()
v1.addWidget(img_lbl7)
v1.addWidget(answer_lbl_7)
v1.addWidget(qest_btn7)
h3.addLayout(v1)

v2 = QVBoxLayout()
v2.addWidget(img_lbl8)
v2.addWidget(answer_lbl_8)
v2.addWidget(qest_btn8)
h3.addLayout(v2)

v3 = QVBoxLayout()
v3 = QVBoxLayout()
v3.addWidget(img_lbl9)
v3.addWidget(answer_lbl_9)
v3.addWidget(qest_btn9)
h3.addLayout(v3)

mine_line.addLayout(h3)



h4 = QHBoxLayout()
v1 = QVBoxLayout()
v1.addWidget(img_lbl10)
v1.addWidget(answer_lbl_10)
v1.addWidget(qest_btn10)
h4.addLayout(v1)

v2 = QVBoxLayout()
v2.addWidget(img_lbl11)
v2.addWidget(answer_lbl_11)
v2.addWidget(qest_btn11)
h4.addLayout(v2)


v3 = QVBoxLayout()
v3.addWidget(img_lbl12)
v3.addWidget(answer_lbl_12)
v3.addWidget(qest_btn12)
h4.addLayout(v3)

mine_line.addLayout(h4)

h5 = QHBoxLayout()
v1 = QVBoxLayout()
v1.addWidget(img_lbl13)
v1.addWidget(answer_lbl_13)
v1.addWidget(qest_btn13)
h5.addLayout(v1)

mine_line.addLayout(h5)







window.setLayout(mine_line)
window.show()
app.exec()
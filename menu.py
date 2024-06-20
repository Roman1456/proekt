from PyQt5.QtWidgets import *

app = QApplication([])



window = QWidget()
window.resize(500,600)


menu_qest_btn1 = QPushButton("Грати")
menu_qest_btn2 = QPushButton("Магазин")
menu_qest_btn3 = QPushButton("Інветрарь")

mine_line = QVBoxLayout()

h1 = QHBoxLayout()
h1.addWidget(menu_qest_btn1)
mine_line.addLayout(h1)

h2 = QHBoxLayout()
h2.addWidget(menu_qest_btn2)
mine_line.addLayout(h2)

h3 = QHBoxLayout()
h3.addWidget(menu_qest_btn3)
mine_line.addLayout(h3)





window.setLayout(mine_line)
window.show()
app.exec()
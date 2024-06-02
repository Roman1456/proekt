from PyQt5.QtWidgets import *


def menu_window():
    window = QDialog()
    qest_lbl = QLabel("Підтрвердіть свій вибір.")
    add_quest_btn = QPushButton("Підтвердити покупку")
    canel_quest_btn = QPushButton("Скасувати")
    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(qest_lbl)
    main_line.addLayout(h1)

    h2 = QHBoxLayout()
    h2.addWidget(canel_quest_btn)
    h2.addWidget(add_quest_btn)
    main_line.addLayout(h2)

    window.setLayout(main_line)

    window.exec()
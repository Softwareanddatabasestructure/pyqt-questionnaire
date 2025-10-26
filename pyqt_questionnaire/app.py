import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QRadioButton, 
                             QButtonGroup, QComboBox, QCheckBox, QPushButton, 
                             QMessageBox, QGroupBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class QuestionnaireApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анкета - PyQt6")
        self.setGeometry(100, 100, 400, 500)
        self.setFixedSize(400, 500)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.create_widgets(layout)
    
    def create_widgets(self, layout):
        title_label = QLabel("Заполните анкету")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 16pt; font-weight: bold; margin: 10px;")
        layout.addWidget(title_label)
        
        image_label = QLabel()
        pixmap = QPixmap(100, 50)
        pixmap.fill(Qt.GlobalColor.gray)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setStyleSheet("border: 1px solid black; margin: 5px;")
        layout.addWidget(image_label)
        
        name_layout = QHBoxLayout()
        name_label = QLabel("Имя:")
        self.name_edit = QLineEdit()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_edit)
        layout.addLayout(name_layout)
        
        gender_group = QGroupBox("Пол")
        gender_layout = QVBoxLayout()
        
        self.gender_group = QButtonGroup()
        self.male_radio = QRadioButton("Мужской")
        self.female_radio = QRadioButton("Женский")
        
        self.gender_group.addButton(self.male_radio)
        self.gender_group.addButton(self.female_radio)
        self.male_radio.setChecked(True)
        
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        gender_group.setLayout(gender_layout)
        layout.addWidget(gender_group)
        
        age_layout = QHBoxLayout()
        age_label = QLabel("Возраст:")
        self.age_combo = QComboBox()
        self.age_combo.addItems([str(i) for i in range(18, 101)])
        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_combo)
        layout.addLayout(age_layout)
        
        self.agree_check = QCheckBox("Согласен с условиями обработки данных")
        layout.addWidget(self.agree_check)
        
        self.submit_btn = QPushButton("Отправить")
        self.submit_btn.clicked.connect(self.submit_form)
        layout.addWidget(self.submit_btn)
        
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("color: blue; font-size: 10pt; margin: 10px;")
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)
        
        layout.addStretch()
    
    def submit_form(self):
        name = self.name_edit.text().strip()
        age = self.age_combo.currentText()
        
        if not name:
            QMessageBox.critical(self, "Ошибка", "Пожалуйста, введите ваше имя")
            return
        
        if not self.agree_check.isChecked():
            QMessageBox.critical(self, "Ошибка", "Необходимо согласие с условиями")
            return
        
        gender = "Мужской" if self.male_radio.isChecked() else "Женский"
        
        result_text = f"Анкета заполнена!\nИмя: {name}\nПол: {gender}\nВозраст: {age}"
        self.result_label.setText(result_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuestionnaireApp()
    window.show()
    sys.exit(app.exec())
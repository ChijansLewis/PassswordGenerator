from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel, QPushButton, QSlider, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import random
import sys

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Layouts
        mainLayout = QVBoxLayout()
        optionsLayout = QHBoxLayout()

        # Widgets
        self.chkNumbers = QCheckBox('Numbers', self)
        self.chkLowercase = QCheckBox('Lowercase letters', self)
        self.chkUppercase = QCheckBox('Uppercase letters', self)
        self.chkSymbols = QCheckBox('Symbols', self)

        # Set checkboxes to checked by default
        self.chkNumbers.setChecked(True)
        self.chkLowercase.setChecked(True)
        self.chkUppercase.setChecked(True)
        self.chkSymbols.setChecked(True)

        optionsLayout.addWidget(self.chkNumbers)
        optionsLayout.addWidget(self.chkLowercase)
        optionsLayout.addWidget(self.chkUppercase)
        optionsLayout.addWidget(self.chkSymbols)

        self.lblSlider = QLabel('Password Length: 8', self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(8, 32)
        self.slider.setValue(8)
        self.slider.valueChanged.connect(self.sliderValueChanged)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(8)


        self.txtPassword = QLineEdit(self)
        self.txtPassword.setReadOnly(True)

        btnGenerate = QPushButton('Generate', self)
        btnGenerate.clicked.connect(self.generatePassword)

        btnCopy = QPushButton('Copy', self)
        btnCopy.clicked.connect(self.copyPassword)

        btnExit = QPushButton('Exit', self)
        btnExit.clicked.connect(self.close)

        # Add widgets to layout
        mainLayout.addLayout(optionsLayout)
        mainLayout.addWidget(self.lblSlider)
        mainLayout.addWidget(self.slider)
        mainLayout.addWidget(self.txtPassword)
        mainLayout.addWidget(btnGenerate)
        mainLayout.addWidget(btnCopy)
        mainLayout.addWidget(btnExit)

        self.setLayout(mainLayout)

        # Window properties
        self.setWindowTitle('Password Generator')
        self.setGeometry(300, 300, 300, 200)

    def sliderValueChanged(self, value):
        self.lblSlider.setText(f'Password Length: {value}')

    def generatePassword(self):
        charSets = {
            'numbers': '0123456789',
            'lowercase': 'abcdefghijklmnopqrstuvwxyz',
            'uppercase': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'symbols': '!@#$%^&*()-_=+[]{}|;:,.<>?'
        }

        selectedChars = ''
        if self.chkNumbers.isChecked():
            selectedChars += charSets['numbers']
        if self.chkLowercase.isChecked():
            selectedChars += charSets['lowercase']
        if self.chkUppercase.isChecked():
            selectedChars += charSets['uppercase']
        if self.chkSymbols.isChecked():
            selectedChars += charSets['symbols']

        if not selectedChars:
            QMessageBox.warning(self, 'Error', 'Please select at least one character set!')
            return

        password = ''.join(random.choice(selectedChars) for _ in range(self.slider.value()))
        self.txtPassword.setText(password)

    def copyPassword(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.txtPassword.text())
        QMessageBox.information(self, 'Copied', 'Password copied to clipboard!')

# For testing
app = QApplication([])
window = PasswordGenerator()
window.show()
app.exec_()

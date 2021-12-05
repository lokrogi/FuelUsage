import sys
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QLineEdit
from MiniDB import MiniDB


class Window(QMainWindow, MiniDB):
    def __init__(self):
        super().__init__()

        self.clear_db()

        self.setup()

    def setup(self):
        self.setWindowTitle('Fuel usage')
        self.setFixedSize(500, 500)

        info = QLabel('To make this program works properly,\n'
                      'you need to fuel the gas fully every time.', self)
        info.setFixedSize(250, 100)
        info.move(150, 50)
        label1 = QLabel('Amount of fuel\nin liters', self)
        label1.setFixedSize(130,125)
        label1.move(20, 140)
        label2 = QLabel('Distance travelled since\nlast refueling in km', self)
        label2.setFixedSize(130, 125)
        label2.move(20, 220)

        self.line1 = QLineEdit(self)
        self.line1.setFixedWidth(330)
        self.line1.move(150, 190)
        self.line2 = QLineEdit(self)
        self.line2.setFixedWidth(330)
        self.line2.move(150, 265)

        calculate_btn = QPushButton('Calculate', self)
        calculate_btn.move(190, 300)
        general_btn = QPushButton('General usage', self)
        general_btn.move(190, 340)
        quit_btn = QPushButton('Quit', self)
        quit_btn.move(390, 460)

        calculate_btn.clicked.connect(self.calculate_usage)
        general_btn.clicked.connect(self.calculate_general_usage)
        quit_btn.clicked.connect(QApplication.instance().quit)

        self.show()

    def calculate_usage(self):
        try:
            fuel = int(self.line1.text())
            distance = int(self.line2.text())

            fuel_general = int(self.load(0)) + fuel
            distance_general = int(self.load(1)) + distance

            usage = round(fuel/(distance/100), 2)
            msg = QMessageBox()
            msg.setWindowTitle('Fuel usage')
            msg.setText(f'Average fuel usage since last\n'
                        f'refueling is {usage} l/100km.')

            self.save(fuel_general, distance_general)

            msg.exec()

        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle('Fuel usage')
            msg.setText('Use only numbers.')
            msg.exec()

    def calculate_general_usage(self):
        fuel_general = int(self.load(0))
        distance_general = int(self.load(1))

        usage_general = round(fuel_general/(distance_general/100), 2)

        msg = QMessageBox()
        msg.setWindowTitle('General fuel usage')
        msg.setText(f'In {distance_general} km, the general\n'
                    f'fuel usage is {usage_general} l/100km')
        msg.exec()

    def closeEvent(self, event: QCloseEvent):
        should_close = QMessageBox.question(self, 'Close App', 'Do you want to close?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication()
    win = Window()

    sys.exit(app.exec())

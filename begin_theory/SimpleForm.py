from PyQt5 import QtWidgets, uic
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = uic.loadUi('MyForm.ui')
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
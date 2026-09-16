from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
from funcs import *


class MainWindow(QMainWindow):
    def __init__(self, poke_id, poke_name, types):
        super().__init__()
        self.setWindowTitle("Scuffedex")
        self.setGeometry(0, 0, 1000, 1000)
        self.setWindowIcon(QIcon("img/scuffeball.png"))
        label = QLabel(f"#{poke_id} {poke_name} {types}", self)
        label.setFont(QFont("Arial", 50))
        label.setGeometry(0, 0, 1000, 1000)
        label.setStyleSheet("color: pink;"
                            "background-color: black;"
                            "font-weight: bold;")

def main():

    running = True
    while running:
        poke_request = input("Type a Pokemon name (press q to quit): ")

        poke_info = get_poke_info(poke_request)

        if poke_info:
            this_poke_id = get_id(poke_info)
            this_poke_name = get_name(poke_info).capitalize()
            this_poke_types = get_types(poke_info)
            app = QApplication(sys.argv)
            window = MainWindow(this_poke_id, this_poke_name, this_poke_types)
            window.show()
            sys.exit(app.exec_())

        elif poke_request == "q":
            running = False
            break
        else:
            print(f"No info available for {poke_request}!")


if __name__ == "__main__":
    main()

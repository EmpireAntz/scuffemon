import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from funcs import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scuffedex")
        self.setGeometry(0, 0, 1000, 1000)
        self.setStyleSheet("background-color: #000000;")
        self.setWindowIcon(QIcon("img/scuffeball.png"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        scroll_widget = QWidget()
        vbox = QVBoxLayout(scroll_widget)

        all_pokemon = show_all_pokemon()["results"]
        for pokemon in all_pokemon:
            poke = get_poke_info(pokemon['name'])
            poke_name = get_name(poke)
            poke_id = get_id(poke)
            poke_types = get_types(poke)[0]
            match poke_types:
                case "normal":
                    bg_color = "#3d3d3d"
                case "fire":
                    bg_color = "#fa4c2d"
                case "water":
                    bg_color = "#115ffa"
                case "grass":
                    bg_color = "#129439"
                case "electric":
                    bg_color = "#f2e038"
                case "ice":
                    bg_color = "#69fffc"
                case "fighting":
                    bg_color = "#753d0c"
                case "poison":
                    bg_color = "#6a08a3"
                case "ground": 
                    bg_color = "#a69753"
                case "flying":
                    bg_color = "#7584d1"
                case "psychic":
                    bg_color = "#d035e8"
                case "bug":
                    bg_color = "#97ab3f"
                case "rock":
                    bg_color = "#706753"
                case "ghost":
                    bg_color = "#1c1740"
                case "dragon":
                    bg_color = "#3f3999"
                case "dark":
                    bg_color = "#21180f"
                case "steel":
                    bg_color = "#575f78"
                case "fairy":
                    bg_color = "#ec8efa"
                case _:
                    bg_color = "#000000"
            label = QLabel(f"#{poke_id} {poke_name.capitalize()} Type:{poke_types.capitalize()}")
            label.setFont(QFont("Arial", 20))
            #label.setGeometry(0, 0, 1000, 100)
            label.setStyleSheet("color: white;"
                                f"background-color: {bg_color};"
                                "font-weight: bold;")
            vbox.addWidget(label)
        scroll_area = QScrollArea()
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(scroll_area)
        central_widget.setLayout(vbox)




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        


if __name__ == "__main__":
    main()


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QGridLayout, QWidget

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Màn Hình Chơi Game")
        self.setGeometry(100, 100, 300, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()

        welcome_label = QLabel("Chào Mừng Đến Với Trò Chơi!")
        info_label = QLabel("Thông tin về trò chơi sẽ được hiển thị ở đây.")

        main_layout.addWidget(welcome_label)
        main_layout.addWidget(info_label)

        buttons = []
        for i in range(1, 10):
            button = QPushButton(f"Ô {i}")
            buttons.append(button)
            grid_layout.addWidget(button, (i-1)//3, (i-1)%3)

        main_layout.addLayout(grid_layout)

        start_button = QPushButton("Bắt Đầu")
        pause_button = QPushButton("Tạm Dừng")
        end_button = QPushButton("Kết Thúc")

        main_layout.addWidget(start_button)
        main_layout.addWidget(pause_button)
        main_layout.addWidget(end_button)

        central_widget.setLayout(main_layout)

def main():
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
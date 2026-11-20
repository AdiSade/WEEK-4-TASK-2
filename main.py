from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ice Cream Profits")
        self.resize(700, 600)

        self.temperatures = []
        self.profits = []

        self.load_button = QPushButton("Load File", self)
        self.load_button.setGeometry(20, 20, 150, 30)
        self.load_button.clicked.connect(self.load_file)

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose ice cream file", "", "CSV files (*.csv)")
        if file_name == "":
            return
        # TODO: clear the two lists
        # TODO: open the file and fill self.temperatures and self.profits
        # TODO: call self.draw_graph() at the end


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
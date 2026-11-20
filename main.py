from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from About import About


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.about_window = About()
        self.setWindowTitle("Ice Cream Profits")
        self.resize(700, 600)

        self.temperatures = []
        self.profits = []

        self.load_button = QPushButton("Load File", self)
        self.load_button.setGeometry(20, 20, 150, 30)
        self.load_button.clicked.connect(self.load_file)
        
        self.figure = Figure()
        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(530, 20, 150, 30)
        self.about_button.clicked.connect(self.show_about_window)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setParent(self)
        self.canvas.setGeometry(20, 110, 660, 470)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setGeometry(20, 65, 660, 40)

        self.draw_graph()

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose ice cream file", "", "CSV files (*.csv)")
        if file_name == "":
            return
        # TODO: clear the two lists
        # TODO: open the file and fill self.temperatures and self.profits
        # TODO: call self.draw_graph() at the end
    
    def draw_graph(self):
        # temporary graph - you will replace the content of this method
        self.ax.clear()
        self.ax.plot([1, 2, 3], [1, 4, 9])
        self.canvas.draw()

    def show_about_window(self):
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
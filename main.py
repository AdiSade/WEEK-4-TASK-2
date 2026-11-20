from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from About import About
import numpy as np


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
        
        with open("style.qss", "r") as f:
            self.setStyleSheet(f.read())

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose ice cream file", "", "CSV files (*.csv)")
        if file_name == "":
            return
        self.profits.clear()
        self.temperatures.clear()
        with open(file_name, 'r') as f:
            header = next(f)
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                data = line.split(',')
                temp = float(data[0])
                money = float(data[1])
                self.profits.append(money)
                self.temperatures.append(temp)
        self.draw_graph()
    
    def draw_graph(self):
        self.ax.clear()
        self.ax.scatter(self.temperatures, self.profits, 1)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.set_title("Profits Vs Temp")                     # כותרת לגרף
        self.ax.set_xlabel("temprature")                  # כותרת לציר X
        self.ax.set_ylabel("profits")
        if len(self.temperatures) > 1:
            slope, intercept = np.polyfit(self.temperatures, self.profits, 1)
        self.canvas.draw()

    def show_about_window(self):
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
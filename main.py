from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QFileDialog,
                               QLabel, QLineEdit)
from PySide6.QtGui import QDoubleValidator
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from About import About
import numpy as np


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.about_window = About()
        self.setWindowTitle("Ice Cream Profits")
        self.resize(700, 650)

        self.temperatures = []
        self.profits = []
        self.slope = 0
        self.intercept = 0

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
        self.predict_label = QLabel("Temperature:", self)
        self.predict_label.setGeometry(20, 600, 100, 30)

        self.predict_input = QLineEdit("", self)
        self.predict_input.setGeometry(125, 600, 80, 30)
        self.predict_input.setValidator(QDoubleValidator())

        self.predict_button = QPushButton("Predict Profit", self)
        self.predict_button.setGeometry(215, 600, 130, 30)
        self.predict_button.clicked.connect(self.predict_profit)

        self.predict_result = QLabel("", self)
        self.predict_result.setGeometry(360, 600, 320, 30)

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
        self.ax.set_xlabel("temperature")                  # כותרת לציר X
        self.ax.set_ylabel("profits")
        if len(self.temperatures) > 1:
            slope, intercept = np.polyfit(self.temperatures, self.profits, 1)
            self.slope = slope
            self.intercept = intercept
            x1 = min(self.temperatures)
            x2 = max(self.temperatures)
            y1 = slope * x1 + intercept
            y2 = slope * x2 + intercept
            self.ax.plot([x1, x2], [y1, y2], color = "red")
            self.ax.text(0.05, 0.95, f"y = {slope:.2f}x + {intercept:.2f}", transform=self.ax.transAxes)
        self.canvas.draw()

    def predict_profit(self):
        todays_temp = self.predict_input.text()
        if todays_temp == "":
            return
        if self.temperatures == []:
            self.predict_result.setText("load a file first")
            return
        todays_temp = float(todays_temp)
        expected_revenue = self.slope* todays_temp + self.intercept
        self.predict_result.setText(f"Expected profit: {expected_revenue:.2f}sheckels")

    def show_about_window(self):
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
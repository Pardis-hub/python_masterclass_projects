# imports
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
import sys

# TimerLogic class that runs the app
class TimerLogic:
    def __init__(self):
        self.remaining_seconds = 0
        self.is_running = False

        # QTimer ticks every 1 second
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tick)

        self.on_tick = None
        self.on_finished = None

    # Starts the countdown
    def start(self):
        if self.remaining_seconds > 0 and not self.is_running:
            self.is_running = True
            self.timer.start()
    # Stops the countdown
    def stop(self):
        self.is_running = False
        self.timer.stop()
    
    # Checks the remaining time and Subtracts 1 second from remaining time unless the time is finished
    def tick(self):
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            if self.on_tick:
                self.on_tick(self.remaining_seconds)
        else:
            self.timer.stop()
            self.is_running = False
            if self.on_finished:
                self.on_finished()

# CountdownApp class that creates a UI for app and interacts with TimerLogic
class CountdownApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Countdown Timer App")
        self.setFixedSize(300, 300)

        self.timer_logic = TimerLogic()
        self.timer_logic.on_tick = self.update_time_label
        self.timer_logic.on_finished = self.timer_finished

        self.create_widgets()
        self.setup_layout()
        self.setup_connections()

    # Creates widgets for the application
    def create_widgets(self):
        self.welcome_label = QLabel(text = "Welcome to my app")
        self.welcome_label.setFont(QFont("Arial", 15))
        self.time_label = QLabel(text = "00:00")
        self.time_label.setFont(QFont("Arial", 40))
        self.time_entry = QLineEdit()
        self.start_btn = QPushButton(text="Start")
        self.stop_btn = QPushButton(text="Stop")

    # Sets up the layout for widgets
    def setup_layout(self): 
        layout = QVBoxLayout() 
        layout.addWidget(self.welcome_label, alignment=Qt.AlignCenter) 
        layout.addWidget(self.time_label, alignment=Qt.AlignCenter) 
        layout.addWidget(self.time_entry, alignment=Qt.AlignCenter) 
        layout.addWidget(self.start_btn, alignment=Qt.AlignCenter) 
        layout.addWidget(self.stop_btn, alignment=Qt.AlignCenter) 
        widget = QWidget() 
        widget.setLayout(layout) 
        self.setCentralWidget(widget)

    # Makes the connections between buttons and their functions
    def setup_connections(self):
        self.start_btn.clicked.connect(self.start_counter)
        self.stop_btn.clicked.connect(self.stop_counter)

    ''' 
    Detects the time entry format, sets the starting
    time label and gives the time to TimerLogic class in seconds.
    '''
    def set_time(self):
        time = self.time_entry.text()
        # if time is in ##:## format 
        if ":" in time:
            time_min_sec = time.split(":")
            minute = int(time_min_sec[0])
            second = int(time_min_sec[1])
            self.time_label.setText(f"{minute:02d}:{second:02d}")
            self.timer_logic.remaining_seconds = minute * 60 + second
        else:
            # if the user only enters a number as the minutes
            # also checks for invalid entries like strings
            try:
                minute = int(time)
                second = 0
                self.time_label.setText(f"{minute:02d}:{second:02d}")
                self.timer_logic.remaining_seconds = minute * 60 + second
            except ValueError:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Entry Error")
                dlg.setText("Entry cannot be a string!")
                dlg.exec()
                return

    # a function that connects the start button to start function in TimerLogic
    def start_counter(self):
        self.set_time()
        self.timer_logic.start()
        
    # a function that connects the stop button to stop function in TimerLogic
    def stop_counter(self):
        self.timer_logic.is_running = False
        self.timer_logic.stop()

    # a function that updates the time label every second
    def update_time_label(self, remaining_secs):
        minute = remaining_secs // 60
        second = remaining_secs % 60
        self.time_label.setText(f"{minute:02d}:{second:02d}")

    # a fuction that runs when the coundown is finished
    def timer_finished(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Notice")
        dlg.setText("Time's up!")
        dlg.exec()
        return

# running the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CountdownApp()
    window.show()
    sys.exit(app.exec())
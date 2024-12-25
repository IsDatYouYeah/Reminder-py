from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QTabWidget, QTextEdit, QSpinBox, QMessageBox
)
from PyQt5.QtCore import Qt
import datetime
import calendar

class ReminderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reminder App")
        self.setGeometry(100, 100, 600, 700)

        self.events = []
        self.birthdays = []

        # Main layout
        self.layout = QVBoxLayout()

        # Tabs
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        # Reminder Tab
        self.reminder_tab = QWidget()
        self.setup_reminder_tab()
        self.tabs.addTab(self.reminder_tab, "Reminders")

        # Calendar Tab
        self.calendar_tab = QWidget()
        self.setup_calendar_tab()
        self.tabs.addTab(self.calendar_tab, "Calendar")

        # Fun Facts Tab
        self.facts_tab = QWidget()
        self.setup_facts_tab()
        self.tabs.addTab(self.facts_tab, "Fun Facts")

        # Birthdays Tab
        self.birthdays_tab = QWidget()
        self.setup_birthdays_tab()
        self.tabs.addTab(self.birthdays_tab, "Birthdays")

        self.setLayout(self.layout)

    def setup_reminder_tab(self):
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.event_name_input = QLineEdit()
        self.event_name_input.setPlaceholderText("Event Name")
        self.event_name_input.setStyleSheet("padding: 8px; border-radius: 10px; font-size: 14px;")
        input_layout.addWidget(self.event_name_input)

        self.event_date_input = QLineEdit()
        self.event_date_input.setPlaceholderText("Event Date (YYYY-MM-DD)")
        self.event_date_input.setStyleSheet("padding: 8px; border-radius: 10px; font-size: 14px;")
        input_layout.addWidget(self.event_date_input)

        add_button = QPushButton("Add Event")
        add_button.setStyleSheet(self.get_button_style("#4CAF50"))
        add_button.clicked.connect(self.add_event)
        input_layout.addWidget(add_button)

        layout.addLayout(input_layout)

        self.events_list = QListWidget()
        self.events_list.setStyleSheet("padding: 8px; font-size: 14px;")
        layout.addWidget(self.events_list)

        self.reminder_tab.setLayout(layout)

    def setup_calendar_tab(self):
        layout = QVBoxLayout()

        control_layout = QHBoxLayout()
        self.year_input = QSpinBox()
        self.year_input.setRange(2021, 2030)
        self.year_input.setValue(datetime.date.today().year)
        self.year_input.setStyleSheet("padding: 8px; border-radius: 10px; font-size: 14px;")
        control_layout.addWidget(self.year_input)

        self.month_input = QSpinBox()
        self.month_input.setRange(1, 12)
        self.month_input.setValue(datetime.date.today().month)
        self.month_input.setStyleSheet("padding: 8px; border-radius: 10px; font-size: 14px;")
        control_layout.addWidget(self.month_input)

        show_button = QPushButton("Show Calendar")
        show_button.setStyleSheet(self.get_button_style("#2196F3"))
        show_button.clicked.connect(self.show_calendar)
        control_layout.addWidget(show_button)

        layout.addLayout(control_layout)

        self.calendar_display = QTextEdit()
        self.calendar_display.setReadOnly(True)
        self.calendar_display.setStyleSheet("padding: 8px; font-size: 14px;")
        layout.addWidget(self.calendar_display)

        self.calendar_tab.setLayout(layout)

    def setup_facts_tab(self):
        layout = QVBoxLayout()

        facts_label = QLabel("Fun Facts about Calendars")
        facts_label.setAlignment(Qt.AlignCenter)
        facts_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(facts_label)

        facts_text = QTextEdit()
        facts_text.setReadOnly(True)
        facts_text.setStyleSheet("padding: 8px; font-size: 14px;")
        facts = (
            "1. The Gregorian calendar was introduced in 1582 by Pope Gregory XIII to replace the Julian calendar.\n\n"
            "2. A year in the Gregorian calendar is 365.2425 days long, which is why leap years exist.\n\n"
            "3. January was named after Janus, the Roman god of doors and gates.\n\n"
            "4. The month of February was added to the calendar by Numa Pompilius, the second king of Rome.\n\n"
            "5. The modern calendar is used by most countries around the world for civil purposes.\n\n"
            "6. The word 'calendar' is derived from the Latin word 'calendae,' meaning the first day of the month.\n\n"
            "7. The earliest known calendar system is over 10,000 years old, discovered in Scotland.\n\n"
        )
        facts_text.setText(facts)
        layout.addWidget(facts_text)

        self.facts_tab.setLayout(layout)

    def setup_birthdays_tab(self):
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.birthday_name_input = QLineEdit()
        self.birthday_name_input.setPlaceholderText("Name")
        self.birthday_name_input.setStyleSheet("padding: 8px; border-radius: 10px; font-size: 14px;")
        input_layout.addWidget(self.birthday_name_input)

        self.birthday_date_input = QLineEdit()
        self.birthday_date_input.setPlaceholderText("Birthday (YYYY-MM-DD)")
        self.birthday_date_input.setStyleSheet("padding: 8px; border-radius: 10px; font-size: 14px;")
        input_layout.addWidget(self.birthday_date_input)

        add_birthday_button = QPushButton("Add Birthday")
        add_birthday_button.setStyleSheet(self.get_button_style("#FF9800"))
        add_birthday_button.clicked.connect(self.add_birthday)
        input_layout.addWidget(add_birthday_button)

        layout.addLayout(input_layout)

        self.birthdays_list = QListWidget()
        self.birthdays_list.setStyleSheet("padding: 8px; font-size: 14px;")
        layout.addWidget(self.birthdays_list)

        self.birthdays_tab.setLayout(layout)

    def get_button_style(self, color):
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: {color};
                opacity: 0.8;
            }}
        """

    def add_event(self):
        name = self.event_name_input.text().strip()
        date_input = self.event_date_input.text().strip()

        try:
            event_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            self.events.append((name, event_date))
            self.events_list.addItem(f"{name} - {event_date}")
            self.event_name_input.clear()
            self.event_date_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Enter a valid date (YYYY-MM-DD).")

    def show_calendar(self):
        year = self.year_input.value()
        month = self.month_input.value()

        cal = calendar.TextCalendar().formatmonth(year, month)
        self.calendar_display.setText(cal)

    def add_birthday(self):
        name = self.birthday_name_input.text().strip()
        date_input = self.birthday_date_input.text().strip()

        try:
            birthday_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            self.birthdays.append((name, birthday_date))
            self.birthdays_list.addItem(f"{name} - {birthday_date.strftime('%B %d')}")
            self.birthday_name_input.clear()
            self.birthday_date_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Enter a valid date (YYYY-MM-DD).")

if __name__ == "__main__":
    app = QApplication([])
    window = ReminderApp()
    window.show()
    app.exec()

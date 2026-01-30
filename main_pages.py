# main_pages.py
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QMessageBox
from PySide6.QtCore import Qt
import sys
from sidebar import Sidebar

# FIXED: Import the correct functions from data.py
from data import (
    generate_dashboard_counters,  # This exists in data.py
    generate_prisoner,  # This exists in data.py
    generate_rhus,  # This exists in data.py
    match_prisoner_to_rhus  # This exists in data.py
)


# Creating widgets for the prisoners
class PrisonerWidget(QWidget):
    def __init__(self, prisoner):
        super().__init__()
        self.prisoner = prisoner

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)

        info = QVBoxLayout()

        name = QLabel(prisoner['name'])
        name.setStyleSheet("font-weight: bold;")
        info.addWidget(name)

        pid = QLabel(f"ID: {prisoner['id']}")
        pid.setStyleSheet("color: gray;")
        info.addWidget(pid)

        layout.addLayout(info)
        layout.addStretch()


# Creating the widgets for the RHUs
class RHUWidget(QWidget):
    def __init__(self, rhu, match_percent):
        super().__init__()
        self.rhu = rhu
        self.match_percent = match_percent

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        top = QHBoxLayout()

        name = QLabel(rhu['name'])
        name.setStyleSheet("color: black; font-weight: bold;")
        top.addWidget(name)

        top.addStretch()

        match_label = QLabel(f"{match_percent}% match")

        # Changing the color of the match label based on the percentage
        if match_percent >= 80:
            color = "green"
        elif match_percent >= 60:
            color = "orange"
        else:
            color = "red"

        match_label.setStyleSheet(f"background-color: {color}; color: white; padding: 2px 5px;")
        top.addWidget(match_label)

        layout.addLayout(top)


# Calling the sidebar
class Main(Sidebar):
    def __init__(self):
        super().__init__()

        # Creating attributes
        self.current_prisoner = None
        self.selected_rhu = None
        self.selected_widget = None
        self.prisoners = []
        self.rhus = []

        self.add_titles()
        self.update_dashboard()
        self.setup_matching()

    # Adding titles for each page
    def add_titles(self):
        titles = {
            "dashboard": "DASHBOARD",
            "licensemanagement_2": "LICENSE MANAGEMENT",
            "RHU_management": "RHU MANAGEMENT",
            "Allocation_matching": "ALLOCATION MATCHING",
            "Release_management": "RELEASE MANAGEMENT",
            "cost_tracking": "COST TRACKING"
        }

        for i in range(self.stackedWidget.count()):
            page = self.stackedWidget.widget(i)
            name = page.objectName()

            if name in titles:
                title_container = QWidget(page)
                title_container.setGeometry(0, 0, page.width(), 60)
                title_container.setStyleSheet("background-color: transparent;")

                title = QLabel(titles[name], title_container)
                title.setGeometry(50, 10, 400, 40)
                title.setStyleSheet("font-size: 24px; font-weight: bold; color: black;")
                title.show()

    # Updating the widgets on the dashboard counter
    def update_dashboard(self):
        counters = generate_dashboard_counters()
        self.pending_count_label.setText(str(counters['pending']))
        self.allocated_count_label.setText(str(counters['allocated']))
        self.exited_count_label.setText(str(counters['exited']))

    # Setting up the matching page
    def setup_matching(self):
        for i in range(self.stackedWidget.count()):
            page = self.stackedWidget.widget(i)
            if page.objectName() == "Allocation_matching":
                # Generate prisoners and RHUs
                self.prisoners = [generate_prisoner() for _ in range(8)]
                self.rhus = generate_rhus(10)

                # Find the prisoner list widget
                lists = page.findChildren(QListWidget)
                if lists:
                    self.prisoner_list = lists[0]
                    self.prisoner_list.itemClicked.connect(self.prisoner_selected)
                    self.load_prisoners()

                # Set search box style
                self.search_box.setStyleSheet("color: black;")

                # Find the scroll area for RHUs
                scrolls = page.findChildren(QScrollArea)
                if scrolls:
                    scroll = scrolls[0]
                    widget = scroll.widget()
                    if widget:
                        self.rhu_container = widget
                        if not self.rhu_container.layout():
                            layout = QVBoxLayout(self.rhu_container)
                            layout.setAlignment(Qt.AlignTop)
                            self.rhu_layout = layout
                        else:
                            self.rhu_layout = self.rhu_container.layout()

                # Find buttons
                self.allocate_btn = page.findChild(QPushButton, "allocate_button")
                self.cancel_btn = page.findChild(QPushButton, "cancel_button")

                if self.allocate_btn and self.cancel_btn:
                    self.allocate_btn.clicked.connect(self.allocate)
                    self.allocate_btn.setEnabled(False)
                    self.cancel_btn.clicked.connect(self.cancel)

                break

    # Function for adding prisoners to the allocation matching screen
    def load_prisoners(self):
        self.prisoner_list.clear()

        for prisoner in self.prisoners:
            widget = PrisonerWidget(prisoner)
            item = QListWidgetItem()
            item.setSizeHint(widget.sizeHint())
            self.prisoner_list.addItem(item)
            self.prisoner_list.setItemWidget(item, widget)

    # Highlighting the selected prisoner
    def prisoner_selected(self, item):
        index = self.prisoner_list.row(item)
        self.current_prisoner = self.prisoners[index]

        # Clear previous matches
        self.clear_matches()

        # Show new matches
        self.show_matches()

        self.selected_rhu = None
        self.selected_widget = None
        if self.allocate_btn:
            self.allocate_btn.setEnabled(False)

    # Clear previous RHU matches
    def clear_matches(self):
        if hasattr(self, 'rhu_layout'):
            # Remove all widgets from the layout
            while self.rhu_layout.count():
                item = self.rhu_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

    # Calculating how well the prisoner matches to the RHU
    def show_matches(self):
        if not self.current_prisoner:
            return

        # Get matched RHUs
        matches = match_prisoner_to_rhus(self.current_prisoner, self.rhus)

        # Add each match as a widget
        for rhu in matches:
            # FIXED: Use the score from match function
            match_percent = rhu['score']  # match_prisoner_to_rhus already returns percentage

            widget = RHUWidget(rhu, match_percent)

            # Connect click event
            def click_handler(event, w=widget, r=rhu):
                self.rhu_selected(w, r)

            widget.mousePressEvent = click_handler
            self.rhu_layout.addWidget(widget)

    # RHU highlighted when selected
    def rhu_selected(self, widget, rhu):
        # Reset previous selection
        if self.selected_widget:
            self.selected_widget.setStyleSheet("background-color: white;")

        self.selected_widget = widget
        self.selected_rhu = rhu

        widget.setStyleSheet("background-color: lightblue; border: 1px solid gray;")

        if self.allocate_btn:
            self.allocate_btn.setEnabled(True)

    # Function for pop up message when a license is allocated to a RHU
    def allocate(self):
        if self.current_prisoner and self.selected_rhu:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Allocation Complete")
            msg_box.setText(f"Allocated {self.current_prisoner['name']} to {self.selected_rhu['name']}")
            msg_box.setStyleSheet("QLabel { color: black; }")
            msg_box.exec()

            # Reset selection
            self.selected_widget.setStyleSheet("background-color: white;")
            self.selected_rhu = None
            self.selected_widget = None
            self.allocate_btn.setEnabled(False)

    # Functionality for the cancel button
    def cancel(self):
        if self.selected_widget:
            self.selected_widget.setStyleSheet("background-color: white;")

        self.selected_rhu = None
        self.selected_widget = None

        if self.allocate_btn:
            self.allocate_btn.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())

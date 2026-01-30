# sidebar.py
from ui_gui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class Sidebar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Gui Menu")

        # Track sidebar state
        self.sidebar_minimized = False

        # Connect sidebar navigation buttons
        self.dashboard_1.clicked.connect(self.switch_to_dashboard)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard)
        self.license_1.clicked.connect(self.switch_to_license_management)
        self.license_2.clicked.connect(self.switch_to_license_management)
        self.RHU_1.clicked.connect(self.switch_to_rhu_management)
        self.RHU_2.clicked.connect(self.switch_to_rhu_management)
        self.allocation_1.clicked.connect(self.switch_to_allocation_matching)
        self.allocation_2.clicked.connect(self.switch_to_allocation_matching)
        self.release_1.clicked.connect(self.switch_to_release_management)
        self.release_2.clicked.connect(self.switch_to_release_management)
        self.cost_1.clicked.connect(self.switch_to_cost_tracking)
        self.cost_2.clicked.connect(self.switch_to_cost_tracking)

        # Set default page
        self.stackedWidget.setCurrentWidget(self.dashboard)

    # Page switching methods
    def switch_to_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_license_management(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_rhu_management(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_allocation_matching(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_release_management(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_cost_tracking(self):
        self.stackedWidget.setCurrentIndex(5)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sidebar()
    window.show()
    sys.exit(app.exec())
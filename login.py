from main_pages import Main
from ui_login import Ui_Dialog #Create a file converting login.ui into ui_login.py
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit
import sys

class Login(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()

        #Setting up the window
        self.setupUi(self)
        self.setWindowTitle("Login")

        self.password.setEchoMode(QLineEdit.Password)  # hides the password

        #Connect button
        self.login_button.clicked.connect(self.login_function)

    #Login function executed when the login button is pressed
    def login_function(self):

        #Only gives access to the user if the password is admin
        if self.password.text() == "admin":

            self.main_window= Main() #Transitions the user to the sidebar.py
            self.main_window.show()
            self.close()
        else:
            #Pop up message for incorrect input of password
            print("Incorrect password")
            QMessageBox.critical(
                self,
                "Login Failed",
                "Incorrect password. Please try again."
            )
            self.password.clear()
            self.password.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #Creating a window instance
    login_window = Login()
    #Show the loaded UI
    login_window.show()
    sys.exit(app.exec())

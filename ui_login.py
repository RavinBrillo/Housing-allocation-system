# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(1440, 872)
        Dialog.setStyleSheet(u"QWidget{\n"
"background-color: rgb(173, 207, 239);\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 230, 591, 241))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 36pt \".AppleSystemUIFont\";")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(540, 410, 401, 41))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \".AppleSystemUIFont\";")
        self.login_button = QPushButton(Dialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(700, 540, 113, 32))
        self.login_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(610, 491, 311, 21))
        self.password.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \".AppleSystemUIFont\";")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 480, 61, 41))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \".AppleSystemUIFont\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"On License allocation housing system", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Please enter your password to access the system", None))
        self.login_button.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.password.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password:", None))
    # retranslateUi


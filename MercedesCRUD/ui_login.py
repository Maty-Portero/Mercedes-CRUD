# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1920, 1080)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 113, 960, 967))
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 1); ")
        self.label.setPixmap(QPixmap(u"../mercedes.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 113, 960, 967))
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5); ")
        self.label_2.setScaledContents(False)
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 1920, 113))
        self.label_3.setStyleSheet(u"background-color: rgb(0, 45, 107);")
        self.label_3.setScaledContents(False)
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(960, 113, 960, 967))
        self.label_4.setStyleSheet(u"background-color: #e8e8e8; ")
        self.label_4.setScaledContents(False)
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(918, 14, 85, 85))
        self.label_5.setStyleSheet(u"")
        self.label_5.setPixmap(QPixmap(u"../logo.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1168, 237, 544, 713))
        self.label_6.setStyleSheet(u"background-color: white;")
        self.label_6.setScaledContents(False)
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: black;")
        self.label_7.setGeometry(QRect(1330, 326, 220, 76))
        font = QFont()
        font.setFamilies([u"icon-ui"])
        font.setPointSize(48)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: black;")
        self.label_8.setGeometry(QRect(1206, 444, 355, 32))
        font1 = QFont()
        font1.setFamilies([u"icon-ui"])
        font1.setPointSize(20)
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: black;")
        self.label_9.setGeometry(QRect(1206, 603, 355, 32))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        
        self.lineEdit.setGeometry(QRect(1208, 482, 436, 58))
        self.lineEdit.setStyleSheet(u"background-color: rgb(235, 235, 235); color:black; font-size: 18px;")
        self.lineEdit_2 = QLineEdit(Widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(1208, 640, 436, 58))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(235, 235, 235); color:black; font-size: 18px;")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1206, 790, 180, 63))
        font2 = QFont()
        font2.setFamilies([u"icon-ui"])
        font2.setPointSize(19)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: black;\n"
"background-color: #ebebeb;")
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1493, 790, 180, 63))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(328, 340, 304, 47))
        font3 = QFont()
        font3.setFamilies([u"icon-ui"])
        font3.setPointSize(30)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: white;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 444, 930, 212))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color:white;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_12 = QLabel(Widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 36, 111, 41))
        font4 = QFont()
        font4.setFamilies([u"icon-ui"])
        font4.setPointSize(26)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: white;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1603, 36, 290, 41))
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"color: white;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_14 = QLabel(Widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1340, 810, 20, 26))
        self.label_14.setStyleSheet(u"")
        self.label_14.setPixmap(QPixmap(u"../a.png"))
        self.label_14.setScaledContents(True)
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.pushButton_2.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Widget", u"Acceso", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Correo electr\u00f3nico / usuario", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Contrase\u00f1a", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Registrar  ", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Iniciar sesi\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Mercedes-CRUD", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"- Acced\u00e9 a tu cuenta para utilizar las \n"
"funciones de tu rol \n"
"- En caso de no contar con una cuenta, envia \n"
"una solicitud de registro", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"INICIO", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Sesi\u00f3n no iniciada", None))
        self.label_14.setText("")
    # retranslateUi


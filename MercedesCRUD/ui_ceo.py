# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ceo_home.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1920, 1080)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 113, 960, 967))
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 1); ")
        self.label.setPixmap(QPixmap(u"mercedes.png"))
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
        self.label_5.setPixmap(QPixmap(u"logo.png"))
        self.label_5.setScaledContents(True)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1340, 25, 199, 63))
        font = QFont()
        font.setFamilies([u"icon-ui"])
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: black;\n"
"background-color: #ebebeb;")
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(328, 340, 304, 47))
        font1 = QFont()
        font1.setFamilies([u"icon-ui"])
        font1.setPointSize(30)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: white;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1051, 364, 199, 63))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: black;")
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1358, 364, 199, 63))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: black;")
        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1665, 364, 199, 63))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: black;")
        self.pushButton_5 = QPushButton(Widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(1051, 540, 199, 63))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: black;")
        self.pushButton_6 = QPushButton(Widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1358, 540, 199, 63))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: black;")
        self.pushButton_7 = QPushButton(Widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(1665, 540, 199, 63))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: black;")
        self.pushButton_8 = QPushButton(Widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(1204, 716, 199, 63))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: black;")
        self.pushButton_9 = QPushButton(Widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(1511, 716, 199, 63))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: black;")
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1836, 29, 56, 56))
        self.label_7.setStyleSheet(u"")
        self.label_7.setPixmap(QPixmap(u"../ola K\u00e4llenius.png"))
        self.label_7.setScaledContents(True)
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1617, 36, 209, 41))
        font2 = QFont()
        font2.setFamilies([u"icon-ui"])
        font2.setPointSize(26)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: white;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.label_10.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.label_7.raise_()
        self.label_13.raise_()

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
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Administraci\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Mercedes-CRUD", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"E-Movilidad", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Producci\u00f3n", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Ventas", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"Compras", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"Log\u00edstica", None))
        self.pushButton_7.setText(QCoreApplication.translate("Widget", u"RRHH", None))
        self.pushButton_8.setText(QCoreApplication.translate("Widget", u"Marketing", None))
        self.pushButton_9.setText(QCoreApplication.translate("Widget", u"Mantenimiento", None))
        self.label_7.setText("")
        self.label_13.setText(QCoreApplication.translate("Widget", u"Ola K\u00e4llenius", None))
    # retranslateUi


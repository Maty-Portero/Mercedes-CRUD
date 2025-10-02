# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rrhh.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 1920, 113))
        self.label_3.setStyleSheet(u"background-color: rgb(0, 45, 107);")
        self.label_3.setScaledContents(False)
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 113, 1920, 967))
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
        self.label_6.setGeometry(QRect(60, 147, 1800, 900))
        self.label_6.setStyleSheet(u"background-color: white;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 30px; /* Bordes redondeados */\n"
"    padding: 5px;")
        self.label_6.setScaledContents(False)
        self.botonAgregar = QPushButton(Widget)
        self.botonAgregar.setObjectName(u"botonAgregar")
        self.botonAgregar.setGeometry(QRect(81, 175, 278, 63))
        font = QFont()
        font.setFamilies([u"icon-ui"])
        font.setPointSize(19)
        self.botonAgregar.setFont(font)
        self.botonAgregar.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../c.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonAgregar.setIcon(icon)
        self.label_12 = QLabel(Widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 36, 361, 41))
        font1 = QFont()
        font1.setFamilies([u"icon-ui"])
        font1.setPointSize(26)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: white;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1700, 36, 126, 41))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: white;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1836, 29, 56, 56))
        self.label_7.setStyleSheet(u"")
        self.label_7.setPixmap(QPixmap(u"../perfil-de-usuario.png"))
        self.label_7.setScaledContents(True)
        self.label_14 = QLabel(Widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(391, 190, 355, 32))
        font2 = QFont()
        font2.setFamilies([u"icon-ui"])
        font2.setPointSize(20)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: black;")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 255, 1920, 3))
        self.label.setStyleSheet(u"background-color: rgb(0, 45, 107);")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 320, 1920, 3))
        self.label_2.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 385, 1920, 3))
        self.label_10.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 515, 1920, 3))
        self.label_11.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 450, 1920, 3))
        self.label_9.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_15 = QLabel(Widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(60, 645, 1920, 3))
        self.label_15.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_16 = QLabel(Widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(60, 580, 1920, 3))
        self.label_16.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_17 = QLabel(Widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(60, 710, 1920, 3))
        self.label_17.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_18 = QLabel(Widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(60, 775, 1920, 3))
        self.label_18.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_19 = QLabel(Widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(60, 840, 1920, 3))
        self.label_19.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_20 = QLabel(Widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(60, 970, 1920, 3))
        self.label_20.setStyleSheet(u"background-color: rgb(0, 45, 107);")
        self.label_21 = QLabel(Widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(60, 905, 1920, 3))
        self.label_21.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.label_35 = QLabel(Widget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(63, 262, 90, 50))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(19)
        self.label_35.setFont(font3)
        self.label_35.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid #00000;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_36 = QLabel(Widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(63, 328, 90, 50))
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid #00000;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_37 = QLabel(Widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(63, 393, 90, 50))
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid #00000;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_38 = QLabel(Widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(177, 262, 248, 50))
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: black;\n"
"\n"
"border: 2px solid #e8e8e8;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_39 = QLabel(Widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(177, 328, 248, 50))
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: black;\n"
"\n"
"border: 2px solid #e8e8e8;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_40 = QLabel(Widget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(177, 393, 248, 50))
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: black;\n"
"\n"
"border: 2px solid #e8e8e8;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botonEditar1 = QPushButton(Widget)
        self.botonEditar1.setObjectName(u"botonEditar1")
        self.botonEditar1.setGeometry(QRect(1734, 266, 42, 42))
        self.botonEditar1.setFont(font)
        self.botonEditar1.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon1 = QIcon()
        icon1.addFile(u"../edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonEditar1.setIcon(icon1)
        self.botonEditar2 = QPushButton(Widget)
        self.botonEditar2.setObjectName(u"botonEditar2")
        self.botonEditar2.setGeometry(QRect(1734, 331, 42, 42))
        self.botonEditar2.setFont(font)
        self.botonEditar2.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonEditar2.setIcon(icon1)
        self.botonEditar3 = QPushButton(Widget)
        self.botonEditar3.setObjectName(u"botonEditar3")
        self.botonEditar3.setGeometry(QRect(1734, 399, 42, 42))
        self.botonEditar3.setFont(font)
        self.botonEditar3.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonEditar3.setIcon(icon1)
        self.botonSacar2 = QPushButton(Widget)
        self.botonSacar2.setObjectName(u"botonSacar2")
        self.botonSacar2.setGeometry(QRect(1791, 331, 42, 42))
        self.botonSacar2.setFont(font)
        self.botonSacar2.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon2 = QIcon()
        icon2.addFile(u"../close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonSacar2.setIcon(icon2)
        self.botonSacar1 = QPushButton(Widget)
        self.botonSacar1.setObjectName(u"botonSacar1")
        self.botonSacar1.setGeometry(QRect(1791, 266, 42, 42))
        self.botonSacar1.setFont(font)
        self.botonSacar1.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonSacar1.setIcon(icon2)
        self.botonSacar3 = QPushButton(Widget)
        self.botonSacar3.setObjectName(u"botonSacar3")
        self.botonSacar3.setGeometry(QRect(1791, 399, 42, 42))
        self.botonSacar3.setFont(font)
        self.botonSacar3.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonSacar3.setIcon(icon2)
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.botonAgregar.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_7.raise_()
        self.label_14.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_9.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.label_40.raise_()
        self.botonEditar1.raise_()
        self.botonEditar2.raise_()
        self.botonEditar3.raise_()
        self.botonSacar2.raise_()
        self.botonSacar1.raise_()
        self.botonSacar3.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.botonAgregar.setText(QCoreApplication.translate("Widget", u" Agregar Empleados", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"RECURSOS HUMANOS", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Usuario", None))
        self.label_7.setText("")
        self.label_14.setText(QCoreApplication.translate("Widget", u"Empleados: {total}", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_9.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_35.setText(QCoreApplication.translate("Widget", u"#0001", None))
        self.label_36.setText(QCoreApplication.translate("Widget", u"#0001", None))
        self.label_37.setText(QCoreApplication.translate("Widget", u"#0001", None))
        self.label_38.setText(QCoreApplication.translate("Widget", u"Chingui Lin", None))
        self.label_39.setText(QCoreApplication.translate("Widget", u"Bebe Lin", None))
        self.label_40.setText(QCoreApplication.translate("Widget", u"Choco Lin", None))
        self.botonEditar1.setText("")
        self.botonEditar2.setText("")
        self.botonEditar3.setText("")
        self.botonSacar2.setText("")
        self.botonSacar1.setText("")
        self.botonSacar3.setText("")
    # retranslateUi


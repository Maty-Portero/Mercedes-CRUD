# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'produccion2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget, QTableWidget, QTableWidgetItem
)


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
        self.label_5.setPixmap(QPixmap(u"logo.png"))
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
        icon.addFile(u"c.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.label_7.setPixmap(QPixmap(u"perfil-de-usuario.png"))
        self.label_7.setScaledContents(True)
        self.label_14 = QLabel(Widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(366, 144, 347, 106))
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
        self.label_35.setGeometry(QRect(66, 261, 237, 50))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(19)
        self.label_35.setFont(font3)
        self.label_35.setStyleSheet(u"background-color: black;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_36 = QLabel(Widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(66, 328, 237, 50))
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"background-color: black;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_37 = QLabel(Widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(66, 393, 237, 50))
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"background-color: black;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_38 = QLabel(Widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(320, 262, 370, 50))
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
        self.label_39.setGeometry(QRect(320, 328, 370, 50))
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
        self.label_40.setGeometry(QRect(320, 393, 370, 50))
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
        icon1.addFile(u"edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon2.addFile(u"close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.label_42 = QLabel(Widget)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(320, 458, 370, 50))
        self.label_42.setFont(font3)
        self.label_42.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: black;\n"
"\n"
"border: 2px solid #e8e8e8;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botonEditar5 = QPushButton(Widget)
        self.botonEditar5.setObjectName(u"botonEditar5")
        self.botonEditar5.setGeometry(QRect(1734, 522, 42, 42))
        self.botonEditar5.setFont(font)
        self.botonEditar5.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonEditar5.setIcon(icon1)
        self.label_43 = QLabel(Widget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(66, 522, 237, 50))
        self.label_43.setFont(font3)
        self.label_43.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid #000000;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botonSacar5 = QPushButton(Widget)
        self.botonSacar5.setObjectName(u"botonSacar5")
        self.botonSacar5.setGeometry(QRect(1791, 522, 42, 42))
        self.botonSacar5.setFont(font)
        self.botonSacar5.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonSacar5.setIcon(icon2)
        self.label_44 = QLabel(Widget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(66, 458, 237, 50))
        self.label_44.setFont(font3)
        self.label_44.setStyleSheet(u"background-color: black;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botonSacar4 = QPushButton(Widget)
        self.botonSacar4.setObjectName(u"botonSacar4")
        self.botonSacar4.setGeometry(QRect(1791, 458, 42, 42))
        self.botonSacar4.setFont(font)
        self.botonSacar4.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonSacar4.setIcon(icon2)
        self.label_46 = QLabel(Widget)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(320, 522, 370, 50))
        self.label_46.setFont(font3)
        self.label_46.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: black;\n"
"\n"
"border: 2px solid #e8e8e8;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botonEditar4 = QPushButton(Widget)
        self.botonEditar4.setObjectName(u"botonEditar4")
        self.botonEditar4.setGeometry(QRect(1734, 458, 42, 42))
        self.botonEditar4.setFont(font)
        self.botonEditar4.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonEditar4.setIcon(icon1)
        self.botonProgreso4 = QPushButton(Widget)
        self.botonProgreso4.setObjectName(u"botonProgreso4")
        self.botonProgreso4.setGeometry(QRect(1490, 459, 91, 42))
        self.botonProgreso4.setFont(font)
        self.botonProgreso4.setStyleSheet(u"background-color: green;\n"
"color:white;\n"
"\n"
"border: 2px solid green;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonProgreso2 = QPushButton(Widget)
        self.botonProgreso2.setObjectName(u"botonProgreso2")
        self.botonProgreso2.setGeometry(QRect(1490, 332, 91, 42))
        self.botonProgreso2.setFont(font)
        self.botonProgreso2.setStyleSheet(u"background-color: green;\n"
"color:white;\n"
"\n"
"border: 2px solid green;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonProgreso5 = QPushButton(Widget)
        self.botonProgreso5.setObjectName(u"botonProgreso5")
        self.botonProgreso5.setGeometry(QRect(1490, 523, 91, 42))
        self.botonProgreso5.setFont(font)
        self.botonProgreso5.setStyleSheet(u"background-color: orange;\n"
"color:white;\n"
"\n"
"border: 2px solid orange;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonProgreso3 = QPushButton(Widget)
        self.botonProgreso3.setObjectName(u"botonProgreso3")
        self.botonProgreso3.setGeometry(QRect(1490, 400, 91, 42))
        self.botonProgreso3.setFont(font)
        self.botonProgreso3.setStyleSheet(u"background-color: green;\n"
"color:white;\n"
"\n"
"border: 2px solid green;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonProgreso1 = QPushButton(Widget)
        self.botonProgreso1.setObjectName(u"botonProgreso1")
        self.botonProgreso1.setGeometry(QRect(1490, 267, 91, 42))
        self.botonProgreso1.setFont(font)
        self.botonProgreso1.setStyleSheet(u"background-color: green;\n"
"color:white;\n"
"\n"
"border: 2px solid green;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_22 = QLabel(Widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(765, 174, 421, 63))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 45, 107);\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(1261, 192, 501, 31))
        self.lineEdit.setStyleSheet(u"color: black;\n"
"background-color: white;\n"
"\n"
"border: 2px solid white;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"font-size:15px;")
        self.botonBorrar = QPushButton(Widget)
        self.botonBorrar.setObjectName(u"botonBorrar")
        self.botonBorrar.setGeometry(QRect(1771, 192, 21, 31))
        self.botonBorrar.setFont(font)
        self.botonBorrar.setStyleSheet(u"color: white;\n"
"background-color: white;\n"
"\n"
"border: 2px solid white;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon3 = QIcon()
        icon3.addFile(u"close2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonBorrar.setIcon(icon3)
        self.botonBorrar.setIconSize(QSize(16, 16))
        self.botonOrdenar1 = QPushButton(Widget)
        self.botonOrdenar1.setObjectName(u"botonOrdenar1")
        self.botonOrdenar1.setGeometry(QRect(990, 180, 141, 50))
        font4 = QFont()
        font4.setFamilies([u"icon-ui"])
        self.botonOrdenar1.setFont(font4)
        self.botonOrdenar1.setStyleSheet(u"background-color: #e8e8e8;\n"
"font-size:20px;\n"
"color:black;\n"
"\n"
"\n"
"border: 2px solid #e8e8e8;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon4 = QIcon()
        icon4.addFile(u"down_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonOrdenar1.setIcon(icon4)
        self.botonBuscar = QPushButton(Widget)
        self.botonBuscar.setObjectName(u"botonBuscar")
        self.botonBuscar.setGeometry(QRect(1221, 187, 31, 41))
        self.botonBuscar.setFont(font)
        self.botonBuscar.setStyleSheet(u"color: white;\n"
"background-color: white;\n"
"\n"
"border: 2px solid white;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon5 = QIcon()
        icon5.addFile(u"search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonBuscar.setIcon(icon5)
        self.botonBuscar.setIconSize(QSize(31, 31))
        self.label_24 = QLabel(Widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(1210, 174, 598, 61))
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"color: white;\n"
"background-color: white;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.botonTareas = QPushButton(Widget)
        self.botonTareas.setObjectName(u"botonTareas")
        self.botonTareas.setGeometry(QRect(320, 25, 209, 63))
        self.botonTareas.setFont(font)
        self.botonTareas.setStyleSheet(u"background-color: #99c5ff;\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"\n"
"\n"
"")
        self.botonAlmacen = QPushButton(Widget)
        self.botonAlmacen.setObjectName(u"botonAlmacen")
        self.botonAlmacen.setGeometry(QRect(593, 25, 209, 63))
        self.botonAlmacen.setFont(font)
        self.botonAlmacen.setStyleSheet(u"background-color: #0081cc;\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"\n"
"\n"
"")
        self.label_47 = QLabel(Widget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(320, 588, 370, 50))
        self.label_47.setFont(font3)
        self.label_47.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: black;\n"
"\n"
"border: 2px solid #e8e8e8;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_45 = QLabel(Widget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(66, 588, 237, 50))
        self.label_45.setFont(font3)
        self.label_45.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid #000000;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botonEditar6 = QPushButton(Widget)
        self.botonEditar6.setObjectName(u"botonEditar6")
        self.botonEditar6.setGeometry(QRect(1734, 590, 42, 42))
        self.botonEditar6.setFont(font)
        self.botonEditar6.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonEditar6.setIcon(icon1)
        self.botonProgreso6 = QPushButton(Widget)
        self.botonProgreso6.setObjectName(u"botonProgreso6")
        self.botonProgreso6.setGeometry(QRect(1490, 590, 91, 42))
        self.botonProgreso6.setFont(font)
        self.botonProgreso6.setStyleSheet(u"background-color: red;\n"
"color:white;\n"
"\n"
"border: 2px solid red;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonSacar6 = QPushButton(Widget)
        self.botonSacar6.setObjectName(u"botonSacar6")
        self.botonSacar6.setGeometry(QRect(1791, 590, 42, 42))
        self.botonSacar6.setFont(font)
        self.botonSacar6.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonSacar6.setIcon(icon2)
        self.botonLogOut = QPushButton(Widget)
        self.botonLogOut.setObjectName(u"botonLogOut")
        self.botonLogOut.setGeometry(QRect(1420, 30, 199, 63))
        self.botonLogOut.setFont(font)
        self.botonLogOut.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: black;\n"
"background-color: #ebebeb;")
        self.botonAdmin = QPushButton(Widget)
        self.botonAdmin.setObjectName(u"botonAdmin")
        self.botonAdmin.setGeometry(QRect(1200, 30, 199, 63))
        self.botonAdmin.setFont(font)
        self.botonAdmin.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: black;\n"
"background-color: #ebebeb;")
        self.tableWidget = QTableWidget(Widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 256, 1800, 791))
        self.tableWidget.setStyleSheet(u"background-color: white;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 30px; /* Bordes redondeados */\n"
"    padding: 5px;")
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
        self.label_42.raise_()
        self.botonEditar5.raise_()
        self.label_43.raise_()
        self.botonSacar5.raise_()
        self.label_44.raise_()
        self.botonSacar4.raise_()
        self.label_46.raise_()
        self.botonEditar4.raise_()
        self.botonProgreso4.raise_()
        self.botonProgreso2.raise_()
        self.botonProgreso5.raise_()
        self.botonProgreso3.raise_()
        self.botonProgreso1.raise_()
        self.label_22.raise_()
        self.botonOrdenar1.raise_()
        self.label_24.raise_()
        self.botonBorrar.raise_()
        self.botonBuscar.raise_()
        self.lineEdit.raise_()
        self.botonTareas.raise_()
        self.botonAlmacen.raise_()
        self.label_47.raise_()
        self.label_45.raise_()
        self.botonEditar6.raise_()
        self.botonProgreso6.raise_()
        self.botonSacar6.raise_()
        self.botonLogOut.raise_()
        self.botonAdmin.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.botonAgregar.setText(QCoreApplication.translate("Widget", u" Agregar Recurso", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"PRODUCCI\u00d3N", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Usuario", None))
        self.label_7.setText("")
        self.label_14.setText(QCoreApplication.translate("Widget", u"Recursos: 6\n"
"(1 completadas)", None))
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
        self.label_35.setText(QCoreApplication.translate("Widget", u"#ACEGA", None))
        self.label_36.setText(QCoreApplication.translate("Widget", u"#TORNI", None))
        self.label_37.setText(QCoreApplication.translate("Widget", u"#OM654", None))
        self.label_38.setText(QCoreApplication.translate("Widget", u"Acero Galvanizado", None))
        self.label_39.setText(QCoreApplication.translate("Widget", u"Tornillo", None))
        self.label_40.setText(QCoreApplication.translate("Widget", u"Motor Diesel", None))
        self.botonEditar1.setText("")
        self.botonEditar2.setText("")
        self.botonEditar3.setText("")
        self.botonSacar2.setText("")
        self.botonSacar1.setText("")
        self.botonSacar3.setText("")
        self.label_42.setText(QCoreApplication.translate("Widget", u"Motor Diesel", None))
        self.botonEditar5.setText("")
        self.label_43.setText(QCoreApplication.translate("Widget", u"#M282", None))
        self.botonSacar5.setText("")
        self.label_44.setText(QCoreApplication.translate("Widget", u"#OM668", None))
        self.botonSacar4.setText("")
        self.label_46.setText(QCoreApplication.translate("Widget", u"Motor Hibrido", None))
        self.botonEditar4.setText("")
        self.botonProgreso4.setText(QCoreApplication.translate("Widget", u"100u", None))
        self.botonProgreso2.setText(QCoreApplication.translate("Widget", u"20mU", None))
        self.botonProgreso5.setText(QCoreApplication.translate("Widget", u"90u", None))
        self.botonProgreso3.setText(QCoreApplication.translate("Widget", u"100u", None))
        self.botonProgreso1.setText(QCoreApplication.translate("Widget", u"200kg", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"Ordenar por:", None))
        self.botonBorrar.setText("")
        self.botonOrdenar1.setText(QCoreApplication.translate("Widget", u"Seleccionar", None))
        self.botonBuscar.setText("")
        self.label_24.setText("")
        self.botonTareas.setText(QCoreApplication.translate("Widget", u"Tareas", None))
        self.botonAlmacen.setText(QCoreApplication.translate("Widget", u"Almac\u00e9n", None))
        self.label_47.setText(QCoreApplication.translate("Widget", u"Bateria de Litio", None))
        self.label_45.setText(QCoreApplication.translate("Widget", u"#BATLIT", None))
        self.botonEditar6.setText("")
        self.botonProgreso6.setText(QCoreApplication.translate("Widget", u"3u", None))
        self.botonSacar6.setText("")
        self.botonLogOut.setText(QCoreApplication.translate("Widget", u"Cerrar Sesi\u00f3n", None))
        self.botonAdmin.setText(QCoreApplication.translate("Widget", u"Administraci\u00f3n", None))
    # retranslateUi


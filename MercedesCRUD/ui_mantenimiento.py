# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mantenimiento.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

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
        self.label_14.setGeometry(QRect(391, 190, 381, 32))
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
        self.label_35.setStyleSheet(u"background-color: green;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid green;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_36 = QLabel(Widget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(63, 328, 90, 50))
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"background-color: green;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid green;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_37 = QLabel(Widget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(63, 393, 90, 50))
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"background-color: green;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid green;\n"
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
        self.label_42.setGeometry(QRect(180, 458, 248, 50))
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
        self.label_43.setGeometry(QRect(63, 522, 90, 50))
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
        self.label_44.setGeometry(QRect(63, 458, 90, 50))
        self.label_44.setFont(font3)
        self.label_44.setStyleSheet(u"background-color: green;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border: 2px solid green;\n"
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
        self.label_46.setGeometry(QRect(180, 522, 248, 50))
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
        self.label_41 = QLabel(Widget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(440, 264, 248, 50))
        self.label_41.setFont(font3)
        self.label_41.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_47 = QLabel(Widget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(443, 524, 248, 50))
        self.label_47.setFont(font3)
        self.label_47.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_45 = QLabel(Widget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(440, 395, 248, 50))
        self.label_45.setFont(font3)
        self.label_45.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_48 = QLabel(Widget)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(443, 460, 248, 50))
        self.label_48.setFont(font3)
        self.label_48.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_49 = QLabel(Widget)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(440, 330, 248, 50))
        self.label_49.setFont(font3)
        self.label_49.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_50 = QLabel(Widget)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(700, 330, 248, 50))
        self.label_50.setFont(font3)
        self.label_50.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_51 = QLabel(Widget)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(703, 460, 248, 50))
        self.label_51.setFont(font3)
        self.label_51.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_52 = QLabel(Widget)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(703, 524, 248, 50))
        self.label_52.setFont(font3)
        self.label_52.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_53 = QLabel(Widget)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(700, 395, 248, 50))
        self.label_53.setFont(font3)
        self.label_53.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_54 = QLabel(Widget)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(700, 264, 248, 50))
        self.label_54.setFont(font3)
        self.label_54.setStyleSheet(u"background-color: rgb(0, 45, 107);\n"
"color: white;\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botonEstado5 = QPushButton(Widget)
        self.botonEstado5.setObjectName(u"botonEstado5")
        self.botonEstado5.setGeometry(QRect(1671, 523, 51, 42))
        self.botonEstado5.setFont(font)
        self.botonEstado5.setStyleSheet(u"background-color: red;\n"
"color:white;\n"
"\n"
"border: 2px solid red;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonEstado2 = QPushButton(Widget)
        self.botonEstado2.setObjectName(u"botonEstado2")
        self.botonEstado2.setGeometry(QRect(1671, 332, 51, 42))
        self.botonEstado2.setFont(font)
        self.botonEstado2.setStyleSheet(u"background-color: green;\n"
"color:white;\n"
"\n"
"border: 2px solid green;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonEstado4 = QPushButton(Widget)
        self.botonEstado4.setObjectName(u"botonEstado4")
        self.botonEstado4.setGeometry(QRect(1671, 459, 51, 42))
        self.botonEstado4.setFont(font)
        self.botonEstado4.setStyleSheet(u"background-color: red;\n"
"color:white;\n"
"\n"
"border: 2px solid red;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonEstado3 = QPushButton(Widget)
        self.botonEstado3.setObjectName(u"botonEstado3")
        self.botonEstado3.setGeometry(QRect(1671, 400, 51, 42))
        self.botonEstado3.setFont(font)
        self.botonEstado3.setStyleSheet(u"background-color: orange;\n"
"color:white;\n"
"\n"
"border: 2px solid orange;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.botonEstado1 = QPushButton(Widget)
        self.botonEstado1.setObjectName(u"botonEstado1")
        self.botonEstado1.setGeometry(QRect(1671, 267, 51, 42))
        self.botonEstado1.setFont(font)
        self.botonEstado1.setStyleSheet(u"background-color: green;\n"
"color:white;\n"
"\n"
"border: 2px solid green;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_24 = QLabel(Widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(1210, 180, 598, 61))
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"color: white;\n"
"background-color: white;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(1261, 198, 501, 31))
        self.lineEdit.setStyleSheet(u"color: black;\n"
"background-color: white;\n"
"\n"
"border: 2px solid white;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"font-size:15px;")
        self.label_22 = QLabel(Widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(765, 180, 421, 63))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 45, 107);\n"
"\n"
"border: 2px solid #002d6b;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.botonOrdenar1 = QPushButton(Widget)
        self.botonOrdenar1.setObjectName(u"botonOrdenar1")
        self.botonOrdenar1.setGeometry(QRect(990, 186, 141, 50))
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
        icon3 = QIcon()
        icon3.addFile(u"down_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonOrdenar1.setIcon(icon3)
        self.botonBorrar = QPushButton(Widget)
        self.botonBorrar.setObjectName(u"botonBorrar")
        self.botonBorrar.setGeometry(QRect(1771, 198, 21, 31))
        self.botonBorrar.setFont(font)
        self.botonBorrar.setStyleSheet(u"color: white;\n"
"background-color: white;\n"
"\n"
"border: 2px solid white;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon4 = QIcon()
        icon4.addFile(u"close2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonBorrar.setIcon(icon4)
        self.botonBorrar.setIconSize(QSize(16, 16))
        self.botonBuscar = QPushButton(Widget)
        self.botonBuscar.setObjectName(u"botonBuscar")
        self.botonBuscar.setGeometry(QRect(1221, 193, 31, 41))
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
<<<<<<< HEAD
        self.tableWidget = QTableWidget(Widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 256, 1800, 791))
        self.tableWidget.setStyleSheet(u"background-color: white;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 30px; /* Bordes redondeados */\n"
"    padding: 5px;")
=======
>>>>>>> 8d5a7b8089c1c1362aee43bffde91a4b8f963bdd
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
        self.label_41.raise_()
        self.label_47.raise_()
        self.label_45.raise_()
        self.label_48.raise_()
        self.label_49.raise_()
        self.label_50.raise_()
        self.label_51.raise_()
        self.label_52.raise_()
        self.label_53.raise_()
        self.label_54.raise_()
        self.botonEstado5.raise_()
        self.botonEstado2.raise_()
        self.botonEstado4.raise_()
        self.botonEstado3.raise_()
        self.botonEstado1.raise_()
        self.label_24.raise_()
        self.lineEdit.raise_()
        self.label_22.raise_()
        self.botonOrdenar1.raise_()
        self.botonBorrar.raise_()
        self.botonBuscar.raise_()
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
        self.botonAgregar.setText(QCoreApplication.translate("Widget", u" Agregar Equipos", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"MANTENIMIENTO", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Usuario", None))
        self.label_7.setText("")
        self.label_14.setText(QCoreApplication.translate("Widget", u"Equipos: {total} (? conectados)", None))
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
        self.label_36.setText(QCoreApplication.translate("Widget", u"#0002", None))
        self.label_37.setText(QCoreApplication.translate("Widget", u"#0003", None))
        self.label_38.setText(QCoreApplication.translate("Widget", u"Brasil 1", None))
        self.label_39.setText(QCoreApplication.translate("Widget", u"Serverside 1", None))
        self.label_40.setText(QCoreApplication.translate("Widget", u"NAS 1", None))
        self.botonEditar1.setText("")
        self.botonEditar2.setText("")
        self.botonEditar3.setText("")
        self.botonSacar2.setText("")
        self.botonSacar1.setText("")
        self.botonSacar3.setText("")
        self.label_42.setText(QCoreApplication.translate("Widget", u"NAS 2", None))
        self.botonEditar5.setText("")
        self.label_43.setText(QCoreApplication.translate("Widget", u"#0005", None))
        self.botonSacar5.setText("")
        self.label_44.setText(QCoreApplication.translate("Widget", u"#0004", None))
        self.botonSacar4.setText("")
        self.label_46.setText(QCoreApplication.translate("Widget", u"Brasil 2", None))
        self.botonEditar4.setText("")
        self.label_41.setText(QCoreApplication.translate("Widget", u"WEB", None))
        self.label_47.setText(QCoreApplication.translate("Widget", u"WEB", None))
        self.label_45.setText(QCoreApplication.translate("Widget", u"DATOS", None))
        self.label_48.setText(QCoreApplication.translate("Widget", u"DATOS", None))
        self.label_49.setText(QCoreApplication.translate("Widget", u"INTERNO", None))
        self.label_50.setText(QCoreApplication.translate("Widget", u"192.168.34.7", None))
        self.label_51.setText(QCoreApplication.translate("Widget", u"128.0.0.2", None))
        self.label_52.setText(QCoreApplication.translate("Widget", u"23.212.35.111", None))
        self.label_53.setText(QCoreApplication.translate("Widget", u"128.0.0.1", None))
        self.label_54.setText(QCoreApplication.translate("Widget", u"23.211.34.677", None))
        self.botonEstado5.setText(QCoreApplication.translate("Widget", u"1", None))
        self.botonEstado2.setText(QCoreApplication.translate("Widget", u"OK", None))
        self.botonEstado4.setText(QCoreApplication.translate("Widget", u"1", None))
        self.botonEstado3.setText(QCoreApplication.translate("Widget", u"2", None))
        self.botonEstado1.setText(QCoreApplication.translate("Widget", u"OK", None))
        self.label_24.setText("")
        self.label_22.setText(QCoreApplication.translate("Widget", u"Ordenar por:", None))
        self.botonOrdenar1.setText(QCoreApplication.translate("Widget", u"Seleccionar", None))
        self.botonBorrar.setText("")
        self.botonBuscar.setText("")
        self.botonLogOut.setText(QCoreApplication.translate("Widget", u"Cerrar Sesi\u00f3n", None))
        self.botonAdmin.setText(QCoreApplication.translate("Widget", u"Administraci\u00f3n", None))
    # retranslateUi


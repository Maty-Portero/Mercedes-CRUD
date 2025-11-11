# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ceo_home.ui'
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
        self.botonAdmin = QPushButton(Widget)
        self.botonAdmin.setObjectName(u"botonAdmin")
        self.botonAdmin.setGeometry(QRect(680, 25, 199, 63))
        font = QFont()
        font.setFamilies([u"icon-ui"])
        font.setPointSize(19)
        self.botonAdmin.setFont(font)
        self.botonAdmin.setStyleSheet(u"border: 2px solid #000000;\n"
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
        self.botonE_movilidad = QPushButton(Widget)
        self.botonE_movilidad.setObjectName(u"botonE_movilidad")
        self.botonE_movilidad.setGeometry(QRect(980, 178, 277, 258))
        self.botonE_movilidad.setFont(font)
        self.botonE_movilidad.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1836, 29, 56, 56))
        self.label_7.setStyleSheet(u"")
        self.label_7.setPixmap(QPixmap(u"ola K\u00e4llenius.png"))
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
        self.botonProduccion = QPushButton(Widget)
        self.botonProduccion.setObjectName(u"botonProduccion")
        self.botonProduccion.setGeometry(QRect(1306, 178, 277, 258))
        self.botonProduccion.setFont(font)
        self.botonProduccion.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.botonVentas = QPushButton(Widget)
        self.botonVentas.setObjectName(u"botonVentas")
        self.botonVentas.setGeometry(QRect(1624, 178, 277, 258))
        self.botonVentas.setFont(font)
        self.botonVentas.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.botonRRHH = QPushButton(Widget)
        self.botonRRHH.setObjectName(u"botonRRHH")
        self.botonRRHH.setGeometry(QRect(1624, 480, 277, 258))
        self.botonRRHH.setFont(font)
        self.botonRRHH.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.botonLogistica = QPushButton(Widget)
        self.botonLogistica.setObjectName(u"botonLogistica")
        self.botonLogistica.setGeometry(QRect(1306, 480, 277, 258))
        self.botonLogistica.setFont(font)
        self.botonLogistica.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.botonCompras = QPushButton(Widget)
        self.botonCompras.setObjectName(u"botonCompras")
        self.botonCompras.setGeometry(QRect(980, 480, 277, 258))
        self.botonCompras.setFont(font)
        self.botonCompras.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.botonMantenimiento = QPushButton(Widget)
        self.botonMantenimiento.setObjectName(u"botonMantenimiento")
        self.botonMantenimiento.setGeometry(QRect(1466, 783, 277, 258))
        self.botonMantenimiento.setFont(font)
        self.botonMantenimiento.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.botonMarketing = QPushButton(Widget)
        self.botonMarketing.setObjectName(u"botonMarketing")
        self.botonMarketing.setGeometry(QRect(1140, 783, 277, 258))
        self.botonMarketing.setFont(font)
        self.botonMarketing.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.label_12 = QLabel(Widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 36, 111, 41))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: white;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
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
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.botonAdmin.raise_()
        self.label_10.raise_()
        self.botonE_movilidad.raise_()
        self.label_7.raise_()
        self.label_13.raise_()
        self.botonProduccion.raise_()
        self.botonVentas.raise_()
        self.botonRRHH.raise_()
        self.botonLogistica.raise_()
        self.botonCompras.raise_()
        self.botonMantenimiento.raise_()
        self.botonMarketing.raise_()
        self.label_12.raise_()
        self.botonLogOut.raise_()

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
        self.botonAdmin.setText(QCoreApplication.translate("Widget", u"Administraci\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Mercedes-CRUD", None))
        self.botonE_movilidad.setText(QCoreApplication.translate("Widget", u"E-Movilidad", None))
        self.label_7.setText("")
        self.label_13.setText(QCoreApplication.translate("Widget", u"Ola K\u00e4llenius", None))
        self.botonProduccion.setText(QCoreApplication.translate("Widget", u"Producci\u00f3n", None))
        self.botonVentas.setText(QCoreApplication.translate("Widget", u"Ventas", None))
        self.botonRRHH.setText(QCoreApplication.translate("Widget", u"RR.HH.", None))
        self.botonLogistica.setText(QCoreApplication.translate("Widget", u"Log\u00edstica", None))
        self.botonCompras.setText(QCoreApplication.translate("Widget", u"Compras", None))
        self.botonMantenimiento.setText(QCoreApplication.translate("Widget", u"Mantenimiento", None))
        self.botonMarketing.setText(QCoreApplication.translate("Widget", u"Marketing", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"INICIO", None))
        self.botonLogOut.setText(QCoreApplication.translate("Widget", u"Cerrar Sesi\u00f3n", None))
    # retranslateUi


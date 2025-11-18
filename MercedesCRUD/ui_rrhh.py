# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rrhh.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
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
        self.label_5.setPixmap(QPixmap(u"logo.png"))
        self.label_5.setScaledContents(True)
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
        self.label_12.setGeometry(QRect(30, 36, 381, 41))
        font1 = QFont()
        font1.setFamilies([u"icon-ui"])
        font1.setPointSize(26)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: white;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
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
        self.label_20 = QLabel(Widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(60, 970, 1920, 3))
        self.label_20.setStyleSheet(u"background-color: rgb(0, 45, 107);")
        self.botonEditar1 = QPushButton(Widget)
        self.botonEditar1.setObjectName(u"botonEditar1")
        self.botonEditar1.setGeometry(QRect(164, 990, 42, 42))
        self.botonEditar1.setFont(font)
        self.botonEditar1.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon1 = QIcon()
        icon1.addFile(u"edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonEditar1.setIcon(icon1)
        self.botonSacar1 = QPushButton(Widget)
        self.botonSacar1.setObjectName(u"botonSacar1")
        self.botonSacar1.setGeometry(QRect(221, 990, 42, 42))
        self.botonSacar1.setFont(font)
        self.botonSacar1.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon2 = QIcon()
        icon2.addFile(u"close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonSacar1.setIcon(icon2)
        self.label_22 = QLabel(Widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(625, 172, 495, 63))
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
        self.botonOrdenar1.setGeometry(QRect(890, 178, 141, 50))
        font3 = QFont()
        font3.setFamilies([u"icon-ui"])
        self.botonOrdenar1.setFont(font3)
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
        self.label_23 = QLabel(Widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(1239, 172, 598, 61))
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"color: white;\n"
"background-color: white;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(1290, 190, 501, 31))
        self.lineEdit.setStyleSheet(u"color: black;\n"
"background-color: white;\n"
"\n"
"border: 2px solid white;\n"
"border-radius: 25px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"font-size:15px;")
        self.botonBuscar = QPushButton(Widget)
        self.botonBuscar.setObjectName(u"botonBuscar")
        self.botonBuscar.setGeometry(QRect(1250, 185, 31, 41))
        self.botonBuscar.setFont(font)
        self.botonBuscar.setStyleSheet(u"color: white;\n"
"background-color: white;\n"
"\n"
"border: 2px solid white;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon4 = QIcon()
        icon4.addFile(u"search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonBuscar.setIcon(icon4)
        self.botonBuscar.setIconSize(QSize(31, 31))
        self.botonBorrar = QPushButton(Widget)
        self.botonBorrar.setObjectName(u"botonBorrar")
        self.botonBorrar.setGeometry(QRect(1800, 190, 21, 31))
        self.botonBorrar.setFont(font)
        self.botonBorrar.setStyleSheet(u"color: white;\n"
"background-color: white;\n"
"\n"
"border: 2px solid white;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon5 = QIcon()
        icon5.addFile(u"close2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonBorrar.setIcon(icon5)
        self.botonBorrar.setIconSize(QSize(16, 16))
        self.botonVer1 = QPushButton(Widget)
        self.botonVer1.setObjectName(u"botonVer1")
        self.botonVer1.setGeometry(QRect(100, 989, 42, 42))
        self.botonVer1.setFont(font)
        self.botonVer1.setStyleSheet(u"background-color: black;\n"
"\n"
"border: 2px solid black;\n"
"border-radius: 20px; /* Bordes redondeados */\n"
"padding: 5px;")
        icon6 = QIcon()
        icon6.addFile(u"eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botonVer1.setIcon(icon6)
        self.botonVer1.setIconSize(QSize(25, 25))
        self.label_24 = QLabel(Widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(1700, 36, 126, 41))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"color: white;")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
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
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1840, 30, 56, 56))
        self.label_8.setStyleSheet(u"")
        self.label_8.setPixmap(QPixmap(u"perfil-de-usuario.png"))
        self.label_8.setScaledContents(True)
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
        self.tableWidget = QTableWidget(Widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 256, 1800, 711))
        self.tableWidget.setStyleSheet(u"background-color: white;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 30px; /* Bordes redondeados */\n"
"    padding: 5px;")
        self.label_4.raise_()
        self.tableWidget.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.botonAgregar.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.label.raise_()
        self.label_20.raise_()
        self.botonEditar1.raise_()
        self.botonSacar1.raise_()
        self.label_22.raise_()
        self.botonOrdenar1.raise_()
        self.label_23.raise_()
        self.lineEdit.raise_()
        self.botonBuscar.raise_()
        self.botonBorrar.raise_()
        self.botonVer1.raise_()
        self.label_24.raise_()
        self.botonAdmin.raise_()
        self.label_8.raise_()
        self.botonLogOut.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.botonAgregar.setText(QCoreApplication.translate("Widget", u" Agregar Empleados", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"RECURSOS HUMANOS", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"Empleados: {total}", None))
        self.label.setText("")
        self.label_20.setText("")
        self.botonEditar1.setText("")
        self.botonSacar1.setText("")
        self.label_22.setText(QCoreApplication.translate("Widget", u"Ordenar por:", None))
        self.botonOrdenar1.setText(QCoreApplication.translate("Widget", u"Seleccionar", None))
        self.label_23.setText("")
        self.botonBuscar.setText("")
        self.botonBorrar.setText("")
        self.botonVer1.setText("")
        self.label_24.setText(QCoreApplication.translate("Widget", u"Usuario", None))
        self.botonAdmin.setText(QCoreApplication.translate("Widget", u"Administraci\u00f3n", None))
        self.label_8.setText("")
        self.botonLogOut.setText(QCoreApplication.translate("Widget", u"Cerrar Sesi\u00f3n", None))
    # retranslateUi


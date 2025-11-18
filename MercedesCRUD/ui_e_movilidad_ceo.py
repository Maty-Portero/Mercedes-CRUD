# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'e_movilidad_ceo.ui'
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
        self.label_12 = QLabel(Widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 36, 381, 41))
        font = QFont()
        font.setFamilies([u"icon-ui"])
        font.setPointSize(26)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: white;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1836, 34, 56, 56))
        self.label_8.setStyleSheet(u"")
        self.label_8.setPixmap(QPixmap(u"perfil-de-usuario.png"))
        self.label_8.setScaledContents(True)
        self.botonAdmin = QPushButton(Widget)
        self.botonAdmin.setObjectName(u"botonAdmin")
        self.botonAdmin.setGeometry(QRect(1200, 30, 199, 63))
        font1 = QFont()
        font1.setFamilies([u"icon-ui"])
        font1.setPointSize(19)
        self.botonAdmin.setFont(font1)
        self.botonAdmin.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: black;\n"
"background-color: #ebebeb;")
        self.label_23 = QLabel(Widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(1700, 36, 126, 41))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: white;")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.botonRegistro = QPushButton(Widget)
        self.botonRegistro.setObjectName(u"botonRegistro")
        self.botonRegistro.setGeometry(QRect(701, 347, 500, 500))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(36)
        self.botonRegistro.setFont(font2)
        self.botonRegistro.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.botonDB = QPushButton(Widget)
        self.botonDB.setObjectName(u"botonDB")
        self.botonDB.setGeometry(QRect(108, 347, 500, 500))
        self.botonDB.setFont(font2)
        self.botonDB.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.botonUsuarioAutorizados = QPushButton(Widget)
        self.botonUsuarioAutorizados.setObjectName(u"botonUsuarioAutorizados")
        self.botonUsuarioAutorizados.setGeometry(QRect(1294, 347, 500, 500))
        self.botonUsuarioAutorizados.setFont(font2)
        self.botonUsuarioAutorizados.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: white;\n"
"background-color: #002d6b;")
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(783, 222, 354, 67))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(42)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: black;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.botonLogOut = QPushButton(Widget)
        self.botonLogOut.setObjectName(u"botonLogOut")
        self.botonLogOut.setGeometry(QRect(1420, 30, 199, 63))
        self.botonLogOut.setFont(font1)
        self.botonLogOut.setStyleSheet(u"border: 2px solid #000000;\n"
"border-radius: 15px; /* Bordes redondeados */\n"
"padding: 5px;\n"
"\n"
"color: black;\n"
"background-color: #ebebeb;")
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_12.raise_()
        self.label_8.raise_()
        self.botonAdmin.raise_()
        self.label_23.raise_()
        self.botonRegistro.raise_()
        self.botonDB.raise_()
        self.botonUsuarioAutorizados.raise_()
        self.label_13.raise_()
        self.botonLogOut.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_12.setText(QCoreApplication.translate("Widget", u"E-MOVILIDAD (ADMIN)", None))
        self.label_8.setText("")
        self.botonAdmin.setText(QCoreApplication.translate("Widget", u"Administraci\u00f3n", None))
        self.label_23.setText(QCoreApplication.translate("Widget", u"Usuario", None))
        self.botonRegistro.setText(QCoreApplication.translate("Widget", u"Registro", None))
        self.botonDB.setText(QCoreApplication.translate("Widget", u"Base de Datos", None))
        self.botonUsuarioAutorizados.setText(QCoreApplication.translate("Widget", u"Usuarios Autorizados", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"E-MOVILIDAD", None))
        self.botonLogOut.setText(QCoreApplication.translate("Widget", u"Cerrar Sesi\u00f3n", None))
    # retranslateUi


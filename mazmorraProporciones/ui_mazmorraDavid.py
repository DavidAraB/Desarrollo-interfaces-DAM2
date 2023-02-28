# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mazmorraDavid.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(645, 530)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Century Schoolbook"])
        MainWindow.setFont(font)
        self.actionEmpezar = QAction(MainWindow)
        self.actionEmpezar.setObjectName(u"actionEmpezar")
        self.actionAyuda = QAction(MainWindow)
        self.actionAyuda.setObjectName(u"actionAyuda")
        self.actionGeneral = QAction(MainWindow)
        self.actionGeneral.setObjectName(u"actionGeneral")
        self.actionSala_Norte = QAction(MainWindow)
        self.actionSala_Norte.setObjectName(u"actionSala_Norte")
        self.actionSala_Sur = QAction(MainWindow)
        self.actionSala_Sur.setObjectName(u"actionSala_Sur")
        self.actionSala_Este = QAction(MainWindow)
        self.actionSala_Este.setObjectName(u"actionSala_Este")
        self.actionSala_Oeste = QAction(MainWindow)
        self.actionSala_Oeste.setObjectName(u"actionSala_Oeste")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 341, 481))
        self.frame.setStyleSheet(u"background-color:#83939D")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(2)
        self.norte = QPushButton(self.frame)
        self.norte.setObjectName(u"norte")
        self.norte.setEnabled(False)
        self.norte.setGeometry(QRect(120, 70, 91, 91))
        sizePolicy.setHeightForWidth(self.norte.sizePolicy().hasHeightForWidth())
        self.norte.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Century Schoolbook"])
        font1.setPointSize(18)
        self.norte.setFont(font1)
        self.norte.setStyleSheet(u"background-color:#B5C1BC;color:black")
        self.norte.setCheckable(False)
        self.norte.setAutoDefault(False)
        self.norte.setFlat(False)
        self.oeste = QPushButton(self.frame)
        self.oeste.setObjectName(u"oeste")
        self.oeste.setEnabled(False)
        self.oeste.setGeometry(QRect(10, 180, 91, 81))
        sizePolicy.setHeightForWidth(self.oeste.sizePolicy().hasHeightForWidth())
        self.oeste.setSizePolicy(sizePolicy)
        self.oeste.setFont(font1)
        self.oeste.setStyleSheet(u"background-color:#B5C1BC;color:black")
        self.este = QPushButton(self.frame)
        self.este.setObjectName(u"este")
        self.este.setEnabled(False)
        self.este.setGeometry(QRect(230, 180, 91, 81))
        sizePolicy.setHeightForWidth(self.este.sizePolicy().hasHeightForWidth())
        self.este.setSizePolicy(sizePolicy)
        self.este.setFont(font1)
        self.este.setStyleSheet(u"background-color:#B5C1BC;color:black")
        self.sur = QPushButton(self.frame)
        self.sur.setObjectName(u"sur")
        self.sur.setEnabled(False)
        self.sur.setGeometry(QRect(120, 280, 91, 91))
        sizePolicy.setHeightForWidth(self.sur.sizePolicy().hasHeightForWidth())
        self.sur.setSizePolicy(sizePolicy)
        self.sur.setFont(font1)
        self.sur.setStyleSheet(u"background-color:#B5C1BC;color:black")
        self.inicio = QPushButton(self.frame)
        self.inicio.setObjectName(u"inicio")
        self.inicio.setEnabled(False)
        self.inicio.setGeometry(QRect(120, 180, 91, 81))
        sizePolicy.setHeightForWidth(self.inicio.sizePolicy().hasHeightForWidth())
        self.inicio.setSizePolicy(sizePolicy)
        self.inicio.setFont(font1)
        self.inicio.setStyleSheet(u"background-color:#B5C1BC;color:black")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(340, 0, 301, 481))
        self.frame_2.setStyleSheet(u"background-color:#83939D")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setLineWidth(5)
        self.frame_2.setMidLineWidth(2)
        self.jugar = QPushButton(self.frame_2)
        self.jugar.setObjectName(u"jugar")
        self.jugar.setEnabled(True)
        self.jugar.setGeometry(QRect(40, 390, 101, 61))
        font2 = QFont()
        font2.setFamilies([u"Century Schoolbook"])
        font2.setPointSize(14)
        self.jugar.setFont(font2)
        self.jugar.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:#B5C1BC\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color : lightgreen;\n"
"};")
        self.salir = QPushButton(self.frame_2)
        self.salir.setObjectName(u"salir")
        self.salir.setEnabled(False)
        self.salir.setGeometry(QRect(170, 390, 101, 61))
        self.salir.setFont(font2)
        self.salir.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color:#B5C1BC\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color :#DF6666;\n"
"};")
        self.verticalLayoutWidget = QWidget(self.frame_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 140, 271, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radio1 = QRadioButton(self.verticalLayoutWidget)
        self.radio1.setObjectName(u"radio1")
        self.radio1.setEnabled(False)
        font3 = QFont()
        font3.setFamilies([u"Century Schoolbook"])
        font3.setPointSize(13)
        self.radio1.setFont(font3)
        self.radio1.setStyleSheet(u"background-color:#B5C1BC;color:black")

        self.verticalLayout.addWidget(self.radio1)

        self.radio2 = QRadioButton(self.verticalLayoutWidget)
        self.radio2.setObjectName(u"radio2")
        self.radio2.setEnabled(False)
        self.radio2.setFont(font3)
        self.radio2.setStyleSheet(u"background-color:#B5C1BC;color:black")

        self.verticalLayout.addWidget(self.radio2)

        self.radio3 = QRadioButton(self.verticalLayoutWidget)
        self.radio3.setObjectName(u"radio3")
        self.radio3.setEnabled(False)
        self.radio3.setFont(font3)
        self.radio3.setStyleSheet(u"background-color:#B5C1BC;color:black")

        self.verticalLayout.addWidget(self.radio3)

        self.infosala = QTextEdit(self.frame_2)
        self.infosala.setObjectName(u"infosala")
        self.infosala.setEnabled(True)
        self.infosala.setGeometry(QRect(10, 10, 271, 121))
        self.infosala.setFont(font2)
        self.infosala.setStyleSheet(u"background-color:#B5C1BC;color:black")
        self.infosala.setFrameShape(QFrame.StyledPanel)
        self.infosala.setFrameShadow(QFrame.Sunken)
        self.infosala.setLineWidth(3)
        self.infosala.setReadOnly(True)
        self.infosala.setOverwriteMode(False)
        self.resultado = QTextEdit(self.frame_2)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setGeometry(QRect(10, 270, 271, 91))
        self.resultado.setFont(font3)
        self.resultado.setStyleSheet(u"background-color:#B5C1BC;color:black")
        self.resultado.setLineWidth(3)
        self.resultado.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 645, 21))
        self.menuJuego = QMenu(self.menubar)
        self.menuJuego.setObjectName(u"menuJuego")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuJuego.menuAction())
        self.menuJuego.addAction(self.actionAyuda)
        self.menuJuego.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        self.norte.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mazmorra de David", None))
        self.actionEmpezar.setText(QCoreApplication.translate("MainWindow", u"Empezar", None))
        self.actionAyuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.actionGeneral.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.actionSala_Norte.setText(QCoreApplication.translate("MainWindow", u"Sala Norte", None))
        self.actionSala_Sur.setText(QCoreApplication.translate("MainWindow", u"Sala Sur", None))
        self.actionSala_Este.setText(QCoreApplication.translate("MainWindow", u"Sala Este", None))
        self.actionSala_Oeste.setText(QCoreApplication.translate("MainWindow", u"Sala Oeste", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.norte.setText(QCoreApplication.translate("MainWindow", u"Norte", None))
        self.oeste.setText(QCoreApplication.translate("MainWindow", u"Oeste", None))
        self.este.setText(QCoreApplication.translate("MainWindow", u"Este", None))
        self.sur.setText(QCoreApplication.translate("MainWindow", u"Sur", None))
        self.inicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.jugar.setText(QCoreApplication.translate("MainWindow", u"Jugar", None))
        self.salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.radio1.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radio2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radio3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.infosala.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Century Schoolbook'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.menuJuego.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi


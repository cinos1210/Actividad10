# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1285, 630)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(270, 20, 1011, 571))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.Particulas_graphicsView = QGraphicsView(self.tab)
        self.Particulas_graphicsView.setObjectName(u"Particulas_graphicsView")
        self.Particulas_graphicsView.setGeometry(QRect(20, 10, 961, 491))
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 510, 311, 25))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Dibujar_pushButton = QPushButton(self.layoutWidget)
        self.Dibujar_pushButton.setObjectName(u"Dibujar_pushButton")

        self.horizontalLayout_7.addWidget(self.Dibujar_pushButton)

        self.Limpiar_pushButton_2 = QPushButton(self.layoutWidget)
        self.Limpiar_pushButton_2.setObjectName(u"Limpiar_pushButton_2")

        self.horizontalLayout_7.addWidget(self.Limpiar_pushButton_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Tabla = QTableWidget(self.tab_2)
        self.Tabla.setObjectName(u"Tabla")

        self.gridLayout.addWidget(self.Tabla, 0, 0, 1, 3)

        self.Buscar_lineEdit = QLineEdit(self.tab_2)
        self.Buscar_lineEdit.setObjectName(u"Buscar_lineEdit")

        self.gridLayout.addWidget(self.Buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.Mostrar_Tabla_pushButton_2 = QPushButton(self.tab_2)
        self.Mostrar_Tabla_pushButton_2.setObjectName(u"Mostrar_Tabla_pushButton_2")

        self.gridLayout.addWidget(self.Mostrar_Tabla_pushButton_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 40, 251, 201))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.layoutWidget1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.layoutWidget2 = QWidget(self.groupBox_4)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 176, 22))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.OrigenX_spinBox = QSpinBox(self.layoutWidget2)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")

        self.horizontalLayout_5.addWidget(self.OrigenX_spinBox)

        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.OrigenY_spinBox_2 = QSpinBox(self.layoutWidget2)
        self.OrigenY_spinBox_2.setObjectName(u"OrigenY_spinBox_2")

        self.horizontalLayout_5.addWidget(self.OrigenY_spinBox_2)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName(u"groupBox")
        self.layoutWidget3 = QWidget(self.groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 196, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.DesX_pinBox = QSpinBox(self.layoutWidget3)
        self.DesX_pinBox.setObjectName(u"DesX_pinBox")
        self.DesX_pinBox.setMaximum(500)

        self.horizontalLayout_3.addWidget(self.DesX_pinBox)

        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.DesY_spinBox_2 = QSpinBox(self.layoutWidget3)
        self.DesY_spinBox_2.setObjectName(u"DesY_spinBox_2")
        self.DesY_spinBox_2.setMaximum(500)

        self.horizontalLayout_3.addWidget(self.DesY_spinBox_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.layoutWidget4 = QWidget(self.groupBox_2)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 20, 229, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.Red_spinBox_4 = QSpinBox(self.layoutWidget4)
        self.Red_spinBox_4.setObjectName(u"Red_spinBox_4")
        self.Red_spinBox_4.setMaximum(255)

        self.horizontalLayout.addWidget(self.Red_spinBox_4)

        self.label_5 = QLabel(self.layoutWidget4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.Green_spinBox_5 = QSpinBox(self.layoutWidget4)
        self.Green_spinBox_5.setObjectName(u"Green_spinBox_5")
        self.Green_spinBox_5.setMaximum(255)

        self.horizontalLayout.addWidget(self.Green_spinBox_5)

        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.Blue_spinBox_6 = QSpinBox(self.layoutWidget4)
        self.Blue_spinBox_6.setObjectName(u"Blue_spinBox_6")
        self.Blue_spinBox_6.setMaximum(255)

        self.horizontalLayout.addWidget(self.Blue_spinBox_6)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 250, 120, 51))
        self.layoutWidget5 = QWidget(self.groupBox_3)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 20, 102, 22))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.Velocidad_spinBox_3 = QSpinBox(self.layoutWidget5)
        self.Velocidad_spinBox_3.setObjectName(u"Velocidad_spinBox_3")
        self.Velocidad_spinBox_3.setMaximum(1000)

        self.horizontalLayout_4.addWidget(self.Velocidad_spinBox_3)

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")
        self.salida.setGeometry(QRect(10, 310, 251, 161))
        self.layoutWidget6 = QWidget(self.centralwidget)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(90, 10, 80, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.ID_pinBox = QSpinBox(self.layoutWidget6)
        self.ID_pinBox.setObjectName(u"ID_pinBox")
        self.ID_pinBox.setMaximum(500000)

        self.horizontalLayout_2.addWidget(self.ID_pinBox)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(150, 250, 88, 54))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.AgragrInicio_pushButton = QPushButton(self.widget)
        self.AgragrInicio_pushButton.setObjectName(u"AgragrInicio_pushButton")

        self.verticalLayout_2.addWidget(self.AgragrInicio_pushButton)

        self.agregarFinal_pushButton = QPushButton(self.widget)
        self.agregarFinal_pushButton.setObjectName(u"agregarFinal_pushButton")

        self.verticalLayout_2.addWidget(self.agregarFinal_pushButton)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 470, 251, 112))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Mostrar_pushButton = QPushButton(self.widget1)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.verticalLayout_3.addWidget(self.Mostrar_pushButton)

        self.Sort_ID_pushButton = QPushButton(self.widget1)
        self.Sort_ID_pushButton.setObjectName(u"Sort_ID_pushButton")

        self.verticalLayout_3.addWidget(self.Sort_ID_pushButton)

        self.Sort_Distancia_pushButton_2 = QPushButton(self.widget1)
        self.Sort_Distancia_pushButton_2.setObjectName(u"Sort_Distancia_pushButton_2")

        self.verticalLayout_3.addWidget(self.Sort_Distancia_pushButton_2)

        self.Sort_Velocidad_pushButton_3 = QPushButton(self.widget1)
        self.Sort_Velocidad_pushButton_3.setObjectName(u"Sort_Velocidad_pushButton_3")

        self.verticalLayout_3.addWidget(self.Sort_Velocidad_pushButton_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1285, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbrir)
        self.menuFile.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.Dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.Limpiar_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Mostrar_Tabla_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostra", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Origenes", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen X:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Origen Y:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Colores", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.AgragrInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Inicio", None))
        self.agregarFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Sort_ID_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar por ID", None))
        self.Sort_Distancia_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Distancia", None))
        self.Sort_Velocidad_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Velocidad", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi


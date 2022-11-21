# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1273, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_main = QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.stackedWidget_main.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_parameters = QGroupBox(self.page)
        self.groupBox_parameters.setObjectName(u"groupBox_parameters")
        self.verticalLayout = QVBoxLayout(self.groupBox_parameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_cell_list = QLabel(self.groupBox_parameters)
        self.label_cell_list.setObjectName(u"label_cell_list")

        self.horizontalLayout_2.addWidget(self.label_cell_list)

        self.comboBox_cell_list = QComboBox(self.groupBox_parameters)
        self.comboBox_cell_list.setObjectName(u"comboBox_cell_list")

        self.horizontalLayout_2.addWidget(self.comboBox_cell_list)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.groupBox_parameters)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_one_measure = QRadioButton(self.groupBox_parameters)
        self.radioButton_one_measure.setObjectName(u"radioButton_one_measure")

        self.verticalLayout_2.addWidget(self.radioButton_one_measure)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_cycle = QRadioButton(self.groupBox_parameters)
        self.radioButton_cycle.setObjectName(u"radioButton_cycle")
        self.radioButton_cycle.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButton_cycle)

        self.lineEdit_delay = QLineEdit(self.groupBox_parameters)
        self.lineEdit_delay.setObjectName(u"lineEdit_delay")

        self.horizontalLayout_4.addWidget(self.lineEdit_delay)

        self.label = QLabel(self.groupBox_parameters)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_remaining_time = QLabel(self.groupBox_parameters)
        self.label_remaining_time.setObjectName(u"label_remaining_time")

        self.verticalLayout.addWidget(self.label_remaining_time)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_measure_cell = QPushButton(self.groupBox_parameters)
        self.pushButton_measure_cell.setObjectName(u"pushButton_measure_cell")

        self.horizontalLayout_3.addWidget(self.pushButton_measure_cell)

        self.pushButton_measure_all = QPushButton(self.groupBox_parameters)
        self.pushButton_measure_all.setObjectName(u"pushButton_measure_all")

        self.horizontalLayout_3.addWidget(self.pushButton_measure_all)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton_stop = QPushButton(self.groupBox_parameters)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.verticalLayout.addWidget(self.pushButton_stop)


        self.horizontalLayout.addWidget(self.groupBox_parameters)

        self.stackedWidget_cells_plot = QStackedWidget(self.page)
        self.stackedWidget_cells_plot.setObjectName(u"stackedWidget_cells_plot")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget_cells_plot.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget_cells_plot.addWidget(self.page_4)

        self.horizontalLayout.addWidget(self.stackedWidget_cells_plot)

        self.horizontalLayout.setStretch(0, 25)
        self.horizontalLayout.setStretch(1, 75)
        self.stackedWidget_main.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_main.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1273, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_parameters.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_cell_list.setText(QCoreApplication.translate("MainWindow", u"Cell", None))
        self.radioButton_one_measure.setText(QCoreApplication.translate("MainWindow", u"One measure", None))
        self.radioButton_cycle.setText(QCoreApplication.translate("MainWindow", u"Cycle:", None))
        self.lineEdit_delay.setText(QCoreApplication.translate("MainWindow", u"600", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.label_remaining_time.setText(QCoreApplication.translate("MainWindow", u"Not Measuring", None))
        self.pushButton_measure_cell.setText(QCoreApplication.translate("MainWindow", u"Measure Cell", None))
        self.pushButton_measure_all.setText(QCoreApplication.translate("MainWindow", u"Measure All", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Stability", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi


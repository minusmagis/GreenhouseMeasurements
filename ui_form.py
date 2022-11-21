# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resource.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1351, 760)
        MainWindow.setMinimumSize(QSize(0, 5))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(75, 81, 72);")
        self.actionSomtheng = QAction(MainWindow)
        self.actionSomtheng.setObjectName(u"actionSomtheng")
        self.actionSomething_else = QAction(MainWindow)
        self.actionSomething_else.setObjectName(u"actionSomething_else")
        self.actionSomething_Dumb = QAction(MainWindow)
        self.actionSomething_Dumb.setObjectName(u"actionSomething_Dumb")
        self.actionSomething_clever = QAction(MainWindow)
        self.actionSomething_clever.setObjectName(u"actionSomething_clever")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.MenuVLayout = QFrame(self.centralwidget)
        self.MenuVLayout.setObjectName(u"MenuVLayout")
        self.MenuVLayout.setStyleSheet(u"background-color: rgb(48, 52, 46);")
        self.verticalLayout = QVBoxLayout(self.MenuVLayout)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.OmegaLogoLabel = QLabel(self.MenuVLayout)
        self.OmegaLogoLabel.setObjectName(u"OmegaLogoLabel")
        self.OmegaLogoLabel.setPixmap(QPixmap(u":/icons/opv_icon_png"))

        self.verticalLayout.addWidget(self.OmegaLogoLabel)

        self.DashboardButton = QPushButton(self.MenuVLayout)
        self.DashboardButton.setObjectName(u"DashboardButton")
        self.DashboardButton.setMinimumSize(QSize(100, 100))
        self.DashboardButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 52, 46);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/greenohouse_icon", QSize(), QIcon.Normal, QIcon.Off)
        self.DashboardButton.setIcon(icon)
        self.DashboardButton.setIconSize(QSize(65, 65))

        self.verticalLayout.addWidget(self.DashboardButton)

        self.JVCurvesButton = QPushButton(self.MenuVLayout)
        self.JVCurvesButton.setObjectName(u"JVCurvesButton")
        self.JVCurvesButton.setMinimumSize(QSize(100, 100))
        self.JVCurvesButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 52, 46);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/curves_icon", QSize(), QIcon.Normal, QIcon.Off)
        self.JVCurvesButton.setIcon(icon1)
        self.JVCurvesButton.setIconSize(QSize(60, 60))

        self.verticalLayout.addWidget(self.JVCurvesButton)

        self.HistoricalDataButton = QPushButton(self.MenuVLayout)
        self.HistoricalDataButton.setObjectName(u"HistoricalDataButton")
        self.HistoricalDataButton.setMinimumSize(QSize(100, 100))
        self.HistoricalDataButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 52, 46);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/historic_icon", QSize(), QIcon.Normal, QIcon.Off)
        self.HistoricalDataButton.setIcon(icon2)
        self.HistoricalDataButton.setIconSize(QSize(65, 65))

        self.verticalLayout.addWidget(self.HistoricalDataButton)

        self.ButtonVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.ButtonVSpacer)

        self.SettingsButton = QPushButton(self.MenuVLayout)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setMinimumSize(QSize(100, 100))
        self.SettingsButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(48, 52, 46);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(75, 81, 72);\n"
"    color: rgb(168, 175, 165);\n"
"	border: none\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/settings_icon", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsButton.setIcon(icon3)
        self.SettingsButton.setIconSize(QSize(65, 65))

        self.verticalLayout.addWidget(self.SettingsButton)


        self.horizontalLayout_3.addWidget(self.MenuVLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.JVCurvesStack = QWidget()
        self.JVCurvesStack.setObjectName(u"JVCurvesStack")
        self.gridLayout_2 = QGridLayout(self.JVCurvesStack)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.JVGraphEastFrame = QFrame(self.JVCurvesStack)
        self.JVGraphEastFrame.setObjectName(u"JVGraphEastFrame")
        self.JVGraphEastFrame.setFrameShape(QFrame.StyledPanel)
        self.JVGraphEastFrame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.JVGraphEastFrame, 0, 0, 1, 1)

        self.JVGraphWestFrame = QFrame(self.JVCurvesStack)
        self.JVGraphWestFrame.setObjectName(u"JVGraphWestFrame")
        self.JVGraphWestFrame.setFrameShape(QFrame.StyledPanel)
        self.JVGraphWestFrame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.JVGraphWestFrame, 0, 1, 1, 1)

        self.JVParametersFrame = QFrame(self.JVCurvesStack)
        self.JVParametersFrame.setObjectName(u"JVParametersFrame")
        self.JVParametersFrame.setStyleSheet(u"background-color: rgb(48, 52, 46);")
        self.JVParametersFrame.setFrameShape(QFrame.StyledPanel)
        self.JVParametersFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.JVParametersFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.String12image2 = QLabel(self.JVParametersFrame)
        self.String12image2.setObjectName(u"String12image2")
        self.String12image2.setPixmap(QPixmap(u":/icons/string_icon"))
        self.String12image2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.String12image2)

        self.String34image2 = QLabel(self.JVParametersFrame)
        self.String34image2.setObjectName(u"String34image2")
        self.String34image2.setPixmap(QPixmap(u":/icons/string_icon"))
        self.String34image2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.String34image2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.String56image2 = QLabel(self.JVParametersFrame)
        self.String56image2.setObjectName(u"String56image2")
        self.String56image2.setPixmap(QPixmap(u":/icons/string_icon"))
        self.String56image2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.String56image2)

        self.String78image2 = QLabel(self.JVParametersFrame)
        self.String78image2.setObjectName(u"String78image2")
        self.String78image2.setPixmap(QPixmap(u":/icons/string_icon"))
        self.String78image2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.String78image2)

        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(1, 10)
        self.horizontalLayout_5.setStretch(2, 5)
        self.horizontalLayout_5.setStretch(3, 10)
        self.horizontalLayout_5.setStretch(4, 10)

        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 1, 1, 2)

        self.ParametersLayout = QVBoxLayout()
        self.ParametersLayout.setObjectName(u"ParametersLayout")
        self.VocLabel = QLabel(self.JVParametersFrame)
        self.VocLabel.setObjectName(u"VocLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VocLabel.sizePolicy().hasHeightForWidth())
        self.VocLabel.setSizePolicy(sizePolicy)
        self.VocLabel.setMinimumSize(QSize(10, 2))
        self.VocLabel.setFont(font)
        self.VocLabel.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.VocLabel.setAlignment(Qt.AlignCenter)
        self.VocLabel.setWordWrap(True)

        self.ParametersLayout.addWidget(self.VocLabel)

        self.JscLabel = QLabel(self.JVParametersFrame)
        self.JscLabel.setObjectName(u"JscLabel")
        sizePolicy.setHeightForWidth(self.JscLabel.sizePolicy().hasHeightForWidth())
        self.JscLabel.setSizePolicy(sizePolicy)
        self.JscLabel.setMinimumSize(QSize(10, 2))
        self.JscLabel.setFont(font)
        self.JscLabel.setStyleSheet(u"  color: rgb(255, 100, 80);")
        self.JscLabel.setAlignment(Qt.AlignCenter)
        self.JscLabel.setWordWrap(True)

        self.ParametersLayout.addWidget(self.JscLabel)

        self.FFLabel = QLabel(self.JVParametersFrame)
        self.FFLabel.setObjectName(u"FFLabel")
        sizePolicy.setHeightForWidth(self.FFLabel.sizePolicy().hasHeightForWidth())
        self.FFLabel.setSizePolicy(sizePolicy)
        self.FFLabel.setMinimumSize(QSize(10, 2))
        self.FFLabel.setFont(font)
        self.FFLabel.setStyleSheet(u"color: rgb(255, 189, 74);")
        self.FFLabel.setAlignment(Qt.AlignCenter)
        self.FFLabel.setWordWrap(True)

        self.ParametersLayout.addWidget(self.FFLabel)

        self.PCELabel = QLabel(self.JVParametersFrame)
        self.PCELabel.setObjectName(u"PCELabel")
        sizePolicy.setHeightForWidth(self.PCELabel.sizePolicy().hasHeightForWidth())
        self.PCELabel.setSizePolicy(sizePolicy)
        self.PCELabel.setMinimumSize(QSize(10, 2))
        self.PCELabel.setFont(font)
        self.PCELabel.setStyleSheet(u"color: rgb(139, 255, 119);")
        self.PCELabel.setAlignment(Qt.AlignCenter)
        self.PCELabel.setWordWrap(True)

        self.ParametersLayout.addWidget(self.PCELabel)


        self.gridLayout_4.addLayout(self.ParametersLayout, 1, 0, 1, 1)

        self.StringParametersLayout1 = QGridLayout()
        self.StringParametersLayout1.setObjectName(u"StringParametersLayout1")
        self.VocStr1 = QLabel(self.JVParametersFrame)
        self.VocStr1.setObjectName(u"VocStr1")
        sizePolicy.setHeightForWidth(self.VocStr1.sizePolicy().hasHeightForWidth())
        self.VocStr1.setSizePolicy(sizePolicy)
        self.VocStr1.setMinimumSize(QSize(10, 2))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setItalic(False)
        self.VocStr1.setFont(font1)
        self.VocStr1.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.VocStr1.setAlignment(Qt.AlignCenter)
        self.VocStr1.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.VocStr1, 0, 0, 1, 1)

        self.VocStr2 = QLabel(self.JVParametersFrame)
        self.VocStr2.setObjectName(u"VocStr2")
        sizePolicy.setHeightForWidth(self.VocStr2.sizePolicy().hasHeightForWidth())
        self.VocStr2.setSizePolicy(sizePolicy)
        self.VocStr2.setMinimumSize(QSize(10, 2))
        self.VocStr2.setFont(font1)
        self.VocStr2.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.VocStr2.setAlignment(Qt.AlignCenter)
        self.VocStr2.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.VocStr2, 0, 1, 1, 1)

        self.VocStr3 = QLabel(self.JVParametersFrame)
        self.VocStr3.setObjectName(u"VocStr3")
        sizePolicy.setHeightForWidth(self.VocStr3.sizePolicy().hasHeightForWidth())
        self.VocStr3.setSizePolicy(sizePolicy)
        self.VocStr3.setMinimumSize(QSize(10, 2))
        self.VocStr3.setFont(font1)
        self.VocStr3.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.VocStr3.setAlignment(Qt.AlignCenter)
        self.VocStr3.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.VocStr3, 0, 2, 1, 1)

        self.VocStr4 = QLabel(self.JVParametersFrame)
        self.VocStr4.setObjectName(u"VocStr4")
        sizePolicy.setHeightForWidth(self.VocStr4.sizePolicy().hasHeightForWidth())
        self.VocStr4.setSizePolicy(sizePolicy)
        self.VocStr4.setMinimumSize(QSize(10, 2))
        self.VocStr4.setFont(font1)
        self.VocStr4.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.VocStr4.setAlignment(Qt.AlignCenter)
        self.VocStr4.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.VocStr4, 0, 3, 1, 1)

        self.JscStr1 = QLabel(self.JVParametersFrame)
        self.JscStr1.setObjectName(u"JscStr1")
        sizePolicy.setHeightForWidth(self.JscStr1.sizePolicy().hasHeightForWidth())
        self.JscStr1.setSizePolicy(sizePolicy)
        self.JscStr1.setMinimumSize(QSize(10, 2))
        self.JscStr1.setFont(font1)
        self.JscStr1.setStyleSheet(u"  color: rgb(255, 100, 80);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.JscStr1.setAlignment(Qt.AlignCenter)
        self.JscStr1.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.JscStr1, 1, 0, 1, 1)

        self.JscStr2 = QLabel(self.JVParametersFrame)
        self.JscStr2.setObjectName(u"JscStr2")
        sizePolicy.setHeightForWidth(self.JscStr2.sizePolicy().hasHeightForWidth())
        self.JscStr2.setSizePolicy(sizePolicy)
        self.JscStr2.setMinimumSize(QSize(10, 2))
        self.JscStr2.setFont(font1)
        self.JscStr2.setStyleSheet(u"  color: rgb(255, 100, 80);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.JscStr2.setAlignment(Qt.AlignCenter)
        self.JscStr2.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.JscStr2, 1, 1, 1, 1)

        self.JscStr3 = QLabel(self.JVParametersFrame)
        self.JscStr3.setObjectName(u"JscStr3")
        sizePolicy.setHeightForWidth(self.JscStr3.sizePolicy().hasHeightForWidth())
        self.JscStr3.setSizePolicy(sizePolicy)
        self.JscStr3.setMinimumSize(QSize(10, 2))
        self.JscStr3.setFont(font1)
        self.JscStr3.setStyleSheet(u"  color: rgb(255, 100, 80);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.JscStr3.setAlignment(Qt.AlignCenter)
        self.JscStr3.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.JscStr3, 1, 2, 1, 1)

        self.JscStr4 = QLabel(self.JVParametersFrame)
        self.JscStr4.setObjectName(u"JscStr4")
        sizePolicy.setHeightForWidth(self.JscStr4.sizePolicy().hasHeightForWidth())
        self.JscStr4.setSizePolicy(sizePolicy)
        self.JscStr4.setMinimumSize(QSize(10, 2))
        self.JscStr4.setFont(font1)
        self.JscStr4.setStyleSheet(u"  color: rgb(255, 100, 80);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.JscStr4.setAlignment(Qt.AlignCenter)
        self.JscStr4.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.JscStr4, 1, 3, 1, 1)

        self.FFStr1 = QLabel(self.JVParametersFrame)
        self.FFStr1.setObjectName(u"FFStr1")
        sizePolicy.setHeightForWidth(self.FFStr1.sizePolicy().hasHeightForWidth())
        self.FFStr1.setSizePolicy(sizePolicy)
        self.FFStr1.setMinimumSize(QSize(10, 2))
        self.FFStr1.setFont(font1)
        self.FFStr1.setStyleSheet(u"color: rgb(255, 189, 74);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.FFStr1.setAlignment(Qt.AlignCenter)
        self.FFStr1.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.FFStr1, 2, 0, 1, 1)

        self.FFStr2 = QLabel(self.JVParametersFrame)
        self.FFStr2.setObjectName(u"FFStr2")
        sizePolicy.setHeightForWidth(self.FFStr2.sizePolicy().hasHeightForWidth())
        self.FFStr2.setSizePolicy(sizePolicy)
        self.FFStr2.setMinimumSize(QSize(10, 2))
        self.FFStr2.setFont(font1)
        self.FFStr2.setStyleSheet(u"color: rgb(255, 189, 74);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.FFStr2.setAlignment(Qt.AlignCenter)
        self.FFStr2.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.FFStr2, 2, 1, 1, 1)

        self.FFStr3 = QLabel(self.JVParametersFrame)
        self.FFStr3.setObjectName(u"FFStr3")
        sizePolicy.setHeightForWidth(self.FFStr3.sizePolicy().hasHeightForWidth())
        self.FFStr3.setSizePolicy(sizePolicy)
        self.FFStr3.setMinimumSize(QSize(10, 2))
        self.FFStr3.setFont(font1)
        self.FFStr3.setStyleSheet(u"color: rgb(255, 189, 74);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.FFStr3.setAlignment(Qt.AlignCenter)
        self.FFStr3.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.FFStr3, 2, 2, 1, 1)

        self.FFStr4 = QLabel(self.JVParametersFrame)
        self.FFStr4.setObjectName(u"FFStr4")
        sizePolicy.setHeightForWidth(self.FFStr4.sizePolicy().hasHeightForWidth())
        self.FFStr4.setSizePolicy(sizePolicy)
        self.FFStr4.setMinimumSize(QSize(10, 2))
        self.FFStr4.setFont(font1)
        self.FFStr4.setStyleSheet(u"color: rgb(255, 189, 74);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.FFStr4.setAlignment(Qt.AlignCenter)
        self.FFStr4.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.FFStr4, 2, 3, 1, 1)

        self.PCEStr1 = QLabel(self.JVParametersFrame)
        self.PCEStr1.setObjectName(u"PCEStr1")
        sizePolicy.setHeightForWidth(self.PCEStr1.sizePolicy().hasHeightForWidth())
        self.PCEStr1.setSizePolicy(sizePolicy)
        self.PCEStr1.setMinimumSize(QSize(10, 2))
        self.PCEStr1.setFont(font1)
        self.PCEStr1.setStyleSheet(u"color: rgb(139, 255, 119);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.PCEStr1.setAlignment(Qt.AlignCenter)
        self.PCEStr1.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.PCEStr1, 3, 0, 1, 1)

        self.PCEStr2 = QLabel(self.JVParametersFrame)
        self.PCEStr2.setObjectName(u"PCEStr2")
        sizePolicy.setHeightForWidth(self.PCEStr2.sizePolicy().hasHeightForWidth())
        self.PCEStr2.setSizePolicy(sizePolicy)
        self.PCEStr2.setMinimumSize(QSize(10, 2))
        self.PCEStr2.setFont(font1)
        self.PCEStr2.setStyleSheet(u"color: rgb(139, 255, 119);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.PCEStr2.setAlignment(Qt.AlignCenter)
        self.PCEStr2.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.PCEStr2, 3, 1, 1, 1)

        self.PCEStr3 = QLabel(self.JVParametersFrame)
        self.PCEStr3.setObjectName(u"PCEStr3")
        sizePolicy.setHeightForWidth(self.PCEStr3.sizePolicy().hasHeightForWidth())
        self.PCEStr3.setSizePolicy(sizePolicy)
        self.PCEStr3.setMinimumSize(QSize(10, 2))
        self.PCEStr3.setFont(font1)
        self.PCEStr3.setStyleSheet(u"color: rgb(139, 255, 119);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.PCEStr3.setAlignment(Qt.AlignCenter)
        self.PCEStr3.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.PCEStr3, 3, 2, 1, 1)

        self.PCEStr4 = QLabel(self.JVParametersFrame)
        self.PCEStr4.setObjectName(u"PCEStr4")
        sizePolicy.setHeightForWidth(self.PCEStr4.sizePolicy().hasHeightForWidth())
        self.PCEStr4.setSizePolicy(sizePolicy)
        self.PCEStr4.setMinimumSize(QSize(10, 2))
        self.PCEStr4.setFont(font1)
        self.PCEStr4.setStyleSheet(u"color: rgb(139, 255, 119);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.PCEStr4.setAlignment(Qt.AlignCenter)
        self.PCEStr4.setWordWrap(True)

        self.StringParametersLayout1.addWidget(self.PCEStr4, 3, 3, 1, 1)


        self.gridLayout_4.addLayout(self.StringParametersLayout1, 1, 1, 1, 1)

        self.StringParametersLayout2 = QGridLayout()
        self.StringParametersLayout2.setObjectName(u"StringParametersLayout2")
        self.VocStr5 = QLabel(self.JVParametersFrame)
        self.VocStr5.setObjectName(u"VocStr5")
        sizePolicy.setHeightForWidth(self.VocStr5.sizePolicy().hasHeightForWidth())
        self.VocStr5.setSizePolicy(sizePolicy)
        self.VocStr5.setMinimumSize(QSize(10, 2))
        self.VocStr5.setFont(font1)
        self.VocStr5.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.VocStr5.setAlignment(Qt.AlignCenter)
        self.VocStr5.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.VocStr5, 0, 0, 1, 1)

        self.VocStr6 = QLabel(self.JVParametersFrame)
        self.VocStr6.setObjectName(u"VocStr6")
        sizePolicy.setHeightForWidth(self.VocStr6.sizePolicy().hasHeightForWidth())
        self.VocStr6.setSizePolicy(sizePolicy)
        self.VocStr6.setMinimumSize(QSize(10, 2))
        self.VocStr6.setFont(font1)
        self.VocStr6.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.VocStr6.setAlignment(Qt.AlignCenter)
        self.VocStr6.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.VocStr6, 0, 1, 1, 1)

        self.VocStr7 = QLabel(self.JVParametersFrame)
        self.VocStr7.setObjectName(u"VocStr7")
        sizePolicy.setHeightForWidth(self.VocStr7.sizePolicy().hasHeightForWidth())
        self.VocStr7.setSizePolicy(sizePolicy)
        self.VocStr7.setMinimumSize(QSize(10, 2))
        self.VocStr7.setFont(font1)
        self.VocStr7.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.VocStr7.setAlignment(Qt.AlignCenter)
        self.VocStr7.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.VocStr7, 0, 2, 1, 1)

        self.VocStr8 = QLabel(self.JVParametersFrame)
        self.VocStr8.setObjectName(u"VocStr8")
        sizePolicy.setHeightForWidth(self.VocStr8.sizePolicy().hasHeightForWidth())
        self.VocStr8.setSizePolicy(sizePolicy)
        self.VocStr8.setMinimumSize(QSize(10, 2))
        self.VocStr8.setFont(font1)
        self.VocStr8.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.VocStr8.setAlignment(Qt.AlignCenter)
        self.VocStr8.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.VocStr8, 0, 3, 1, 1)

        self.JscStr5 = QLabel(self.JVParametersFrame)
        self.JscStr5.setObjectName(u"JscStr5")
        sizePolicy.setHeightForWidth(self.JscStr5.sizePolicy().hasHeightForWidth())
        self.JscStr5.setSizePolicy(sizePolicy)
        self.JscStr5.setMinimumSize(QSize(10, 2))
        self.JscStr5.setFont(font1)
        self.JscStr5.setStyleSheet(u"  color: rgb(255, 100, 80);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.JscStr5.setAlignment(Qt.AlignCenter)
        self.JscStr5.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.JscStr5, 1, 0, 1, 1)

        self.JscStr6 = QLabel(self.JVParametersFrame)
        self.JscStr6.setObjectName(u"JscStr6")
        sizePolicy.setHeightForWidth(self.JscStr6.sizePolicy().hasHeightForWidth())
        self.JscStr6.setSizePolicy(sizePolicy)
        self.JscStr6.setMinimumSize(QSize(10, 2))
        self.JscStr6.setFont(font1)
        self.JscStr6.setStyleSheet(u"  color: rgb(255, 100, 80);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.JscStr6.setAlignment(Qt.AlignCenter)
        self.JscStr6.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.JscStr6, 1, 1, 1, 1)

        self.JscStr7 = QLabel(self.JVParametersFrame)
        self.JscStr7.setObjectName(u"JscStr7")
        sizePolicy.setHeightForWidth(self.JscStr7.sizePolicy().hasHeightForWidth())
        self.JscStr7.setSizePolicy(sizePolicy)
        self.JscStr7.setMinimumSize(QSize(10, 2))
        self.JscStr7.setFont(font1)
        self.JscStr7.setStyleSheet(u"  color: rgb(255, 100, 80);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.JscStr7.setAlignment(Qt.AlignCenter)
        self.JscStr7.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.JscStr7, 1, 2, 1, 1)

        self.JscStr8 = QLabel(self.JVParametersFrame)
        self.JscStr8.setObjectName(u"JscStr8")
        sizePolicy.setHeightForWidth(self.JscStr8.sizePolicy().hasHeightForWidth())
        self.JscStr8.setSizePolicy(sizePolicy)
        self.JscStr8.setMinimumSize(QSize(10, 2))
        self.JscStr8.setFont(font1)
        self.JscStr8.setStyleSheet(u"  color: rgb(255, 100, 80);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.JscStr8.setAlignment(Qt.AlignCenter)
        self.JscStr8.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.JscStr8, 1, 3, 1, 1)

        self.FFStr5 = QLabel(self.JVParametersFrame)
        self.FFStr5.setObjectName(u"FFStr5")
        sizePolicy.setHeightForWidth(self.FFStr5.sizePolicy().hasHeightForWidth())
        self.FFStr5.setSizePolicy(sizePolicy)
        self.FFStr5.setMinimumSize(QSize(10, 2))
        self.FFStr5.setFont(font1)
        self.FFStr5.setStyleSheet(u"color: rgb(255, 189, 74);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.FFStr5.setAlignment(Qt.AlignCenter)
        self.FFStr5.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.FFStr5, 2, 0, 1, 1)

        self.FFStr6 = QLabel(self.JVParametersFrame)
        self.FFStr6.setObjectName(u"FFStr6")
        sizePolicy.setHeightForWidth(self.FFStr6.sizePolicy().hasHeightForWidth())
        self.FFStr6.setSizePolicy(sizePolicy)
        self.FFStr6.setMinimumSize(QSize(10, 2))
        self.FFStr6.setFont(font1)
        self.FFStr6.setStyleSheet(u"color: rgb(255, 189, 74);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.FFStr6.setAlignment(Qt.AlignCenter)
        self.FFStr6.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.FFStr6, 2, 1, 1, 1)

        self.FFStr7 = QLabel(self.JVParametersFrame)
        self.FFStr7.setObjectName(u"FFStr7")
        sizePolicy.setHeightForWidth(self.FFStr7.sizePolicy().hasHeightForWidth())
        self.FFStr7.setSizePolicy(sizePolicy)
        self.FFStr7.setMinimumSize(QSize(10, 2))
        self.FFStr7.setFont(font1)
        self.FFStr7.setStyleSheet(u"color: rgb(255, 189, 74);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.FFStr7.setAlignment(Qt.AlignCenter)
        self.FFStr7.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.FFStr7, 2, 2, 1, 1)

        self.FFStr8 = QLabel(self.JVParametersFrame)
        self.FFStr8.setObjectName(u"FFStr8")
        sizePolicy.setHeightForWidth(self.FFStr8.sizePolicy().hasHeightForWidth())
        self.FFStr8.setSizePolicy(sizePolicy)
        self.FFStr8.setMinimumSize(QSize(10, 2))
        self.FFStr8.setFont(font1)
        self.FFStr8.setStyleSheet(u"color: rgb(255, 189, 74);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.FFStr8.setAlignment(Qt.AlignCenter)
        self.FFStr8.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.FFStr8, 2, 3, 1, 1)

        self.PCEStr5 = QLabel(self.JVParametersFrame)
        self.PCEStr5.setObjectName(u"PCEStr5")
        sizePolicy.setHeightForWidth(self.PCEStr5.sizePolicy().hasHeightForWidth())
        self.PCEStr5.setSizePolicy(sizePolicy)
        self.PCEStr5.setMinimumSize(QSize(10, 2))
        self.PCEStr5.setFont(font1)
        self.PCEStr5.setStyleSheet(u"color: rgb(139, 255, 119);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.PCEStr5.setAlignment(Qt.AlignCenter)
        self.PCEStr5.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.PCEStr5, 3, 0, 1, 1)

        self.PCEStr6 = QLabel(self.JVParametersFrame)
        self.PCEStr6.setObjectName(u"PCEStr6")
        sizePolicy.setHeightForWidth(self.PCEStr6.sizePolicy().hasHeightForWidth())
        self.PCEStr6.setSizePolicy(sizePolicy)
        self.PCEStr6.setMinimumSize(QSize(10, 2))
        self.PCEStr6.setFont(font1)
        self.PCEStr6.setStyleSheet(u"color: rgb(139, 255, 119);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.PCEStr6.setAlignment(Qt.AlignCenter)
        self.PCEStr6.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.PCEStr6, 3, 1, 1, 1)

        self.PCEStr7 = QLabel(self.JVParametersFrame)
        self.PCEStr7.setObjectName(u"PCEStr7")
        sizePolicy.setHeightForWidth(self.PCEStr7.sizePolicy().hasHeightForWidth())
        self.PCEStr7.setSizePolicy(sizePolicy)
        self.PCEStr7.setMinimumSize(QSize(10, 2))
        self.PCEStr7.setFont(font1)
        self.PCEStr7.setStyleSheet(u"color: rgb(139, 255, 119);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.PCEStr7.setAlignment(Qt.AlignCenter)
        self.PCEStr7.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.PCEStr7, 3, 2, 1, 1)

        self.PCEStr8 = QLabel(self.JVParametersFrame)
        self.PCEStr8.setObjectName(u"PCEStr8")
        sizePolicy.setHeightForWidth(self.PCEStr8.sizePolicy().hasHeightForWidth())
        self.PCEStr8.setSizePolicy(sizePolicy)
        self.PCEStr8.setMinimumSize(QSize(10, 2))
        self.PCEStr8.setFont(font1)
        self.PCEStr8.setStyleSheet(u"color: rgb(139, 255, 119);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.PCEStr8.setAlignment(Qt.AlignCenter)
        self.PCEStr8.setWordWrap(True)

        self.StringParametersLayout2.addWidget(self.PCEStr8, 3, 3, 1, 1)


        self.gridLayout_4.addLayout(self.StringParametersLayout2, 1, 2, 1, 1)

        self.UnitsLayout = QVBoxLayout()
        self.UnitsLayout.setObjectName(u"UnitsLayout")
        self.VoltsLabel = QLabel(self.JVParametersFrame)
        self.VoltsLabel.setObjectName(u"VoltsLabel")
        sizePolicy.setHeightForWidth(self.VoltsLabel.sizePolicy().hasHeightForWidth())
        self.VoltsLabel.setSizePolicy(sizePolicy)
        self.VoltsLabel.setMinimumSize(QSize(10, 2))
        self.VoltsLabel.setFont(font)
        self.VoltsLabel.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.VoltsLabel.setAlignment(Qt.AlignCenter)
        self.VoltsLabel.setWordWrap(True)

        self.UnitsLayout.addWidget(self.VoltsLabel)

        self.am2Label = QLabel(self.JVParametersFrame)
        self.am2Label.setObjectName(u"am2Label")
        sizePolicy.setHeightForWidth(self.am2Label.sizePolicy().hasHeightForWidth())
        self.am2Label.setSizePolicy(sizePolicy)
        self.am2Label.setMinimumSize(QSize(10, 2))
        self.am2Label.setFont(font)
        self.am2Label.setStyleSheet(u"  color: rgb(255, 100, 80);")
        self.am2Label.setAlignment(Qt.AlignCenter)
        self.am2Label.setWordWrap(True)

        self.UnitsLayout.addWidget(self.am2Label)

        self.pecentagelabelff = QLabel(self.JVParametersFrame)
        self.pecentagelabelff.setObjectName(u"pecentagelabelff")
        sizePolicy.setHeightForWidth(self.pecentagelabelff.sizePolicy().hasHeightForWidth())
        self.pecentagelabelff.setSizePolicy(sizePolicy)
        self.pecentagelabelff.setMinimumSize(QSize(10, 2))
        self.pecentagelabelff.setFont(font)
        self.pecentagelabelff.setStyleSheet(u"color: rgb(255, 189, 74);")
        self.pecentagelabelff.setAlignment(Qt.AlignCenter)
        self.pecentagelabelff.setWordWrap(True)

        self.UnitsLayout.addWidget(self.pecentagelabelff)

        self.percentageLabelPCE = QLabel(self.JVParametersFrame)
        self.percentageLabelPCE.setObjectName(u"percentageLabelPCE")
        sizePolicy.setHeightForWidth(self.percentageLabelPCE.sizePolicy().hasHeightForWidth())
        self.percentageLabelPCE.setSizePolicy(sizePolicy)
        self.percentageLabelPCE.setMinimumSize(QSize(10, 2))
        self.percentageLabelPCE.setFont(font)
        self.percentageLabelPCE.setStyleSheet(u"color: rgb(139, 255, 119);")
        self.percentageLabelPCE.setAlignment(Qt.AlignCenter)
        self.percentageLabelPCE.setWordWrap(True)

        self.UnitsLayout.addWidget(self.percentageLabelPCE)


        self.gridLayout_4.addLayout(self.UnitsLayout, 1, 3, 1, 1)

        self.gridLayout_4.setRowStretch(0, 10)
        self.gridLayout_4.setRowStretch(1, 90)
        self.gridLayout_4.setColumnStretch(0, 10)
        self.gridLayout_4.setColumnStretch(1, 40)
        self.gridLayout_4.setColumnStretch(2, 40)
        self.gridLayout_4.setColumnStretch(3, 10)

        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.JVParametersFrame, 1, 0, 1, 2)

        self.gridLayout_2.setRowStretch(0, 50)
        self.gridLayout_2.setRowStretch(1, 50)
        self.stackedWidget.addWidget(self.JVCurvesStack)
        self.HistoricalData = QWidget()
        self.HistoricalData.setObjectName(u"HistoricalData")
        self.verticalLayout_2 = QVBoxLayout(self.HistoricalData)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_cell_list = QComboBox(self.HistoricalData)
        self.comboBox_cell_list.setObjectName(u"comboBox_cell_list")
        self.comboBox_cell_list.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.comboBox_cell_list.setEditable(False)

        self.verticalLayout_2.addWidget(self.comboBox_cell_list)

        self.stackedWidget_cells_plot = QStackedWidget(self.HistoricalData)
        self.stackedWidget_cells_plot.setObjectName(u"stackedWidget_cells_plot")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_cells_plot.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_cells_plot.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget_cells_plot)

        self.stackedWidget.addWidget(self.HistoricalData)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.TimeBetweenJV = QDoubleSpinBox(self.Settings)
        self.TimeBetweenJV.setObjectName(u"TimeBetweenJV")
        self.TimeBetweenJV.setGeometry(QRect(110, 200, 151, 31))
        palette = QPalette()
        brush = QBrush(QColor(75, 81, 72, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.TimeBetweenJV.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.TimeBetweenJV.setFont(font2)
        self.TimeBetweenJV.setStyleSheet(u"font: 20pt \"Bahnschrift\";")
        self.TimeBetweenJV.setWrapping(True)
        self.TimeBetweenJV.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.TimeBetweenJV.setDecimals(0)
        self.TimeBetweenJV.setMinimum(0.000000000000000)
        self.TimeBetweenJV.setMaximum(200.000000000000000)
        self.TimeBetweenJV.setSingleStep(1.000000000000000)
        self.TimeBetweenJV.setValue(10.000000000000000)
        self.TimeBetweenJVCurvesLabel = QLabel(self.Settings)
        self.TimeBetweenJVCurvesLabel.setObjectName(u"TimeBetweenJVCurvesLabel")
        self.TimeBetweenJVCurvesLabel.setGeometry(QRect(10, 160, 361, 33))
        sizePolicy.setHeightForWidth(self.TimeBetweenJVCurvesLabel.sizePolicy().hasHeightForWidth())
        self.TimeBetweenJVCurvesLabel.setSizePolicy(sizePolicy)
        self.TimeBetweenJVCurvesLabel.setMinimumSize(QSize(10, 2))
        self.TimeBetweenJVCurvesLabel.setFont(font)
        self.TimeBetweenJVCurvesLabel.setStyleSheet(u"  color: rgb(231, 255, 158);")
        self.TimeBetweenJVCurvesLabel.setWordWrap(True)
        self.TimeBetweenPowerMeasurements = QDoubleSpinBox(self.Settings)
        self.TimeBetweenPowerMeasurements.setObjectName(u"TimeBetweenPowerMeasurements")
        self.TimeBetweenPowerMeasurements.setGeometry(QRect(110, 90, 151, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.TimeBetweenPowerMeasurements.setPalette(palette1)
        self.TimeBetweenPowerMeasurements.setFont(font2)
        self.TimeBetweenPowerMeasurements.setStyleSheet(u"font: 20pt \"Bahnschrift\";")
        self.TimeBetweenPowerMeasurements.setWrapping(True)
        self.TimeBetweenPowerMeasurements.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.TimeBetweenPowerMeasurements.setDecimals(0)
        self.TimeBetweenPowerMeasurements.setMinimum(5.000000000000000)
        self.TimeBetweenPowerMeasurements.setMaximum(500.000000000000000)
        self.TimeBetweenPowerMeasurements.setSingleStep(1.000000000000000)
        self.TimeBetweenPowerLabel = QLabel(self.Settings)
        self.TimeBetweenPowerLabel.setObjectName(u"TimeBetweenPowerLabel")
        self.TimeBetweenPowerLabel.setGeometry(QRect(10, 50, 361, 33))
        sizePolicy.setHeightForWidth(self.TimeBetweenPowerLabel.sizePolicy().hasHeightForWidth())
        self.TimeBetweenPowerLabel.setSizePolicy(sizePolicy)
        self.TimeBetweenPowerLabel.setMinimumSize(QSize(10, 2))
        self.TimeBetweenPowerLabel.setFont(font)
        self.TimeBetweenPowerLabel.setStyleSheet(u"  color: rgb(231, 255, 158);")
        self.TimeBetweenPowerLabel.setWordWrap(True)
        self.PathDataLabel = QLabel(self.Settings)
        self.PathDataLabel.setObjectName(u"PathDataLabel")
        self.PathDataLabel.setGeometry(QRect(500, 50, 361, 33))
        sizePolicy.setHeightForWidth(self.PathDataLabel.sizePolicy().hasHeightForWidth())
        self.PathDataLabel.setSizePolicy(sizePolicy)
        self.PathDataLabel.setMinimumSize(QSize(10, 2))
        self.PathDataLabel.setFont(font)
        self.PathDataLabel.setStyleSheet(u"  color: rgb(231, 255, 158);")
        self.PathDataLabel.setWordWrap(True)
        self.PathToSaveButton = QPushButton(self.Settings)
        self.PathToSaveButton.setObjectName(u"PathToSaveButton")
        self.PathToSaveButton.setGeometry(QRect(440, 100, 501, 61))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.PathToSaveButton.sizePolicy().hasHeightForWidth())
        self.PathToSaveButton.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(20)
        self.PathToSaveButton.setFont(font3)
        self.PathToSaveButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(100, 79, 79);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 100, 100);\n"
"color: rgb(100, 79, 79);\n"
"	border: none\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 80, 80);\n"
"color: rgb(100, 79, 79);\n"
"	border: none\n"
"}\n"
"\n"
"")
        self.PathToSaveButton.setAutoRepeat(False)
        self.PathToSaveButton.setFlat(False)
        self.stackedWidget_MeasurementTriggers = QStackedWidget(self.Settings)
        self.stackedWidget_MeasurementTriggers.setObjectName(u"stackedWidget_MeasurementTriggers")
        self.stackedWidget_MeasurementTriggers.setGeometry(QRect(870, 670, 271, 45))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.StartMeasurementsButton = QPushButton(self.page_3)
        self.StartMeasurementsButton.setObjectName(u"StartMeasurementsButton")
        self.StartMeasurementsButton.setFont(font3)
        self.StartMeasurementsButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 130, 132);\n"
"color: rgb(100, 79, 79);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 100, 100);\n"
"color: rgb(100, 79, 79);\n"
"	border: none\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 80, 80);\n"
"color: rgb(100, 79, 79);\n"
"	border: none\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.StartMeasurementsButton)

        self.stackedWidget_MeasurementTriggers.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.PauseMeasurementsButton = QPushButton(self.page_4)
        self.PauseMeasurementsButton.setObjectName(u"PauseMeasurementsButton")
        self.PauseMeasurementsButton.setFont(font3)
        self.PauseMeasurementsButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 130, 132);\n"
"color: rgb(100, 79, 79);\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 100, 100);\n"
"color: rgb(100, 79, 79);\n"
"	border: none\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(255, 80, 80);\n"
"color: rgb(100, 79, 79);\n"
"	border: none\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.PauseMeasurementsButton)

        self.stackedWidget_MeasurementTriggers.addWidget(self.page_4)
        self.stackedWidget.addWidget(self.Settings)
        self.DashBoardStack = QWidget()
        self.DashBoardStack.setObjectName(u"DashBoardStack")
        self.gridLayout = QGridLayout(self.DashBoardStack)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.DashboardMainVLayout = QVBoxLayout()
        self.DashboardMainVLayout.setObjectName(u"DashboardMainVLayout")
        self.DashboardMainVLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.DashboardMainVLayout.setContentsMargins(5, 5, 5, 5)
        self.DashboardTopLayout = QHBoxLayout()
        self.DashboardTopLayout.setObjectName(u"DashboardTopLayout")
        self.SunPowerFrame = QFrame(self.DashBoardStack)
        self.SunPowerFrame.setObjectName(u"SunPowerFrame")
        self.SunPowerFrame.setFrameShape(QFrame.StyledPanel)
        self.SunPowerFrame.setFrameShadow(QFrame.Raised)
        self.SunPowerFrame.setLineWidth(0)
        self.label = QLabel(self.SunPowerFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 291, 301))
        self.label.setPixmap(QPixmap(u":/icons/sun_full_png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_3 = QWidget(self.SunPowerFrame)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(140, 130, 91, 61))
        self.SunPowerLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.SunPowerLayout.setSpacing(0)
        self.SunPowerLayout.setObjectName(u"SunPowerLayout")
        self.SunPowerLayout.setContentsMargins(0, 0, 0, 0)
        self.SunPowerLabel = QLabel(self.verticalLayoutWidget_3)
        self.SunPowerLabel.setObjectName(u"SunPowerLabel")
        sizePolicy.setHeightForWidth(self.SunPowerLabel.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel.setSizePolicy(sizePolicy)
        self.SunPowerLabel.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel.setFont(font)
        self.SunPowerLabel.setStyleSheet(u"  color: rgb(254, 249, 193);\n"
"background: transparent;")
        self.SunPowerLabel.setAlignment(Qt.AlignCenter)
        self.SunPowerLabel.setWordWrap(True)

        self.SunPowerLayout.addWidget(self.SunPowerLabel)

        self.SunPowerUnitsLabel = QLabel(self.verticalLayoutWidget_3)
        self.SunPowerUnitsLabel.setObjectName(u"SunPowerUnitsLabel")
        sizePolicy.setHeightForWidth(self.SunPowerUnitsLabel.sizePolicy().hasHeightForWidth())
        self.SunPowerUnitsLabel.setSizePolicy(sizePolicy)
        self.SunPowerUnitsLabel.setMinimumSize(QSize(10, 2))
        self.SunPowerUnitsLabel.setFont(font)
        self.SunPowerUnitsLabel.setStyleSheet(u"  color: rgb(254, 249, 193);\n"
"background: transparent;")
        self.SunPowerUnitsLabel.setWordWrap(True)

        self.SunPowerLayout.addWidget(self.SunPowerUnitsLabel)


        self.DashboardTopLayout.addWidget(self.SunPowerFrame)

        self.EnergyDashboardLayout = QGridLayout()
        self.EnergyDashboardLayout.setObjectName(u"EnergyDashboardLayout")
        self.EnergyDashboardLayout.setVerticalSpacing(30)
        self.GeneratedNeedsVlayout = QVBoxLayout()
        self.GeneratedNeedsVlayout.setObjectName(u"GeneratedNeedsVlayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SunPowerLabel_8 = QLabel(self.DashBoardStack)
        self.SunPowerLabel_8.setObjectName(u"SunPowerLabel_8")
        sizePolicy.setHeightForWidth(self.SunPowerLabel_8.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_8.setSizePolicy(sizePolicy)
        self.SunPowerLabel_8.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_8.setFont(font)
        self.SunPowerLabel_8.setStyleSheet(u"  color: rgb(190, 255, 236);")
        self.SunPowerLabel_8.setWordWrap(True)

        self.horizontalLayout.addWidget(self.SunPowerLabel_8)

        self.SunPowerLabel_6 = QLabel(self.DashBoardStack)
        self.SunPowerLabel_6.setObjectName(u"SunPowerLabel_6")
        sizePolicy.setHeightForWidth(self.SunPowerLabel_6.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_6.setSizePolicy(sizePolicy)
        self.SunPowerLabel_6.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_6.setFont(font)
        self.SunPowerLabel_6.setStyleSheet(u"  color: rgb(13, 255, 180);")
        self.SunPowerLabel_6.setWordWrap(True)

        self.horizontalLayout.addWidget(self.SunPowerLabel_6)


        self.GeneratedNeedsVlayout.addLayout(self.horizontalLayout)

        self.SunPowerLabel_7 = QLabel(self.DashBoardStack)
        self.SunPowerLabel_7.setObjectName(u"SunPowerLabel_7")
        sizePolicy.setHeightForWidth(self.SunPowerLabel_7.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_7.setSizePolicy(sizePolicy)
        self.SunPowerLabel_7.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_7.setFont(font)
        self.SunPowerLabel_7.setStyleSheet(u"  color:rgb(190, 255, 236);")
        self.SunPowerLabel_7.setWordWrap(True)

        self.GeneratedNeedsVlayout.addWidget(self.SunPowerLabel_7)


        self.EnergyDashboardLayout.addLayout(self.GeneratedNeedsVlayout, 2, 1, 1, 1)

        self.TodaysEnergyVlayout = QVBoxLayout()
        self.TodaysEnergyVlayout.setObjectName(u"TodaysEnergyVlayout")
        self.SunPowerLabel_4 = QLabel(self.DashBoardStack)
        self.SunPowerLabel_4.setObjectName(u"SunPowerLabel_4")
        sizePolicy.setHeightForWidth(self.SunPowerLabel_4.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_4.setSizePolicy(sizePolicy)
        self.SunPowerLabel_4.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_4.setFont(font)
        self.SunPowerLabel_4.setStyleSheet(u"  color: rgb(231, 255, 158);")
        self.SunPowerLabel_4.setWordWrap(True)

        self.TodaysEnergyVlayout.addWidget(self.SunPowerLabel_4)

        self.SunPowerLabel_5 = QLabel(self.DashBoardStack)
        self.SunPowerLabel_5.setObjectName(u"SunPowerLabel_5")
        sizePolicy.setHeightForWidth(self.SunPowerLabel_5.sizePolicy().hasHeightForWidth())
        self.SunPowerLabel_5.setSizePolicy(sizePolicy)
        self.SunPowerLabel_5.setMinimumSize(QSize(10, 2))
        self.SunPowerLabel_5.setFont(font)
        self.SunPowerLabel_5.setStyleSheet(u"  color: rgb(195, 255, 17);")
        self.SunPowerLabel_5.setWordWrap(True)

        self.TodaysEnergyVlayout.addWidget(self.SunPowerLabel_5)


        self.EnergyDashboardLayout.addLayout(self.TodaysEnergyVlayout, 0, 1, 1, 1)

        self.NextMeasTimeVlayout = QVBoxLayout()
        self.NextMeasTimeVlayout.setObjectName(u"NextMeasTimeVlayout")
        self.NextMeasurementInLabel = QLabel(self.DashBoardStack)
        self.NextMeasurementInLabel.setObjectName(u"NextMeasurementInLabel")
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(18)
        font4.setBold(False)
        font4.setItalic(False)
        self.NextMeasurementInLabel.setFont(font4)
        self.NextMeasurementInLabel.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.NextMeasurementInLabel.setAlignment(Qt.AlignCenter)

        self.NextMeasTimeVlayout.addWidget(self.NextMeasurementInLabel)

        self.NextMeasurementTimeIntervalLabel = QLabel(self.DashBoardStack)
        self.NextMeasurementTimeIntervalLabel.setObjectName(u"NextMeasurementTimeIntervalLabel")
        self.NextMeasurementTimeIntervalLabel.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")
        self.NextMeasurementTimeIntervalLabel.setAlignment(Qt.AlignCenter)

        self.NextMeasTimeVlayout.addWidget(self.NextMeasurementTimeIntervalLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.NextMeasTimeVlayout.addItem(self.verticalSpacer)

        self.NextMeasTimeVlayout.setStretch(0, 30)
        self.NextMeasTimeVlayout.setStretch(1, 70)

        self.EnergyDashboardLayout.addLayout(self.NextMeasTimeVlayout, 2, 0, 1, 1)

        self.CurrentSolarPowerVlayout = QVBoxLayout()
        self.CurrentSolarPowerVlayout.setObjectName(u"CurrentSolarPowerVlayout")
        self.CurrentSolarPowerLabel = QLabel(self.DashBoardStack)
        self.CurrentSolarPowerLabel.setObjectName(u"CurrentSolarPowerLabel")
        sizePolicy.setHeightForWidth(self.CurrentSolarPowerLabel.sizePolicy().hasHeightForWidth())
        self.CurrentSolarPowerLabel.setSizePolicy(sizePolicy)
        self.CurrentSolarPowerLabel.setMinimumSize(QSize(10, 2))
        self.CurrentSolarPowerLabel.setFont(font)
        self.CurrentSolarPowerLabel.setStyleSheet(u"  color: rgb(255, 200, 136);")
        self.CurrentSolarPowerLabel.setWordWrap(True)

        self.CurrentSolarPowerVlayout.addWidget(self.CurrentSolarPowerLabel)

        self.CurrentPowerLabel = QLabel(self.DashBoardStack)
        self.CurrentPowerLabel.setObjectName(u"CurrentPowerLabel")
        sizePolicy.setHeightForWidth(self.CurrentPowerLabel.sizePolicy().hasHeightForWidth())
        self.CurrentPowerLabel.setSizePolicy(sizePolicy)
        self.CurrentPowerLabel.setMinimumSize(QSize(10, 2))
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dlg 2"])
        font5.setPointSize(36)
        font5.setBold(False)
        font5.setItalic(False)
        self.CurrentPowerLabel.setFont(font5)
        self.CurrentPowerLabel.setStyleSheet(u"  color: rgb(255, 152, 30);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.CurrentPowerLabel.setAlignment(Qt.AlignCenter)
        self.CurrentPowerLabel.setWordWrap(True)

        self.CurrentSolarPowerVlayout.addWidget(self.CurrentPowerLabel)


        self.EnergyDashboardLayout.addLayout(self.CurrentSolarPowerVlayout, 0, 0, 1, 1)


        self.DashboardTopLayout.addLayout(self.EnergyDashboardLayout)

        self.DashboardTopLayout.setStretch(0, 35)
        self.DashboardTopLayout.setStretch(1, 65)

        self.DashboardMainVLayout.addLayout(self.DashboardTopLayout)

        self.DashboardBotLayout = QHBoxLayout()
        self.DashboardBotLayout.setObjectName(u"DashboardBotLayout")
        self.StringPowerWidgetLayout = QGridLayout()
        self.StringPowerWidgetLayout.setSpacing(0)
        self.StringPowerWidgetLayout.setObjectName(u"StringPowerWidgetLayout")
        self.UselessFrame1 = QFrame(self.DashBoardStack)
        self.UselessFrame1.setObjectName(u"UselessFrame1")
        self.UselessFrame1.setFrameShape(QFrame.StyledPanel)
        self.UselessFrame1.setFrameShadow(QFrame.Raised)

        self.StringPowerWidgetLayout.addWidget(self.UselessFrame1, 2, 0, 1, 1)

        self.PowerBarMetersLayout = QFrame(self.DashBoardStack)
        self.PowerBarMetersLayout.setObjectName(u"PowerBarMetersLayout")
        self.PowerBarMetersLayout.setFrameShape(QFrame.StyledPanel)
        self.PowerBarMetersLayout.setFrameShadow(QFrame.Raised)

        self.StringPowerWidgetLayout.addWidget(self.PowerBarMetersLayout, 1, 1, 1, 1)

        self.PowerMeterYaxisLayout = QVBoxLayout()
        self.PowerMeterYaxisLayout.setObjectName(u"PowerMeterYaxisLayout")
        self.MaxPowerLabel = QLabel(self.DashBoardStack)
        self.MaxPowerLabel.setObjectName(u"MaxPowerLabel")
        self.MaxPowerLabel.setFont(font)
        self.MaxPowerLabel.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.PowerMeterYaxisLayout.addWidget(self.MaxPowerLabel)

        self.PowerWLabel = QLabel(self.DashBoardStack)
        self.PowerWLabel.setObjectName(u"PowerWLabel")
        self.PowerWLabel.setFont(font)
        self.PowerWLabel.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.PowerMeterYaxisLayout.addWidget(self.PowerWLabel)

        self.MinPowerLabel = QLabel(self.DashBoardStack)
        self.MinPowerLabel.setObjectName(u"MinPowerLabel")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        self.MinPowerLabel.setFont(font6)
        self.MinPowerLabel.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.PowerMeterYaxisLayout.addWidget(self.MinPowerLabel)


        self.StringPowerWidgetLayout.addLayout(self.PowerMeterYaxisLayout, 1, 0, 1, 1)

        self.StringsXaxisLayout = QHBoxLayout()
        self.StringsXaxisLayout.setSpacing(0)
        self.StringsXaxisLayout.setObjectName(u"StringsXaxisLayout")
        self.String1Label = QLabel(self.DashBoardStack)
        self.String1Label.setObjectName(u"String1Label")
        sizePolicy.setHeightForWidth(self.String1Label.sizePolicy().hasHeightForWidth())
        self.String1Label.setSizePolicy(sizePolicy)
        self.String1Label.setMinimumSize(QSize(10, 2))
        self.String1Label.setFont(font6)
        self.String1Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String1Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String1Label)

        self.String2Label = QLabel(self.DashBoardStack)
        self.String2Label.setObjectName(u"String2Label")
        sizePolicy.setHeightForWidth(self.String2Label.sizePolicy().hasHeightForWidth())
        self.String2Label.setSizePolicy(sizePolicy)
        self.String2Label.setMinimumSize(QSize(10, 2))
        self.String2Label.setFont(font6)
        self.String2Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String2Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String2Label)

        self.String3Label = QLabel(self.DashBoardStack)
        self.String3Label.setObjectName(u"String3Label")
        sizePolicy.setHeightForWidth(self.String3Label.sizePolicy().hasHeightForWidth())
        self.String3Label.setSizePolicy(sizePolicy)
        self.String3Label.setMinimumSize(QSize(10, 2))
        self.String3Label.setFont(font6)
        self.String3Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String3Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String3Label)

        self.String4Label = QLabel(self.DashBoardStack)
        self.String4Label.setObjectName(u"String4Label")
        sizePolicy.setHeightForWidth(self.String4Label.sizePolicy().hasHeightForWidth())
        self.String4Label.setSizePolicy(sizePolicy)
        self.String4Label.setMinimumSize(QSize(10, 2))
        self.String4Label.setFont(font6)
        self.String4Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String4Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String4Label)

        self.StringNumberLabelLayout = QVBoxLayout()
        self.StringNumberLabelLayout.setSpacing(0)
        self.StringNumberLabelLayout.setObjectName(u"StringNumberLabelLayout")
        self.StringNumberString = QLabel(self.DashBoardStack)
        self.StringNumberString.setObjectName(u"StringNumberString")
        sizePolicy.setHeightForWidth(self.StringNumberString.sizePolicy().hasHeightForWidth())
        self.StringNumberString.setSizePolicy(sizePolicy)
        self.StringNumberString.setMinimumSize(QSize(10, 2))
        self.StringNumberString.setFont(font6)
        self.StringNumberString.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.StringNumberLabelLayout.addWidget(self.StringNumberString)

        self.StringNumberNumber = QLabel(self.DashBoardStack)
        self.StringNumberNumber.setObjectName(u"StringNumberNumber")
        sizePolicy.setHeightForWidth(self.StringNumberNumber.sizePolicy().hasHeightForWidth())
        self.StringNumberNumber.setSizePolicy(sizePolicy)
        self.StringNumberNumber.setMinimumSize(QSize(10, 2))
        self.StringNumberNumber.setFont(font6)
        self.StringNumberNumber.setStyleSheet(u"  color: rgb(211, 213, 211);")

        self.StringNumberLabelLayout.addWidget(self.StringNumberNumber)


        self.StringsXaxisLayout.addLayout(self.StringNumberLabelLayout)

        self.String5Label = QLabel(self.DashBoardStack)
        self.String5Label.setObjectName(u"String5Label")
        sizePolicy.setHeightForWidth(self.String5Label.sizePolicy().hasHeightForWidth())
        self.String5Label.setSizePolicy(sizePolicy)
        self.String5Label.setMinimumSize(QSize(10, 2))
        self.String5Label.setFont(font6)
        self.String5Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String5Label.setScaledContents(False)
        self.String5Label.setAlignment(Qt.AlignCenter)
        self.String5Label.setWordWrap(True)

        self.StringsXaxisLayout.addWidget(self.String5Label)

        self.String6Label = QLabel(self.DashBoardStack)
        self.String6Label.setObjectName(u"String6Label")
        sizePolicy.setHeightForWidth(self.String6Label.sizePolicy().hasHeightForWidth())
        self.String6Label.setSizePolicy(sizePolicy)
        self.String6Label.setMinimumSize(QSize(10, 2))
        self.String6Label.setFont(font6)
        self.String6Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String6Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String6Label)

        self.String7Label = QLabel(self.DashBoardStack)
        self.String7Label.setObjectName(u"String7Label")
        sizePolicy.setHeightForWidth(self.String7Label.sizePolicy().hasHeightForWidth())
        self.String7Label.setSizePolicy(sizePolicy)
        self.String7Label.setMinimumSize(QSize(10, 2))
        self.String7Label.setFont(font6)
        self.String7Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String7Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String7Label)

        self.String8Label = QLabel(self.DashBoardStack)
        self.String8Label.setObjectName(u"String8Label")
        sizePolicy.setHeightForWidth(self.String8Label.sizePolicy().hasHeightForWidth())
        self.String8Label.setSizePolicy(sizePolicy)
        self.String8Label.setMinimumSize(QSize(10, 2))
        self.String8Label.setFont(font6)
        self.String8Label.setStyleSheet(u"  color: rgb(211, 213, 211);")
        self.String8Label.setAlignment(Qt.AlignCenter)

        self.StringsXaxisLayout.addWidget(self.String8Label)


        self.StringPowerWidgetLayout.addLayout(self.StringsXaxisLayout, 2, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.DashBoardStack)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/string_icon"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.DashBoardStack)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icons/string_icon"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.DashBoardStack)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/icons/string_icon"))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.DashBoardStack)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/icons/string_icon"))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 10)
        self.horizontalLayout_4.setStretch(2, 5)
        self.horizontalLayout_4.setStretch(3, 10)
        self.horizontalLayout_4.setStretch(4, 10)

        self.StringPowerWidgetLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.StringPowerWidgetLayout.setRowStretch(0, 5)
        self.StringPowerWidgetLayout.setRowStretch(1, 90)
        self.StringPowerWidgetLayout.setRowStretch(2, 5)
        self.StringPowerWidgetLayout.setColumnStretch(0, 5)
        self.StringPowerWidgetLayout.setColumnStretch(1, 95)

        self.DashboardBotLayout.addLayout(self.StringPowerWidgetLayout)

        self.HistoricalGraphHolder = QFrame(self.DashBoardStack)
        self.HistoricalGraphHolder.setObjectName(u"HistoricalGraphHolder")
        self.HistoricalGraphHolder.setFrameShape(QFrame.StyledPanel)
        self.HistoricalGraphHolder.setFrameShadow(QFrame.Raised)

        self.DashboardBotLayout.addWidget(self.HistoricalGraphHolder)

        self.DashboardBotLayout.setStretch(0, 70)
        self.DashboardBotLayout.setStretch(1, 30)

        self.DashboardMainVLayout.addLayout(self.DashboardBotLayout)

        self.DashboardMainVLayout.setStretch(0, 45)
        self.DashboardMainVLayout.setStretch(1, 55)

        self.gridLayout.addLayout(self.DashboardMainVLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.DashBoardStack)

        self.horizontalLayout_3.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_cells_plot.setCurrentIndex(1)
        self.stackedWidget_MeasurementTriggers.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSomtheng.setText(QCoreApplication.translate("MainWindow", u"Somtheng", None))
        self.actionSomething_else.setText(QCoreApplication.translate("MainWindow", u"Something else", None))
        self.actionSomething_Dumb.setText(QCoreApplication.translate("MainWindow", u"Something Dumb", None))
        self.actionSomething_clever.setText(QCoreApplication.translate("MainWindow", u"Something clever", None))
        self.OmegaLogoLabel.setText("")
        self.DashboardButton.setText("")
        self.JVCurvesButton.setText("")
        self.HistoricalDataButton.setText("")
        self.SettingsButton.setText("")
        self.String12image2.setText("")
        self.String34image2.setText("")
        self.String56image2.setText("")
        self.String78image2.setText("")
        self.VocLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">V</span><span style=\" font-size:28pt; vertical-align:sub;\">oc</span></p></body></html>", None))
        self.JscLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">J</span><span style=\" font-size:28pt; vertical-align:sub;\">sc</span></p></body></html>", None))
        self.FFLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">FF</span></p></body></html>", None))
        self.PCELabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">PCE</span></p></body></html>", None))
        self.VocStr1.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.VocStr2.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.VocStr3.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.VocStr4.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.JscStr1.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.JscStr2.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.JscStr3.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.JscStr4.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.FFStr1.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.FFStr2.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.FFStr3.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.FFStr4.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.PCEStr1.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.PCEStr2.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.PCEStr3.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.PCEStr4.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.VocStr5.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.VocStr6.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.VocStr7.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.VocStr8.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.JscStr5.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.JscStr6.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.JscStr7.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.JscStr8.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.FFStr5.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.FFStr6.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.FFStr7.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.FFStr8.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.PCEStr5.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.PCEStr6.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.PCEStr7.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.PCEStr8.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.VoltsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">V</span></p></body></html>", None))
        self.am2Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">A m</span><span style=\" font-size:28pt; vertical-align:super;\">-2</span></p></body></html>", None))
        self.pecentagelabelff.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">%</span></p></body></html>", None))
        self.percentageLabelPCE.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">%</span></p></body></html>", None))
        self.comboBox_cell_list.setCurrentText("")
        self.comboBox_cell_list.setPlaceholderText("")
        self.TimeBetweenJV.setSuffix(QCoreApplication.translate("MainWindow", u" min", None))
        self.TimeBetweenJVCurvesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Time Between JV Curves</span></p></body></html>", None))
        self.TimeBetweenPowerMeasurements.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.TimeBetweenPowerLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Power Update Interval</span></p></body></html>", None))
        self.PathDataLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Path to Save Data</span></p></body></html>", None))
        self.PathToSaveButton.setText(QCoreApplication.translate("MainWindow", u"C/blablalbalblalblablalb/abababababab", None))
        self.StartMeasurementsButton.setText(QCoreApplication.translate("MainWindow", u"Start Measurements", None))
        self.PauseMeasurementsButton.setText(QCoreApplication.translate("MainWindow", u"Pause Measurements", None))
        self.label.setText("")
        self.SunPowerLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;\">864</span></p></body></html>", None))
        self.SunPowerUnitsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">W m</span><span style=\" font-size:11pt; vertical-align:super;\">-2</span></p></body></html>", None))
        self.SunPowerLabel_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:25pt;\">Generated</span></p></body></html>", None))
        self.SunPowerLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:60pt;\">15%</span></p></body></html>", None))
        self.SunPowerLabel_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">of today's greenhouse energy needs</span></p></body></html>", None))
        self.SunPowerLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Today's Solar Energy</span></p></body></html>", None))
        self.SunPowerLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:60pt;\">2547 kWh</span></p></body></html>", None))
        self.NextMeasurementInLabel.setText(QCoreApplication.translate("MainWindow", u"Next Measurement in:", None))
        self.NextMeasurementTimeIntervalLabel.setText(QCoreApplication.translate("MainWindow", u"Not Measuring", None))
        self.CurrentSolarPowerLabel.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Bahnschrift'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Current Solar Power</span></p></body></html>", None))
        self.CurrentPowerLabel.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.MaxPowerLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">200</span></p></body></html>", None))
        self.PowerWLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Power (W)</span></p></body></html>", None))
        self.MinPowerLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">0</span></p></body></html>", None))
        self.String1Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">1</span></p></body></html>", None))
        self.String2Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">2</span></p></body></html>", None))
        self.String3Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">3</span></p></body></html>", None))
        self.String4Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">4</span></p></body></html>", None))
        self.StringNumberString.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">String</span></p></body></html>", None))
        self.StringNumberNumber.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Number</span></p></body></html>", None))
        self.String5Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">5</span></p></body></html>", None))
        self.String6Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">6</span></p></body></html>", None))
        self.String7Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">7</span></p></body></html>", None))
        self.String8Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">8</span></p></body></html>", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
    # retranslateUi


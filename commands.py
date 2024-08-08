import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from database import get_commands  # Import the get_commands function from the database script


class Ui_command_screen(object):
    def setupUi(self, command_screen):
        command_screen.setObjectName("command_screen")
        command_screen.resize(811, 510)
        self.centralwidget = QtWidgets.QWidget(parent=command_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: transparent;")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/Commands.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 30, 711, 381))
        self.tableWidget.setStyleSheet("""
        QTableWidget {
            background-color: rgba(0, 0, 0, 150);  /* Semi-transparent black background */
            color: #FFFFFF;  /* Default text color */
            font: bold 12px "Arial";
            gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            border-radius: 15px;  /* Rounded corners */
        }
        QTableWidget::item {
            background-color: rgba(0, 0, 0, 50);  /* Semi-transparent black */
            border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            padding: 5px;
        }
        QHeaderView::section {
            background-color: rgba(0, 0, 0, 150);  /* Semi-transparent black */
            color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 white);  /* Gradient text color */
            font: bold 14px "Arial";
            border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
        }
        QHeaderView {
            background-color: transparent;
        }
        QTableCornerButton::section {
            background-color: rgba(0, 0, 0, 150);  /* Semi-transparent black */
            border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
        }

        /* Scrollbar styling */
        QScrollBar:vertical {
            background: rgba(0, 0, 0, 150);
            width: 16px;
            margin: 20px 0 20px 0;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            min-height: 20px;
            border-radius: 8px;
        }
        QScrollBar::add-line:vertical {
            background: rgba(0, 0, 0, 150);
            height: 20px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
            border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            border-radius: 8px;
        }
        QScrollBar::sub-line:vertical {
            background: rgba(0, 0, 0, 150);
            height: 20px;
            subcontrol-position: top;
            subcontrol-origin: margin;
            border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            border-radius: 8px;
        }
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
            border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            width: 3px;
            height: 3px;
            background: white;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }

        QScrollBar:horizontal {
            background: rgba(0, 0, 0, 150);
            height: 16px;
            margin: 0px 20px 0px 20px;
        }
        QScrollBar::handle:horizontal {
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            min-width: 20px;
            border-radius: 8px;
        }
        QScrollBar::add-line:horizontal {
            background: rgba(0, 0, 0, 150);
            width: 20px;
            subcontrol-position: right;
            subcontrol-origin: margin;
            border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            border-radius: 8px;
        }
        QScrollBar::sub-line:horizontal {
            background: rgba(0, 0, 0, 150);
            width: 20px;
            subcontrol-position: left;
            subcontrol-origin: margin;
            border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            border-radius: 8px;
        }
        QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
            border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 cyan, stop:1 purple);
            width: 3px;
            height: 3px;
            background: white;
        }
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
        }
        """)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        command_screen.setCentralWidget(self.centralwidget)



        self.retranslateUi(command_screen)
        QtCore.QMetaObject.connectSlotsByName(command_screen)

    def retranslateUi(self, command_screen):
        _translate = QtCore.QCoreApplication.translate
        command_screen.setWindowTitle(_translate("command_screen", "MainWindow"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("command_screen", "Command_Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("command_screen", "Action"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("command_screen", "Description"))

        # Fetch commands from the database
        commands = get_commands()

        # Set the number of rows in the table widget
        self.tableWidget.setRowCount(len(commands))

        # Populate the table widget with data from the database
        for row, command in enumerate(commands):
            for col, value in enumerate(command):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    command_screen = QtWidgets.QMainWindow()
    ui = Ui_command_screen()
    ui.setupUi(command_screen)
    command_screen.show()
    sys.exit(app.exec())

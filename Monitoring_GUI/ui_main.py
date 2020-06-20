import serial.tools.list_ports as prtlst
import cv2
import threading
from PyQt5 import uic
from PyQt5 import QtGui
import serial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QTableWidgetItem
from Monitoring_GUI.Create_item import Create_Item
from dao.sah_dao import SAHDao

running = False

initial_serial_devices = set()
result = {"state": "stable", "port_id": []}
#17~39까지는 아두이노 포트 자동탐지 코드이며 아두이노 사용하지 않을 시에는 주석 처리해줘야함
try:
    ports = prtlst.comports()
    for port in ports:
        if True:
            res_port = str(port).split(sep=' ')
        if 'USB' in port[1]:
            if str(port[0]) not in initial_serial_devices:
                initial_serial_devices.add(str(port[0]))

except Exception as e:
    print("Error getting serial ports list: " + str(e))

ser = serial.Serial(
    port=res_port[0],
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1,
    xonxoff=False,
    rtscts=False,
    dsrdtr=False
)


def create_table(table=None, data=None):
    table.setHorizontalHeaderLabels(data)
    # row단위선택
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 수정불가
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 균일 간격 재배치
    # table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    return table


def create_table_vertical(table=None, data=None):
    table.setVerticalHeaderLabels(data)
    table.setHorizontalHeaderLabels([''])
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 헤더 중앙정렬
    table.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
    return table

class Monitor_form():

    def __init__(self):
        super().__init__()
        self.timeout = 0
        sd = SAHDao()
        self.ui = uic.loadUi("Monitoring_GUI/Monitor.ui")
        self.Data_Frame_table = create_table(table=self.ui.Data_Frame,
                                             data=[''])
        self.Data_Frame2_table = create_table_vertical(table=self.ui.Data_Frame2,
                                                       data=[''])
        res = sd.select_item_join()
        self.load_data(res)
        DF = self.ui.Data_Frame
        for i in range(DF.rowCount()):
            if DF.item(i,1).text() == '':
                for j in range(DF.columnCount()):
                    DF.item(i,j).setBackground(Qt.yellow)
            elif DF.item(i,1).text() == '':
                for j in range(DF.columnCount()):
                    DF.item(i,j).setBackground(QtGui.QColor(0,255,120))

        self.ui.Data_Frame.clicked.connect(self.more_info)
        self.ui.start_btn.clicked.connect(self.start)
        self.ui.stop_btn.clicked.connect(self.stop)
        self.ui.reset_btn.clicked.connect(self.reset)
        #self.ui.restart_btn.clicked.connect(self.ok)
        self.ui.show()

    #
    # def ok(self):
    #     ser.write(b'H\n')

    def reset(self):
        sd = SAHDao()
        res = sd.select_item_join()
        DF = self.ui.Data_Frame
        self.ui.Data_Frame2.clearContents()
        row_res = self.ui.Data_Frame.rowCount()
        [self.ui.Data_Frame.removeRow(i) for i in reversed(range(row_res))]
        self.load_data(res)
        for i in range(DF.rowCount()):
            if DF.item(i, 1).text() == '':
                for j in range(DF.columnCount()):
                    DF.item(i, j).setBackground(Qt.yellow)
            elif DF.item(i, 1).text() == '':
                for j in range(DF.columnCount()):
                    DF.item(i, j).setBackground(QtGui.QColor(0, 255, 120))

    def more_info(self):
        FirstF = self.ui.Data_Frame
        TwoF = self.ui.Data_Frame2
        for cnt in range(len(FirstF.selectedItems())):
            row = FirstF.selectedIndexes()[0]
            row_text = FirstF.item(row.row(), cnt).text()
            item_test = QTableWidgetItem()
            item_test.setTextAlignment(Qt.AlignCenter)
            item_test.setData(Qt.DisplayRole, row_text)
            TwoF.setItem(0, cnt, item_test)


    def load_data(self, data=None):
        create = Create_Item()
        try:
            for idx, (ProductCode, ProductSeparator, ProductName, ProductionDate, ProductStock) in enumerate(data):
                item_ProductCode, item_ProductSeparator, item_ProductName, item_ProductionDate, item_ProductStock = create.create_item_join(
                    ProductCode, ProductSeparator, ProductName, ProductionDate, ProductStock)
                nextIdx = self.ui.Data_Frame.rowCount()
                self.ui.Data_Frame.insertRow(nextIdx)
                self.ui.Data_Frame.setItem(nextIdx, 0, item_ProductCode)
                self.ui.Data_Frame.setItem(nextIdx, 1, item_ProductSeparator)
                self.ui.Data_Frame.setItem(nextIdx, 2, item_ProductName)
                self.ui.Data_Frame.setItem(nextIdx, 3, item_ProductionDate)
                self.ui.Data_Frame.setItem(nextIdx, 4, item_ProductStock)
        except ValueError:
            pass

    def run(self):
        global running
        cap = cv2.VideoCapture(0)
        while running:
            ret, img = cap.read()
            if ret:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h,w,c = img.shape
                qImg = QtGui.QImage(img.data, w,h,w*c, QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qImg)
                self.ui.Main_Frame.setPixmap(pixmap)
                self.ui.Main_Frame.setScaledContents(True)
            else:
                break

        cap.release()
        print("Thread end.")

    def stop(self):
        global running
        running = False
        print("stoped..")
        for i in range(10):
            ser.write(b'X\n')

    def start(self):
        global running
        running = True
        ser.write(b'H\n')
        th = threading.Thread(target=self.run)
        th.start()
        print("started..")

    def onExit(self):
        print("exit")
        self.stop()

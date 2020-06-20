from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

class Create_Item():
    def __init__(self):
        pass

    def create_item(self, ProductCode, ProductName, ProductLength, ProductThickness, ProductSeparator, ProductStock,
                    MaterialCode):
        item_ProductCode = QTableWidgetItem()
        item_ProductCode.setTextAlignment(Qt.AlignCenter)
        item_ProductCode.setData(Qt.DisplayRole, ProductCode)
        item_ProductName = QTableWidgetItem()
        item_ProductName.setTextAlignment(Qt.AlignCenter)
        item_ProductName.setData(Qt.DisplayRole, ProductName)
        item_ProductLength = QTableWidgetItem()
        item_ProductLength.setTextAlignment(Qt.AlignCenter)
        item_ProductLength.setData(Qt.DisplayRole, ProductLength)
        item_ProductThickness = QTableWidgetItem()
        item_ProductThickness.setTextAlignment(Qt.AlignCenter)
        item_ProductThickness.setData(Qt.DisplayRole, ProductThickness)
        item_ProductSeparator = QTableWidgetItem()
        item_ProductSeparator.setTextAlignment(Qt.AlignCenter)
        item_ProductSeparator.setData(Qt.DisplayRole, ProductSeparator)
        item_ProductStock = QTableWidgetItem()
        item_ProductStock.setTextAlignment(Qt.AlignCenter)
        item_ProductStock.setData(Qt.DisplayRole, ProductStock)
        item_MaterialCode = QTableWidgetItem()
        item_MaterialCode.setTextAlignment(Qt.AlignCenter)
        item_MaterialCode.setData(Qt.DisplayRole, MaterialCode)

        return item_ProductCode, item_ProductName, item_ProductLength, item_ProductThickness, item_ProductSeparator, item_ProductStock, item_MaterialCode

    def create_item_join(self, ProductCode, ProductSeparator, ProductName, ProductionDate, ProductStock):
        item_ProductCode = QTableWidgetItem()
        item_ProductCode.setTextAlignment(Qt.AlignCenter)
        item_ProductCode.setData(Qt.DisplayRole, ProductCode)
        item_ProductSeparator = QTableWidgetItem()
        item_ProductSeparator.setTextAlignment(Qt.AlignCenter)
        item_ProductSeparator.setData(Qt.DisplayRole, ProductSeparator)
        item_ProductName = QTableWidgetItem()
        item_ProductName.setTextAlignment(Qt.AlignCenter)
        item_ProductName.setData(Qt.DisplayRole, ProductName)
        item_ProductionDate = QTableWidgetItem()
        item_ProductionDate.setTextAlignment(Qt.AlignCenter)
        item_ProductionDate.setData(Qt.DisplayRole, ProductionDate)
        item_ProductStock = QTableWidgetItem()
        item_ProductStock.setTextAlignment(Qt.AlignCenter)
        item_ProductStock.setData(Qt.DisplayRole, ProductStock)


        return item_ProductCode, item_ProductSeparator, item_ProductName, item_ProductionDate, item_ProductStock

    def create_item2(self, ProductQuantityPerMaterial, UpdateUser, UpdateTime, UpdateProgram, CreateUser, CreateTime,
                     CreateProgram):
        item_ProductQuantityPerMaterial = QTableWidgetItem()
        item_ProductQuantityPerMaterial.setTextAlignment(Qt.AlignCenter)
        item_ProductQuantityPerMaterial.setData(Qt.DisplayRole, ProductQuantityPerMaterial)
        item_UpdateUser = QTableWidgetItem()
        item_UpdateUser.setTextAlignment(Qt.AlignCenter)
        item_UpdateUser.setData(Qt.DisplayRole, UpdateUser)
        item_UpdateTime = QTableWidgetItem()
        item_UpdateTime.setTextAlignment(Qt.AlignCenter)
        item_UpdateTime.setData(Qt.DisplayRole, UpdateTime)
        item_UpdateProgram = QTableWidgetItem()
        item_UpdateProgram.setTextAlignment(Qt.AlignCenter)
        item_UpdateProgram.setData(Qt.DisplayRole, UpdateProgram)
        item_CreateUser = QTableWidgetItem()
        item_CreateUser.setTextAlignment(Qt.AlignCenter)
        item_CreateUser.setData(Qt.DisplayRole, CreateUser)
        item_CreateTime = QTableWidgetItem()
        item_CreateTime.setTextAlignment(Qt.AlignCenter)
        item_CreateTime.setData(Qt.DisplayRole, CreateTime)
        item_CreateProgram = QTableWidgetItem()
        item_CreateProgram.setTextAlignment(Qt.AlignCenter)
        item_CreateProgram.setData(Qt.DisplayRole, CreateProgram)

        return item_ProductQuantityPerMaterial, item_UpdateUser, item_UpdateTime, item_UpdateProgram, item_CreateUser, item_CreateTime, item_CreateProgram
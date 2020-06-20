import base64
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA1
from dao.sah_dao import SAHDao

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.img_label = QLabel(self)
        self.pixmap = QPixmap()
        self.pixmap.load('Login_ui/data/bbb.jpg')
        self.img_label.setPixmap(self.pixmap)
        self.id_label = QLabel(self)
        self.id_label.setText('아이디')
        self.pw_label = QLabel(self)
        self.pw_label.setText("비밀번호")
        self.id_name = QtWidgets.QLineEdit(self)
        self.pw = QtWidgets.QLineEdit(self)
        self.pw.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)

        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        self.setWindowTitle('로그인')
        self.setWindowIcon(QIcon('Login_ui/data/testicon.png'))
        layout.addWidget(self.img_label)
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_name)
        layout.addWidget(self.pw_label)
        layout.addWidget(self.pw)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        sd = SAHDao()
        res = sd.select_item2()
        res2 = sd.select_item_pw()
        res_salt = sd.select_item_salt()
        tmp_dict = {}
        salt_list = []

        for i in range(len(res)):
            dict1 = {res[i][0]: res2[i][0]}
            tmp_dict.update(dict1)
            salt_list.append(res_salt[i][0])

        dict_list_id = list(tmp_dict.keys())
        dict_list_pw = list(tmp_dict.values())
        print(dict_list_pw)

        for i in range(len(dict_list_id)):
            dict_list_id[i] = dict_list_id[i].strip()

        salt_index = dict_list_id.index(self.id_name.text())
        salt_res_2= salt_list[salt_index]

        if self.id_name.text() in dict_list_id:
            password = self.pw.text()
            salt = base64.urlsafe_b64decode(salt_res_2)
            pb = PBKDF2(password, salt, 128, 10000, hmac_hash_module=SHA1)
            key = base64.b64encode(pb).decode('utf-8')
            if key in dict_list_pw:
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(self, '비밀번호 오류', '비밀번호가 틀렸습니다.')
        else:
            QtWidgets.QMessageBox.warning(self, '아이디오류', '아이디가 틀렸습니다.')


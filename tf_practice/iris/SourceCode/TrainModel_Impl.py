import os
import re
import numpy as np
import logging
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from PyQt5.QtWidgets import QMessageBox
from xuexiaolei.python.tf_practice.iris.SourceCode.config.config import ConfigPath
from xuexiaolei.python.tf_practice.iris.SourceCode.pub_func import QT_public_func
from xuexiaolei.python.tf_practice.iris.SourceCode.TrainModel_ui import TrainModel_ui
logging.basicConfig(filename=os.path.join(ConfigPath.LogPath.value, __name__ + '.log'),
                    format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
                    level=logging.DEBUG, filemode='a')


class TrainModel_Impl(TrainModel_ui):
    def __init__(self):
        super(TrainModel_Impl, self).__init__()
        ml_func = ['KNeighbor']  # type of algorithms
        self.setupUi()  # initial user interface
        self.comboBox_model_type.addItems(ml_func)  # put algorithms to the combox to select
        self.toolButton_choosedata.clicked.connect(self.choose_data)  # choose train data's file path
        self.pushButton_predict.clicked.connect(self.train_model)  # predict and receive a model
        self.pushButton_save_model.clicked.connect(self.save_model)  # save model local
        self.data, self.model = None, None
        self.show()

    def choose_data(self):
        file_path = QT_public_func.choose_one_file(self)
        self.lineEdit_data.setText(file_path)

    def train_model(self):
        data_path = self.lineEdit_data.text()
        if data_path:
            try:
                self.data = np.array([re.split(',|\s+', _.strip()) for _ in open(data_path, 'r').readlines()], dtype=np.float)
                np.random.shuffle(self.data)
                iris_X, iris_Y = self.data[:, :-1], self.data[:, -1]
                test_size = 10
                X_train = iris_X[:-test_size, :]
                # X_test = iris_X[-test_size:, :]
                y_train = iris_Y[:-test_size]
                # y_test = iris_Y[-test_size:]
                if self.comboBox_model_type.currentText() == 'KNeighbor':
                    self.model = KNeighborsClassifier()
                    self.model.fit(X_train, y_train)
                QMessageBox.information(self, "Information", "Predict success", QMessageBox.Close)
            except Exception as e:
                QMessageBox.warning(self, "Warning", "Train fail", QMessageBox.Close)
                logging.debug(repr(e))
        else:
            QMessageBox.warning(self, "Warning", "Choose data file", QMessageBox.Close)

    def save_model(self):
        save_path = QT_public_func.save_one_file(self)
        if save_path:
            if self.model:
                joblib.dump(self.model, save_path)
                QMessageBox.information(self, "Information", "Saved success", QMessageBox.Close)
            else:
                QMessageBox.warning(self, "Warning", "Train model in advance", QMessageBox.Close)

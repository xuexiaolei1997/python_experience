import os
import re
import numpy as np
import sip
import logging
from PIL import Image
from PyQt5.QtWidgets import QMessageBox
from sklearn.externals import joblib
from xuexiaolei.python.tf_practice.iris.SourceCode.pub_func.Figure_Canvas import Figure_Canvas
from xuexiaolei.python.tf_practice.iris.SourceCode.config.config import IrisType
from xuexiaolei.python.tf_practice.iris.SourceCode.config.config import ConfigPath
from xuexiaolei.python.tf_practice.iris.SourceCode.pub_func import QT_public_func
from xuexiaolei.python.tf_practice.iris.SourceCode.ML_ui import ML_ui
from xuexiaolei.python.tf_practice.iris.SourceCode.TrainModel_Impl import TrainModel_Impl
logging.basicConfig(filename=os.path.join(ConfigPath.LogPath.value, __name__ + '.log'),
                    format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
                    level=logging.DEBUG, filemode='a')


class ML_Impl(ML_ui):
    def __init__(self):
        super(ML_Impl, self).__init__()
        figure_types = ['Image', 'Scatter', 'ROC']
        self.setupUi()
        self.actionTrain.triggered.connect(self.train_model)
        self.actionLoad.triggered.connect(self.load_model)
        self.lineEdit_model_state.setStyleSheet('color: red')
        self.pushButton_predict.clicked.connect(self.predict)
        self.data, self.model = None, None
        self.comboBox_figure.addItems(figure_types)
        self.comboBox_figure.currentTextChanged.connect(self.draw_graph)
        self.welcome()

    def welcome(self):
        cur_fig = self.verticalLayout_figure.itemAt(0)
        if cur_fig is not None:
            self.verticalLayout_figure.removeItem(cur_fig)
            sip.delete(cur_fig)
        fc = Figure_Canvas(width=4, height=4)
        ax = fc.ax
        ax.imshow(Image.open(ConfigPath.WelcomePath.value), 'gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.plot()
        self.verticalLayout_figure.addWidget(fc, 0)

    def predict(self):
        x = self.lineEdit_feature.text()
        try:
            features = np.array(re.split(',|\s+', x.strip()), dtype=np.float).reshape(1, -1)
        except Exception as e:
            QMessageBox.warning(self, 'Warning', 'Enter right datatype', QMessageBox.Close)
            return
        if self.model:
            target = self.model.predict(features)
            target = np.array(target, dtype=np.int).flatten().tolist()
            target = [str(_) for _ in target]

            target = ['%s:%s' % (_, IrisType.IrisType.value[_]) for _ in target]
            self.lineEdit_target.setText(' '.join(target))
            self.draw_graph()
        else:
            QMessageBox.warning(self, 'Warning', 'Please load model', QMessageBox.Close)

    def draw_graph(self):
        figure_type = self.comboBox_figure.currentText()
        if self.model and figure_type:
            cur_fig = self.verticalLayout_figure.itemAt(0)
            if cur_fig is not None:
                self.verticalLayout_figure.removeItem(cur_fig)
                sip.delete(cur_fig)

            fc = Figure_Canvas(width=4, height=4)
            ax = fc.ax
            if figure_type == 'Image':
                iris_num = re.split(':', self.lineEdit_target.text())[0]
                if iris_num:
                    ax.imshow(Image.open(os.path.join(ConfigPath.ImagesPath.value,
                                                      IrisType.IrisType.value[iris_num] + '.jpg')))
                else:
                    ax.imshow(Image.open(ConfigPath.WelcomePath.value))
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['bottom'].set_visible(False)
                ax.spines['left'].set_visible(False)
            if figure_type == 'Scatter':
                features = self.lineEdit_feature.text()
                if features:
                    features = re.split('\s+|,', features)
                    x, y = [], []
                    for i, feature in enumerate(features):
                        x.append(i+1)
                        y.append(float(feature))
                    ax.scatter(x, y, c=np.random.randn(len(x)))
                else:
                    QMessageBox.warning(self, 'Warning', 'Enter features', QMessageBox.Close)
            elif figure_type == 'ROC':
                x = np.linspace(-np.pi * 7, np.pi * 7, 300)
                ax.plot(x, np.sin(x) + (1 / 3) * np.sin(3 * x) + (1 / 5) * np.sin(5 * x) + (1 / 7) * np.sin(7 * x) + (
                        1 / 9) * np.sin(9 * x) + (1 / 11) * np.sin(11 * x))
                ax.set_title('FFT By myself')
            ax.plot()
            self.verticalLayout_figure.addWidget(fc, 0)

    def load_model(self):
        file_path = QT_public_func.choose_one_file(self)
        if file_path:
            try:
                self.model = joblib.load(file_path)
                QMessageBox.information(self, 'Information', 'Load success', QMessageBox.Close)
                self.lineEdit_model_state.setText('OK')
                self.lineEdit_model_state.setStyleSheet('color: green')
                self.draw_graph()
            except Exception as e:
                QMessageBox.warning(self, 'Warning', 'Load fail', QMessageBox.Close)

    def train_model(self):
        train = TrainModel_Impl()
        train.show()
        train.exec_()
        self.data, self.model = train.data, train.model
        if self.model:
            self.lineEdit_model_state.setText('OK')
            self.lineEdit_model_state.setStyleSheet('color: green')
            self.draw_graph()
        else:
            self.lineEdit_model_state.setText('Wait for loading')
            self.lineEdit_model_state.setStyleSheet('color: red')
            self.draw_graph()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are u sure to quit?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

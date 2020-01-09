"""
Get cracking
"""
import sys
from PyQt5.QtWidgets import QApplication
from xuexiaolei.python.tf_practice.iris.SourceCode.ML_impl import ML_Impl

if __name__ == '__main__':
    app = QApplication(sys.argv)
    knn = ML_Impl()
    knn.show()
    sys.exit(app.exec_())

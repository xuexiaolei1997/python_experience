"""
The common functions about PyQt5.
"""
from PyQt5.QtWidgets import QMdiSubWindow, QFileDialog


def choose_directory(self, txt="Choose Folder"):
    target_catalog = QFileDialog.getExistingDirectory(self, txt, "./")
    return target_catalog


def choose_one_file(self, txt="Choose File"):
    """
    choose one file
    :param self: the class
    :param txt: show text at the top of dialog pop up
    :return: the file path you choose
    """
    choosefilename, choosefiletype = \
        QFileDialog.getOpenFileName(self, txt, "./", "All Files (*);;Text Files (*.txt)")
    return choosefilename


def choose_many_file(self, txt="Choose Files"):
    """
    choose many file
    :param self: the class
    :param txt: the text to show
    :return: the file path you choose, type: list
    """
    choosefilename, choosefiletype = \
        QFileDialog.getOpenFileNames(self, txt, "./", "All Files (*);;Text Files (*.txt)")
    return choosefilename


def save_one_file(self, txt='Save File'):
    savefile_name, ok = QFileDialog.getSaveFileName(self, txt)
    return savefile_name


def create_new_window(cls, show_panel, title):
    """
    Add a sub-mdi window at the mainwindow you point
    :param cls: class name
    :param show_panel: the widget you point, generally it's a mainwindow
    :param title: subwindow title
    :return: None
    """
    widget = show_panel
    sub = QMdiSubWindow()
    sub.setWidget(widget)
    sub.setWindowTitle(title)
    cls.mdiArea.addSubWindow(sub)
    sub.show()
    widget.show()


def show_dialog(dialog):
    """
    Show the dialog you point
    :param dialog: sub widget
    :return: None
    """
    dialog.show()
    dialog.exec_()


def set_widget_at_docwidget(dock_widget, widget):
    """
    Add a sub widget at th dock widget
    :param dock_widget: dock widget
    :param widget: sub widget
    :return: None
    """
    if widget != '' or dock_widget != '':
        dock_widget.show()
        dock_widget.clearMask()
        dock_widget.setWidget(widget)

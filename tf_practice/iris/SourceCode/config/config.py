import os
from enum import Enum, unique


@unique
class ConfigPath(Enum):
    WelcomePath = os.path.join('Resource', 'images', 'welcome.jpg')
    ImagesPath = os.path.join('Resource', 'images')
    WindowsIcon = os.path.join('Resource', 'images', 'icons8-linux-64.png')
    LogPath = os.path.join('Resource', 'log')


@unique
class IrisType(Enum):
    IrisType = {'0': 'Setosa', '1': 'Versicolour', '2': 'Virginica'}
    # Setosa, Versicolour, Virginica = 0, 1, 2

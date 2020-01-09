#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
给图片加图片水印
'''
import matplotlib.pyplot as plt
from skimage.transform import resize
import numpy as np
import glob
import os


def ImgWatermark(img_src, dest, wm_src, loc, scale=7, alpha=0.5):
  '''
  img_src: origin image's path
  dest: the target image's path
  wm_src: the watermark image's path
  loc: watermark's location
  scale: I don't know! ??? Maybe is the narrow done ???
  alpha: transparency -- 透明度
  '''
  fig = plt.figure()
  watermark = plt.imread(wm_src)  # 读取水印
  # 调整水印大小
  new_size = [int(watermark.shape[0]/scale), int(watermark.shape[1]/scale), watermark.shape[2]]
  watermark = resize(watermark, new_size, mode='constant')
  watermark[:, :, -1] *= alpha  # 调整水印透明度

  plt.imshow(plt.imread(img_src))  # 读取图像
  plt.figimage(watermark, loc[0], loc[1], zorder=10)  # 添加水印
  plt.axis('off')
  plt.savefig(dest, dpi=fig.dpi, bbox_inches='tight')
  return fig


# 源图片存放位置与输出位置
input_dir, output_dir = 'ori_img', 'img_img'
watermark_img = os.path.join(input_dir, 'watermark.png')  # 水印图片
for img in glob.glob(os.path.join(input_dir, '*.jpg')):
  print(img)
  img_name = os.path.basename(img)
  dest = os.path.join(output_dir, 'wm_%s' % img_name)
  ImgWatermark(img_src=img, dest=dest, wm_src=watermark_img, loc=[60, 250])

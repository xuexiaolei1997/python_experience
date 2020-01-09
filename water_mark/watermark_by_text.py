'''
给图片加文字水印
'''
from matplotlib import pyplot as plt
import glob
import os


def TextWatermark(img_src, dest, text, loc, fontsize=20, alpha=0.5):
  fig = plt.figure()
  plt.imshow(plt.imread(img_src))  # 读取图像
  # 添加文字水印
  plt.text(loc[0], loc[1], text, fontsize=fontsize, alpha=alpha, color='gray')
  plt.axis('off')  # 隐藏坐标轴
  plt.savefig(dest, dpi=fig.dpi, bbox_inches='tight')  # 保存图像
  return fig


# 源图片存放位置与输出位置
input_dir, output_dir = 'ori_img', 'text_img'
# 自己输入水印，不可输入中文
text = input('Please input mark\'s text:')
for img in glob.glob(os.path.join(input_dir, '*.jpg')):
  img_name = os.path.basename(img)
  dest = os.path.join(output_dir, 'wm_%s' % img_name)
  TextWatermark(img_src=img, dest=dest, text=text, loc=[30,50])

import os
import time
from PIL import Image


# 批量修改图片尺寸，输入原图目录和修改后存放目录地址即可
def resize_batch(path, save_path, rate=1.0):
    files = os.listdir(path)  # 返回path目录下的所有文件名

    # 遍历每一张图片并修改其尺寸
    for i in files:
        f = 0
        document = os.path.join(path, i)  # 返回path和i拼接之后的路径，即第i张图片
        print(document)
        img = Image.open(document)  # 读取第i张图片
        img_resize = img.resize((int(1080 * rate), int(2400 * rate)))  # 修改为100x128尺寸
        # fileName = str(i)[:-4]  # 原图除后缀外的名字，这里原图后缀是.jpg
        save_path = save_path + "/" + '%s.jpg' % (i.split(".")[0])
        img_resize.save(save_path)
        assert 0
# save 暂时只能保存至当前文件夹

if __name__ == '__main__':
    pass
    path = r"E:/Desktop/test1"
    save_path = r"E:/Desktop/test1/rec"
    resize_batch(path, save_path, rate=0.4)

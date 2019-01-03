# coding:utf-8
import zlib
import os
import bz2
import shutil


#  使用zlib压缩文件
def file_compress():
    file = open('./bbe.txt', 'rb')
    if os.path.exists('./yasuo.zip'):
        os.remove('./yasuo.txt')
    file_compressed = open('./yasuo.txt', 'wb')
    compressobj = zlib.compressobj(level=9)
    data = file.read(1024)
    while data:
        file_compressed.write(compressobj.compress(data))
        data = file.read(1024)
    file_compressed.write(compressobj.flush())
    file.close()
    file_compressed.close()
    print('压缩前：  ', round(os.path.getsize('./bbe.txt') / (1024 ** 2), 2), 'M')
    print('压缩后：  ', round(os.path.getsize('./yasuo.txt') / (1024 ** 2), 2), 'M')


#  使用zlib解压文件
def file_decompress():
    if not os.path.exists('./yasuo.txt'):
        file_compress()
    file_compressed = open('./yasuo.txt', 'rb')
    if os.path.exists('./jieya.txt'):
        os.remove('./jieya.txt')
    file_decompress = open('./jieya.txt', 'wb')
    decompressobj = zlib.decompressobj()
    data = file_compressed.read(1024)
    while data:
        file_decompress.write(decompressobj.decompress(data))
        data = file_compressed.read(1024)
    file_decompress.write(decompressobj.flush())
    file_decompress.close()
    file_compressed.close()
    print('解压前：  ', round(os.path.getsize('./yasuo.txt') / (1024 ** 2), 2), 'M')
    print('解压后：  ', round(os.path.getsize('./jieya.txt') / (1024 ** 2), 2), 'M')


#  压缩
def bz2_compress():
    with open('bbe.txt', 'rb') as r, bz2.open('bbe.bz2', 'wb') as w:
        shutil.copyfileobj(r, w)
        r.close()
        w.close()
        print(os.path.getsize('bbe.bz2'))


#  解压
def bz2_decompress():
    with open('bbe.bz2', 'rb') as r, bz2.open('bbe.txt', 'wb') as w:
        shutil.copyfileobj(r, w)
        r.close()
        w.close()
        print(os.path.getsize('bbe.txt'))


if __name__ == '__main__':
    # file_compress()
    # file_decompress()
    # bz2_compress()
    bz2_decompress()

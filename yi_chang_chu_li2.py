#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("C:/tmp/testfile.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print "Error: 没有找到文件或读取文件失败"

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   wangluo163 = 0
   wangluo162 = 0
   wangluo161 = 0
   nan = 0
   nv = 0
 
   def __init__(self, name, stu_no, stu_class, male):
      self.name = name
      self.stu_no = stu_no
      self.stu_class = stu_class
      self.male = male
      if stu_class == '163': Student.wangluo163 += 1
      elif stu_class == '162': Student.wangluo162 += 1
      elif stu_class == '161': Student.wangluo161 += 1
      else : pass
      if male == '0': Student.nan += 1
      elif male == '1': Student.nv += 1
   def displayCountByClass(self):
     print "Total wangluo163 %d" % Student.wangluo163
     print "Total wangluo162 %d" % Student.wangluo162
     print "Total wangluo161 %d" % Student.wangluo161
   def displayStu(self):
      print "Name : ", self.name,  ", stu_no: ", self.stu_no, ",stu_class:",self.stu_class, ",male:",self.male
      
   def displayxb(self):
      print "Total nan %d" % Student.nan
      print "Total nv %d" % Student.nv
      

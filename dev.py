#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author tom
class DEVConfig(object):
    DEBUG=True
    SECRET_KEY='wocao' #session秘钥
    # 数据库配置
    # '数据库类型://账号:密码@数据库IP:端口/数据库名'
    SQLALCHEMY_DATABASE_URI = 'mysql://lpw:comp9323@rm-bp178e2k124vtax5nho.mysql.rds.aliyuncs.com:3306/myproject'
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True
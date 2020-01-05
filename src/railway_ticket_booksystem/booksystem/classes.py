# -*- coding: UTF-8 -*-  
# income List 的 数据类型
class IncomeMetric:
    metric = '00'  # 时间段度量标准
    railway_sum = 0
    income = 0

    def __init__(self, metric, railway_sum, income):
        self.metric = metric
        self.railway_sum = railway_sum
        self.income = income


# 订单信息
class Order:
    passenger_name = ''
    railway_name = ''
    railway_route = ''
    railway_ltime = ''
    railway_price = ''

    def __init__(self, pname, fname, froute, fltime, fprice):
        self.passenger_name = pname
        self.railway_name = fname
        self.railway_route = froute
        self.railway_ltime = fltime
        self.railway_price = fprice

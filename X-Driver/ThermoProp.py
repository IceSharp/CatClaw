#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-14 23:49:03
# @Author  : Robin (rainville@163.com)
# @Link    : https://www.busuanzi.net
# @Version : 0.2

import hprose
import json
from iapws import IAPWS97

sc = 4.41202148223476     # Critic entropy
# Pmin = _PSat_T(273.15)   # Minimum pressure
Pmin = 0.000611212677444
# Ps_623 = _PSat_T(623.15)  # P Saturation at 623.15 K, boundary region 1-3
Ps_623 = 16.5291642526

Region = {0: '未知', 1: '液态', 2: '汽态'}
Unit = {
    "T": "T, K",
    "P": "P, MPa",
    "v": "v, m³/kg",
    "h": "h, kJ/kg",
    "s": "s, kJ/kgK"}

def pt_h(p, t, x):
    """焓值

    已知蒸汽压力、温度、干度求解焓值。

    Arguments:
        p {[type]} -- 压力 MPa.a
        t {[type]} -- 温度 DegC
        x {[type]} -- 干度 %

    Returns:
        [type] -- [description]
    """
    t = t + 273.15  # 转换为绝对温度
    result = [0, 0]
    # result[0] = Region.get(Region_TP(t, p))  # 水的状态
    result[0] = "%0.3f" % (t - (IAPWS97(P=p, x=x).T))  # 过热度
    result[1] = "%0.3f" % (IAPWS97(P=p, T=t).h)  # 焓值
    return json.dumps(result, ensure_ascii=False)

def main():
    server = hprose.HttpServer(port=8181)
    server.addFunction(pt_h)
    server.start()

if __name__ == '__main__':
    main()

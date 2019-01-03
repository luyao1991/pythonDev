# coding:utf-8

mileage= {'西直门':0,'大钟寺': 2839, '知春路': 1206, '五道口': 1829, '上地': 4866, '西二旗': 2538, '龙泽': 3623, '回龙观': 1423, '霍营': 2110,
          '立水桥': 4785, '北苑': 2272, '望京西': 6720, '芍药居': 2152, '光熙门': 1110, '柳芳': 1135, '东直门': 1769}
# k=mileage.keys()
# print(list(k))
print(sum(list(mileage.values())))


def mile(start,final):
    s=0
    station=list(mileage.keys())
    start_index = station.index(start)
    print('起点索引{0}'.format(start_index))
    final_index = station.index(final)
    print('终点索引{0}'.format(final_index))
    if start_index<final_index:
        station=station[start_index:final_index+1]
        for i in station:
            print(mileage[i])
            s+=mileage[i]/1000
    else:
        station = station[final_index:start_index + 1]
        station=station[::-1]
        print(station)
        for i in station[final_index:start_index + 1]:
            print(mileage[i])
            s+=mileage[i]/1000
    print('乘车里程为{0}'.format(s))
    if s>32:
            k= (s-32)/20
            if k-int(k)>0:
                fee=6+int(k)+1
            else:
                fee=6+int(k)
            print('乘车费用是{0}元'.format(fee))
    elif 22<s<=32:
        print('乘车费用是6元')
    elif 12<s<=22:
        print('乘车费用是5元')
    elif 6<s<=12:
        print('乘车费用是4元')
    else:
        print('乘车费用是3元')


mile('西直门','东直门')

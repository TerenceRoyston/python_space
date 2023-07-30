import csv
import re

class DingTalkRecord:
    transactionNumber = ''
    commodityOrServiceName = ''
    amountOfMoney = ''
    paymentMethod=''
    paymentTime = ''
    ticketArchiveFile=''
    remarks = ''
    counterparty = ''

class AlipayRecord:
    transactionNumber = ''
    merchantOrderNumber = ''
    transactionCreationTime = ''
    paymentTime = ''
    lastModifiedTime = ''
    sourceOfTransaction = ''
    type = ''
    counterparty = ''
    commodityOrServiceName = ''
    amountOfMoney = ''
    revenueOrExpenditure = ''
    transactionStatus = ''
    serviceCharge = ''
    successfullyRefunded = ''
    remarks = ''
    fundingStatus = ''

    def __str__(self):
        return obj_to_string(AlipayRecord, self)


class WechatRecord:
    transactionCreationTime = ''
    type = ''
    counterparty = ''
    commodityOrServiceName = ''
    revenueOrExpenditure = ''
    amountOfMoney = ''
    paymentMethod = ''
    transactionStatus = ''
    transactionNumber = ''
    merchantOrderNumber = ''
    remarks = ''

    def __str__(self):
        return obj_to_string(WechatRecord, self)


def obj_to_string(cls, obj):
    """
    简单地实现类似对象打印的方法
    :param cls: 对应的类(如果是继承的类也没有关系，比如A(object), cls参数传object一样适用，如果你不想这样，可以修改第一个if)
    :param obj: 对应类的实例
    :return: 实例对象的to_string
    """
    if not isinstance(obj, cls):
        raise TypeError("obj_to_string func: 'the object is not an instance of the specify class.'")
    to_string = str(cls.__name__) + "("
    items = obj.__dict__
    n = 0
    for k in items:
        if k.startswith("_"):
            continue
        to_string = to_string + str(k) + "=" + str(items[k]) + ","
        n += 1
    if n == 0:
        to_string += str(cls.__name__).lower() + ": 'Instantiated objects have no property values'"
    return to_string.rstrip(",") + ")"


def alipayRecordHandle(): 
    with open('alipay_record.csv', 'r', newline='', encoding='gb2312', errors='ignore') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        startLineNum = 5
        endLineNum = -7
        csvList = []
        for row in csvreader:
            row = ','.join(row)
            row = re.sub('\s', '', row)
            csvList.append(row)
        alipayRecordList = []
        csvList = csvList[startLineNum:endLineNum]
        for item in csvList:
            alipayRecord = AlipayRecord()
            itemSplitList = item.split(',')
            alipayRecord.lastModifiedTime = itemSplitList[4]
            alipayRecord.counterparty = itemSplitList[7]
            alipayRecord.commodityOrServiceName = itemSplitList[8]
            alipayRecord.amountOfMoney = itemSplitList[9]
            alipayRecordList.append(alipayRecord)
        for i in alipayRecordList:
            print(i.__dict__)


def wechatpayRecordHandle():
    with open('wechat_record.csv', 'r', newline='', encoding='utf8', errors='ignore') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        startLineNum = 17
        endLineNum = None
        csvList = []
        for row in csvreader:
            row = ','.join(row)
            row = re.sub('\s', '', row)
            csvList.append(row)
        wechatpayRecordList = []
        csvList = csvList[startLineNum:endLineNum]
        for item in csvList:
            wechatpayRecord = WechatRecord()
            itemSplitList = item.split(',')
            wechatpayRecord.transactionCreationTime = itemSplitList[0]
            wechatpayRecord.counterparty = itemSplitList[2]
            wechatpayRecord.commodityOrServiceName = itemSplitList[3]
            wechatpayRecord.amountOfMoney = itemSplitList[5]
            wechatpayRecordList.append(wechatpayRecord)
        for i in wechatpayRecordList:
            print(i.__dict__)


if __name__ == "__main__":
    wechatpayRecordHandle()
    alipayRecordHandle()

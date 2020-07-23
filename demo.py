#import pymongo
import random
import copy


"""
1. 先写脚本自造3000条数据入库。
"""
def generateData(NUM, list_pay):
	"""
	client = pymongo.MongoClient(host='localhost', port=27017)
	db = client.test
	collection = db.pay
	"""
	necessary = ['clothing', 'food', 'living', 'walk']
	unnecessary = ['book', 'train', 'entertainment', 'social']
	pay = {
		'pay_id': '20200719',
		'pay_time': None,
		'pay_tpye': 'necessary',
		'pay_subtype': necessary[0],
		'payment': 0
	}

	for i in range(NUM):
		ix_type = random.randint(0, 1)
		ix_subtype = random.randint(0, 3)
		if ix_type:
			pay['pay_tpye'] = 'necessary'
			pay['pay_subtype'] = necessary[ix_subtype]
		else:
			pay['pay_tpye'] = 'unnecessary'
			pay['pay_subtype'] = unnecessary[ix_subtype]
		pay['pay_time'] = '2020-7-' + str(random.randint(1, 31))
		pay['payment'] = random.randint(1, 1000)
		#result = collection.insert(pay)
		cur_pay = copy.deepcopy(pay)
		list_pay.append(cur_pay)
	#data_pay = collection.find()
	return list_pay


"""
2. 找出本月单笔最高消费。
"""
def topConsume(list_pay):
	payment_list = sorted(list_pay, key=lambda e: (e.__getitem__('payment')), reverse=True)
	ret = payment_list[0]['payment']
	print('\n2. 本月单笔最高消费：', ret)
	return ret

"""
3. 找出本月单日最高消费。
"""
def topDayConsume(list_pay):
	day_payment = {}
	for i in range(len(list_pay)):
		time = list_pay[i]['pay_time']
		if time in day_payment:
			day_payment[time] += list_pay[i]['payment']
		else:
			day_payment[time] = list_pay[i]['payment']
	ret = sorted(day_payment.items(), key=lambda d: d[1], reverse=True)
	print('\n3. 本月单日最高消费:', ret[0])
	print(ret)
	return ret[0]

"""
4. 统计本月非必需品消费各子类最高消费，按消费额度高低排序。
5. 统计本月非必需品消费各子类消费笔数，按笔数高低排序。
"""
def topSubtype(list_pay):
	subtype_payment = {'book': 0, 'train': 0, 'entertainment': 0, 'social': 0}
	cnt_subtype = {'book': 0, 'train': 0, 'entertainment': 0, 'social': 0}
	for i in range(len(list_pay)):
		if list_pay[i]['pay_tpye'] == 'unnecessary':
			subtype, payment = list_pay[i]['pay_subtype'], list_pay[i]['payment']
			subtype_payment[subtype] = max(subtype_payment[subtype], payment)
			cnt_subtype[subtype] += 1
	sort_subtype_payment = sorted(subtype_payment.items(),key=lambda d: d[1], reverse=True)
	sort_cnt_subtype = sorted(cnt_subtype.items(), key=lambda d: d[1], reverse=True)
	print('\n4. 本月非必需品消费各子类最高消费，按消费额度高低排序:', sort_subtype_payment)
	print(subtype_payment)
	print('\n5. 统计本月非必需品消费各子类消费笔数，按笔数高低排序:', sort_cnt_subtype)
	print(cnt_subtype)
	return sort_subtype_payment, sort_cnt_subtype


if __name__ == '__main__':
	NUM = 3000

	list_pay = generateData(NUM, [])  #1. 先写脚本自造3000条数据入库

	topConsume(list_pay)  #2. 找出本月单笔最高消费

	topDayConsume(list_pay) #3. 找出本月单日最高消费

	topSubtype(list_pay) #4. 本月非必需品消费各子类最高消费，按消费额度高低排序, 5. 统计本月非必需品消费各子类消费笔数，按笔数高低排序

	#print('\n1. 3000条数据如下:\n', list_pay)



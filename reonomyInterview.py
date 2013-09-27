import re, numpy, datetime

def estimatePrice(address):
	address = address.lower()
	addresses = {}
	xs, ys = [], []
	for line in open('manhattan_sales_sample.csv'):
		line = line.split(",")
		a = line[0].lower()
		dt = line[3].split('-')
		d = datetime.date(int(dt[0]), int(dt[1]), int(dt[2]))
		xs.append((datetime.date.today() - d).days)
		ys.append(float(line[4].strip())/int(line[2]))
		if a in addresses:
			addresses[a].append((line[4], d))
		else:
			addresses[a] = [(line[4], d)]

	curRow = addresses[address]
	print curRow
	if curRow is None:
		print "Estimating based on Square Footage"
	elif len(curRow) == 1:
		print "Estimating on Average Slope of entire data set"
	else:
		print "Using Regression as we probably have enough data (kinda)"
		x = []
		xs = [f[0].strip() for f in addresses[address]]
		ys = [(datetime.date.today() - f[1]).days for f in addresses[address]]
		print xs
		print ys
		z = numpy.polyfit(xs, ys, 3)
		p = numpy.poly1d(z)
		print p
		price = p(0) * int(line[2])
	for ad in addresses[address]:
		print price - int(float(ad[0]))

estimatePrice('570 5 Avenue')

import sys
def convert(string):
	res=bytes()
	char_dict={
	'\x80':b'\x80',
	'\x81':b'\x81',
	'\x82':b'\x82',
	'\x83':b'\x83',
	'\x84':b'\x84',
	'\x85':b'\x85',
	'\x86':b'\x86',
	'\x87':b'\x87',
	'\x88':b'\x88',
	'\x89':b'\x89',
	'\x90':b'\x90',
	'\x91':b'\x91',
	'\x92':b'\x92',
	'\x93':b'\x93',
	'\x94':b'\x94',
	'\x95':b'\x95',
	'\x96':b'\x96',
	'\x97':b'\x97',
	'\x98':b'\x98',
	'\x99':b'\x99',
	'\x9a':b'\x9a',
	'\x9b':b'\x9b',
	'\x9c':b'\x9c',
	'\x9d':b'\x9d',
	'\x9e':b'\x9e',
	'\x9f':b'\x9f',
	'\x8a':b'\x8a',
	'\x8b':b'\x8b',
	'\x8c':b'\x8c',
	'\x8d':b'\x8d',
	'\x8e':b'\x8e',
	'\x8f':b'\x8f'
	}
	for i in string:
		if i in char_dict:
			res+=char_dict[i]
		else:
			res+=i.encode('cp1252')
	return res

def to_utf8(bytestr):
	try:
		return bytestr.decode('utf8')
	except UnicodeDecodeError as e:
		return bytestr[:e.start].decode('utf8')+to_utf8(bytestr[e.start+1:])

if len(sys.argv) == 1:
	print('用法:python3 convert.py [乱码文件] [目标文件]')
	print('如果未给定目标文件，将直接输出到标准输出')
	sys.exit()
if len(sys.argv) == 2:
	with open(sys.argv[1]) as f:
		for i in f:
			tmp=convert(i)
			print(to_utf8(tmp))

if len(sys.argv) == 3:
	result=""
	with open(sys.argv[1]) as f:
		for i in f:
			tmp=convert(i)
			result+=to_utf8(tmp)
	with open(sys.argv[2],'w') as f:
		f.write(result)
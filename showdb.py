import plyvel

db = plyvel.DB('/Users/eduardmaghakyan/Library/Application Support/Google/Chrome/Default/Local Storage/leveldb', create_if_missing=False)


for key, value in db.iterator(prefix=b'ke'):
	print(key, value)



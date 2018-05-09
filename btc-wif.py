import hashlib
import sys
import binascii

def Base58Btc(num):
	alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
	encode = ''
	base_count = len(alphabet)
	while (num >= base_count):
		tmp = num / base_count
		mod = num - base_count * tmp
		encode = alphabet[mod] + encode
		num = tmp
	if (num):
		encode = alphabet[tmp] + encode
	return encode

hex_key = sys.argv[1]
bin_key = binascii.unhexlify(hex_key)
with80 = "\x80"+bin_key

sha= hashlib.sha256()
sha.update(with80)
round1 = sha.digest()

sha= hashlib.sha256()
sha.update(round1)
extended_key = sha.digest()
checksum = extended_key[:4]

print Base58Btc(int(binascii.hexlify(with80 + checksum), 16))

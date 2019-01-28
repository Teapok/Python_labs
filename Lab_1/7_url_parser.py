# www -> http://
# *.com if *.*
def analyze(adress):
	if adress.startswith('www'):
		return 'http://' + adress
	elif not adress.endswith('.com'):
		return adress + '.com'


Url = ('www.vk.com','google.ru','https://mini.webmoney.ru','www.yandex.ru','n/a')
print([analyze(adress) for adress in Url])

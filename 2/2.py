# pip install qrcode

import requests
import qrcode

def get_data(url='https://google.com', name='default'):
	qr = qrcode.make(data=url)
	qr.save(stream=f'{name}.png')
	return f'QR code war created! open the {name}.png'


def main():
	get_data()

if __name__ == '__main__':
	main()
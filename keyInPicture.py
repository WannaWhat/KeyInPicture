import binascii
import argparse
import sys
from random import randint

try:
	from PIL import Image, ImageDraw
	from colorama import Fore, Back, Style
except:
	print("You don't have libraries\n Please try: pip install -r requirements.txt")
	
class Picture():
	def __init__(self, args):
		self.FILE_NAME = args.inPhoto
		if args.outPhoto:
			self.WORDS = str(args.secretWord)
			self.OUTPHOTO = args.outPhoto
			self.MODE = "Code"
		else:
			self.SECRETCODE = str(args.password).split(" ")
			self.MODE = "Decode"
		print(self.MODE + " image")

	def checkImg(self):
		try:
			open(self.FILE_NAME, "rb")
		except:
			print("Bad Picture can't open!!!")
			sys.exit(-2)

	def cipherCoder(self, encoding='utf-8', errors='surrogatepass'):
		text = self.WORDS
		bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
		self.binary_string = bits.zfill(8 * ((len(bits) + 7) // 8))

	def createTrack(self):
		self.track = []
		for i in self.binary_string:
			self.track.append(int(i))
		if len(self.track) > self.SIZE[0] * self.SIZE[1]:
			print("Your message to big for this picture. \nSorry")
			sys.exit(-1)

	def getImg(self):
		self.originIMG = Image.open(self.FILE_NAME)
		self.SIZE = self.originIMG.size
		self.PIX = self.originIMG.load()
		self.NEWPIX = {}
		for x in range(1, self.SIZE[0]):
			for y in range(1, self.SIZE[1]):
				self.NEWPIX[x, y] = self.PIX[x, y]

	def getTrack(self):
		self.originIMG = Image.open(self.FILE_NAME)
		self.SIZE = self.originIMG.size
		self.PIX = self.originIMG.load()
		self.NEWPIX = {}
		self.track = []
		for x in range(1, self.SIZE[0]):
			for y in range(1, self.SIZE[1]):
				for pix in range(3):
					self.track.append(self.PIX[x, y][pix] % 2)

	def drawNewPix(self):
		messChecker = 0
		start_poz = 0
		go_flag = False
		self.start_checker = randint(0, self.SIZE[0] * self.SIZE[1] - len(self.track) - 1)
		for x in range(1, self.SIZE[0]):
			for y in range(1, self.SIZE[1]):
				pix = []
				for poz in range(3):
					if start_poz == self.start_checker:
						go_flag = True
					if go_flag: 
						if messChecker < len(self.track):
							if self.NEWPIX[x, y][poz] % 2 != self.track[messChecker]:
								if self.NEWPIX[x, y][poz] == 255:
									pix.append(self.NEWPIX[x, y][poz] - 1)
								else:
									pix.append(self.NEWPIX[x, y][poz] + 1)
							else:
								pix.append(self.NEWPIX[x, y][poz])
							messChecker += 1
						else:
							pix.append(self.NEWPIX[x, y][poz])
							go_flag == False
					else:
						pix.append(self.NEWPIX[x, y][poz])
					start_poz += 1 
				self.DRAW.point((x, y), (pix[0], pix[1], pix[2]))
		print(self.OUTPHOTO)
		self.NEWIGM.save(self.OUTPHOTO + ".png")

	def newImage(self):
		self.NEWIGM = Image.new("RGB", self.SIZE)
		self.DRAW = ImageDraw.Draw(self.NEWIGM)

	def decodeTrack(self):
		code = self.track[int(self.SECRETCODE[0]):int(self.SECRETCODE[1]):]
		secret_code = "0b"
		for i in code:
			secret_code += str(i)
		n = int(secret_code, 2)
		print(str(binascii.unhexlify('%x' % n))[1::])

	def crypt(self):
		self.checkImg()
		self.getImg()
		self.cipherCoder()
		self.createTrack()
		self.newImage()
		self.drawNewPix()
		print("Secret code: ", self.start_checker, " ", str(self.start_checker + len(self.track)))

	def uncrypt(self):
		self.checkImg()
		self.getTrack()
		self.decodeTrack()

	def main(self):
		if self.MODE == "Code":
			self.crypt()

		elif self.MODE == "Decode":
			self.uncrypt()





if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Image script')
	parser.add_argument(action = "store", dest = "inPhoto", help = "Input photo")
	parser.add_argument('-o', action = "store", dest = "outPhoto", help = "Output photo") 
	parser.add_argument('-s', action = "store", dest = "secretWord", help = "Message for crypt")
	parser.add_argument('-p', action = "store", dest = "password", help = "Password for decode")
	args = parser.parse_args()
	print(Fore.GREEN + Back.WHITE +"Created by wannaWhat \n GitHub: https://github.com/WannaWhat \n Telegram: @wannaWhat \n Mail: wannaWhat@tutanota.com" + Style.RESET_ALL)
	pic = Picture(args)
	pic.main()
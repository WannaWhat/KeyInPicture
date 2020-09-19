from PIL import Image, ImageDraw
import binascii
import argparse

class Picture():
	def __init__(self, args):
		self.FILE_NAME = args.inPhoto
		if args.outPhoto:
			self.WORDS = args.secretWord
			self.OUTPHOTO = args.outPhoto
			self.MODE = "code"
		else:
			self.SECRETCODE = args.password.split(" ")
			self.MODE = "decode"

	def checkImg(self):
		try:
			open(self.FILE_NAME, "rb")
		except:
			print("Bad Picture!!!")
			sys.exit(-2)

	def cipherCoder(self, encoding='utf-8', errors='surrogatepass'):
		text = self.WORDS
		bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
		self.binary_string = bits.zfill(8 * ((len(bits) + 7) // 8))

	def createTrack(self):
		self.track = []
		for i in self.binary_string:
			self.track.append(int(i))

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
		for x in range(1, self.SIZE[0]):
			for y in range(1, self.SIZE[1]):
				pix = []
				for poz in range(3):
					if messChecker < len(self.track): 
						if self.NEWPIX[x, y][poz] % 2 != self.track[messChecker]:
							if self.NEWPIX[x, y][poz] == 255:
								pix.append(self.NEWPIX[x, y][poz] - 1)
							else:
								pix.append(self.NEWPIX[x, y][poz] + 1)
						else:
							pix.append(self.NEWPIX[x, y][poz])
					else:
						pix.append(self.NEWPIX[x, y][poz])
					messChecker += 1
				self.DRAW.point((x, y), (pix[0], pix[1], pix[2]))
		self.NEWIGM.save("exmpl.png")

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
		self.cipherCoder()
		self.createTrack()
		print("Secret code: 0, ", len(self.track))
		self.getImg()
		self.newImage()
		self.drawNewPix()

	def uncrypt(self):
		self.checkImg()
		self.getTrack()
		self.decodeTrack()

	def main(self):
		if self.MODE == "code":
			print("code")
			self.crypt()

		elif self.MODE == "decode":
			print("decode")
			self.uncrypt()




if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Image script')
	parser.add_argument(action = "store", dest = "inPhoto", help = "Input photo")
	parser.add_argument('-o', action = "store", dest = "outPhoto", help = "Output photo") 
	parser.add_argument('-s', action = "store", dest = "secretWord", help = "Message for crypt")
	parser.add_argument('-p', action = "store", dest = "password", help = "Password for decode")
	args = parser.parse_args()

	pic = Picture(args)
	pic.main()
from PIL import Image
import sys

class Picture():
	def __init__(self, args):
		if len(args) < 3:
			print("Bad argument!!!")
			sys.exit(-1)
		self.FILE_NAME = args[1]
		self.WORDS = args[2]
		self.BEGIN = "1" * 17
		self.END = "0" * 17

	def checkImg(self):
		try:
			open(self.FILE_NAME, "rb")
		except:
			print("Bad Picture!!!")
			sys.exit(-2)

	def cipherGenerator(self):

		byte_array = self.WORDS.encode()

		binary_int = int.from_bytes(byte_array, "big")
		self.binary_string = bin(binary_int)[2::]
		self.binary_string

	def createTrack(self):
		self.track = []
		for i in self.BEGIN:
			self.track.append(int(i))
		for i in self.binary_string:
			self.track.append(i)
		for i in self.END:
			self.track.append(int(i))

	def getImg(self):
		self.originIMG = Image.open(self.FILE_NAME)
		self.originIMG.show()

	def main(self):
		self.checkImg()
		self.cipherGenerator()
		self.createTrack()
		print(self.track)
		self.getImg()


if __name__ == "__main__":
	pic = Picture(sys.argv)
	pic.main()
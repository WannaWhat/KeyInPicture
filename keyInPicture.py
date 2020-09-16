from PIL import Image
import sys

class Picture():
	def __init__(self, args):
		if len(args) < 3:
			print("Bad argument!!!")
			sys.exit(-1)
		self.FILE_NAME = args[1]
		self.WORDS = args[2]

	def checkImg(self):
		try:
			open(self.FILE_NAME, "rb")
		except:
			print("Bad Picture!!!")
			sys.exit(-2)

	def cipherGenerator(self):
		byte_array = self.WORDS.encode()

		binary_int = int.from_bytes(byte_array, "big")
		binary_string = bin(binary_int)

		print(binary_string)


if __name__ == "__main__":
	pic = Picture(sys.argv)
	print(pic.cipherGenerator())
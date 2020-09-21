# KeyInPicture


## Installing:

	git clone https://github.com/wannaWhat/KeyInPicture.git
	cd KeyInPicture
	pip install -r requirements.txt
	python keyInPicture.py []

## How to use:


### Help menu:

	python keyInPicture.py --help
	
	positional arguments:
		inPhoto        Input photo

	optional arguments:
		-h, --help     show this help message and exit                                                                               
		-o OUTPHOTO    Output photo                                                                                                  
		-s SECRETWORD  Message for crypt                                                                                             
		-p PASSWORD    Password for decode

### For crypt photo:
```diff
- ORIGINAL PHOTO MUST BE IN .jpeg FORMAT
```
	python keyInPicture.py [path to original photo] -o [name of output photo] -s [message for crypt]

#### Output:

	Secret code: [your code]


### For decrypt photo:

	python keyInPicture.py [path to original photo] -p [your secret code]

#### Output:

	Youre secret message
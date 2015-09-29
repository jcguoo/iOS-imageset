import os, sys, Image, json

def make_imageset(path):
	if not os.path.isfile(path):
		print('[ios_imageset] Invalid png file path, please check your input.')
		return

	(dir, file) = os.path.split(path)
	if not file[-4:] == '.png' or file[0] == '.':
		print('[ios_imageset] Invalid png file path, please check your input.')
		return

	print('[ios_imageset] Processing ' + file)

	name = file[:-4]
	imagesetpath = name + '.imageset' if dir == '' else dir + '/' + name + '.imageset'
	if not os.path.exists(imagesetpath):
		os.mkdir(imagesetpath)

	im = Image.open(path)
	(w, h) = im.size

	im.save('%s/%s@3x.png' % (imagesetpath, name), quality = 100)

	im2 = im.resize((w*2//3, h*2//3), Image.ANTIALIAS)
	im2.save('%s/%s@2x.png' % (imagesetpath, name), quality = 100)

	contents = {
	  "images" : [
	    {
	      "idiom" : "universal",
	      "filename" : "%s@2x.png" % name,
	      "scale" : "2x"
	    },
	    {
	      "idiom" : "universal",
	      "filename" : "%s@3x.png" % name,
	      "scale" : "3x"
	    }
	  ],
	  "info" : {
	    "version" : 1,
	    "author" : "xcode"
	  }
	}

	fp = open("%s/Contents.json" % imagesetpath, "w+")
	fp.write(json.dumps(contents))
	fp.close()

def make_imagesets(dir):
	if dir[-1:] != '/':
		dir = dir + '/'
	if not os.path.isdir(dir):
		print('[ios_imageset] Invalid directory, please check your input.')
		return

	files = os.listdir(dir)
	paths = []

	for file in files:
		path = dir + file
		if os.path.isfile(path):
			if file[0] != '.' and file[-4:] == '.png':
				paths.append(path)

	print('[ios_imageset] Find %d png file(s) in directory: %s' % (len(paths), dir))
	for path in paths:
		make_imageset(path)

def help():
	print('')
	print('\t[ios_imageset] ***** Help *****')
	print('1. python imageset.py -d(or --dir) [directory]:')
	print('    make imagesets from all png files in directory')
	print('2. python imageset.py [filepath]:')
	print('    make one imageset from the specific png file at filepath')
	print('\t[ios_imageset] by jcggg')
	print('')

def main(argv):
	l = len(argv)
	if l == 2:
		if argv[1] == '--help' or argv[1] == '-h':
			help()
		else:
			make_imageset(argv[1])
	elif l == 3:
		if argv[1] == '--dir' or argv[1] == '-d':
			make_imagesets(argv[2])
	else:
		print('[ios_imageset] Argument error! Please refer to \'--help\'')

if __name__ == '__main__':
	main(sys.argv)
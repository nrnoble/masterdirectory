import pickle


#http://www.tutorialspoint.com/python/python_files_io.htm

class pixel(object):
    def __init__(self, px, py, prgb):
        self.x = px
        self.y = py
        self.rgb = prgb


file = open(".\\Content\\testData.json",mode="rb+")

testdata = [1,2,"#fffff3"]

pixels = []

testObj = pixel (1,1,"#ffFFF1")
pixels.append(testObj)

testObj = pixel (1,2,"#ffFFF2")
pixels.append(testObj)

testObj = pixel (1,3,"#ffFFF3")
pixels.append(testObj)
print (len(pixels))
#print ("pixels:" + )

pickle.dump(pixels, file)
#file.close()

file = open(".\\Content\\testData.json",mode="rb+")
readTestData = pickle.load(file)

print (len(readTestData))

for pix in readTestData:
    print (pix.x, pix.y, pix.rgb)


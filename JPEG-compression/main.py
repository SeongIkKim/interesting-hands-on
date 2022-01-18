from struct import unpack

marker_mapping = {
    0xffd8: "Start of Image",
    0xffe0: "Application Default Header",
    0xffdb: "Quantization Table",
    0xffc0: "Start of Frame",
    0xffc4: "Define Huffman Table",
    0xffda: "Start of Scan",
    0xffd9: "End of Image"
}

class JPEG:
    def __init__(self, image_file_path: str):
        with open(image_file_path, 'rb') as f:
            self.img_data = f.read()

    def decode(self):
        data = self.img_data
        while len(data):
            # >H : read data as big endian, unsigned short
            marker, _ = unpack(">H", data[0:2])
            print(marker_mapping.get(marker))
            if marker == 0xffd8: # start
                data = data[2:]
            elif marker == 0xffd9: # end
                return
            elif marker == 0xffda: # start of scan section, not length-specified
                data = data[-2:]
            else:
                lenchunk, _ = unpack(">H", data[2:4])
                data = data[2+lenchunk]



if __name__ == "__main__":
    img = JPEG("profile.jpg")
    img.decode()


from FileReaderWriter import FileReaderWriter


class TextFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        with open(filepath, 'r') as txtfile:
            data = txtfile.readlines()
            for line in data:
                print(line.strip())
            return data

    def write(self, filepath, data):
        with open(filepath, 'w') as write_file:
            write_file.write(data)

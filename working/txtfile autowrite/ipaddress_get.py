import sys
import re


class FindString:
    def __init__(self):
        print('Start Find String\n')
        self.lines = []

    def __del__(self):
        print('\nEnd Find String')

    def readfile(self, filePath):
        try:
            self.file = open(filePath, 'r')
            while True:
                line = self.file.readline()
                if not line:
                    break
                self.lines.append(line)

            self.file.close()

        except IOError:
            print('Cannot read file : ' + filePath)
            sys.exit()

    def parseFile_ipExtract(self):
        for line in self.lines:
            line = line.replace('\n', '')
            re_ips = re.findall('[0-9]+(?:\.[0-9]+){3}', line)
            for ip in re_ips:
                print(ip)

    def parseFile_urlHTTPExtract(self):
        regex = re.compile(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.IGNORECASE)

        for line in self.lines:
            m = regex.search(line)
            # if m != None:
            #     print(m.group())

        """
        for line in self.lines :
            line = line.replace('\n', '')
            re_urls = re.findall('^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$', line)
            for url in re_urls :
                print url
        """


if __name__ == "__main__":
    findString = FindString()
    findString.readfile("wrt.txt")
    findString.parseFile_ipExtract()
    findString.parseFile_urlHTTPExtract()

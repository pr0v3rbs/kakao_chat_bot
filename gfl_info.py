

class gfl_info:
    dollTimeSet = dict()

    def __init__(self):
        lines = open('./gfl/doll_time').read().split()
        tmpTime = lines[0].replace(':', '')
        tmpInfo = ''
        for line in lines[1:]:
            if line == '': continue
            if len(line) == 5 and line[2] == ':':
                self.dollTimeSet[tmpTime] = tmpInfo
                tmpTime = line.replace(':', '')
                tmpInfo = ''
            else:
                tmpInfo += line + '\n'

    def getDollTime(self, timeList):
        result = ''
        for time in timeList:
            timeKey = time.strip().replace(':', '').rjust(4, '0').encode('ascii')
            result += timeKey + '\n'
            result += self.dollTimeSet.get(time.strip().replace(':', '').rjust(4, '0'), 'no info') + '\n'
        return result

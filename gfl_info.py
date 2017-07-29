

class gfl_info:
    def __init__(self):
        self.__dollTimeMap = self.__parseTimeTable('./gfl/doll_time')
        self.__equipTimeMap = self.__parseTimeTable('./gfl/equip_time')

    def __parseTimeTable(self, filePath):
        resultMap = dict()
        lines = open(filePath).read().split()
        tmpTime = lines[0].replace(':', '')
        tmpInfo = ''
        for line in lines[1:]:
            if line == '': continue
            if len(line) == 5 and line[2] == ':':
                resultMap[tmpTime] = tmpInfo
                tmpTime = line.replace(':', '')
                tmpInfo = ''
            else:
                tmpInfo += line + '\n'

        return resultMap

    def getDollTime(self, timeList):
        return self.__makeResponse(self.__dollTimeMap, timeList).strip()

    def getEquipTime(self, timeList):
        return self.__makeResponse(self.__equipTimeMap, timeList).strip()

    def __makeResponse(self, targetMap, timeList):
        result = ''
        for time in timeList:
            timeKey = time.strip().replace(':', '').rjust(4, '0').encode('ascii')
            result += timeKey + '\n'
            result += targetMap.get(timeKey, 'no info') + '\n'

        return result

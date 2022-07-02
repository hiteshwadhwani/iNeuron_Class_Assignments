import logging as lg

lg.basicConfig(filename="string.log", level=lg.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class StringClass:
    def __init__(self, str):
        self.str = str

    def extract(self):
        try:
            ans = self.str[1:300:3]
            self.info_log("extract function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside extract function")
            self.error_log(e)

    def reverse(self):
        try:
            ans = self.str[1:300:3]
            self.info_log("extract function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside reverse function")
            self.error_log(e)
        ans = self.str[::-1]
        self.info_log("reverse function --> " + str(ans))
        return ans

    def split(self):
        try:
            ans = self.str.upper().split(" ")
            self.info_log("split function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside split function")
            self.error_log(e)

    def lower_case(self):
        try:
            ans = self.str.lower()
            self.info_log("lower_case function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside lower_case function")
            self.error_log(e)

    def capitalize(self):
        try:
            ans = self.str.capitalize()
            self.info_log("capitalize function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside capitalize function")
            self.error_log(e)

    def expand_tab(self, str1):
        try:
            ans = str1.expandtabs()
            self.info_log("expand_tab function --> " + "on string " + str(str1) + " is " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside expand_tab function")
            self.error_log(e)

    def strip(self):
        try:
            ans = self.str.strip()
            self.info_log("strip function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside strip function")
            self.error_log(e)

    def ltrip(self):
        try:
            ans = self.str.lstrip(" ")
            self.info_log("ltrip function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside ltrip function")
            self.error_log(e)

    def rstrip(self):
        try:
            aans = self.str.rstrip()
            self.info_log("rstrip function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside rstrip function")
            self.error_log(e)

    def replace(self, old, new):
        try:
            ans = self.str.replace(old, new)
            self.info_log("replace function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside replace function")
            self.error_log(e)

    def string_centre(self, width, char):
        try:
            ans = self.str.center(width, char)
            self.info_log("string_centre function --> " + str(ans))
            return ans
        except Exception as e:
            self.error_log("Error inside string_centre function")
            self.error_log(e)

    def info_log(self, e):
        lg.info(str(e))

    def error_log(self, e):
        lg.error(str(e))


stringObject = StringClass("hitesh wadhwani")
stringObject.extract()
stringObject.reverse()
stringObject.split()
stringObject.lower_case()
stringObject.capitalize()
stringObject.expand_tab("H\ti\tt\te\ts\th")
stringObject.strip()
stringObject.ltrip()
stringObject.rstrip()
stringObject.replace('h', 'H')
stringObject.string_centre(30, "#")

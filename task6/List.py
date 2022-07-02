import logging as lg

lg.basicConfig(filename="list.log", level=lg.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class ListClass:
    def __init__(self, l):
        self.l = l

    def extract_list(self):
        try:
            l1 = []
            for i in self.l:
                if type(i) == list:
                    l1.append(i)
            self.info_log("extract_list function --> " + str(l1))
            return l1
        except Exception as e:
            self.error_log(e)

    def extract_dict(self):
        try:
            l1 = []
            for i in self.l:
                if type(i) == dict:
                    l1.append(i)
            self.info_log("extract_dict function --> " + str(l1))
            return l1
        except Exception as e:
            self.error_log(e)

    def extract_tuple(self):
        try:
            l1 = []
            for i in self.l:
                if type(i) == tuple:
                    l1.append(i)
            self.info_log("extract function --> " + str(l1))
            return l1
        except Exception as e:
            self.error_log(e)

    def extract_numerical(self):
        try:
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            self.info_log("extract_numerical function --> " + str(l1))
            return l1
        except Exception as e:
            self.error_log(e)

    def summation(self):
        try:
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            self.info_log("summation function --> " + str(sum(l1)))
            return sum(l1)
        except Exception as e:
            self.error_log(e)

    def filter_odd_values(self):
        try:
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            l2 = []
            for i in l1:
                if i % 2 == 0:
                    pass
                else:
                    l2.append(i)
            self.info_log("filter_odd_values function --> " + str(l2))
            return l2
        except Exception as e:
            self.error_log(e)

    def extract_ineuron(self):
        try:
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if g == 'ineuron':
                                l1.append(g)
            self.info_log("extract_ineuron function --> " + str(l1))
            return l1
        except Exception as e:
            self.error_log(e)

    def number_of_occurences(self):
        try:
            x = set()
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        x.add(j)
                if (type(i) == dict):
                    for key, val in i.items():
                        x.add(key)
                        x.add(val)
            d = {}
            for i in x:
                d[i] = 0
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        d[j] = d[j] + 1
                if type(i) == dict:
                    for key, val in i.items():
                        d[key] = d[key] + 1
                        d[val] = d[val] + 1
            self.info_log("number_of_occurences function --> " + str(d))
            return d
        except Exception as e:
            self.error_log(e)

    def keys_in_dict(self):
        try:
            keys = 0
            for i in self.l:
                if type(i) == dict:
                    for key, val in i.items():
                        keys = keys + 1
            self.info_log("keys_in_dict function --> " + str(keys))
            return keys
        except Exception as e:
            self.error_log(e)

    def string_data(self):
        try:
            l1 = []
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            l1.append(j)
                if type(i) == dict:
                    for key, val in i.items():
                        if type(key) == str:
                            l1.append(key)
                        if type(val) == str:
                            l1.append(val)
            self.info_log("string_data function --> " + str(l1))
            return l1
        except Exception as e:
            self.error_log(e)

    def aplhanum(self):
        try:
            l1 = []
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == str and j.isalnum():
                            l1.append(j)
                if type(i) == dict:
                    for key, val in i.items():
                        if type(key) == str and key.isalnum():
                            l1.append(key)
                        if type(val) == str and val.isalnum():
                            l1.append(val)
            self.info_log("aplhanum function --> " + str(l1))
            return l1
        except Exception as e:
            self.error_log(e)

    def multiplication_of_numeric_data(self):
        try:
            l1 = []

            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    mul = 1
                    for j in i:
                        if type(j) == int:
                            mul = mul * j
                    l1.append(mul)
                if type(i) == dict:
                    mul = 1
                    for key, val in i.items():
                        if type(val) == int:
                            mul = mul * val
                    l1.append(mul)
            self.info_log("multiplication_of_numeric_data function --> " + str(l1))
            return l1
        except Exception as e:
            self.error_log(e)

    def info_log(self, msg):
        lg.info(str(msg))

    def error_log(self, e):
        lg.error(str(e))


listObj = ListClass([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
listObj.extract_list()
listObj.extract_dict()
listObj.extract_tuple()
listObj.extract_numerical()
listObj.summation()
listObj.filter_odd_values()
listObj.extract_ineuron()
listObj.number_of_occurences()
listObj.keys_in_dict()
listObj.string_data()
listObj.aplhanum()
listObj.multiplication_of_numeric_data()


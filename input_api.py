def filter(data):
    wrong_flag = -1
    noise = 500
    if float(data) > noise:
        data = str(wrong_flag)
    return data


class input_api:

    def __init__(self, user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time):

        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.heartrate = heartrate
        self.Systolic_BP = Systolic_BP
        self.Diastolic_BP = Diastolic_BP
        self.blood_oxygen = blood_oxygen
        self.temperature = temperature
        self.time = time
        self.dic = {"gender": gender, "heartrate": heartrate,
                    "Diastolic_BP": Diastolic_BP, "Systolic_BP": Systolic_BP, "blood_oxygen": blood_oxygen,
                    "temperature": temperature, "time": time}

    def implement_filter(self):
        for key in self.dic.keys():
            if key != "user_id" and key != "age" and key != "gender" and key != "time":
                self.dic[key] = filter(self.dic[key])

    def return_request(self, wire):
        alert = 1
        data_db = 2
        if wire == alert:
            user_data_dic = {"heartrate": self.heartrate,
                             "Diastolic_BP": self.Diastolic_BP, "Systolic_BP": self.Systolic_BP,
                             "blood_oxygen": self.blood_oxygen,
                             "temperature": self.temperature, "time": self.time}
            return user_data_dic
        if wire == data_db:
            return self.user_id, self.dic


# my_data = input_api('a', 1, 'male', 1, 1, 10000, 1, 1, 1)
# print(my_data.dic)
# my_data.implement_filter()
# print(my_data.dic)
# print(my_data.return_request(1))

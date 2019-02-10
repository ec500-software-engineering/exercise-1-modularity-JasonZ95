authenDB = {'admin': "123456"}
infoDB = {}

"""
data format of infoDB:
{
    'XXXXXX(user_id)': [{
        'time': '2019-02-06 17:11',
        'gender': 'male',
        'heartrate': 100,
        'blood_pressure': 125,
        'blood_oxygen': 0.7
        },
        {
            ...
        }
    ]
}
"""


class DataBaseModule:

    def __init__(self):
        self.infoDB = infoDB
        self.authDB = authenDB
        self.auth = False

    def authen(self, username, password):
        """
        user log in, must call this function before using delete\insert\search 
        :param username: user id
        :param password: user password
        :return void
        """
        if self.authDB[username] == password:
            print("Authentication Succeed!")
            self.auth = True
        else:
            print("Try username and password again")

    def delete(self, ID):
        """
        delete patient's data based on user id
        :param ID: user id
        :return void
        """
        if self.auth:
            infoDB.popitem(ID)
        else:
            print("Authentation Failed")

    def insert(self, ID, info):
        """
        insert patient's data, it will be stored by user id
        :param ID: user id
        :param info: patient's data, type: dict, format example:
        {
        'time': '2019-02-06 17:11',
        'gender': 'male',
        'heartrate': 100,
        'blood_pressure': 125,
        'blood_oxygen': 0.7
        }
        :return void 
        """
        if self.auth:
            infoDB[ID] = info
        else:
            print("Authentation Failed")

    def search(self, ID):
        """
        search all patient's historical data based on user id
        :param ID: user id
        :return type: dict, format example:
        {
        'time': '2019-02-06 17:11',
        'gender': 'male',
        'heartrate': 100,
        'blood_pressure': 125,
        'blood_oxygen': 0.7
        }
        """
        if self.auth:
            return self.infoDB[ID]
        else:
            print("Authentation Failed")

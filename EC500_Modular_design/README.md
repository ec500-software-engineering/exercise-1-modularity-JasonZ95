# EC500-Modular Design-2.4

### System Diagram(Leyang Shen)

<img align = center src = "https://github.com/leonshen95/EC500/blob/master/EC500%20diagram%201.jpg?raw=true">
 
## Database Module(Yuxuan Su & Zifan Wang)
before using the Database Module, you should construct the database object first:  
```
db_module = DataBaseModule()
# must authen the db_module before using it
db_module.authen(userid, password)

# to insert patient's data into database module
# here's the example format of patient's data:
data = {
            'time': '2019-02-06 17:11',
            'gender': 'male',
            'heartrate': 100,
            'blood_pressure': 125,
            'blood_oxygen': 0.7
        }
db_module.insert(userid, data)

# to search patient's data from database module
data = db_module.search(userid)

# to delete patirent's data
db_module.delete(userid)
```
### Rough code for authentation
```
class authentation:
    def __init__(self):
      self.username = ""
      self.password = ""
    
    def ifmatch(self, username, password):
        do search in authDB
        if match:
            return true
        else:
            return authentation().failure
     
    def failure(self):
        print("Authentation Failed")
        return false
```
#### Rough structure for authDB
```
| username | password | permission |
|   test   |  a123adf |    full    |
```
permission part reserved for future function extension

### for infoDB
```
class infoDB:
    def __init__(self):
        self.personalInfo = {}
        self.bioInfo = {}
        
    def search(self, keyword):
        do search
        return 
    
    def delete(self, keyword):
        do delete
    
    def insert(self, personalInfo, bioInfo):
        self.personalInfo = personalInfo
        self.bioInfo = bioInfo
```
##### DB structure
```
|----Personal Info---- | --------------- Bio Info ---------------|
| ID | AGE | gender |.....| Pulse | Heart Rate | Blood Pressure |
```
## Input Module(Boyang Zhou)
### Input:
Waveforms used for health detection:

* Heart rate

* Blood pressure

* Blood oxygen

* Temperature

User information used for data archiving and access verification:

* User_id

* Age

* Gender

### Output:
All the waveforms mentioned above(with preprocessing)

Data encapsulation used for databse storage

### Class and Interface:
```
class intput:
    def __init__(self, user_id, age, gender, heartbeat, blood_pressure, blood_oxygen, temperature)
    
    def filter(data, noise, data_type)
    
    def return data(dic)
    
    def return_request(wire)
```

## Analyzer Module(Yicun Hou & Yang Qiao)
### Input: 
Analog waveform of:
Blood pressure, 
Heart rate, 
Heart Oxygen level,
Body temperature

### Output:
Signal loss alert;
Shock alert;
Oxygen supplemental alert;
Fever sign;
Hypotension or hypertension sign.

### Definition:
Heart_Rate:
    Module to find signal loss to and shock alert to report emergency

Systolic_BP & Diastolic_BP:
   To check if patient’s blood pressure is in a normal scope

Heart_O2_Level:
    Check if the Oxygen Level under a normal range

Body_temp:
    Check if the body temperature is so high that the patient catch a fever

### Class and Interface:
```
class Analyzer():
    
    def __init__(self, Systolic_BP, Diastolic_BP, Heart_Rate, Heart_O2_Level, Body_temp):
        self.Systolic_BP = Systolic_BP
        self.Diastolic_BP = Diastolic_BP
        self.Heart_Rate = Heart_Rate
        self.Heart_O2_Level = Heart_O2_Level
        self.Body_temp = Body_temp

    def Signal_Loss(self, Heart_Rate, Body_temp):
        # Signal loss judgement

    def Shock_Alert(self, Heart_Rate, Body_temp):
        # Shock emergency judgement

    def Oxygen_Supply(self, Heart_O2_Level):
        # Oxygen supply judgement
    
    def Fever(self, Body_temp):
        # Fever judgement

    def Hypotension(self, Systolic_BP, Diastolic_BP):
        # Hypotension judgement
    
    def Hypertension(self, Systolic_BP, Diastolic_BP):
        # Hypertension judgement
```

## Display Module(Haoyu Xu & Leyang Shen)


### Input:
* Emergency: when the data is analyzed to be vital
* Signal loss alert: when sensor is lost attached, parameter: Singal_Loss
* Shock alert: when patient is in shock, parameter: Shock_Alert
* Oxygen supplement alert: patient does not enough oxygen, needs to increase amount of oxygen, parameter: Oxygen_Supply

Condition: Normal
* Fever sign: light is still on, parameter: Fever
* Hypotension and hypertension sign: light is still on, parameter: Hypotension, Hypertension

Condition: AI - based module -- prediction alert

Normal parameters: Pulse, Blood pressure, Blood Oxygen

### Output:
* Pulse: pulse on configurable time intervals
* Blood pressure: blood pressure on configurable time intervals
* Blood Oxygen: blood Oxygen levels on configurable time intervals
* Whether to get alerts
* Get future prediction based on AI module

### Class and Interface:
```
class outputAlert:

    def receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension);

    def send_basic_input_data(BasicResult);

    def receive_AI_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension);

    def send_AI_input_data(AIResult); 
```


## AI Module (Wanxuan Chen & YunCheng Zhu)

### Input:
* Database Data:
* Measurement Time: The Measurement time
* Pulse: Measurement Data
* Blood Oxygen: Measurement Data
* Blood Pressure:Measurement Data

### Output:
* Pulse Prediction Trend
* Blood Oxygen Prediction Trend
* Blood Pressure Prediction Trend
* Alert: When the Prediction Trends are going abnormal, it will display a prediction alert.


### Query the Data From DB:
* Extract the patient data from database and separate as three group: Pulse, Blood Oxygen and Blood Pressure. Return these data.

### AI Prediction Module:
* Input three groups data into the AI module to do the prediction. The Module will give the prediction feedback( like the blood pressure will decrease and become worse)
* Also we set up the Alert value, once one of these three values under or upper a danger value, it will give an alert. 

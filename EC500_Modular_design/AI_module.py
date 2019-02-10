import numpy as np
from Database_Module import DataBaseModule


# Input: ID(from main function perhaps), infoDB(from Database function)
# output: Three predicted parameters, three Alert signals(Type:Boolean

class AI_module(object):
    def __init__(self, dict):
        self._dict = dict

    def Query_Data_From_Database(self, ID, infoDB):
        # connect database, query previous one day data from Database
        # Database = database_dict()
        Blood_oxygen = list()
        Blood_pressure = list()
        Systolic = list()
        Diastolic = list()
        DataBaseModule.search(ID)
        # Username = input("")
        # get dictionary from database
        for key in infoDB:
            if key == ID:
                pressure = dict.get('blood_pressure')
                oxygen = dict.get('blood_oxygen')
                Diastolic_BP = dict.get('Diastolic_BP')
                Systolic_BP = dict.get('Systolic_BP')
                Blood_pressure.append(pressure)
                Blood_oxygen.append(oxygen)
                Systolic.append(Systolic_BP)
                Diastolic.append(Diastolic_BP)

        return Blood_oxygen, Blood_pressure, Systolic, Diastolic

    def AI_Module(self, Blood_oxygen, Blood_pressure, Systolic, Diastolic):

        # AI module do the prediction, The AI module uses previous data
        oxygen = np.array(Blood_oxygen)
        pressure = np.array(Blood_pressure)
        diastolic = np.array(Diastolic)
        systolic = np.array(Systolic)
        pressure_predict_result = np.mean(pressure)
        oxygen_predict_result = np.mean(oxygen)
        Diastolic_predict_result = np.mean(diastolic)
        Systolic_predict_result = np.mean(systolic)

        return pressure_predict_result, oxygen_predict_result, Diastolic_predict_result, Systolic_predict_result

    def Feedback(self,
                 Blood_pressure_predict_result,
                 Blood_oxygen_predict_result,
                 Diastolic_predict_result,
                 Systolic_predict_result):
        lower_BP = 80
        upper_BP = 120
        lower_BO = 80
        upper_BO = 120
        BP_Alert = False
        BO_Alert = False

        Pulse_Alert = False
        if Blood_oxygen_predict_result < lower_BO or Blood_oxygen_predict_result > upper_BO:
            BO_Alert = True
        if Blood_pressure_predict_result < lower_BP or Blood_pressure_predict_result > upper_BP:
            BP_Alert = True
        if Systolic_predict_result < 90 or \
                Diastolic_predict_result < 60 or \
                Systolic_predict_result > 140 or \
                Diastolic_predict_result > 90:
            Pulse_Alert = True
        # feedback the AI prediction result to the interface
        # It will turn on the Alert when the statues get worse.
        return BO_Alert, BP_Alert, Pulse_Alert

from input_api import input_api
from Database_Module import DataBaseModule
from Analyzer import Analyzer
from OutputAlert_module import OutputAlert_module
import queue
import threading
import time
#import AI_module

input_queue = queue.Queue()
output_queue = queue.Queue()


def input_thread():
    # authentication for databese
    # no use in this program
    # authenDB = {'admin': "123456"}
    username = 'admin'
    password = '123456'

    # initialize the database
    mydatabase = DataBaseModule()
    mydatabase.authen(username, password)

    for line in open("userdata.txt"):
        element = line.split()
        information = input_api(element[0], element[1], element[2], element[3],
                                    element[4], element[5], element[6], element[7], element[8])
        information.implement_filter()

        # Write data to the database
        user_id, data_dic = information.return_request(2)
        mydatabase.insert(user_id, data_dic)

        # Uniform variable name
        data_dic["Heart_O2_Level"] = data_dic.pop("blood_oxygen")
        data_dic["Heart_Rate"] = data_dic.pop("heartrate")
        data_dic["Body_temp"] = data_dic.pop("temperature")

        input_queue.put(data_dic)
        time.sleep(1)


def process_thread():
    while True:
        print("analyzing")
        data_dic =input_queue.get()
        if data_dic is None:
            break

        # use analyzer to trigger the alert
        myAnalyzer = Analyzer(data_dic["Systolic_BP"],
                              data_dic["Diastolic_BP"],
                              data_dic["Heart_Rate"],
                              data_dic["Heart_O2_Level"],
                              data_dic["Body_temp"])
        # call functions to trigger the alert
        Signal_Loss = myAnalyzer.Signal_Loss(myAnalyzer.Heart_Rate, myAnalyzer.Body_temp)
        Shock_Alert = myAnalyzer.Shock_Alert(myAnalyzer.Heart_Rate, myAnalyzer.Body_temp)
        Oxygen_Supply = myAnalyzer.Oxygen_Supply(myAnalyzer.Heart_O2_Level)
        Fever = myAnalyzer.Fever(myAnalyzer.Body_temp)
        Hypotension = myAnalyzer.Hypotension(myAnalyzer.Systolic_BP, myAnalyzer.Diastolic_BP)
        Hypertension = myAnalyzer.Hypertension(myAnalyzer.Systolic_BP, myAnalyzer.Diastolic_BP)

        # generate regular output base on presented data
        basic_result = receive_basic_iuput_data(Signal_Loss,
                                                Shock_Alert,
                                                Oxygen_Supply,
                                                Fever,
                                                Hypotension,
                                                Hypertension)
        time.sleep(1)
        print("done")
        output_queue.put(basic_result)


def output_thread():
    while True:
        basic_result =  output_queue.get()
        if basic_result is None:
            break
        print("The result is:")
        print(basic_result)


def main():
    threads = []
    t1 = threading.Thread(target=input_thread)
    threads.append(t1)
    t2 = threading.Thread(target=process_thread)
    threads.append(t2)
    t3 = threading.Thread(target=output_thread)
    threads.append(t3)

    for thread in threads:
        thread.start()
        time.sleep(0.1)


if __name__ == '__main__':
    main()

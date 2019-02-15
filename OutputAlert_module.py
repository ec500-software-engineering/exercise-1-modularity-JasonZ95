from AI_module import AI_module


def receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
    # Recevie data from input module, then analyze it using some judge functions to generate boolean result
    # Boolean Parameters
    # If paramter returns True, means it should be alerted, then add it to the array
    BasicResult = {'Signal_Loss': False, 'Shock_Alert': False, 'Oxygen_Supply': False, 'Fever': False,
                   'Hypotension': False, 'Hypertension': False}
    if Singal_Loss:
        BasicResult['Signal Loss'] = True
    if Shock_Alert:
        BasicResult['Shock_Alert'] = True
    if Oxygen_Supply:
        BasicResult['Oxygen_Supply'] = True
    if Fever:
        BasicResult['Fever'] = True
    if Hypotension:
        BasicResult['Hypotension'] = True
    if Hypertension:
        BasicResult['Hypertension'] = True

    return BasicResult


# def send_basic_input_data(BasicResult, BasicData):
# Receive the result and show it on terminal or web page
#   sentData = analyze(BasicResult)
#   return sentData, BasicData


def display_AI_iuput_data():
    # Recevie AI data from input module, then analyze it using some judge functions to generate boolean result
    # Paramter is boolean
    # If paramter is True, means it should be alerted, then add it to the array

    AI_module.AI_Module(Blood_oxygen, Blood_pressure, Pulses)
    print('blood pressure prediction:')
    print(pressure_predict_result)
    print('blood oxygen prediction:')
    print(oxygen_predict_result)
    print('Pulse_predict_result:')
    print(Pulse_predict_result)

# def send_AI_input_data(AIResult):
# Receive the result and show it on terminal or web page
#   sentData = analyze(AIResult)
#   return sentData

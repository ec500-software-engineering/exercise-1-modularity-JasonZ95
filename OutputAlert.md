## Module: Output alert

### System Diagram
<img align = center src = "https://github.com/leonshen95/EC500/blob/master/EC500%20diagram%201.jpg?raw=true">
 
### Input:
* Emergency: when the data is analyzed to be vital 
* Signal loss alert: when sensor is lost attached
* Shock alert: when patient is in shock
* Oxygen supplement alert: patient does not enough oxygen, needs to increase amount of oxygen

Condition: Normal
* Fever sign: light is still on
* Hypotension and hypertension sign: light is still on

Condition: AI - based module -- prediction alert

Normal parameters: Pulse, Blood pressure, Blood Oxygen

### Output:
* Pulse: pulse on configurable time intervals
* Blood pressure: blood pressure on configurable time intervals
* Blood Oxygen: blood Oxygen levels on configurable time intervals
* Whether to get alerts
* Get future prediction based on AI module

### Class and Interface:
class Alerts {
* Objects: Signal loss alert, Shock alert, Oxygen supplement alert, Prediction alert
* method: receiveAlerts(Objects), judgeAlerts(Objects), sendAlerts()
* 
}

class normalParameter {
* Objects: Pulse, Blood pressure, Blood Oxygen
* method: receiveParameter(Objects), handleParameter(Objects), sendParameter(),
*
}

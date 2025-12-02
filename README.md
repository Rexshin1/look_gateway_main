<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=eclipse-mosquitto&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

</div>

<p align="center">
<img alt="Look Gateway" src="https://github.com/Javadwipa/look_gateway/blob/main/flask_server/app/static/assets/img/logo.png?raw=true" title="LOOK" width="350"/>
</p>


# LOOK GATEWAY

Look APP Gateway adalah aplikasi untuk penghubung antara sensor maupun controller dengan server

### Sensor Device: 
<table width="100%" valign="top">
<tr>
<td>
    <ul>
<li>Sensor Power Meter</li>
<li> Sensor Water (AWLR & Water Quallity)</li>
<li> Sensor Humidity</li>
<li> Sensor Temperature</li>
<li> Wheather Station</li>
    </ul>
</td>
<td>
<ul>
<li>Fire Detection</li>
<li>Smoke Detection</li>
<li>Gas Metering</li>
<li>LUX Sensor</li>
</ul>
</td>
</tr>
</table> 


### Informasi Aplikasi: 
- Python 3.10 =< 
- MQTT Mosquitto
- FLASK (WEB APP & REST FULL )

    ##### Python Package :
    - Flask 
    - Flask-SQLalchemy 
    - Flask-Migrate 
    - Flask-Login 
    - Flask-Bcrypt
    - Flask-WTF 
    - paho-mqtt 
    - requests 
    - Flask-JWT-Extended 
    - psutil 
    - speedtest-cli
    #### Struktur File:
```
.
├── README.md
├── config
│   ├── __init__.py
│   ├── api.py
│   ├── app.db
│   ├── config.py
│   └── model.py
├── core
│   ├── __init__.py
│   ├── checkpoint.py
│   ├── cisco_switch.py
│   ├── mqtt_sensor.py
│   ├── networking.py
│   ├── send_server.py
│   └── system_info.py
├── flask_server
│   └── app
│       ├── __init__.py
│       ├── blueprints
│       │   ├── api_routes.py
│       │   └── web_routes.py
│       ├── controller
│       │   ├── api
│       │   │   ├── device_controller.py
│       │   │   └── network_controller.py
│       │   ├── auth_controller.py
│       │   ├── device_controller.py
│       │   ├── home_Controller.py
│       │   ├── network_controller.py
│       │   └── setting.py
│       ├── model
│       │   ├── model.py
│       │   └── user_model.py
│       ├── request_form
│       │   ├── LoginForm.py
│       │   ├── RegisterForm.py
│       ├── static
│       │   └── assets
│       │       ├── css
│       │       ├── img
│       │       ├── js
│       │       ├── less
│       │       └── lib
│       └── views
│           ├── device_list.html
│           ├── home.html
│           ├── layouts
│           │   ├── app.html
│           │   └── auth.html
│           ├── login.html
│           ├── networking.html
│           └── register.html
├── config.ii
├── main.py
└── requirements.txt
```
### Installation
Clone ripository github:<br>

````
$ git clone https://github.com/Javadwipa/look_gateway.git
````
Masuk dalam directory:
````
$ cd look_gateway/
````
Membuat environment:
````
$ python venv .env
````
Mengaktifkan environment:
````
Linux or Mac:
 $ source .env/bin/activate 

Windows:
 $ .\venv\Scripts\activate
````

Update package:
````
$ pip install -r requirements.txt
````
Running program:
```
Linux or Mac:
$ python main.py

Windows:
$ py main.py
```

### File main.py
````python
from core import MqttSensor,SystemInfo
from config import config
import threading

from flask_server.app import create_app,db


app = create_app()





def start_flask():
    with app.app_context():
        db.create_all()
       
    app.run(host='0.0.0.0',port=config.port_app,debug=True,threaded=False ,use_reloader=False)

def publis_system():
    mqtt = MqttSensor(config.hostmqtt)
    topic= config.device_id+"/status"
    return mqtt.system_info_msg(topic)
# 
# print(SystemInfo.get_cpu_temperature())

if __name__ == '__main__':
    
    # publis_system()
    flask_thred = threading.Thread(target=start_flask)
    mqtt_thread = threading.Thread(target=publis_system)

    # flask_thred.daemon = True
    # mqtt_thread.daemon = True

    flask_thred.start()
    # mqtt_thread.start()
    flask_thred.join()
    # mqtt_thread.join()

    # # Start threads
    # thread1.start()
    # thread2.start()

    
    # start_flask()
    

    # mqtt.system_info_msg(topic)
````

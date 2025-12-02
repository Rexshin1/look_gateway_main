import os
import configparser



conf = configparser.ConfigParser()
conf.read('config.ini')

device_id = conf['APP']['GATEWAY_ID']
port_app = conf['APP']['PORT_WEB']
hostmqtt = conf['MQTT']['HOST']
port_mqtt = conf['MQTT']['PORT']
user_mqtt = conf['MQTT']['USERNAME']
pass_mqtt = conf['MQTT']['PASSWORD']
secret_key = conf['APP']['SECRET_KEY']
database = conf['APP']['DATABASE']
token_api = conf['SERVER_API']['TOKEN_API']

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, database)
SQLALCHEMY_TRACK_MODIFICATIONS = True
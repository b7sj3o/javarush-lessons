from datetime import datetime

def log_action(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        result = func(*args, **kwargs)
        print(f"[{now}] Датчик {func.__name__} зафіксував значення {result}")
        return result
    return wrapper


def cache_result(func):
    result = None
    last_time_used: datetime = datetime.now()
    def wrapper(*args, **kwargs):
        nonlocal result, last_time_used
        now = datetime.now()
        if result is None or (now - last_time_used).total_seconds() > 2:
            result = func(*args, **kwargs)
        return result
    return wrapper



class Sensor:
    def __init__(self, name, value, min_value, max_value):
        self.name = name
        self.__value = value
        self.min_value = min_value
        self.max_value = max_value


    @property
    @cache_result
    def value(self):
        return self.__value

    @value.setter
    @log_action
    def value(self, value):
        if value > self.max_value or value < self.min_value:
            raise ValueError(f"{self.__class__.__name__} вийшов за межі зі значенням: {value}")
        self.__value = value

class CPUSensor(Sensor):
    ...

class TempSensor(Sensor):
    ...


class SmartHome:
    def __init__(self):
        self.sensors: list[Sensor] = []

    def add_sensor(self, sensor: Sensor):
        self.sensors.append(sensor)

    def monitor_anomalies(self, threshold: float):
        for sensor in self.sensors:
            percentage = (sensor.value / sensor.max_value) * 100
            print(sensor.value, sensor.max_value)
            if percentage > threshold:
                yield f"{sensor.name} досяг відмітки {percentage}% ({percentage-threshold}% більше threshold)"



smart_home = SmartHome()

cpu_sensor = CPUSensor("Intel I-9", value=50, min_value=0, max_value=100)
temp_sensor = TempSensor("'Kitchen-Termo", value=20, min_value=-20, max_value=40)
smart_home.add_sensor(cpu_sensor)
smart_home.add_sensor(temp_sensor)

print("Шукаємо аномалії")
for alert in smart_home.monitor_anomalies(threshold=80):
    print(f'УВАГА : {alert}')


temp_sensor.value -= 40
cpu_sensor.value += 20


print("Шукаємо аномалії")
for alert in smart_home.monitor_anomalies(threshold=80):
    print(f'УВАГА : {alert}')

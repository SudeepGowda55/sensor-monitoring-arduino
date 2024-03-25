import threading
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from serial import Serial

app = FastAPI(
    title="Sensor Monitoring",
    description="A simple Application to monitor Arduino Serial Port data",
    version="0.1",
)

sensor_data_list = []
lock = threading.Lock()
templates = Jinja2Templates(directory="templates")


def serialmonitor(comport, baudrate):
    serial_port = Serial(comport, baudrate, timeout=0.1)
    while True:
        data = serial_port.readline().decode().strip()
        if data:
            with lock:
                print("Data", data)
                sensor_data_list.append(data)
                print(sensor_data_list)


@app.get("/")
async def read_root():
    return "Goto this link http://127.0.0.1:8000/serialmonitor to start monitoring"


@app.get("/html", response_class=HTMLResponse)
async def render_html(request: Request):
    return templates.TemplateResponse(request=request, name="charts.html", context={"id": sensor_data_list})


@app.get("/sensordata")
async def sensor_data():
    print(sensor_data_list)
    return sensor_data_list


@app.get("/serialmonitor")
async def start_monitoring():
    thread = threading.Thread(
        target=serialmonitor, args=("/dev/ttyUSB0", 9600), daemon=True
    )
    thread.start()
    return "Monitoring started Checkout your console and if you want data go to http://127.0.0.1:8000/sensordata"

import time

from AK7010MotorControl import Motor, BRAKE_CUR
import can

def printout(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("starting bus")
bus = can.ThreadSafeBus(interface="socketcan", channel="can0", bitrate=1000000)

motors = [3, 5]
print("starting motors")
motor_obj = [Motor(i, bus, printout) for i in motors]

print("setting motors")
for i in motor_obj:
    i.start()
    # i.set_origin()

print("accelerating motors")
for i in motor_obj:
    i.set_speed(500)
    # i.set_spd_pos(500, 10, 1)
time.sleep(2)

print("stopping motors")
for i in motor_obj:
    i.stop()

bus.shutdown()

# m1.set_speed(50)
# time.sleep(5)
#
# m1.set_speed(100)
# time.sleep(3)
#
# m1.set_origin()
#
# m1.set_speed(200)
# time.sleep(5)
#
# m1.stop()
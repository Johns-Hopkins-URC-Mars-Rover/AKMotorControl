import time

from AK7010MotorControl import Motor, BRAKE_CUR
import can
import moteus
import moteus_pi3hat

def printout(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("starting bus")
# bus = can.ThreadSafeBus(interface="socketcan", channel="can0", bitrate=1000000)
default_can_config = moteus_pi3hat.CanConfiguration()
default_can_config.fdcan_frame = False
can_config = {i: default_can_config for i in range(1, 6)}
# can_config = {
#     2: default_can_config
# }
print(can_config)

transport = moteus_pi3hat.Pi3HatRouter(can=can_config)


print("starting motors")

# m1 = Motor(0, 1, transport)
# m2 = Motor(0, 5, transport)
# m3 = Motor(0, 3, transport)
# m4 = Motor(0, 4, transport)
# m5 = Motor(0, 5, transport)
m6 = Motor(2, 3, transport)

# motor_obj = [m1, m2, m3, m4, m5, m6]
motor_obj = [m6]
print("setting motors")
for i in motor_obj:
    i.start()
    # i.set_origin()

print("accelerating motors")
for i in motor_obj:
    i.set_speed(500)
    # i.set_spd_pos(500, 10, 1)
time.sleep(2)

for i in motor_obj:
    i.stop()

print("stopping motors")
for i in motor_obj:
    i.shutdown()

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
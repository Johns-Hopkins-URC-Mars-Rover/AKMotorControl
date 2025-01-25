import time

from AK7010MotorControl import Motor, BRAKE_CUR

m1 = Motor("can0", 8)

m1.start()
m1.set_origin()

m1.set_speed(50)
time.sleep(5)

m1.set_speed(100)
time.sleep(3)

m1.set_origin()

m1.set_speed(200)
time.sleep(5)

m1.stop()
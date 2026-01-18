import threading
from typing import List
import asyncio

import moteus_pi3hat
import moteus

class ThreadSafePi3hatCan:
    def __init__(self, this_id: int, bus_id: int, transport: moteus_pi3hat.Pi3HatRouter):
        self.transport = transport
        self.controller = moteus.Controller(id=this_id, transport=transport)
        self.bus = bus_id
        self.lock = threading.Lock()

    def send_msg(self, arbitration_id: int, data: List[int]):
        msg = moteus.Command()
        msg.raw = True
        msg.bus = self.bus
        msg.arbitration_id = arbitration_id
        msg.reply_required = False
        msg.data = bytes(data)

        self.lock.acquire()

        results = asyncio.run(self.transport.cycle([msg, self.controller.make_query()]))

        self.lock.release()

        return results
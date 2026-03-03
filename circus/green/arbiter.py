from circus.arbiter import Arbiter as _Arbiter
from circus.green.controller import Controller

from zmq.green.eventloop import ioloop
from zmq.green import Context


class Arbiter(_Arbiter):
    def _init_context(self, context):
        self.context = context or Context.instance()
        # ensure event loop is created
        from circus.eventloop import get_or_create_event_loop
        get_or_create_event_loop()
        self.loop = ioloop.IOLoop.current()
        self.ctrl = Controller(self.endpoint, self.multicast_endpoint,
                               self.context, self.loop, self, self.check_delay)

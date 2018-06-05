# import aspectlib
#
#
# class Client(object):
#     def __init__(self, address):
#         self.address = address
#         self.connect()
#     def connect(self):
#         # establish connection
#     def action(self, data):
#         # do some stuff
#
# def retry(retries=(1, 5, 15, 30, 60), retry_on=(IOError, OSError), prepare=None):
#     assert len(retries)
#
#     @aspectlib.Aspect
#     def retry_aspect(*args, **kwargs):
#         durations = retries
#         while True:
#             try:
#                 yield aspectlib.Proceed
#                 break
#             except retry_on as exc:
#                 if durations:
#                     logging.warn(exc)
#                     time.sleep(durations[0])
#                     durations = durations[1:]
#                     if prepare:
#                         prepare(*args, **kwargs)
#                 else:
#                     raise
#
#     return retry_aspect

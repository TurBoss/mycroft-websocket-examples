from websocket import create_connection, WebSocket
import ssl

class MyWebSocket(WebSocket):
    def recv_message(self):
        message = super().recv_frame()
        print('Recieved message: {}'.format(message))
        return message

ws = create_connection("ws://0.0.0.0:8181/core", sslopt={"cert_reqs": ssl.CERT_NONE}, class_=MyWebSocket)

mycroft_request = 'what is the weather'

mycroft_type = 'recognizer_loop:utterance'
mycroft_data = '{"utterances": ["%s"]}' % mycroft_request
message = '{"type": "' + mycroft_type + '", "data": ' + mycroft_data + '}'
print("Sending request 'Message'...")
ws.send(message)
print(ws.recv())
print(ws.recv())
print("Request sent")

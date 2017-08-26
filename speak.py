from websocket import create_connection, WebSocket
import ssl

class MyWebSocket(WebSocket):
    def recv_message(self):
        message = super().recv_frame()
        print('Recieved message: {}'.format(message))
        return message



ws = create_connection("ws://0.0.0.0:8181/core", sslopt={"cert_reqs": ssl.CERT_NONE}, class_=MyWebSocket)
mycroft_speak = '"Hey Brian"'
mycroft_type = '"speak"'
mycroft_data = '{"expect_response": false, "utterance": %s}, "context": null' % mycroft_speak
message = '{"type": ' + mycroft_type + ', "data": ' + mycroft_data + '}'
print(message)
print("Sending 'Message'...")
ws.send(message)
print(ws.recv())
print("Sent")

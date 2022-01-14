import sys
import ctypes

if len(sys.argv) < 2:
    print("Usage: find_load.py <address>")
    exit()

with open("KB421DSP.BIN", "rb") as fp:
    data = fp.read()

dest_address = int("0x" + sys.argv[1], base=16)

LOAD_OP_START = (0x9F << 40) | (0x80 << 32)
full_load = LOAD_OP_START + dest_address

found_address = False
for reg in range(16):
    in_bytes = (full_load + (reg << 32)).to_bytes(6, 'big')
    if in_bytes in data:
        print("!!Found {} being loaded into register {} at address {}".format(sys.argv[1], reg, hex(data.index(in_bytes) + 0x10000000)))
        found_address = True
if not found_address:
    print("Address not found in firmware as a jump to register")
    print("Trying to look for offset calls")

CALL_D_OP_START =   0b1101100000000000
CALL_OP_START =     0b1101000000000000

for i in range(len(data)//2):
    binary_offset = i*2
    cur_opcode = (data[binary_offset] << 8) + data[binary_offset + 1]
    if cur_opcode & CALL_D_OP_START == CALL_D_OP_START:
        if dest_address == binary_offset + 0x10000000 + ((ctypes.c_int32(cur_opcode & 0b11111111111).value << 22) >> 21) + 2:
            print("!!Found call:d at {}".format(hex(binary_offset + 0x10000000)))
    elif cur_opcode & CALL_OP_START == CALL_OP_START:
        if dest_address == binary_offset + 0x10000000 + ((ctypes.c_int32(cur_opcode & 0b11111111111).value << 22) >> 21):
            print("!!Found call at {}".format(hex(binary_offset + 0x10000000)))


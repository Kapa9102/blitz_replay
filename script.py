import pickle
import subprocess

FILE = "battle_results.dat"

with open(FILE, "rb") as f:
    FULLRAW = f.read();

# HEX_DUMP = subprocess.check_output("hexdump -C " + FILE +  "| head -1", shell=True, text=True);
# print(HEX_DUMP.strip())

try:
    PROTO_ID, RAW = pickle.loads(FULLRAW, encoding="latin1")
    LIM=128
    print("[1] Loaded Data from FULLRAW")
    print(f"version: {PROTO_ID}")
    print(f"RAW[0-128]: Type: {type(RAW)} Data:{RAW[0:LIM].encode()}")
    open("battle_results.bin", "wb").write(RAW.encode("latin1"));
except Exception as E:
    print("[0] Couldn't load Pickle data: ", E)
    pass

LIM = 128




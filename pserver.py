import lib.prng as prng
import json
import sys
import os
import signal
import time
import uuid

halt = False

def exit_fn (*args):
    global halt
    halt = True


signal.signal(signal.SIGINT, exit_fn)
signal.signal(signal.SIGTERM, exit_fn)

generator = prng.UhePrng()

pipeline_file = os.path.sep + 'tmp' + os.path.sep + 'random.pipeline'

if len(sys.argv) >= 2:
    pipeline_file = sys.argv[1]

if os.path.exists(pipeline_file):
    os.remove(pipeline_file)

os.mkfifo(pipeline_file, 0o666 )
pipeline = os.open(pipeline_file, os.O_WRONLY)

while True:
    # print('-')

    generator.add_entropy(str(uuid.getnode()))
    random = bytes(generator.string(1024), 'UTF-8')
    os.write(pipeline, random)

    # print('+')

    if halt:
        print()
        print('Process stopped by signal')
        break

os.close(pipeline)

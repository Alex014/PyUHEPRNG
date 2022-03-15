import lib.prng as prng
import json
import sys
import os
import signal
import time

halt = False


def exit_fn (*args):
    global halt
    halt = True


signal.signal(signal.SIGINT, exit_fn)
signal.signal(signal.SIGTERM, exit_fn)

generator = prng.UhePrng()



directory = ''

if len(sys.argv) >= 2:
    directory = sys.argv[1]

if directory != '':
    if not os.path.exists(directory):
        print('Directory ' + directory + ' does not exist')
        exit(1)
    else:
        directory += os.path.sep
else:
    directory = '/tmp/'

while True:
    # print('.')

    generator.add_entropy()
    seed = generator.string(256)

    with open(directory + 'seed.txt', 'w+') as file:
        file.seek(0)
        file.write(seed)
        file.truncate()
        file.close()

    numbers = generator.generate(0, 100)
    numbers = json.dumps(numbers)
    # print(numbers)

    with open(directory + 'numbers.json', 'w+') as file:
        file.seek(0)
        file.write(numbers)
        file.truncate()
        file.close()

    generator.add_entropy()
    seed = generator.string(1024)
    # print(seed)

    with open(directory + 'seed-big.txt', 'w+') as file:
        file.seek(0)
        file.write(seed)
        file.truncate()
        file.close()

    numbers = generator.generate(0, 1000)
    numbers = json.dumps(numbers)
    # print(numbers)

    with open(directory + 'numbers-big.json', 'w+') as file:
        file.seek(0)
        file.write(numbers)
        file.truncate()
        file.close()

    # print('.')

    if halt:
        print()
        print('Process stopped by signal')
        break

    time.sleep(1)

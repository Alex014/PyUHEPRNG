import lib.prng as prng
import json
import sys

if len(sys.argv) == 3:
    arg = sys.argv[1]
    cnt = int(sys.argv[2])

    generator = prng.UhePrng()
    generator.add_entropy()

    if arg == '-s' or arg == '-seed':
        if cnt < 256:
            cnt = 256
        print(generator.string(cnt))
    elif arg == '-n' or arg == '-numbers':
        cnt += 1
        if cnt < 1:
            cnt = 1
        seed = generator.string(1024)
        numbers = generator.generate(0, cnt)
        numbers = json.dumps(numbers)
        print(numbers)
else:
    print('Usage')
    print('prng.py -s <length> or prng.py --seed  <length> display the random generated seed')
    print('Usage prng.py -n <count> or prng.py --numbers <count> display the random generated numbers')

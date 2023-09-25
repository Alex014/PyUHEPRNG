# Py UHEPRNG
## UHEPRNG - Ultra High Entropy Pseudo-Random Number Generator

This is Steve Gibson's [UHEPRNG](https://ness3.app/GRC's%c2%a0%7c%c2%a0UHE%20PRNG%20Demo.htm) adaptation to python 

### Running
```
python main.py [directory]
```
Where *[directory]* is dir, where you want to store your files with random-generated data.
*[directory]* is optional, if no params, then current directory is used.
*Tmpfs* or other memory storage is recomended.

#### Four files will be generated:
1. seed.txt - seed of 256 random characters
2. seed-big.txt - seed of 1024 random characters
3. numbers.json - array of 100 random floating-point numbers
4. numbers-big.json - array of 1000 random floating-point numbers

--In PRNG-mode:
Every X seconds the seed and the numbers are regenerated. The regeneration interval should be fined-tuned based on the server/node capacity.

--In VRF mode (Verifiable Randomness Feed (& Function):
In this mode, the results must be Verifiable after execution to ensure fairness. The seeds must then persist much longer than a few seconds.
Depending on the actual use-case, if it's appropriate, the seed is published as EmerNVS record in Emercoin blockchain as Proof of Fairness to allow Full reproductibility hence Fairness.

--There is a third mode in between: feeding directly the /dev/urandom: 
In this mode, the seeds doesn't theorically need to be regenerated so no need for them to be published either for reproductivity proofs.

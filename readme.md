# Py UHEPRNG
## UHEPRNG - Ultra High Entropy Pseudo-Random Number Generator

This is Steve Gibson's [UHEPRNG](https://ness3.app/GRC's%c2%a0%7c%c2%a0UHE%20PRNG%20Demo.htm) adoptation to python 

### Running server
```
python server.py [directory]
```
Where *[directory]* is dir, where you want to store your files with random-generated data.
*[directory]* is optional, if no params, then current directory is used.
*Tmpfs* or other memory storage is recomended.

#### Four files will be generated:
1. seed.txt - seed of 256 random characters
2. seed-big.txt - seed of 1024 random characters
3. numbers.json - array of 100 random floating-point numbers
4. numbers-big.json - array of 1000 random floating-point numbers

Every second the seed and the numbers are regenerated.

### Running utility
```
python prng.py -s 555
```
Output random seed 555 characters length

```
python prng.py -n 5
```
Output 5 random floating point numbers in JSON format
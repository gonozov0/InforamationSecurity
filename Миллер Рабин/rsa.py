import miller_rabin as ml, random

def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def get_coprime_int(number, bits=64):
    for i in range(random.randrange(2 ** int(bits/3), 2 ** int(bits/2)), 2 ** (bits-1)):
        if gcd(i, number) == 1:
            return i
    raise Exception("Coprime int hasn't been generated")

def modinv(e, phi, bits=64):
    for d in range(random.randrange(2 ** int(bits/5), 2 ** int(bits/2)), 2 ** (bits*2)):
        if (d*e) % phi == 1:
            return d
    raise Exception("ModInv int hasn't been generated")

bits = 12
p = ml.generate_prime(bits)
print('p = {}'.format(p))
q = ml.generate_prime(bits)
print('q = {}'.format(q))
n = p*q
phi = (p-1)*(q-1)
e = get_coprime_int(phi, bits)
print('e = {}'.format(e))
d = modinv(e, phi, bits)
print('d = {}'.format(d))


batch_size = 2
unicode_bits = 3

def encode_data(input_data):
    batches = []
    k = int(len(input_data) / batch_size)
    if len(input_data) % batch_size != 0:
        k += 1
    for i in range(k):
        concatinated_char_codes = ''
        fake_end = (i+1)*batch_size
        end = fake_end if fake_end < len(input_data) else len(input_data)
        for char in input_data[i*batch_size : end]:
            char_code = str(ord(char))
            concatinated_char_codes += '0'*(unicode_bits - len(char_code)) + char_code
        batches.append(int(concatinated_char_codes))
    # print(batches[0])
    # print((batches[0] ** e % n) ** d % n)
    return list(map(lambda M: M**e % n, batches))

def decode_data(encode_data):
    if isinstance(encode_data, list):
        decode_str = ''
        for item in map(lambda X: str(X**d % n), encode_data):
            item = '0'*(batch_size*unicode_bits - len(item)) + item
            # print(item)
            for i in range(batch_size):
                decode_str += chr(int(item[i*unicode_bits : i*unicode_bits+unicode_bits]))
        return decode_str
    else:
        raise TypeError('Function argument isnt list')


data = encode_data(input())
print('incode data - {}'.format(data))
data = decode_data(data)
print('decode data - {}'.format(data))
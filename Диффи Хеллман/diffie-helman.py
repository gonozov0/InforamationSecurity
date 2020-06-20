import random

def isPrime(n):
   d = 2
   while d * d <= n and n % d != 0:
       d += 1
   return d * d > n

def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def primitive_roots(modulo):
    result_set = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            result_set.append(g)
    return result_set

primes = [i for i in range(2, 1000) if isPrime(i)]

class Listener:
    def init(self):
        self.p = random.choice(primes)
        self.g = random.choice(primitive_roots(self.p))
        self.alpha = random.randint(0, 100)
        self.A = self.g**self.alpha % self.p
    
    def give_values(self):
        return {
            'p': self.p,
            'g': self.g,
            'A': self.A
        }
    
    def init_with_values(self, values):
        self.p = values['p']
        self.g = values['g']
        self.A = values['A']
        self.alpha = random.randint(0, 100)
        return self.g**self.alpha % self.p

    def generate_key(self, B=None):
        if not B is None:
            self.A = B
        self.key = self.A**self.alpha % self.p

alice = Listener()
bob = Listener()
alice.init()
alice.generate_key(bob.init_with_values(alice.give_values()))
bob.generate_key()

print(alice.key, bob.key)
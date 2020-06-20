import hashlib
from srp_rfc5054 import *

## Default hash factory
DEFAULT_HASHER = hashlib.sha512

## Default gN group (generator, safe prime) tuple
DEFAULT_GROUP = gN_1024

## Default salt size
DEFAULT_SALTSIZE = 8

## Default secret (peer private value) size
DEFAULT_SECRETSIZE = 64

## Default username-password separator
DEFAULT_SEPARATOR = b':'

## Default byteorder for integer storage
DEFAULT_BYTEORDER = 'big'

## Default string encoding
DEFAULT_ENCODING = 'utf-8'

## Default integer number radix
DEFAULT_RADIX = 2

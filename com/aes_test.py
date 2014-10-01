#!/usr/bin/python #

import aes as AES
import BitVector

#Some helper functions
def newBV(val, length=8):
    if type(val) is str:
        return BitVector.BitVector(bitstring = val, size = length)
    elif type(val) is int:
        return BitVector.BitVector(intVal = val, size = length)
    return None

#Define a few values.
val1 = newBV(0x00)
val2 = newBV(0xff)
val3 = newBV(0xac)
val4 = newBV(0x9d)

exp1 = newBV(0x63)
exp2 = newBV(0x16)
exp3 = newBV(0x91)
exp4 = newBV(0x5e)

# State array.
sa = [[newBV(0x19), newBV(0x3d), newBV(0xe3), newBV(0xbe)],\
      [newBV(0xa0), newBV(0xf4), newBV(0xe2), newBV(0x2b)],\
      [newBV(0x9a), newBV(0xc6), newBV(0x8d), newBV(0x2a)],\
      [newBV(0xe9), newBV(0xf8), newBV(0x48), newBV(0x08)]]

# S-box substituted state array. 
subbedSA = [[newBV(0xd4), newBV(0x27), newBV(0x11), newBV(0xae)],\
      [newBV(0xe0), newBV(0xbf), newBV(0x98), newBV(0xf1)],\
      [newBV(0xb8), newBV(0xb4), newBV(0x5d), newBV(0xe5)],\
      [newBV(0x1e), newBV(0x41), newBV(0x52), newBV(0x30)]]

# Row shifted version of subbedSA
shiftedSA = [[newBV(0xd4), newBV(0xbf), newBV(0x5d), newBV(0x30)],\
      [newBV(0xe0), newBV(0xb4), newBV(0x52), newBV(0xae)],\
      [newBV(0xb8), newBV(0x41), newBV(0x11), newBV(0xf1)],\
      [newBV(0x1e), newBV(0x27), newBV(0x98), newBV(0xe5)]]

# Mix column-ed version of subbedSA
mixColSA = [[newBV(0x04), newBV(0x66), newBV(0x81), newBV(0xe5)],\
      [newBV(0xe0), newBV(0xcb), newBV(0x19), newBV(0x9a)],\
      [newBV(0x48), newBV(0xf8), newBV(0xd3), newBV(0x7a)],\
      [newBV(0x28), newBV(0x06), newBV(0x26), newBV(0x4c)]]


def test_sub_key_bytes():
    ''' Iterate through round-key key_word (4-byte word) performing sbox
        substitutions, returning the transformed round-key key_word '''
    # To sub root word on 4th step.
    keyVal = [val1, val2, val3, val4]
    expect = [exp1, exp2, exp3, exp4]
    actual = AES.sub_key_bytes(keyVal)
    assert actual == expect

def test_init_key_schedule():
    '''key_bv is the 128-bit input key value represented as a BitVector; return
       key_schedule as an array of (4*(1+#rounds)) 32-bit BitVector words '''
    key = AES.key_bv('2b7e151628aed2a6abf7158809cf4f3c')
    expected = \
    [AES.key_bv("2b7e1516"), AES.key_bv("28aed2a6"), AES.key_bv("abf71588"), AES.key_bv("09cf4f3c"),\
     AES.key_bv("a0fafe17"), AES.key_bv("88542cb1"), AES.key_bv("23a33939"), AES.key_bv("2a6c7605"),\
     AES.key_bv("f2c295f2"), AES.key_bv("7a96b943"), AES.key_bv("5935807a"), AES.key_bv("7359f67f"),\
     AES.key_bv("3d80477d"), AES.key_bv("4716fe3e"), AES.key_bv("1e237e44"), AES.key_bv("6d7a883b"),\
     AES.key_bv("ef44a541"), AES.key_bv("a8525b7f"), AES.key_bv("b671253b"), AES.key_bv("db0bad00"),\
     AES.key_bv("d4d1c6f8"), AES.key_bv("7c839d87"), AES.key_bv("caf2b8bc"), AES.key_bv("11f915bc"),\
     AES.key_bv("6d88a37a"), AES.key_bv("110b3efd"), AES.key_bv("dbf98641"), AES.key_bv("ca0093fd"),\
     AES.key_bv("4e54f70e"), AES.key_bv("5f5fc9f3"), AES.key_bv("84a64fb2"), AES.key_bv("4ea6dc4f"),\
     AES.key_bv("ead27321"), AES.key_bv("b58dbad2"), AES.key_bv("312bf560"), AES.key_bv("7f8d292f"),\
     AES.key_bv("ac7766f3"), AES.key_bv("19fadc21"), AES.key_bv("28d12941"), AES.key_bv("575c006e"),\
     AES.key_bv("d014f9a8"), AES.key_bv("c9ee2589"), AES.key_bv("e13f0cc8"), AES.key_bv("b6630ca6"),]
    actual = AES.init_key_schedule(key)
    assert actual == expected;

def test_add_round_key():
    ''' XOR state array sa with roundkey rk to return new state array.
        param sa is a 4x4 state array, param rk is a 4-word round key '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 40-42
    roundKey = [AES.key_bv("a0fafe17"), AES.key_bv("88542cb1"), AES.key_bv("23a33939"), AES.key_bv("2a6c7605")]
    # mixColSA with the above round key added.
    expected = [[newBV(0xa4), newBV(0x9c), newBV(0x7f), newBV(0xf2)],\
          [newBV(0x68), newBV(0x9f), newBV(0x35), newBV(0x2b)],\
          [newBV(0x6b), newBV(0x5b), newBV(0xea), newBV(0x43)],\
          [newBV(0x02), newBV(0x6a), newBV(0x50), newBV(0x49)]]
    actual = AES.add_round_key(mixColSA, roundKey)
    assert actual == expected

def test_sbox_lookup():
    ''' Given an 8-bit BitVector input, look up the sbox value corresponding
        to that byte value, returning the sbox value as an 8-bit BitVector.  '''
    act1 = AES.sbox_lookup(val1)
    act2 = AES.sbox_lookup(val2)
    act3 = AES.sbox_lookup(val3)
    act4 = AES.sbox_lookup(val4)
    
    assert act1 == exp1
    assert act2 == exp2
    assert act3 == exp3
    assert act4 == exp4

def test_inv_sbox_lookup():
    ''' Given an 8-bit BitVector input, look up the sboxinv value corresponding
        to that byte, returning the sboxinv value as an 8-bit BitVector. '''
    act1 = AES.inv_sbox_lookup(exp1)
    act2 = AES.inv_sbox_lookup(exp2)
    act3 = AES.inv_sbox_lookup(exp3)
    act4 = AES.inv_sbox_lookup(exp4)

    assert act1 == val1
    assert act2 == val2
    assert act3 == val3
    assert act4 == val4

def test_sub_bytes():
    ''' Iterate throught state array sa to perform sbox substitution 
    returning new state array. '''
    actual = AES.sub_bytes(sa)
    assert subbedSA == actual

def test_inv_sub_bytes():
    ''' Iterate throught state array sa to perform inv-sbox substitution 
    returning new state array. '''
    actual = AES.inv_sub_bytes(subbedSA)
    assert sa == actual # Python does nested equality on lists.

def test_shift_bytes_left():
    ''' Return the value of BitVector bv after rotating it to the left
        by num bytes'''
    bitVector = newBV(0xff00, 16)
    expect = newBV(0x00ff, 16)
    actual = AES.shift_bytes_left(bitVector, 1)
    assert actual == expect

def test_shift_bytes_right():
    ''' Return the value of BitVector bv after rotating it to the right
        by num bytes'''
    bitVector = newBV(0x00ff, 16)
    expect = newBV(0xff00, 16)
    actual = AES.shift_bytes_right(BitVector, 1)
    assert actual == expect

def test_shift_rows():
    ''' shift rows in state array sa to return new state array '''
    actual = AES.shift_rows(subbedSA)
    assert actual == shiftedSA

def test_inv_shift_rows():
    ''' shift rows on state array sa to return new state array '''
    actual = AES.inv_shift_rows(shiftedSA)
    assert subbedSA == actual

def test_gf_mult():
    ''' Used by mix_columns and inv_mix_columns to perform multiplication in
    GF(2^8).  param bv is an 8-bit BitVector, param factor is an integer.
        returns an 8-bit BitVector, whose value is bv*factor in GF(2^8) '''
    bitVector = newBV(0x87)
    factor = 0x02
    expected = newBV(0x15)
    actual = AES.gf_mult(bitVector, factor)
    assert expected == actual

def test_mix_columns():
    ''' Mix columns on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 33-35   
    actual = AES.mix_columns(subbedSA)
    assert mixColSA == actual

def test_inv_mix_columns():
    ''' Inverse mix columns on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDE 36  
    actual = AES.inv_mix_columns(mixColSA)
    assert subbedSA == mixColSA
  
def test_encrypt():
    ''' perform AES encryption using 128-bit hex_key on 128-bit plaintext 
        hex_plaintext, where both key and plaintext values are expressed
    in hexadecimal string notation. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 14-15
    assert False

def test_decrypt():
    ''' perform AES decryption using 128-bit hex_key on 128-bit ciphertext
           hex_ciphertext, where both key and ciphertext values are expressed
    in hexadecimal string notation. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 14-15
    # ADD YOUR CODE HERE - SEE LEC SLIDES 14-15
    assert False

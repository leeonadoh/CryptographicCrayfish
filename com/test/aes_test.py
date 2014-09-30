#!/usr/bin/python #

import com.src.aes.*
import BitVector

#Some helper functions
def newBV(val):
    if type(val) is str:
        return BitVector.BitVector(bitstring = val)
    elif type(val) is int
        return BitVector.BitVector(intVal = val)
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
sa = [[newBV(0x00), newBV(0x12), newBV(0x23), newBV(0xa5)],\
      [newBV(0xad), newBV(0xc4), newBV(0xbb), newBV(0xff)],\
      [newBV(0xbc), newBV(0x34), newBV(0xaf), newBV(0xd3)],\
      [newBV(0x98), newBV(0x7d), newBV(0x52), newBV(0x26)]]
# S-box substituted state array. 
subbedSA = [[newBV(0x63), newBV(0xc9), newBV(0x26), newBV(0x06)],\
      [newBV(0x95), newBV(0x1c), newBV(0xea), newBV(0x16)],\
      [newBV(0x65), newBV(0x18), newBV(0x79), newBV(0x66)],\
      [newBV(0x46), newBV(0xff), newBV(0x00), newBV(0xf7)]]

shiftedSA = [[newBV(0x00), newBV(0x12), newBV(0x23), newBV(0xa5)],\
      [newBV(0xc4), newBV(0xbb), newBV(0xff), newBV(0xad)],\
      [newBV(0xaf), newBV(0xd3), newBV(0xbc), newBV(0x34)],\
      [newBV(0x26), newBV(0x98), newBV(0x7d), newBV(0x52)]]

def test_sub_key_bytes():
    ''' Iterate through round-key key_word (4-byte word) performing sbox
        substitutions, returning the transformed round-key key_word '''
    # To sub root word on 4th step.
    keyVal = [val1, val2, val3, val4]
    expect = [exp1, exp2, exp3, exp4]
    actual = sub_key_bytes(keyVal)
    assert actual == expect

def test_init_key_schedule():
    '''key_bv is the 128-bit input key value represented as a BitVector; return
       key_schedule as an array of (4*(1+#rounds)) 32-bit BitVector words '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 44-47  
    assert False

def test_add_round_key():
    ''' XOR state array sa with roundkey rk to return new state array.
        param sa is a 4x4 state array, param rk is a 4-word round key '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 40-42  
    assert False

def test_sbox_lookup():
    ''' Given an 8-bit BitVector input, look up the sbox value corresponding
        to that byte value, returning the sbox value as an 8-bit BitVector.  '''
    act1 = sbox_lookup(val1)
    act2 = sbox_lookup(val2)
    act3 = sbox_lookup(val3)
    act4 = sbox_lookup(val4)
    
    assert act1 == exp1
    assert act2 == exp2
    assert act3 == exp3
    assert act4 == exp4

def test_inv_sbox_lookup():
    ''' Given an 8-bit BitVector input, look up the sboxinv value corresponding
        to that byte, returning the sboxinv value as an 8-bit BitVector. '''
    act1 = inv_sbox_lookup(exp1)
    act2 = inv_sbox_lookup(exp2)
    act3 = inv_sbox_lookup(exp3)
    act4 = inv_sbox_lookup(exp4)

    assert act1 == val1
    assert act2 == val2
    assert act3 == val3
    assert act4 == val4

def test_sub_bytes():
    ''' Iterate throught state array sa to perform sbox substitution 
    returning new state array. '''
    actual = sub_bytes(sa)
    assert subbedSA == actual

def test_inv_sub_bytes():
    ''' Iterate throught state array sa to perform inv-sbox substitution 
    returning new state array. '''
    actual = inv_sub_bytes(subbedSA)
    assert sa == actual # Python does nested equality on lists.

def test_shift_bytes_left():
    ''' Return the value of BitVector bv after rotating it to the left
        by num bytes'''
    bitVector = newBV(0xff00)
    expect = newBV(0x00ff)
    actual = shift_bytes_left(bitVector)
    assert actual == expect

def test_shift_bytes_right():
    ''' Return the value of BitVector bv after rotating it to the right
        by num bytes'''
    bitVector = newBV(0x00ff)
    expect = newBV(0xff00)
    actual = shift_bytes_right(BitVector)
    assert actual == expect

def test_shift_rows():
    ''' shift rows in state array sa to return new state array '''
    actual = shift_rows(sa)
    assert actual == shiftedSA

def test_inv_shift_rows():
    ''' shift rows on state array sa to return new state array '''
    actaul = inv_shift_rows(shiftedSA)
    assert sa == actual

def test_gf_mult():
    ''' Used by mix_columns and inv_mix_columns to perform multiplication in
    GF(2^8).  param bv is an 8-bit BitVector, param factor is an integer.
        returns an 8-bit BitVector, whose value is bv*factor in GF(2^8) '''
    bitVector = newBV(0x87)
    factor = 0x02
    expected = newBV(0x15)
    actual = gf_mult(bitVector, factor)
    assert expected == actual

def test_mix_columns():
    ''' Mix columns on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 33-35   
    assert False

def test_inv_mix_columns():
    ''' Inverse mix columns on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDE 36  
    assert False
  
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

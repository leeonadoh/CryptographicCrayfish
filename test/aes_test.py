#!/usr/bin/python #

import aes
import BitVector

def test_sub_key_bytes():
    ''' Iterate through round-key key_word (4-byte word) performing sbox
        substitutions, returning the transformed round-key key_word '''
    key_word = ['00', 'ff', 'a4', 'cb']
	expected = ['63', '16', '49', '1f']
	actual = aes.sub_key_bytes(key_word)

def test_init_key_schedule():
    '''key_bv is the 128-bit input key value represented as a BitVector; return
       key_schedule as an array of (4*(1+#rounds)) 32-bit BitVector words '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 44-47  
    assert fail

def test_add_round_key():
    ''' XOR state array sa with roundkey rk to return new state array.
        param sa is a 4x4 state array, param rk is a 4-word round key '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 40-42  
    assert fail

def test_sbox_lookup():
    ''' Given an 8-bit BitVector input, look up the sbox value corresponding
        to that byte value, returning the sbox value as an 8-bit BitVector.  '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 18-20  
    assert fail

def test_inv_sbox_lookup():
    ''' Given an 8-bit BitVector input, look up the sboxinv value corresponding
        to that byte, returning the sboxinv value as an 8-bit BitVector. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 18-20   
    assert fail

def test_sub_bytes():
    ''' Iterate throught state array sa to perform sbox substitution 
	returning new state array. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 18-20   
    assert fail

def test_inv_sub_bytes():
    ''' Iterate throught state array sa to perform inv-sbox substitution 
	returning new state array. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 18-20   
    assert fail

def test_shift_bytes_left():
    ''' Return the value of BitVector bv after rotating it to the left
        by num bytes'''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 30-32   
    assert fail

def test_shift_bytes_right():
    ''' Return the value of BitVector bv after rotating it to the right
        by num bytes'''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 30-32  
    assert fail

def test_shift_rows():
    ''' shift rows in state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 30-32  
    assert fail

def test_inv_shift_rows():
    ''' shift rows on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 30-32   
    assert fail

def test_gf_mult():
    ''' Used by mix_columns and inv_mix_columns to perform multiplication in
	GF(2^8).  param bv is an 8-bit BitVector, param factor is an integer.
        returns an 8-bit BitVector, whose value is bv*factor in GF(2^8) '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 33-36
    assert fail

def test_mix_columns():
    ''' Mix columns on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 33-35   
    assert fail

def test_inv_mix_columns():
    ''' Inverse mix columns on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDE 36  
    assert fail
  
def test_encrypt():
    ''' perform AES encryption using 128-bit hex_key on 128-bit plaintext 
        hex_plaintext, where both key and plaintext values are expressed
	in hexadecimal string notation. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 14-15
    assert fail

def test_decrypt():
    ''' perform AES decryption using 128-bit hex_key on 128-bit ciphertext
       	hex_ciphertext, where both key and ciphertext values are expressed
	in hexadecimal string notation. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 14-15
    # ADD YOUR CODE HERE - SEE LEC SLIDES 14-15
    assert fail

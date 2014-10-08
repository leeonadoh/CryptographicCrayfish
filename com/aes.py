#!/usr/bin/python #

''' Compiler/OS Used: cygwin Win7
    Sources Used: BitVector documentation, NIST AES-spec appendix for tests
'''

import sys
import BitVector
import binascii

rounds = 10  # 128-bit AES uses 10 rounds

''' S-box for use in encryption '''
sbox = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
       [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
       [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
       [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
       [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
       [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
       [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
       [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
       [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
       [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
       [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
       [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
       [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
       [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
       [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
       [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

''' inverse S-box for use in decryption '''
sboxinv = [[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
          [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
          [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
          [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
          [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
          [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
          [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
          [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
          [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
          [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
          [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
          [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
          [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
          [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
          [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
          [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]

''' rcon is a table of round constants used to compute the key schedule '''
rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
        0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39,
        0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a,
        0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8,
        0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef,
        0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc,
        0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b,
        0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
        0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94,
        0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20,
        0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35,
        0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f,
        0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
        0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63,
        0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd,
        0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb]

gfMatrix = [[2, 3, 1, 1],\
            [1, 2, 3, 1],\
            [1, 1, 2, 3],\
            [3, 1, 1, 2]]
invGfMatrix = [[14, 11, 13, 9],\
               [9, 14, 11, 13],\
               [13, 9, 14, 11],\
               [11, 13, 9, 14]]

''' HELPER functions (you are free to use or ignore these)'''

def bv_hex_str(bv):
    ''' DEBUG HELPER to convert BitVector value bv to a hex string '''
    cstr = ""
    for n in range((len(bv)/8)):
        c = chr(bv[n*8:n*8+8].intValue())
    cstr += c
    return binascii.hexlify(cstr)

def print_state(state_array, label = " "):
    ''' DEBUG HELPER to print a state_array, optionally with a label '''
    for col in state_array:
        psa = ""
        for row in col:
            psa += bv_hex_str(row)
            print psa,
    print label

def state_str(state_array):
    ''' DEBUG HELPER to convert a state_array value to a hex string '''
    psa = ""
    for col in state_array:
        for row in col:
            psa += bv_hex_str(row)
    return psa

def key_str(round_key):
    ''' DEBUG HELPER to convert a list of round key words to a hex string '''
    kstr = ""
    for word in round_key:
        kstr += bv_hex_str(word)
    return kstr

def key_to_bv(hex_key):
    ''' HELPER to convert a hex-string representation of a key to the
        equivalent BitVector value '''
    keybytes = binascii.a2b_hex(hex_key)  # hex string to byte string
    key_bv = BitVector.BitVector(size = 0) # initialize BitVector
    for byte in keybytes: 
        byte_bv = BitVector.BitVector(intVal=ord(byte), size=8) # one byte to add to BitVector
        key_bv += byte_bv # catenate new BitVector byte onto return value
    return key_bv

def init_state_array(bv):
    ''' Return a state array corresponding to 128-bit BitVector param bv,
        where the state array is a column-ordered array (list) of 16 8-bit
    BitVector values, organized as 4 columns (sublists) each containing
    4 8-bit BitVector bytes, as shown on slide #17 '''
    output = []
    for i in range(4):
        col = []
        for j in range(4):
            col.append(bv[(i*32)+(j*8):(i*32)+(j*8)+8])
        output.append(col)
    return output


def sub_key_bytes(key_word):
    ''' Iterate through round-key key_word (4-byte word) performing sbox
        substitutions, returning the transformed round-key key_word '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 44-47
    # Modified to convert whole 32 bit words instead of a list of 4 x 8 bits.
    subbedKey = sbox_lookup(key_word[0:8]) + sbox_lookup(key_word[8:16]) +\
                sbox_lookup(key_word[16:24]) + sbox_lookup(key_word[24:32])
    return subbedKey
    

def init_key_schedule(key_bv):
    '''key_bv is the 128-bit input key value represented as a BitVector; return
       key_schedule as an array of (4*(1+#rounds)) 32-bit BitVector words '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 44-47
    
    key_schedule = [key_bv[0:32], key_bv[32:64], key_bv[64:96], key_bv[96:128]]

    for r in range(rounds):
        # compute word4
        word4 = key_schedule[-1].deep_copy() # ensure its a copy, not a reference.
        word4 = shift_bytes_left(word4, 1) # RotWord by 1 byte

        # Sub bytes
        word4 = sub_key_bytes(word4)
        
        # XOR 4th previous and rcon
        word4 = key_schedule[-4] ^ word4 
        rcb = BitVector.BitVector(intVal = rcon[r + 1], size = 8)
        rcb.pad_from_right(24)
        word4 = word4 ^ rcb
        key_schedule.append(word4)
    
        # compute word5 to word7 and add to round-key
        for i in range(3):
            key_schedule.append(key_schedule[-1] ^ key_schedule[-4])
        
    return key_schedule

def add_round_key(sa, rk):
    ''' XOR state array sa with roundkey rk to return new state array.
        param sa is a 4x4 state array, param rk is a 4-word round key '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 40-42

    # Convert rk from 4 x 32bit words to 4x4 matrix of 8 bit hex.
    # Will still have each nested array as columns instead of rows to match
    # the sa. 
    convertedRK = []
    for bitV in rk:
        convertedRK.append([bitV[0: 8], bitV[8: 16], bitV[16: 24], bitV[24: 32]])
    
    new_sa = []  # new output state
    for i in range(len(sa)):  # iterate columns
        col = []   # new column
        for j in range(len(sa[i])):   # iterate rows
            some_val = sa[i][j] ^ convertedRK[i][j]
            col.append(some_val)  # insert XOR result into col
        new_sa.append(col)  # insert new col into result state_array
    return new_sa

def sbox_lookup(input):
    ''' Given an 8-bit BitVector input, look up the sbox value corresponding
        to that byte value, returning the sbox value as an 8-bit BitVector.  '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 18-20  
    row = int(input[0:4])
    col = int(input[4:8])
    # convert to BitVector 
    return BitVector.BitVector(intVal = sbox[row][col], size = 8) 

def inv_sbox_lookup(input):
    ''' Given an 8-bit BitVector input, look up the sboxinv value corresponding
        to that byte, returning the sboxinv value as an 8-bit BitVector. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 18-20   
    row = int(input[0:4])
    col = int(input[4:8])
    # convert to BitVector
    return BitVector.BitVector(intVal = sboxinv[row][col], size = 8) 

def sub_bytes(sa):
    ''' Iterate throught state array sa to perform sbox substitution 
    returning new state array. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 18-20   
    for i in range(len(sa)):
        for j in range(len(sa[0])):
            sa[i][j] = sbox_lookup(sa[i][j])
    return sa

def inv_sub_bytes(sa):
    ''' Iterate throught state array sa to perform inv-sbox substitution 
    returning new state array. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 18-20   
    for i in range(len(sa)):
        for j in range(len(sa[0])):
            sa[i][j] = inv_sbox_lookup(sa[i][j])
    return sa

def shift_bytes_left(bv, num):
    ''' Return the value of BitVector bv after rotating it to the left
        by num bytes'''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 30-32
    return bv.__lshift__(8 * num)

def shift_bytes_right(bv, num):
    ''' Return the value of BitVector bv after rotating it to the right
        by num bytes'''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 30-32  
    return bv.__rshift__(8 * num)

def shift_rows(sa):
    ''' shift rows in state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 30-32  

    for i in range(len(sa)):  # number of columns
        bv = sa[0][i] + sa[1][i] + sa[2][i] + sa[3][i]
        bv = shift_bytes_left(bv, i)
        sa[0][i] = bv[0:8]
        sa[1][i] = bv[8:16]
        sa[2][i] = bv[16:24]
        sa[3][i] = bv[24:32]
    
    return sa

def inv_shift_rows(sa):
    ''' shift rows on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 30-32   
    for i in range(len(sa)):  # number of columns
        bv = sa[0][i] + sa[1][i] + sa[2][i] + sa[3][i]
        bv = shift_bytes_right(bv, i)
        sa[0][i] = bv[0:8]
        sa[1][i] = bv[8:16]
        sa[2][i] = bv[16:24]
        sa[3][i] = bv[24:32]
    
    return sa

def gf_mult(bv, factor):
    ''' Used by mix_columns and inv_mix_columns to perform multiplication in
    GF(2^8).  param bv is an 8-bit BitVector, param factor is an integer.
        returns an 8-bit BitVector, whose value is bv*factor in GF(2^8) '''
    # Rijndael finite field algorithm used is documented here: 
    # https://en.wikipedia.org/wiki/Finite_field_arithmetic#Rijndael.27s_finite_field
    bvNum = bv.deep_copy()
    bvFac = BitVector.BitVector(intVal = factor, size = 8)
    prod = BitVector.BitVector(intVal = 0, size = 8)
    gfConst = BitVector.BitVector(intVal = 0x1b, size = 8)

    has8thBit = False
    for i in range(8):
        if bvFac[7]:
            prod = prod ^ bvNum
        has8thBit = bvNum[0]
        bvNum << 1
        bvNum[7] = 0
        if has8thBit:
            bvNum = bvNum ^ gfConst
        bvFac >> 1
        bvFac[0] = 0
    return prod

def mix_columns(sa):
    ''' Mix columns on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 33-35   
    newsa = []  # result state-array

    for saCol in sa:
        # for each column in state array, mutiply it with gf matrix.
        # initalize a list containing the new bytes for the column.
        newCol = []
        for gfRow in gfMatrix:
            # initialize a zero byte to accumulate additions (xors)
            newByte = BitVector.BitVector(intVal = 0, size = 8)
            for saByte, factor in zip(saCol, gfRow):
                # for each element in the state array column, and each 
                # factor in the gf matrix row, multiply them, and accumulate
                # onto newByte.
                newByte = newByte ^ gf_mult(saByte, factor)
            # append it to the new column.
            newCol.append(newByte);
        # append mixed column to newsa
        newsa.append(newCol)
    # end of for loop
    return newsa

def inv_mix_columns(sa):
    ''' Inverse mix columns on state array sa to return new state array '''
    # ADD YOUR CODE HERE - SEE LEC SLIDE 36  
    newsa = []  # result state-array

    for saCol in sa:
        # for each column in state array, mutiply it with gf matrix.
        # initalize a list containing the new bytes for the column.
        newCol = []
        for invGfRow in invGfMatrix:
            # initialize a zero byte to accumulate additions (xors)
            newByte = BitVector.BitVector(intVal = 0, size = 8)
            for saByte, factor in zip(saCol, invGfRow):
                # for each element in the state array column, and each 
                # factor in the gf matrix row, multiply them, and accumulate
                # onto newByte.
                newByte = newByte ^ gf_mult(saByte, factor)
            # append it to the new column.
            newCol.append(newByte);
        # append mixed column to newsa
        newsa.append(newCol)
    # end of for loop
    return newsa
  
def encrypt(hex_key, hex_plaintext):
    ''' perform AES encryption using 128-bit hex_key on 128-bit plaintext 
        hex_plaintext, where both key and plaintext values are expressed
    in hexadecimal string notation. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 14-15
    pass

def decrypt(hex_key, hex_ciphertext):
    ''' perform AES decryption using 128-bit hex_key on 128-bit ciphertext
        hex_ciphertext, where both key and ciphertext values are expressed
    in hexadecimal string notation. '''
    # ADD YOUR CODE HERE - SEE LEC SLIDES 14-15
    pass


if __name__ == "__main__":
    # test key from AES-Spec Appendix B
    NIST_test_key = '2b7e151628aed2a6abf7158809cf4f3c'
    
    # plaintext test-value from AES-Spec Appendix B 
    NIST_test_plaintext = '3243f6a8885a308d313198a2e0370734'
    
    # input-to-round-1 value from AES-Spec Appendix B 
    NIST_input_round_1 = '193de3bea0f4e22b9ac68d2ae9f84808'
    x = key_to_bv(NIST_test_key)
    key_schedule = init_key_schedule(x)    

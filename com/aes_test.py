#!/usr/bin/python #

import aes as AES
import BitVector
import copy 
import nose

#Some helper functions
def newBV(val, length=8):
    if type(val) is str:
        return BitVector.BitVector(bitstring = val, size = length)
    elif type(val) is int:
        return BitVector.BitVector(intVal = val, size = length)
    return None

def test_sub_key_bytes():
    ''' Iterate through round-key key_word (4-byte word) performing sbox
        substitutions, returning the transformed round-key key_word '''
    # To sub root word on 4th step.
    keyVal = AES.key_to_bv("19a09ae9")
    expect = AES.key_to_bv("d4e0b81e")
    actual = AES.sub_key_bytes(keyVal)
    assert actual == expect

    keyVal = AES.key_to_bv("a4686b02")
    expect = AES.key_to_bv("49457f77")
    actual = AES.sub_key_bytes(keyVal)
    assert actual == expect

    keyVal = AES.key_to_bv("61dde3ef")
    expect = AES.key_to_bv("efc111df")
    actual = AES.sub_key_bytes(keyVal)
    assert actual == expect

def test_init_key_schedule():
    '''key_bv is the 128-bit input key value represented as a BitVector; return
       key_schedule as an array of (4*(1+#rounds)) 32-bit BitVector words '''
    key = AES.key_to_bv('2b7e151628aed2a6abf7158809cf4f3c')
    expected = \
    [AES.key_to_bv("2b7e1516"), AES.key_to_bv("28aed2a6"), AES.key_to_bv("abf71588"), AES.key_to_bv("09cf4f3c"),\
     AES.key_to_bv("a0fafe17"), AES.key_to_bv("88542cb1"), AES.key_to_bv("23a33939"), AES.key_to_bv("2a6c7605"),\
     AES.key_to_bv("f2c295f2"), AES.key_to_bv("7a96b943"), AES.key_to_bv("5935807a"), AES.key_to_bv("7359f67f"),\
     AES.key_to_bv("3d80477d"), AES.key_to_bv("4716fe3e"), AES.key_to_bv("1e237e44"), AES.key_to_bv("6d7a883b"),\
     AES.key_to_bv("ef44a541"), AES.key_to_bv("a8525b7f"), AES.key_to_bv("b671253b"), AES.key_to_bv("db0bad00"),\
     AES.key_to_bv("d4d1c6f8"), AES.key_to_bv("7c839d87"), AES.key_to_bv("caf2b8bc"), AES.key_to_bv("11f915bc"),\
     AES.key_to_bv("6d88a37a"), AES.key_to_bv("110b3efd"), AES.key_to_bv("dbf98641"), AES.key_to_bv("ca0093fd"),\
     AES.key_to_bv("4e54f70e"), AES.key_to_bv("5f5fc9f3"), AES.key_to_bv("84a64fb2"), AES.key_to_bv("4ea6dc4f"),\
     AES.key_to_bv("ead27321"), AES.key_to_bv("b58dbad2"), AES.key_to_bv("312bf560"), AES.key_to_bv("7f8d292f"),\
     AES.key_to_bv("ac7766f3"), AES.key_to_bv("19fadc21"), AES.key_to_bv("28d12941"), AES.key_to_bv("575c006e"),\
     AES.key_to_bv("d014f9a8"), AES.key_to_bv("c9ee2589"), AES.key_to_bv("e13f0cc8"), AES.key_to_bv("b6630ca6")]
    actual = AES.init_key_schedule(key)
    assert actual == expected;

    key = AES.key_to_bv("00000000000000000000000000000000")
    expected = \
    [AES.key_to_bv("00000000"), AES.key_to_bv("00000000"), AES.key_to_bv("00000000"), AES.key_to_bv("00000000"),\
     AES.key_to_bv("62636363"), AES.key_to_bv("62636363"), AES.key_to_bv("62636363"), AES.key_to_bv("62636363"),\
     AES.key_to_bv("9b9898c9"), AES.key_to_bv("f9fbfbaa"), AES.key_to_bv("9b9898c9"), AES.key_to_bv("f9fbfbaa"),\
     AES.key_to_bv("90973450"), AES.key_to_bv("696ccffa"), AES.key_to_bv("f2f45733"), AES.key_to_bv("0b0fac99"),\
     AES.key_to_bv("ee06da7b"), AES.key_to_bv("876a1581"), AES.key_to_bv("759e42b2"), AES.key_to_bv("7e91ee2b"),\
     AES.key_to_bv("7f2e2b88"), AES.key_to_bv("f8443e09"), AES.key_to_bv("8dda7cbb"), AES.key_to_bv("f34b9290"),\
     AES.key_to_bv("ec614b85"), AES.key_to_bv("1425758c"), AES.key_to_bv("99ff0937"), AES.key_to_bv("6ab49ba7"),\
     AES.key_to_bv("21751787"), AES.key_to_bv("3550620b"), AES.key_to_bv("acaf6b3c"), AES.key_to_bv("c61bf09b"),\
     AES.key_to_bv("0ef90333"), AES.key_to_bv("3ba96138"), AES.key_to_bv("97060a04"), AES.key_to_bv("511dfa9f"),\
     AES.key_to_bv("b1d4d8e2"), AES.key_to_bv("8a7db9da"), AES.key_to_bv("1d7bb3de"), AES.key_to_bv("4c664941"),\
     AES.key_to_bv("b4ef5bcb"), AES.key_to_bv("3e92e211"), AES.key_to_bv("23e951cf"), AES.key_to_bv("6f8f188e")]
    actual = AES.init_key_schedule(key)
    assert actual == expected

    key = AES.key_to_bv("ffffffffffffffffffffffffffffffff")
    expected = \
    [AES.key_to_bv("ffffffff"), AES.key_to_bv("ffffffff"), AES.key_to_bv("ffffffff"), AES.key_to_bv("ffffffff"),\
     AES.key_to_bv("e8e9e9e9"), AES.key_to_bv("17161616"), AES.key_to_bv("e8e9e9e9"), AES.key_to_bv("17161616"),\
     AES.key_to_bv("adaeae19"), AES.key_to_bv("bab8b80f"), AES.key_to_bv("525151e6"), AES.key_to_bv("454747f0"),\
     AES.key_to_bv("090e2277"), AES.key_to_bv("b3b69a78"), AES.key_to_bv("e1e7cb9e"), AES.key_to_bv("a4a08c6e"),\
     AES.key_to_bv("e16abd3e"), AES.key_to_bv("52dc2746"), AES.key_to_bv("b33becd8"), AES.key_to_bv("179b60b6"),\
     AES.key_to_bv("e5baf3ce"), AES.key_to_bv("b766d488"), AES.key_to_bv("045d3850"), AES.key_to_bv("13c658e6"),\
     AES.key_to_bv("71d07db3"), AES.key_to_bv("c6b6a93b"), AES.key_to_bv("c2eb916b"), AES.key_to_bv("d12dc98d"),\
     AES.key_to_bv("e90d208d"), AES.key_to_bv("2fbb89b6"), AES.key_to_bv("ed5018dd"), AES.key_to_bv("3c7dd150"),\
     AES.key_to_bv("96337366"), AES.key_to_bv("b988fad0"), AES.key_to_bv("54d8e20d"), AES.key_to_bv("68a5335d"),\
     AES.key_to_bv("8bf03f23"), AES.key_to_bv("3278c5f3"), AES.key_to_bv("66a027fe"), AES.key_to_bv("0e0514a3"),\
     AES.key_to_bv("d60a3588"), AES.key_to_bv("e472f07b"), AES.key_to_bv("82d2d785"), AES.key_to_bv("8cd7c326")]
    actual = AES.init_key_schedule(key)
    assert actual == expected

def test_add_round_key():
    ''' XOR state array sa with roundkey rk to return new state array.
        param sa is a 4x4 state array, param rk is a 4-word round key '''
    stateArr = [[newBV(0x04), newBV(0x66), newBV(0x81), newBV(0xe5)], \
                [newBV(0xe0), newBV(0xcb), newBV(0x19), newBV(0x9a)], \
                [newBV(0x48), newBV(0xf8), newBV(0xd3), newBV(0x7a)], \
                [newBV(0x28), newBV(0x06), newBV(0x26), newBV(0x4c)]]
    roundKey = [AES.key_to_bv("a0fafe17"), AES.key_to_bv("88542cb1"), AES.key_to_bv("23a33939"), AES.key_to_bv("2a6c7605")]
    expected = [[newBV(0xa4), newBV(0x9c), newBV(0x7f), newBV(0xf2)],\
                [newBV(0x68), newBV(0x9f), newBV(0x35), newBV(0x2b)],\
                [newBV(0x6b), newBV(0x5b), newBV(0xea), newBV(0x43)],\
                [newBV(0x02), newBV(0x6a), newBV(0x50), newBV(0x49)]]
    actual = AES.add_round_key(stateArr, roundKey)
    assert actual == expected

    stateArr = [[newBV(0x58), newBV(0x4d), newBV(0xca), newBV(0xf1)], \
                [newBV(0x1b), newBV(0x4b), newBV(0x5a), newBV(0xac)], \
                [newBV(0xdb), newBV(0xe7), newBV(0xca), newBV(0xa8)], \
                [newBV(0x1b), newBV(0x6b), newBV(0xb0), newBV(0xe5)]]
    roundKey = [AES.key_to_bv("f2c295f2"), AES.key_to_bv("7a96b943"), AES.key_to_bv("5935807a"), AES.key_to_bv("7359f67f")]
    expected = [[newBV(0xaa), newBV(0x8f), newBV(0x5f), newBV(0x03)], \
                [newBV(0x61), newBV(0xdd), newBV(0xe3), newBV(0xef)], \
                [newBV(0x82), newBV(0xd2), newBV(0x4a), newBV(0xd2)], \
                [newBV(0x68), newBV(0x32), newBV(0x46), newBV(0x9a)]]
    actual = AES.add_round_key(stateArr, roundKey)
    assert actual == expected

    stateArr = [[newBV(0x75), newBV(0xec), newBV(0x09), newBV(0x93)], \
                [newBV(0x20), newBV(0x0b), newBV(0x63), newBV(0x33)], \
                [newBV(0x53), newBV(0xc0), newBV(0xcf), newBV(0x7c)], \
                [newBV(0xbb), newBV(0x25), newBV(0xd0), newBV(0xdc)]]
    roundKey = [AES.key_to_bv("3d80477d"), AES.key_to_bv("4716fe3e"), AES.key_to_bv("1e237e44"), AES.key_to_bv("6d7a883b")]
    expected = [[newBV(0x48), newBV(0x6c), newBV(0x4e), newBV(0xee)], \
                [newBV(0x67), newBV(0x1d), newBV(0x9d), newBV(0x0d)], \
                [newBV(0x4d), newBV(0xe3), newBV(0xb1), newBV(0x38)], \
                [newBV(0xd6), newBV(0x5f), newBV(0x58), newBV(0xe7)]]
    actual = AES.add_round_key(stateArr, roundKey)
    AES.print_state(expected)
    AES.print_state(actual)
    assert actual == expected

def test_sbox_lookup():
    ''' Given an 8-bit BitVector input, look up the sbox value corresponding
        to that byte value, returning the sbox value as an 8-bit BitVector.  '''
    actual = AES.sbox_lookup(newBV(0x00))
    expect = newBV(0x63)
    assert actual == expect

    actual = AES.sbox_lookup(newBV(0xff))
    expect = newBV(0x16)
    assert actual == expect

    actual = AES.sbox_lookup(newBV(0xac))
    expect = newBV(0x91)
    assert actual == expect

    actual = AES.sbox_lookup(newBV(0x9d))
    expect = newBV(0x5e)
    assert actual == expect

def test_inv_sbox_lookup():
    ''' Given an 8-bit BitVector input, look up the sboxinv value corresponding
        to that byte, returning the sboxinv value as an 8-bit BitVector. '''
    expect = AES.sbox_lookup(newBV(0x00))
    actual = newBV(0x63)
    assert actual == expect

    expect = AES.sbox_lookup(newBV(0xff))
    actual = newBV(0x16)
    assert actual == expect

    expect = AES.sbox_lookup(newBV(0xac))
    actual = newBV(0x91)
    assert actual == expect

    expect = AES.sbox_lookup(newBV(0x9d))
    actual = newBV(0x5e)
    assert actual == expect

def test_sub_bytes():
    ''' Iterate throught state array sa to perform sbox substitution 
    returning new state array. '''
    stateArr = [[newBV(0xaa), newBV(0x8f), newBV(0x5f), newBV(0x03)], \
                [newBV(0x61), newBV(0xdd), newBV(0xe3), newBV(0xef)], \
                [newBV(0x82), newBV(0xd2), newBV(0x4a), newBV(0xd2)], \
                [newBV(0x68), newBV(0x32), newBV(0x46), newBV(0x9a)]]
    expected = [[newBV(0xac), newBV(0x73), newBV(0xcf), newBV(0x7b)], \
                [newBV(0xef), newBV(0xc1), newBV(0x11), newBV(0xdf)], \
                [newBV(0x13), newBV(0xb5), newBV(0xd6), newBV(0xb5)], \
                [newBV(0x45), newBV(0x23), newBV(0x5a), newBV(0xb8)]]
    actual = AES.sub_bytes(stateArr)
    assert expected == actual

    stateArr = [[newBV(0x48), newBV(0x67), newBV(0x4d), newBV(0xd6)], \
                [newBV(0x6c), newBV(0x1d), newBV(0xe3), newBV(0x5f)], \
                [newBV(0x4e), newBV(0x9d), newBV(0xb1), newBV(0x58)], \
                [newBV(0xee), newBV(0x0d), newBV(0x38), newBV(0xe7)]]
    expected = [[newBV(0x52), newBV(0x85), newBV(0xe3), newBV(0xf6)], \
                [newBV(0x50), newBV(0xa4), newBV(0x11), newBV(0xcf)], \
                [newBV(0x2f), newBV(0x5e), newBV(0xc8), newBV(0x6a)], \
                [newBV(0x28), newBV(0xd7), newBV(0x07), newBV(0x94)]]
    actual = AES.sub_bytes(stateArr)
    assert expected == actual

    stateArr = [[newBV(0xe0), newBV(0xc8), newBV(0xd9), newBV(0x85)], \
                [newBV(0x92), newBV(0x63), newBV(0xb1), newBV(0xb8)], \
                [newBV(0x7f), newBV(0x63), newBV(0x35), newBV(0xbe)], \
                [newBV(0xe8), newBV(0xc0), newBV(0x50), newBV(0x01)]]
    expected = [[newBV(0xe1), newBV(0xe8), newBV(0x35), newBV(0x97)], \
                [newBV(0x4f), newBV(0xfb), newBV(0xc8), newBV(0x6c)], \
                [newBV(0xd2), newBV(0xfb), newBV(0x96), newBV(0xae)], \
                [newBV(0x9b), newBV(0xba), newBV(0x53), newBV(0x7c)]]
    actual = AES.sub_bytes(stateArr)
    assert expected == actual

def test_inv_sub_bytes():
    ''' Iterate throught state array sa to perform inv-sbox substitution 
    returning new state array. '''
    expected = [[newBV(0xaa), newBV(0x8f), newBV(0x5f), newBV(0x03)], \
                [newBV(0x61), newBV(0xdd), newBV(0xe3), newBV(0xef)], \
                [newBV(0x82), newBV(0xd2), newBV(0x4a), newBV(0xd2)], \
                [newBV(0x68), newBV(0x32), newBV(0x46), newBV(0x9a)]]
    stateArr = [[newBV(0xac), newBV(0x73), newBV(0xcf), newBV(0x7b)], \
                [newBV(0xef), newBV(0xc1), newBV(0x11), newBV(0xdf)], \
                [newBV(0x13), newBV(0xb5), newBV(0xd6), newBV(0xb5)], \
                [newBV(0x45), newBV(0x23), newBV(0x5a), newBV(0xb8)]]
    actual = AES.inv_sub_bytes(stateArr)
    assert expected == actual

    expected = [[newBV(0x48), newBV(0x67), newBV(0x4d), newBV(0xd6)], \
                [newBV(0x6c), newBV(0x1d), newBV(0xe3), newBV(0x5f)], \
                [newBV(0x4e), newBV(0x9d), newBV(0xb1), newBV(0x58)], \
                [newBV(0xee), newBV(0x0d), newBV(0x38), newBV(0xe7)]]
    stateArr = [[newBV(0x52), newBV(0x85), newBV(0xe3), newBV(0xf6)], \
                [newBV(0x50), newBV(0xa4), newBV(0x11), newBV(0xcf)], \
                [newBV(0x2f), newBV(0x5e), newBV(0xc8), newBV(0x6a)], \
                [newBV(0x28), newBV(0xd7), newBV(0x07), newBV(0x94)]]
    actual = AES.inv_sub_bytes(stateArr)
    assert expected == actual

    expected = [[newBV(0xe0), newBV(0xc8), newBV(0xd9), newBV(0x85)], \
                [newBV(0x92), newBV(0x63), newBV(0xb1), newBV(0xb8)], \
                [newBV(0x7f), newBV(0x63), newBV(0x35), newBV(0xbe)], \
                [newBV(0xe8), newBV(0xc0), newBV(0x50), newBV(0x01)]]
    stateArr = [[newBV(0xe1), newBV(0xe8), newBV(0x35), newBV(0x97)], \
                [newBV(0x4f), newBV(0xfb), newBV(0xc8), newBV(0x6c)], \
                [newBV(0xd2), newBV(0xfb), newBV(0x96), newBV(0xae)], \
                [newBV(0x9b), newBV(0xba), newBV(0x53), newBV(0x7c)]]
    actual = AES.inv_sub_bytes(stateArr)
    assert expected == actual

def test_shift_bytes_left():
    ''' Return the value of BitVector bv after rotating it to the left
        by num bytes'''
    bitVec = newBV(0xff00, 16)
    expect = newBV(0x00ff, 16)
    actual = AES.shift_bytes_left(bitVec, 1)
    assert actual == expect

    bitVec = newBV(0xffff, 16)
    expect = newBV(0xffff, 16)
    actual = AES.shift_bytes_left(bitVec, 1)
    assert actual == expect

    bitVec = newBV(0xa5f3, 16)
    expect = newBV(0xf3a5, 16)
    actual = AES.shift_bytes_left(bitVec, 1)
    assert actual == expect

    bitVec = newBV(0x8d87, 16)
    expect = newBV(0x878d, 16)
    actual = AES.shift_bytes_left(bitVec, 1)
    assert actual == expect

def test_shift_bytes_right():
    ''' Return the value of BitVector bv after rotating it to the right
        by num bytes'''
    expect = newBV(0xff00, 16)
    bitVec = newBV(0x00ff, 16)
    actual = AES.shift_bytes_left(bitVec, 1)
    assert actual == expect

    expect = newBV(0xffff, 16)
    bitVec = newBV(0xffff, 16)
    actual = AES.shift_bytes_left(bitVec, 1)
    assert actual == expect

    expect = newBV(0xa5f3, 16)
    bitVec = newBV(0xf3a5, 16)
    actual = AES.shift_bytes_left(bitVec, 1)
    assert actual == expect

    expect = newBV(0x8d87, 16)
    bitVec = newBV(0x878d, 16)
    actual = AES.shift_bytes_left(bitVec, 1)
    assert actual == expect

def test_shift_rows():
    ''' shift rows in state array sa to return new state array '''
    stateArr = [[newBV(0xbe), newBV(0x83), newBV(0x2c), newBV(0xc8)], \
                [newBV(0xd4), newBV(0x3b), newBV(0x86), newBV(0xc0)], \
                [newBV(0x0a), newBV(0xe1), newBV(0xd4), newBV(0x4d)], \
                [newBV(0xda), newBV(0x64), newBV(0xf2), newBV(0xfe)]]
    expected = [[newBV(0xbe), newBV(0x3b), newBV(0xd4), newBV(0xfe)], \
                [newBV(0xd4), newBV(0xe1), newBV(0xf2), newBV(0xc8)], \
                [newBV(0x0a), newBV(0x64), newBV(0x2c), newBV(0xc0)], \
                [newBV(0xda), newBV(0x83), newBV(0x86), newBV(0x4d)]]
    actual = AES.shift_rows(stateArr)
    assert actual == expected

    stateArr = [[newBV(0x87), newBV(0xec), newBV(0x4a), newBV(0x8c)], \
                [newBV(0xf2), newBV(0x6e), newBV(0xc3), newBV(0xd8)], \
                [newBV(0x4d), newBV(0x4c), newBV(0x46), newBV(0x95)], \
                [newBV(0x97), newBV(0x90), newBV(0xe7), newBV(0xa6)]]
    expected = [[newBV(0x87), newBV(0x6e), newBV(0x46), newBV(0xa6)], \
                [newBV(0xf2), newBV(0x4c), newBV(0xe7), newBV(0x8c)], \
                [newBV(0x4d), newBV(0x90), newBV(0x4a), newBV(0xd8)], \
                [newBV(0x97), newBV(0xec), newBV(0xc3), newBV(0x95)]]
    actual = AES.shift_rows(stateArr)
    assert actual == expected

    stateArr = [[newBV(0xe9), newBV(0x09), newBV(0x89), newBV(0x72)], \
                [newBV(0xcb), newBV(0x31), newBV(0x07), newBV(0x5f)], \
                [newBV(0x3d), newBV(0x32), newBV(0x7d), newBV(0x94)], \
                [newBV(0xaf), newBV(0x2e), newBV(0x2c), newBV(0xb5)]]
    expected = [[newBV(0xe9), newBV(0x31), newBV(0x7d), newBV(0xb5)], \
                [newBV(0xcb), newBV(0x32), newBV(0x2c), newBV(0x72)], \
                [newBV(0x3d), newBV(0x2e), newBV(0x89), newBV(0x5f)], \
                [newBV(0xaf), newBV(0x09), newBV(0x07), newBV(0x94)]]
    actual = AES.shift_rows(stateArr)
    assert actual == expected

def test_inv_shift_rows():
    ''' shift rows on state array sa to return new state array '''
    expected = [[newBV(0xbe), newBV(0x83), newBV(0x2c), newBV(0xc8)], \
                [newBV(0xd4), newBV(0x3b), newBV(0x86), newBV(0xc0)], \
                [newBV(0x0a), newBV(0xe1), newBV(0xd4), newBV(0x4d)], \
                [newBV(0xda), newBV(0x64), newBV(0xf2), newBV(0xfe)]]
    stateArr = [[newBV(0xbe), newBV(0x3b), newBV(0xd4), newBV(0xfe)], \
                [newBV(0xd4), newBV(0xe1), newBV(0xf2), newBV(0xc8)], \
                [newBV(0x0a), newBV(0x64), newBV(0x2c), newBV(0xc0)], \
                [newBV(0xda), newBV(0x83), newBV(0x86), newBV(0x4d)]]
    actual = AES.inv_shift_rows(stateArr)
    assert actual == expected

    expected = [[newBV(0x87), newBV(0xec), newBV(0x4a), newBV(0x8c)], \
                [newBV(0xf2), newBV(0x6e), newBV(0xc3), newBV(0xd8)], \
                [newBV(0x4d), newBV(0x4c), newBV(0x46), newBV(0x95)], \
                [newBV(0x97), newBV(0x90), newBV(0xe7), newBV(0xa6)]]
    stateArr = [[newBV(0x87), newBV(0x6e), newBV(0x46), newBV(0xa6)], \
                [newBV(0xf2), newBV(0x4c), newBV(0xe7), newBV(0x8c)], \
                [newBV(0x4d), newBV(0x90), newBV(0x4a), newBV(0xd8)], \
                [newBV(0x97), newBV(0xec), newBV(0xc3), newBV(0x95)]]
    actual = AES.inv_shift_rows(stateArr)
    assert actual == expected

    expected = [[newBV(0xe9), newBV(0x09), newBV(0x89), newBV(0x72)], \
                [newBV(0xcb), newBV(0x31), newBV(0x07), newBV(0x5f)], \
                [newBV(0x3d), newBV(0x32), newBV(0x7d), newBV(0x94)], \
                [newBV(0xaf), newBV(0x2e), newBV(0x2c), newBV(0xb5)]]
    stateArr = [[newBV(0xe9), newBV(0x31), newBV(0x7d), newBV(0xb5)], \
                [newBV(0xcb), newBV(0x32), newBV(0x2c), newBV(0x72)], \
                [newBV(0x3d), newBV(0x2e), newBV(0x89), newBV(0x5f)], \
                [newBV(0xaf), newBV(0x09), newBV(0x07), newBV(0x94)]]
    actual = AES.inv_shift_rows(stateArr)
    assert actual == expected

def test_gf_mult():
    ''' Used by mix_columns and inv_mix_columns to perform multiplication in
    GF(2^8).  param bv is an 8-bit BitVector, param factor is an integer.
        returns an 8-bit BitVector, whose value is bv*factor in GF(2^8) '''
    bitVector = newBV(0x87)
    factor = 0x02
    expected = newBV(0x15)
    actual = AES.gf_mult(bitVector, factor)
    assert expected == actual

    bitVector = newBV(0xca)
    factor = 0x53
    expected = newBV(0x01)
    actual = AES.gf_mult(bitVector, factor)
    assert expected == actual

    bitVector = newBV(0xb6)
    factor = 0x53
    expected = newBV(0x36)
    actual = AES.gf_mult(bitVector, factor)
    assert expected == actual

def test_mix_columns():
    ''' Mix columns on state array sa to return new state array '''
    stateArr = [[newBV(0xac), newBV(0xc1), newBV(0xd6), newBV(0xb8)], \
                [newBV(0xef), newBV(0xb5), newBV(0x5a), newBV(0x7b)], \
                [newBV(0x13), newBV(0x23), newBV(0xcf), newBV(0xdf)], \
                [newBV(0x45), newBV(0x73), newBV(0x11), newBV(0xb5)]]
    expected = [[newBV(0x75), newBV(0xec), newBV(0x09), newBV(0x93)], \
                [newBV(0x20), newBV(0x0b), newBV(0x63), newBV(0x33)], \
                [newBV(0x53), newBV(0xc0), newBV(0xcf), newBV(0x7c)], \
                [newBV(0xbb), newBV(0x25), newBV(0xd0), newBV(0xdc)]]
    actual = AES.mix_columns(stateArr)
    assert expected == actual

    stateArr = [[newBV(0x52), newBV(0xa4), newBV(0xc8), newBV(0x94)], \
                [newBV(0x85), newBV(0x11), newBV(0x6a), newBV(0x28)], \
                [newBV(0xe3), newBV(0xcf), newBV(0x2f), newBV(0xd7)], \
                [newBV(0xf6), newBV(0x50), newBV(0x5e), newBV(0x07)]]
    expected = [[newBV(0x0f), newBV(0xd6), newBV(0xda), newBV(0xa9)], \
                [newBV(0x60), newBV(0x31), newBV(0x38), newBV(0xbf)], \
                [newBV(0x6f), newBV(0xc0), newBV(0x10), newBV(0x6b)], \
                [newBV(0x5e), newBV(0xb3), newBV(0x13), newBV(0x01)]]
    actual = AES.mix_columns(stateArr)
    assert expected == actual
    
    stateArr = [[newBV(0xe1), newBV(0xfb), newBV(0x96), newBV(0x7c)], \
                [newBV(0xe8), newBV(0xc8), newBV(0xae), newBV(0x9b)], \
                [newBV(0x35), newBV(0x6c), newBV(0xd2), newBV(0xba)], \
                [newBV(0x97), newBV(0x4f), newBV(0xfb), newBV(0x53)]]
    expected = [[newBV(0x25), newBV(0xd1), newBV(0xa9), newBV(0xad)], \
                [newBV(0xbd), newBV(0x11), newBV(0xd1), newBV(0x68)], \
                [newBV(0xb6), newBV(0x3a), newBV(0x33), newBV(0x8e)], \
                [newBV(0x4c), newBV(0x4c), newBV(0xc0), newBV(0xb0)]]
    actual = AES.mix_columns(stateArr)
    assert expected == actual
    
def test_inv_mix_columns():
    ''' Inverse mix columns on state array sa to return new state array '''
    expected = [[newBV(0xac), newBV(0xc1), newBV(0xd6), newBV(0xb8)], \
                [newBV(0xef), newBV(0xb5), newBV(0x5a), newBV(0x7b)], \
                [newBV(0x13), newBV(0x23), newBV(0xcf), newBV(0xdf)], \
                [newBV(0x45), newBV(0x73), newBV(0x11), newBV(0xb5)]]
    stateArr = [[newBV(0x75), newBV(0xec), newBV(0x09), newBV(0x93)], \
                [newBV(0x20), newBV(0x0b), newBV(0x63), newBV(0x33)], \
                [newBV(0x53), newBV(0xc0), newBV(0xcf), newBV(0x7c)], \
                [newBV(0xbb), newBV(0x25), newBV(0xd0), newBV(0xdc)]]
    actual = AES.inv_mix_columns(stateArr)
    AES.print_state(expected)
    AES.print_state(actual)
    assert expected == actual

    expected = [[newBV(0x52), newBV(0xa4), newBV(0xc8), newBV(0x94)], \
                [newBV(0x85), newBV(0x11), newBV(0x6a), newBV(0x28)], \
                [newBV(0xe3), newBV(0xcf), newBV(0x2f), newBV(0xd7)], \
                [newBV(0xf6), newBV(0x50), newBV(0x5e), newBV(0x07)]]
    stateArr = [[newBV(0x0f), newBV(0xd6), newBV(0xda), newBV(0xa9)], \
                [newBV(0x60), newBV(0x31), newBV(0x38), newBV(0xbf)], \
                [newBV(0x6f), newBV(0xc0), newBV(0x10), newBV(0x6b)], \
                [newBV(0x5e), newBV(0xb3), newBV(0x13), newBV(0x01)]]
    actual = AES.inv_mix_columns(stateArr)
    assert expected == actual
    
    expected = [[newBV(0xe1), newBV(0xfb), newBV(0x96), newBV(0x7c)], \
                [newBV(0xe8), newBV(0xc8), newBV(0xae), newBV(0x9b)], \
                [newBV(0x35), newBV(0x6c), newBV(0xd2), newBV(0xba)], \
                [newBV(0x97), newBV(0x4f), newBV(0xfb), newBV(0x53)]]
    stateArr = [[newBV(0x25), newBV(0xd1), newBV(0xa9), newBV(0xad)], \
                [newBV(0xbd), newBV(0x11), newBV(0xd1), newBV(0x68)], \
                [newBV(0xb6), newBV(0x3a), newBV(0x33), newBV(0x8e)], \
                [newBV(0x4c), newBV(0x4c), newBV(0xc0), newBV(0xb0)]]
    actual = AES.inv_mix_columns(stateArr)
    assert expected == actual

def test_encrypt():
    ''' perform AES encryption using 128-bit hex_key on 128-bit plaintext 
        hex_plaintext, where both key and plaintext values are expressed
    in hexadecimal string notation. '''
    p = "00112233445566778899aabbccddeeff"
    k = "000102030405060708090a0b0c0d0e0f"
    c = "69c4e0d86a7b0430d8cdb78070b4c55a"
    actual = AES.encrypt(k, p)
    assert actual == c

    p = "6bc1bee22e409f96e93d7e117393172a"
    k = "2b7e151628aed2a6abf7158809cf4f3c"
    c = "3ad77bb40d7a3660a89ecaf32466ef97"
    actual = AES.encrypt(k, p)
    assert actual == c

    p = "ae2d8a571e03ac9c9eb76fac45af8e51"
    k = "2b7e151628aed2a6abf7158809cf4f3c"
    c = "f5d3d58503b9699de785895a96fdbaaf"
    actual = AES.encrypt(k, p)
    assert actual == c
    
    p = "30c81c46a35ce411e5fbc1191a0a52ef"
    k = "2b7e151628aed2a6abf7158809cf4f3c"
    c = "43b1cd7f598ece23881b00e3ed030688"
    actual = AES.encrypt(k, p)
    assert actual == c

    p = "f69f2445df4f9b17ad2b417be66c3710"
    k = "2b7e151628aed2a6abf7158809cf4f3c"
    c = "7b0c785e27e8ad3f8223207104725dd4"
    actual = AES.encrypt(k, p)
    assert actual == c
    

def test_decrypt():
    ''' perform AES decryption using 128-bit hex_key on 128-bit ciphertext
           hex_ciphertext, where both key and ciphertext values are expressed
    in hexadecimal string notation. '''
    p = "00112233445566778899aabbccddeeff"
    k = "000102030405060708090a0b0c0d0e0f"
    c = "69c4e0d86a7b0430d8cdb78070b4c55a"
    actual = AES.decrypt(k, c)
    assert actual == p

    p = "6bc1bee22e409f96e93d7e117393172a"
    k = "2b7e151628aed2a6abf7158809cf4f3c"
    c = "3ad77bb40d7a3660a89ecaf32466ef97"
    actual = AES.decrypt(k, c)
    assert actual == p

    p = "ae2d8a571e03ac9c9eb76fac45af8e51"
    k = "2b7e151628aed2a6abf7158809cf4f3c"
    c = "f5d3d58503b9699de785895a96fdbaaf"
    actual = AES.decrypt(k, c)
    assert actual == p
    
    p = "30c81c46a35ce411e5fbc1191a0a52ef"
    k = "2b7e151628aed2a6abf7158809cf4f3c"
    c = "43b1cd7f598ece23881b00e3ed030688"
    actual = AES.decrypt(k, c)
    assert actual == p

    p = "f69f2445df4f9b17ad2b417be66c3710"
    k = "2b7e151628aed2a6abf7158809cf4f3c"
    c = "7b0c785e27e8ad3f8223207104725dd4"
    actual = AES.decrypt(k, c)
    assert actual == p


if __name__ == "__main__":
    nose.main();

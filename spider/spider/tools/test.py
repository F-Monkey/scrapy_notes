'''
Created on 2019年6月2日

@author: tangjf
'''


def md5(s):
    import hashlib
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()
#     return enumerate(m.hexdigest())


def mode(s, mode_size):
    result = 0
    s_len = len(s)
    for idx , ch in enumerate(s):
        result = (result * s_len + int(ch, s_len)) % mode_size
    return result


from pybloom_live import BloomFilter

if __name__ == '__main__':
    print(2 << 25)
    bloomFilter = BloomFilter(capacity=2 << 25)
    s = 'https://blog.csdn.net/qq_33042187/article/details/78929834'
    bloomFilter.add(s)
    print(s in bloomFilter)

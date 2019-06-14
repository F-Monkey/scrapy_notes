'''
Created on 2019-06-14

@author: F-Monkey
'''
from resultHandler.word import queryUsers
import json
dict = {}

def testQueryUser():
    users = queryUsers()
    for u in users:
        print(str(u))

if __name__ == '__main__':
    testQueryUser()
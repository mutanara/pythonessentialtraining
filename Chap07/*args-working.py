#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def new():
    source('meow', 'grrr', 'purr')

def source(*args):  #standard way of naming your function argument lists 
    if len(args):          # def name of your function (*args)
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': new()

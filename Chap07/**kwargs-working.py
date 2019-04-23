#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#EXAMPLE 1
def new():
    source(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

def source(**kwargs): #naming convention for function keyword arguments( they behave like dictionaries instead of lists)
    if len(kwargs):                #def function name (**kwargs)
        for k in kwargs:
            print('source {} says {}'.format(k, kwargs[k])) #how to do string substitue in a dictionary.
    else: print('Meow.')

if __name__ == '__main__': new() 


#if __name__ == '__main__': is used to call functions predefined before.

#Format

def function name (**kwargs):
    name of the other function: (a = b, c = d, e =f, ...) a,c,e are keys (don't need to be in "") while b,d,f are considered as words (theys should be in "")
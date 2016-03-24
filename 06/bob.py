#!/usr/bin/env python
responses = {'empty': 'Fine. Be that way!',
             'yelling': 'Woah, chill out!',
             'question': 'Sure.',
             'statement': 'Whatever.'}

def get_sentence_type(sentence):
    if sentence.strip() == '':
        return 'empty'
    if sentence.isupper():
        return 'yelling'
    if sentence[-1] == '?':
        return 'question'
    return 'statement'

def hey(sentence):
    return responses[get_sentence_type(sentence)]

#!/usr/bin/env python

import speech_recognition as sr

def main():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		audio = r.listen(source)
		text = r.recognize_sphinx(audio)
		print(text)

if __name__ == '__main__':
	main()

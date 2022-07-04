# brew install portaudio 
# pip install pyaudio 
# pip install SpeechRecognition

import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def greeting():
	return 'HI - jak'

def create_task():
	print('какую задачу добавляем')
	with speech_recognition.Microphone() as mic:
		sr.adjust_for_ambient_noise(source=mic, duration=0.5)
		audio = sr.listen(source=mic)
		query = sr.recognize_google(audio_data = audio, language='ru-RU').lower()
	
	with open('todo-list.txt', 'a') as file:
		file.write(f' - {query}\n')
	return f'task {query} added in to-do list'

with speech_recognition.Microphone() as mic:
	sr.adjust_for_ambient_noise(source=mic, duration=0.5)
	audio = sr.listen(source=mic)
	query = sr.recognize_google(audio_data = audio, language='ru-RU').lower()

if query == 'привет друг':
	print(greeting())
elif query == 'добавить задачу':
	print(create_task())
else:
	print('no-no neraspoznan')
import speech_recognition as sr

#마이크로부터 음성듣기
r = sr.Recognizer() # 객체생성
with sr.Microphone() as source:
    print("듣고있습니다.")
    audio = r.listen(source) #마이크로부터 음성 듣기

#파일로부터 음성 불러오기(wav,aiff,flac)
# r = sr.Recognizer()
# with sr.AudioFile('sample.wav') as source:
#     audio=r.record(source)

try:
    #구글 API 인식
    #영어
    #text = r.recognize_google(audio,language='en-US')
    #print(text)

    #한글
    text = r.recognize_google(audio,language='KO')
    print(text)

except sr.UnknownValueError:
    print('인식 실패') #음성 인식 실패
    
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) # API KEY 오류, 또는 네트워크 단절 등 오류


from venv import create
from vosk import Model, KaldiRecognizer
import sys, logging, faulthandler, traceback, subprocess, os
from gtts import gTTS
from io import BytesIO
import pyaudio, json
from mat import abusive_language
import webbrowser
import viewer

def log_exception(where: str):
    etype, value, tb = sys.exc_info()
    print(f"\n[EXC in {where}] {etype.__name__}: {value}")
    traceback.print_exception(etype, value, tb)

def check_profanity(text):
    if any(word in text for word in abusive_language):
        print("Замечен мат")
        return True


def main():
    faulthandler.enable()
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
    
    

    model = Model("vosk-model-small-ru-0.22")
    rec = KaldiRecognizer(model, 16000)
    # mp3_fp = BytesIO()
    p = pyaudio.PyAudio()

    stream_input = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=44100, input_device_index=1)
    # stream_output = p.open(format=pyaudio.paInt16, channels=1, rate=16000, output=True, output_device_index=5)
    stream_input.start_stream()


    try:
        print("Прослушка началась")
        while True:
            data = stream_input.read(4000, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text != "":

                    if (check_profanity(text)):
                        webbrowser.open('https://i.pinimg.com/736x/9e/f4/24/9ef424fdceb9851426ab397c9b365c6a.jpg')

                    tts = gTTS(result["text"], lang='ru')
                    tts.save(f"audio.mp3")


                    viewer.print_transcribation(result["text"])
                
    except Exception:
        # log_exception("Где-то ошибка")
        print("Прослушка остановлена")
    finally:
        stream_input.stop_stream()
        stream_input.close()
        # stream_output.stop_stream()
        # stream_output.close()
        p.terminate
        
if __name__ == "__main__":
    main()

import pyaudio

def handle_devices(type: str, num_devices: int, p):
    for i in range(num_devices):
        device_info = p.get_device_info_by_index(i)
        if device_info.get(type) > 0:
            print(f"  Index: {device_info['index']}, Name: {device_info['name']}")
        
def main():
    indent = ""
    p = pyaudio.PyAudio()
    num_devices = p.get_device_count()
    
    print("Available Input Devices:")
    handle_devices('maxInputChannels', num_devices, p)

    for _ in range(4): print(indent)

    print('Available Output Devices:')
    handle_devices('maxOutputChannels', num_devices, p)

    p.terminate()
    
if __name__ == "__main__":
    main()
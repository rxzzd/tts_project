import pyaudio

# Create an instance of PyAudio
p = pyaudio.PyAudio()

# Get the total number of audio devices
num_devices = p.get_device_count()

print("Available Output Devices:")

# Iterate through all devices
for i in range(num_devices):
    # Get device information by index
    device_info = p.get_device_info_by_index(i)

    # Check if the device has output channels
    if device_info.get('maxInputChannels') > 0:
        print(f"  Index: {device_info['index']}, Name: {device_info['name']}")

# Terminate the PyAudio instance
p.terminate()
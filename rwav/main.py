import wave

import pyaudio
import argparse
import sys


def record_audio(filename, samplerate):
    # Open an audio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=samplerate,
                    input=True,
                    frames_per_buffer=1024)

    # Start recording
    frames = []
    print("Recording...")
    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    # Stop the stream and close the audio device
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a file
    with wave.open(filename, 'wb') as wavfile:
        wavfile.setnchannels(1)
        wavfile.setsampwidth(2)  # 16-bit audio
        wavfile.setframerate(samplerate)
        wavfile.writeframes(b''.join(frames))

    print(f"Recording saved to {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Record audio from microphone and save as a WAV file.")
    parser.add_argument("filename", type=str, help="name of the output file (e.g. output.wav)")
    parser.add_argument("-sr", "--samplerate", type=int, default=44100,
                        help="sampling rate (default: 44100 Hz)")
    args = parser.parse_args()

    try:
        record_audio(args.filename, args.samplerate)
    except KeyboardInterrupt:
        sys.exit(0)

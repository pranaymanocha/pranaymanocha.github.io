import librosa
import soundfile as sf
import os

os.mkdir('asserts_16k')

path = '/Users/pranaymanocha/Desktop/stafd/pranaymanocha.github.op/asserts'
output_path = '/Users/pranaymanocha/Desktop/stafd/pranaymanocha.github.op/asserts_16k'

for file in os.listdir(path):
    if file[-3:]=='wav':
        # Load the audio file
        audio_file = os.path.join(path, file)
        audio_data, sample_rate = sf.read(audio_file)
        print(file, sample_rate, audio_data.shape, len(audio_data))
        # Normalize the audio data (optional but recommended)
        max_amplitude = max(abs(audio_data))
        if max_amplitude > 1.0:
            audio_data /= max_amplitude

        # Convert to 16-bit integers
        audio_data_int16 = (audio_data * 32767).astype('int16')

        # Save the converted audio to a new file
        output_file = os.path.join(output_path, file)
        sf.write(output_file, audio_data_int16, sample_rate)

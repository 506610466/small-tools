# pip install ffmpy 或者 ffmpy3
from ffmpy3 import FFmpeg

exe = r'D:\install\ffmpeg-master-latest-win64-lgpl-shared\bin\ffmpeg.exe'

source_file = r"C:\Users\shell\Downloads\Compressed\京剧《击鼓骂曹》王佩瑜.flv"
output_file = source_file.split(".")[0] + ".mp4"
print(source_file)
print(output_file)
ff = FFmpeg(
    executable=exe,
    inputs={source_file: None},
    outputs={output_file: None}
)
ff.run_async()
ff.run()

import ffmpy
import os
import threading
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(PATH, 'videos')
OUTPUT_PATH = os.path.join(PATH, 'gifs')


def mp4_to_gif(name):
    file_name, _ = os.path.splitext(name)
    if not os.path.exists(os.path.join(OUTPUT_PATH, f'{file_name}.gif')):
        ff = ffmpy.FFmpeg(
            inputs={os.path.join(INPUT_PATH, name): None},
            outputs={os.path.join(OUTPUT_PATH, f'{file_name}.gif'): None}
        )
        ff.run()


threads = []

for name in os.listdir(INPUT_PATH):
    t = threading.Thread(target=mp4_to_gif, args=(name,))
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()

sys.exit()

# for name in os.listdir(INPUT_PATH):
#     file_name, _ = os.path.splitext(name)
#     if not os.path.exists(os.path.join(OUTPUT_PATH, f'{file_name}.gif')):
#         ff = ffmpy.FFmpeg(
#             inputs={os.path.join(INPUT_PATH, name): None},
#             outputs={os.path.join(OUTPUT_PATH, f'{file_name}.gif'): None}
#         )
#         ff.run()

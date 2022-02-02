from time import  time

def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))
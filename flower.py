import math
import sys
import time

max_x = 80
max_y = 24
buffsize = (max_x * max_y)
buffer = [' '] * buffsize
zbuf = [0] * buffsize
A, B = 0, 1.62


def draw_buffer():
    global buffer
    for n in range(0, buffsize):
        if n % max_x == max_x - 1:
            sys.stdout.write('\n')
        else:
            sys.stdout.write(buffer[n])
    sys.stdout.flush()


def process_frame():
    global A, B, buffer, zbuf
    buffer = [' '] * buffsize
    zbuf = [0] * buffsize
    s = 120
    s_ = 100
    for a in range(0, s):
        a = a * (6.28 / s)
        for b in range(0, s_):
            b = b * (6.28 / s_)
            pettals = 11
            rsa = math.sin(A)
            rsb = math.sin(B)
            msa = (math.cos(pettals * a) + 2.5) * math.sin(a)
            msb = math.sin(b)
            rca = math.cos(A)
            rcb = math.cos(B)
            mca = (math.cos(pettals * a) + 2.5) * math.cos(a)
            mcb = math.cos(b) + 1

            z = 1 / (msa * mcb * rsa + msb * rca + 8)
            t = msa * mcb * rca - msb * rsa
            x = max_x / 2 + 30 * z * (mca * mcb * rcb - t * rsb)
            y = max_y / 2 + 15 * z * (mca * mcb * rsb + t * rcb)
            n = int(x) + max_x * int(y)
            l = 0.5*(mcb*(-mca*rsb-msa*rca*rcb)+msb*rcb*rsa)-mcb*msa*rsa-msb*rca
            l = int(2*l)
            if max_y > y > 0 and max_x > x > 0 and z > zbuf[n]:
                zbuf[n] = z
                buffer[n] = ".,-~\"=+*%$#&@8"[(l if l < 13 else 13) if l > 0 else 0]

    A += 0.10
    B += 0.01


def main():
    import os, platform

    while True:
        if "Windows" in platform.system():
            os.system("cls")
        else:
            os.system("clear")

        draw_buffer()
        process_frame()


main()

## Cap 7 - Classes
# EX2 - test TV

from C7EX1 import TV

def main():
    tv1 = TV()
    tv1.turn_on()
    tv1.set_channel(30)
    tv1.set_volume_level(3)

    tv2 = TV()
    tv2.turn_on()
    tv2.channel_up()
    tv2.channel_up()
    tv2.set_volume_up()

    print("tv1`s channel is", tv1.get_channel(), "and volume level is", tv1.get_volume_level())
    print("tv2`s channel is", tv2.get_channel(), "and volume level is", tv2.get_volume_level())

main()
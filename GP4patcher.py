import binascii
import hashlib


def sha1file():
    sha1h = hashlib.sha1()
    ba = bytearray(128*1024)
    mv = memoryview(ba)
    try:
        with open('GP4.exe', 'rb', buffering=0) as gp4:
            for n in iter(lambda: gp4.readinto(mv), 0):
                sha1h.update(mv[:n])
        return sha1h.hexdigest()
    except IOError:
        print(
            "Couldn't find GP4.exe!\nMake sure it's in the same folder as this tool.")


def main():
    print("This tool will patch Grand Prix 4 v1.02 cracked .exe to remove the CD Drive check\nthat requires you to have the ISO mounted despite it being cracked.")
    if (input("Proceed? Y/N\n").lower() == 'Y'.lower()):
        if (sha1file() == '592903176a7d52e0ad0deef2541a88554ed4181d'):
            try:
                print("Patching...")
                with open('GP4.exe', 'r+b') as gp4:
                    gp4.seek(0x0014bc0f)
                    gp4.write(binascii.unhexlify('9090'))
                    gp4.seek(0x0014bc18)
                    gp4.write(binascii.unhexlify('9090'))
                    print("Patch completed successfully.")
            except IOError:
                print(
                    "Couldn't find GP4.exe!\nMake sure it's in the same folder as this tool.")
        elif(sha1file() == '346e63c4ed47032e496a6ae90e6ff70109fb9529'):
            print("The file has already been patched.")
        else:
            print(
                f"Your GP4.exe is not the proper file. The supported file has SHA256 hash 592903176a7d52e0ad0deef2541a88554ed4181d\nYour file is {sha1file()}")
    else:
        print("Bye.")


if __name__ == '__main__':
    main()

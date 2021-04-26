import streams, strutils, std/sha1

proc calculateSHA1() : string =
    try:
        let hash = secureHashFile("GP4.exe")
        return $hash
    except IOError:
        echo "Couldn't open GP4.exe! Make sure it's in the same directory as this tool and that you have rights to that directory!"
        

proc main() =
    echo "This tool will patch the common Grand Prix 4 1.02 cracked exe to remove the requirement for a CD Drive."
    if calculateSHA1() == "592903176A7D52E0AD0DEEF2541A88554ED4181D":
        echo "Proceed? Y/N"
        let proceed = readLine(stdin)
        if proceed.toLowerAscii == "y":
            try:
                echo "Patching..."
                let gp4file = newFileStream("GP4.exe", fmReadWriteExisting)
                defer: gp4file.close
                gp4file.setPosition(0x0014bc0f)
                gp4file.write("\x90\x90")
                gp4file.setPosition(0x0014bc18)
                gp4file.write("\x90\x90")
                gp4file.close()
                echo "Patching complete. Press enter to quit."
                let quit = readLine(stdin)
            except IOError:
                echo "Couldn't open GP4.exe! Make sure it's in the same directory as this tool and that you have rights to that directory!"
        else:
            echo "Bye."
    elif calculateSHA1() == "346E63C4ED47032E496A6AE90E6FF70109FB9529":
        echo "The file has already been patched. Press enter to quit."
        let quit = readLine(stdin)
    else:
        echo "Your GP4.exe is not the one expected by this tool. Press enter to quit."
        let quit = readLine(stdin)

main()
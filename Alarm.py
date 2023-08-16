import playsound as ply
import time
CLEAR="\033[3J"
CLEAR_AND_RETURN ="\033[H"
def alram(secound):
    time_elapsed=0
    #print(CLEAR)
    while time_elapsed<secound:
        time.sleep(1)
        time_elapsed +=1

        time_left=secound-time_elapsed
        minitue_left=time_left//60
        secound_left=time_left%60
        print(f"{CLEAR_AND_RETURN}{minitue_left:02d}:{secound_left:02d}\n\n")
    ply.playsound("play.mp3")
    

alram(5)

import pygame
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)

def main(axes: list):

    clock = pygame.time.Clock()

    while 1:

        for event in pygame.event.get():
            
            if event.type == pygame.JOYAXISMOTION:

                
                
                sessions = AudioUtilities.GetAllSessions()

                for axe, app in axes:

                    volume_value = abs(round(joystick.get_axis(axe), 3) / 2 - 0.5)
                    
                    """
                    100% (on joystick) -> -1 (return) -> 1 (x / 2 - 0.5)
                    50%  (on joystick) -> 0 (return) -> 0.5 (x / 2 - 0.5)
                    0% (on joystick) -> 1 (return) -> 0 (x / 2 - 0.5)
                    """



                    for session in sessions:
                        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                        if session.Process and session.Process.name().lower() == app:

                            volume.SetMasterVolume(volume_value, None)

        clock.tick(60)


if __name__ == "__main__":

    main([(2, "csgo.exe"), (3, "spotify.exe"), (4, "discord.exe")])
import datetime
import os
import PIL.ImageGrab
from pynput import keyboard
import PlayerProfile
import DatabaseConnections


class ImageGrabber(object):

    def __init__(self, alliance):
        self.alliance = alliance
        self.num_saved = 0
        self.db = DatabaseConnections.get_database()

        self._root = r"E:\OneDrive\101_Personal\100_Games\InfinityKingdom\S79\ScreenScraper"
        self._date = datetime.date.today()
        self.path = os.path.join(self._root, str(self._date), self.alliance)

        if os.path.exists(self.path):
            raise ValueError("Path already exists")
        else:
            os.makedirs(self.path)

    def grab_screen(self):
        _path = os.path.join(self.path, "{}.png".format(self.num_saved))
        PIL.ImageGrab.grab().save(
            _path
        )

        try:
            print("capturing")
            p = PlayerProfile.PlayerProfile(_path)
            print(p.name, 'captured')
        except Exception as e:
            print("Unable to calculate values", e)

        self.num_saved += 1

    def key_pressed(self, key):
        if key == keyboard.KeyCode(char="c"):
            self.grab_screen()
        else:
            print("Wrong key pressed, skipping.")

if __name__ == "__main__":
    ig = ImageGrabber("FATE")

    with keyboard.Listener(on_press=ig.key_pressed) as listener:
        listener.join()
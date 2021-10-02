import os
import airtable
import pytesseract
import cv2


class PlayerProfile(object):
    def __init__(self, img_path):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

        # IMAGE DATA
        self.img_path = img_path
        self.img = cv2.imread(self.img_path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

        # PLAYER INFO
        self.name = self._parse_img(545, 595, 440, 700)
        self.rank = self._parse_img(180, 230, 530, 1000)

        # STATS
        self.tech_contributions = int(self._parse_img(335, 365, 840, 1100).replace(',', ''))
        self.alliance_helps = int(self._parse_img(335, 365, 1200, 1500).replace(',', ''))
        self.highest_power = int(self._parse_img(495, 540, 840, 1100).replace(',', ''))
        self.strongest_troop = int(self._parse_img(495, 540, 1200, 1500).replace(',', ''))
        self.defeat = int(self._parse_img(660, 700, 840, 1100).replace(',', ''))
        self.dismantle_durability = int(self._parse_img(660, 700, 1200, 1500).replace(',', ''))

    def push_to_database(self):
        table = airtable.Airtable('appm8f92LjQairrC2', 'Players')
        print(table)

    def _parse_img(self, y1, y2, x1, x2):
        _i = self.img[y1:y2, x1:x2]
        # Currently basic logic returning the first item it is remotely confident in
        data = pytesseract.image_to_string(
            _i,
            lang="eng",
            config="--psm 7"
        )

        return data.strip()


if __name__ == "__main__":
    _path = r"E:\OneDrive\101_Personal\100_Games\InfinityKingdom\S79\ScreenScraper\2021-09-20\FATE"

    players = []

    for _f in os.listdir(_path):
        _p = os.path.join(_path, _f)


        pp = PlayerProfile(_p)
        print(pp.name, " - ", pp.rank)
        print("Alliance Tech Contributions: ", pp.tech_contributions)
        print("Alliance Helps: ", pp.alliance_helps)
        print("Highest Power:", pp.highest_power)
        print("Strongest Troop Power:", pp.strongest_troop)
        print("Defeat:", pp.defeat)
        print("Dismantle Durability:", pp.dismantle_durability)
        print("++++++++++++++++++++++++++++++")

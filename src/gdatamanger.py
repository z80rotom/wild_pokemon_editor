import rapidjson

from collections import OrderedDict

from core import FieldEncountTable

class GLocale:
    locale_info = {}

    @staticmethod
    def parse_locale_obj(data):
        locale_info = {}
        labelDataArray = data["labelDataArray"]
        for labelData in labelDataArray:
            labelName = labelData["labelName"]
            wordDataArray = labelData["wordDataArray"]
            localized_label = "".join([wordData["str"].encode("ascii", "ignore").decode() for wordData in wordDataArray])
            locale_info[labelName] = localized_label.replace("\n", "").replace("\r", "")
        return locale_info

    @classmethod
    def load_locale(cls, ifpath):
        with open(ifpath, "rb") as ifobj:
            locale_obj = rapidjson.load(ifobj)
            cls.locale_info.update(cls.parse_locale_obj(locale_obj))
        return cls.locale_info

    @classmethod
    def getLocalized(cls, label):
        return cls.locale_info[label]

    @classmethod
    def getPokemonName(cls, monsNo):
        return cls.getLocalized("MONSNAME_{:03d}".format(monsNo))

    @classmethod
    def getAbilityName(cls, abilityNo):
        return cls.getLocalized("TOKUSEI_{:03d}".format(abilityNo))

    @classmethod
    def getTypeName(cls, typeNo):
        if typeNo >= 9:
            return cls.getLocalized("TYPENAME_{:03d}".format(typeNo+1))
        return cls.getLocalized("TYPENAME_{:03d}".format(typeNo))
    
    @classmethod
    def getItemName(cls, itemNo):
        return cls.getLocalized("ITEMNAME_{:03d}".format(itemNo))
    
    @classmethod
    def getMoveName(cls, wazaNo):
        return cls.getLocalized("WAZANAME_{:03d}".format(wazaNo))

class GDataManager:
    MOVE_LIST = []
    POKEMON_LIST = []
    ITEM_LIST = []
    NATURE_LIST = []
    ABILITY_LIST = []
    TRAINER_MSG_LIST = []
    TRAINER_NAMES = OrderedDict()
    TRAINER_NAMES_REVERSE = OrderedDict()
    TRAINER_DATA = []
    TRAINER_POKE = []
    FIELD_ENCOUNT_TABLE: FieldEncountTable = None

    @classmethod
    def getMoveById(cls, moveId):
        move_list = cls.getMoveList()
        return move_list[moveId]

    @classmethod
    def getMoveList(cls):
        # TODO: Base this off of WazaTable instead
        if not cls.MOVE_LIST:
            with open("AssetFolder/english_Export/english_ss_wazaname.json", "r", encoding='utf-8') as ifobj:
                data = rapidjson.load(ifobj)
                for i, entry in enumerate(data["labelDataArray"]):
                    labelName = int(entry["labelName"].replace("WAZANAME_", ""))
                    if labelName != i:
                        print("Warning Bad Data: {} != {}".format(labelName, i))
                    string = entry["wordDataArray"][0]["str"]
                    string = string.encode('utf-8')
                    string = string.replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', b'-')
                    string = string.decode('utf-8')
                    cls.MOVE_LIST.append(string)
        return cls.MOVE_LIST    

    @classmethod
    def getPokemonById(cls, pokemonId):
        pokemon_list = cls.getPokemonList()
        return pokemon_list[pokemonId]

    @classmethod
    def getPokemonList(cls):
        if not cls.POKEMON_LIST:
            with open("AssetFolder/common_msbt_Export/english_ss_monsname.json", "r", encoding='utf-8') as ifobj:
                data = rapidjson.load(ifobj)
                for i, entry in enumerate(data["labelDataArray"]):
                    labelName = int(entry["labelName"].replace("MONSNAME_", ""))
                    if labelName != i:
                        print("Warning Bad Data: {} != {}".format(labelName, i))
                    string = entry["wordDataArray"][0]["str"]
                    string = string.encode('utf-8')
                    string = string.replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', b'-')
                    string = string.decode('utf-8')
                    cls.POKEMON_LIST.append(string)
        return cls.POKEMON_LIST 

    @classmethod
    def getItemById(cls, itemId):
        item_list = cls.getItemList()
        return item_list[itemId]

    @classmethod
    def getItemList(cls):
        if not cls.ITEM_LIST:
            with open("AssetFolder/english_Export/english_ss_itemname.json", "r", encoding='utf-8') as ifobj:
                data = rapidjson.load(ifobj)
                for i, entry in enumerate(data["labelDataArray"]):
                    if entry["labelName"] == "":
                        continue
                    string = entry["wordDataArray"][0]["str"]
                    string = string.encode('utf-8')
                    string = string.replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', b'-')
                    string = string.decode('utf-8')
                    cls.ITEM_LIST.append(string)
        return cls.ITEM_LIST 

    @classmethod
    def getAbilityById(cls, abilityId):
        ability_list = cls.getAbilityList()
        return ability_list[abilityId]

    @classmethod
    def getAbilityList(cls):
        if not cls.ABILITY_LIST:
            with open("AssetFolder/english_Export/english_ss_tokusei.json", "r", encoding='utf-8') as ifobj:
                data = rapidjson.load(ifobj)
                for i, entry in enumerate(data["labelDataArray"]):
                    if entry["labelName"] == "":
                        continue
                    string = entry["wordDataArray"][0]["str"]
                    string = string.encode('utf-8')
                    string = string.replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', b'-')
                    string = string.decode('utf-8')
                    cls.ABILITY_LIST.append(string)
        return cls.ABILITY_LIST 

    @classmethod
    def getNatureById(cls, natureId):
        nature_list = cls.getNatureList()
        return nature_list[natureId]

    @classmethod
    def getNatureList(cls):
        if not cls.NATURE_LIST:
            with open("AssetFolder/english_Export/english_ss_seikaku.json", "r", encoding='utf-8') as ifobj:
                data = rapidjson.load(ifobj)
                for i, entry in enumerate(data["labelDataArray"]):
                    if entry["labelName"] == "":
                        continue
                    string = entry["wordDataArray"][0]["str"]
                    string = string.encode('utf-8')
                    string = string.replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', b'-')
                    string = string.decode('utf-8')
                    cls.NATURE_LIST.append(string)
        return cls.NATURE_LIST 

    @classmethod
    def getFieldEncountTable(cls):
        if not cls.FIELD_ENCOUNT_TABLE:
            with open("AssetFolder/gamesettings_Export/FieldEncountTable_d.json", "r", encoding='utf-8') as ifobj:
                cls.FIELD_ENCOUNT_TABLE = FieldEncountTable.Schema().loads(ifobj.read())
        return cls.FIELD_ENCOUNT_TABLE
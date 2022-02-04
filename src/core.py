from marshmallow_dataclass import dataclass
from marshmallow_enum import EnumField
from typing import List, Optional
from zoneid import ZoneID

@dataclass
class EncEntry:
    maxlv : int
    minlv : int
    monsNo : int

    class Meta:
        ordered = True

@dataclass
class FieldEncount:
    zoneID: int
    encRate_gr: int
    """Regular Encounters"""
    ground_mons: List[EncEntry]
    """Morning Encounters"""
    tairyo: List[EncEntry]
    """Day Encounters"""
    day: List[EncEntry]
    """Night Encounters"""
    night: List[EncEntry]
    """Poke Radar Encounters"""
    swayGrass: List[EncEntry]
    """Liklihood of getting an alternate form"""
    FormProb: list
    """Unused"""
    Nazo: list
    """What Unown can spawn"""
    AnnoonTable: list
    """Unused block, leftover from NDS games. Can get the game to use them with cheats"""
    gbaRuby: List[EncEntry]
    gbaSapp: List[EncEntry]
    gbaEme: List[EncEntry]
    gbaFire: List[EncEntry]
    gbaLeaf: List[EncEntry]
    encRate_wat: int
    """Surf Encounters"""
    water_mons: List[EncEntry]
    encRate_turi_boro: int
    """Old Rod"""
    boro_mons: List[EncEntry]
    encRate_turi_ii: int
    """Good Rod"""
    ii_mons: List[EncEntry]
    encRate_sugoi: int
    """Super Rod"""
    sugoi_mons: List[EncEntry]

    class Meta:
        ordered = True

@dataclass
class Mitsu:
    Rate: int
    Normal: int
    Rare: int
    SuperRare: int

    class Meta:
        ordered = True

@dataclass
class HoneyTree:
    Normal: int
    Rare: int

    class Meta:
        ordered = True

@dataclass
class Mvpoke:
    zoneID: int
    nextCount: int
    nextZoneID: list

    class Meta:
        ordered = True

@dataclass
class LegendPoke:
    monsNo: int
    formNo: int
    isFixedEncSeq: int
    encSeq: str
    isFixedBGM: int
    bgmEvent: str
    isFixedBtlBg: int
    btlBg: int
    isFixedSetupEffect: int
    setupEffect: int
    waza1: int
    waza2: int
    waza3: int
    waza4: int

    class Meta:
        ordered = True

@dataclass
class Zui:
    zoneID: int
    form: list

    class Meta:
        ordered = True

@dataclass
class UnityGameObject:
    m_FileID: int
    m_PathID: int

    class Meta:
        ordered = True

@dataclass
class FieldEncountTable:
    m_GameObject: Optional[UnityGameObject]
    m_Enabled: Optional[int]
    m_Script: Optional[UnityGameObject]
    m_Name: Optional[str]
    table: List[FieldEncount]
    urayama: list
    mistu: List[Mitsu]
    honeytree: List[HoneyTree]
    safari: list
    mvpoke: List[Mvpoke]
    legendpoke: List[LegendPoke]
    zui: List[Zui]

    class Meta:
        ordered = True
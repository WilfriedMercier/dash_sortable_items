import typing

class DashComplexId(typing.TypedDict):
    type  : str
    index : str | int

class DropAnimationOptions(typing.TypedDict):
    duration : int
    easing   : str

type DashId   = str | DashComplexId | None
handlePosType = typing.Literal['start', 'end']
restrictType  = typing.Literal['vertical', 'horizontal'] | None
CSSDict       = dict[str, typing.Any]
stylesType    = dict[str, CSSDict]
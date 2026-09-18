import typing

class DashComplexId(typing.TypedDict):

    type  : str
    index : str | int

type DashId   = str | DashComplexId | None
handlePosType = typing.Literal['start', 'end']
restrictType  = typing.Literal['vertical', 'horizontal'] | None
CSSDict       = dict[str, str]
stylesType    = dict[str, CSSDict]
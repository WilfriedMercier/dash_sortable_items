import typing

class DashComplexId(typing.TypedDict):
    type  : typing.Required[str]
    index : typing.Required[str | int]

type DashId   = str | DashComplexId | None
handlePosType = typing.Literal['start', 'end']
restrictType  = typing.Literal['vertical', 'horizontal'] | None
CSSDict       = dict[str, typing.Any]

class AnimationOptions(typing.TypedDict):
    duration : typing.ReadOnly[typing.NotRequired[int]]
    easing   : typing.ReadOnly[typing.NotRequired[str]]

class stylesType(typing.TypedDict):
    div    : typing.ReadOnly[typing.NotRequired[CSSDict]]
    handle : typing.ReadOnly[typing.NotRequired[CSSDict]]

class handleDynamicType(typing.TypedDict):
    drag : typing.ReadOnly[typing.NotRequired[typing.Any]]
    drop : typing.ReadOnly[typing.NotRequired[typing.Any]]
    lock : typing.ReadOnly[typing.NotRequired[typing.Any]]
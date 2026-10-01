from ._SortableGroup import _SortableGroup
from .SortableItem   import SortableItem
from .types          import DashId, CSSDict, AnimationOptions

class SortableGroup(_SortableGroup):
    r'''
    A sortable group containing SortableItem children.

    :param items: List of SortableItem components that can be sorted within this group
    :param id: Unique ID of the component.
    :param className: Class name of the component.
    :param style: Style to apply to the div element containing the children.
    :param showClone: Whether a clone should be shown in the list when one of the elements is dragged or not.
    :param dropAnimation: Specify the duration and easing of the drop animation. If None, the dragged item instantly reaches its destination.
    '''

    def __init__(
        self,
        children      : list[SortableItem],
        id            : DashId                  = None,
        className     : str                     = '',
        style         : CSSDict                 = {},
        showClone     : bool                    = False,
        dropAnimation : AnimationOptions | None = None
    ) -> None:

        super().__init__(
            children      = children,
            id            = id,
            className     = className,
            style         = style,
            showClone     = showClone,
            dropAnimation = dropAnimation
        )
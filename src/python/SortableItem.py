import typing
from   .types import (
    DashId, 
    handlePosType, 
    restrictType, 
    dynamicHandleType,
    dynamicHandlePosType,
    stylesType,
    AnimationOptions
)

from ._SortableItem import _SortableItem

class SortableItem(_SortableItem):
    r"""
    A sortable item used as a wrapper around any Dash component. 
    This item must be placed within a SortableGroup to make it draggable and sortable.
    
    :param id: Unique ID of the component
    :param children: Children of the component.
    :param className: Class name of the component.
    :param dynamicHandle: Dictionary with keys 'drag', 'drop', and 'lock' whose values are Dash components used as handles during grabbing, dropping, or when locked, respectively. If not provided, handle is used instead.
    :param dynamicHandlePos: Same as dynamicHandle but for the position of the handle.
    :param handle: Dash component used as handle to grab the row. None means the entire row is draggable.
    :param handlePos: Position of the handle either at the start or at the end of the row.
    :param lock: Whether to lock the item (i.e. make it not moveable) or not.
    :param restrict: Whether to restrict items to vertical or horizontal motions only. None means there is no restriction.
    :param styles: CSS styles to apply. This is a dictionary with keys 'div' and 'handle', each taking a dictionary with CSS properties.
    :param stylesDrag: CSS styles to apply when the item is being draggeds. See styles.
    :param stylesDrop: CSS styles to apply when the item is being dropped. See styles.
    :param stylesLock: CSS styles to apply when the item is locked. See styles.
    :param transitionAnimation: Dictionary with properties to style the animation when an item moves from one position to another. None disables the animation.
    """

    def __init__(
        self,
        id                  : DashId,
        children            : typing.Any              = None,
        className           : str                     = '',
        dynamicHandle       : dynamicHandleType       = {},
        dynamicHandlePos    : dynamicHandlePosType    = {},
        handle              : typing.Any              = None,
        handlePos           : handlePosType           = 'start',
        lock                : bool                    = False,
        restrict            : restrictType            = None,
        styles              : stylesType              = {},
        stylesDrag          : stylesType              = {},
        stylesDrop          : stylesType              = {},
        stylesLock          : stylesType              = {},
        transitionAnimation : AnimationOptions | None = {'duration' : 250, 'easing' : 'ease'}
    ):

        self._args = {
            'children'            : children,
            'className'           : className,
            'handlePos'           : handlePos,
            'lock'                : lock,
            'restrict'            : restrict,
            'styles'              : styles,
            'stylesDrag'          : stylesDrag,
            'stylesDrop'          : stylesDrop,
            'stylesLock'          : stylesLock,
            'transitionAnimation' : transitionAnimation
        }

        if handle is not None           : self._args['handle'] = handle
        if dynamicHandle is not None    : self._args['dynamicHandle'] = dynamicHandle
        if dynamicHandlePos is not None : self._args['dynamicHandlePos'] = dynamicHandlePos
        if id     is not None           : self._args['id']     = id

        super().__init__(**self._args)

        return
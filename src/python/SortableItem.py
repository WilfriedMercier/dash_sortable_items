r'''
This file defines a placeholder that users must use to create sortable items. When creating a SortableGroup component,
the class below is converted into a _SortableItem which maps to the React component.
'''

import typing
from   .types import DashId, handlePosType, restrictType, stylesType

class SortableItem:
    r"""
    A sortable item used as a wrapper around any Dash component. 
    This item must be placed within a SortableGroup to make it draggable and sortable.
    
    :param id: Unique ID of the component
    :param children: Children of the component. Default is None.
    :param className: Class name of the component. Default is ''.
    :param handle: Dash component used as handle to grab the row. None means the entire row is draggable. Default is None.
    :param handlePos: Position of the handle either at the start or at the end of the row. Default is 'start'.
    :param lock: Whether to lock the item (i.e. make it not moveable) or not. Default is False.
    :param restrict: Whether to restrict items to vertical or horizontal motions only. None means there is no restriction. Default is None.
    :param styles: CSS styles to apply. This is a dictionary with keys 'div' and 'handle', each taking a dictionary with CSS properties. Default is {}.
    :param styles_drag: CSS styles to apply when the item is being draggeds. This is a dictionary with keys 'div' and 'handle', each taking a dictionary with CSS properties. Default is {}.
    """

    def __init__(
        self,
        id          : DashId,
        children    : typing.Any    = None,
        className   : str           = '',
        handle      : typing.Any    = None,
        handlePos   : handlePosType = 'start',
        lock        : bool          = False,
        restrict    : restrictType  = None,
        styles      : stylesType    = {},
        styles_drag : stylesType    = {}
    ): 

        self.id          = id
        self.children    = children
        self.className   = className
        self.handle      = handle
        self.handlePos   = handlePos
        self.lock        = lock
        self.restrict    = restrict
        self.styles      = styles
        self.styles_drag = styles_drag

        return
r'''
This file defines a placeholder that users must use to create a sortable group. 
This returns a _SortableGroup object which is the Python structure that creates the React component.
'''

# _SortableGroup and _SortableItem are used as placeholders here to avoid typing errors
from ._SortableGroup import _SortableGroup
from ._SortableItem  import _SortableItem
from .SortableItem   import SortableItem
from .types          import DashId, CSSDict

class SortableGroup:
    r'''
    A sortable group containing SortableItem children.

    :param items: List of SortableItem components that can be sorted within this group
    :param id: Unique ID of the component. Default is None.
    :param className: Class name of the component. Default is ''.
    :param style: Style to apply to the div element containing the children. Default is {}.
    '''

    def __new__(
        cls,
        items     : list[SortableItem],
        id        : DashId     = None,
        className : str        = '',
        style     : CSSDict    = {}
    ) -> _SortableGroup:
        

        # Output list containing the new sortable items with indices set
        new_items = []

        for pos, item in enumerate(items):

            handle_trick = {'handle' : item.handle} if item.handle is not None else {}
            id_trick     = {'id' : item.id} if item.id is not None else {}

            # Create the real SortableItem component by giving it its position in the list
            # as its index
            new_item = _SortableItem(
                index     = pos,
                children  = item.children,
                className = item.className,
                handlePos = item.handlePos,
                lock      = item.lock,
                restrict  = item.restrict,
                styles    = item.styles,
                **handle_trick, **id_trick
            )

            new_items.append(new_item)

        return _SortableGroup(
            children  = new_items,
            id        = id,
            className = className,
            style     = style
        )
Dash sortable items is a third party extension that wraps [dnd-kit](https://dndkit.com/react/quickstart/) to provide sortable lists to Dash. 

## Installation

XXX

## Basic usage

This extension provides two new Dash components: `SortableGroup` and `SortableItem`. A `SortableGroup` must only contain `SortableItem` components as children and exposes in callbacks the `sortedIDs` property which can be used to retrievce the order of the children or re-order them programmatically. Each `SortableItem` is a component that can be sorted within its parent group. A typical example would be

```python
import dash
from   dash_sortable_items import SortableGroup, SortableItem

app = dash.Dash(__name__)

item1 = SortableItem(
    id        = 'item1', 
    index     = 1,
    children  = [dash.html.Label('Row #1')],
)

item3 = SortableItem(
    id        = 'item3', 
    index     = 3,
    children  = [dash.html.Label('Row #3')],
)

item2 = SortableItem(
    id        = 'item2', 
    index     = 2,
    children  = [dash.html.Label('Row #2')],
)

group = SortableGroup(
    id        = 'group',
    children  = [item1, item3, item2],
)

app.layout = group

app.run(debug=True)
```

!!! important "Important:"
    All `SortableItem` component must have `id` and `index` provided. The `id` argument uniquely identifies the component, while `index` provides the initial position of the item in the sorted list.

Note that, even though children of the `SortableGroup` are provided in the following order `item1, item3, item2`, they are rendered as `item1, item2, item3`. This behaviour is due to the fact that the initial order of the items is set by the `index` argument. Since `item2` has an index of 2 and `item3` an index of 3, `item2` is rendered before `item3`.

!!! info "Note:"
    Drag and drop can be cancelled at any moment by pressing ++esc++

## Callbacks

The order of the `SortableItem` children can be recovered via a callback as follows

```python
@app.callback(
    ...
    dash.Input('group', 'sortedIds')
)
def callback(sortedIds: list[str] | None) -> str:

    if sortedIDs is None: raise dash.exceptions.PreventUpdate
    
    return sortedIds
```

!!! info "Note:"
    The output of sortedIds is a sorted list of the IDs of the `SortableItem` children.

For more details on `SortableGroup` and `SortableItem` see their respective API pages and check the provided [examples](./examples/index.md)
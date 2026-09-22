Dash sortable items is a third party extension that wraps [dnd-kit](https://dndkit.com/react/quickstart/) to provide sortable lists to Dash. 

## Installation

XXX

## Basic usage

This python package provides two new Dash components: `SortableGroup` and `SortableItem`. A `SortableGroup` must only contain `SortableItem` components and exposes in callbacks the `sortedIDs` property which can be used to retrieve the order of the children. Each `SortableItem` is a Dash component that can be dragged and sorted within its parent group. See below for a typical example.

!!! info "Note:"
    Drag and drop can be cancelled at any moment by pressing ++esc++

```python
import dash
from   dash_sortable_items import SortableGroup, SortableItem

app = dash.Dash(__name__)

item1 = SortableItem(
    id       = 'item1',
    children = [dash.html.Label('Row #1')],
)

item2 = SortableItem(
    id       = 'item2',
    children = [dash.html.Label('Row #2')],
)

item3 = SortableItem(
    id       = 'item3',
    children = [dash.html.Label('Row #3')],
)

group = SortableGroup(
    id    = 'group',
    items = [item1, item2, item3],
)

app.layout = group

app.run(debug=True)
```

!!! important "Important:"
    All `SortableItem` component must have `id` provided as it uniquely identifies the component in its parent group.

The order in which `SortableItem` components appear in the `items` argument of `SortableGroup` will define the order in which they appear every time the application loads.

## Callbacks

The order of the `SortableItem` components can be recovered via a callback as follows

```python
@app.callback(
    ...
    dash.Input('group', 'sortedIds')
)
def callback(sortedIds: list[str] | None) -> str:

    if sortedIDs is None: raise dash.exceptions.PreventUpdate
    
    return sortedIds
```

For more details on `SortableGroup` and `SortableItem` see their respective API pages and check the provided examples.
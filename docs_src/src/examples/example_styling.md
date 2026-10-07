## Showing a clone in the sortable list

It is possible to show a clone of the dragged component inside the list by providing `#!py3 showClone = True` to [`SortableGroup`](../API/sortable_group.md). The clone cannot be styled directly but it is possible to override its default style using CSS stylesheets since it holds the `#!css data-dnd-placeholder="clone"` attribute. For instance, in the example below the background of all the clones of [`SortableItem`](../API/sortable_item.md) components with the `#!py3 'item'` class name is set to green, and the background of the component with ID `#!py3 'mycustomitem'` is set to red:

```css
.item[data-dnd-placeholder="clone"] {
    background-color : green !important;
}

#mycustomitem[data-dnd-placeholder="clone"] {
    background-color : red !important;
}
```

## Customizing the drop animation

When a dragged item is released, it is brought to its final position. By default, no animation is shown but it is possible to define one by providing `dropAnimation` as an argument of [`SortableGroup`](../API/sortable_group.md) as follows:

```python
SortableGroup(
    ...
    dropAnimation = {
        'duration' : 1000,
        'easing'   : 'ease-in-out'
    }
    ...
)
```

If provided and not `None`, `dropAnimation` must contain two keys: `#!py3 'duration'` and `#!py3 'easing'`. The former corresponds to the length of the animation in millisecond and the latter specifies a [CSS easing function](https://developer.mozilla.org/fr/docs/Web/CSS/Reference/Values/easing-function).

## Customizing the transition animation

Similarly to the drop animation, it is possible to customize the animation played when an item moves from one position to another in the list when dragging occurs. This is set in [`SortableItem`](../API/sortable_item.md) using the `transitionAnimation` argument as follows:

```python
SortableItem(
    ...
    transitionAnimation = {
        'duration' : 1000,
        'easing'   : 'ease-in-out'
    }
    ...
)
```

## Dynamically style items

For each [`SortableItem`](../API/sortable_item.md), it is possible to provide CSS stylesheets that are applied when the item is being dragged or dropped without using callbacks. The three following style dictionaries can be provided:

- `#!py3 'styles'` which corresponds to the default style
- `#!py3 'stylesDrag'` which is applied on top of `#!py3  'styles'` when the item is being dragged
- `#!py3 'stylesDrop'` which is applied on top of `#!py3  'styles'` when the item is being dropped
- `#!py3 'styleLock'` which is applied on top of `#!py3  'styles'` when the item is locked

Each is a dictionary with the following structure: `#!py3 {'div' : CSSDict, 'handle' : CSSDict}`, where `#!py3 'div'` styles the parent Div HTML element and `#!py3 'handle'` styles the handle, if provided. It is also possible to style dynamically the items with callbacks, though it is recommended to rather use `#!py3 'stylesDrag'`, `#!py3 'stylesDrop'`, and `#!py3 'styleLock'`.

Alternatively, a dragged component (e.g. with class name `#!py3 'item'`) can be customized via CSS stylesheets as follows:

```css
.item[data-dnd-dragging="true"] {
    ...
}
```

## Dynamically update the handle

It is possible to update the Dash component used as handle and its position when dragging, dropping, or locking it by passing the arguments `#!py3 dynamicHandle`' and `#!py3 dynamicHandlePos` to [`SortableItem`](../API/sortable_item.md). Both are dictionaries with the following keys:

- `#!py3 'drag'` applied when the item is being dragged
- `#!py3 'drop'` applied when the item is being dropped
- `#!py3 'lock'` applied when the item is locked

For `#!py3 dynamicHandle`, the values associated to the keys must be Dash components, whereas for `#!py3 dynamicHandlePos` they must be either `#!py3 'start'` or `#!py3 'end'`. Alternatively, one can update `#!py3 handle` and `#!py3 handlePos` in a callback using the `#!py3 'isDragging'`, `#!py3 'isDropping'`, and `#!py3 'lock'` properties as inputs, though it is recommended to rather use `#!py3 dynamicHandle`' and `#!py3 dynamicHandlePos`.

In the example below, different icons are used depending on the item's state and its position changes from `#!py3 'start'`' to `#!py3 'end'`' when locked and dragged:

```python
import dash
from   dash_iconify        import DashIconify
from   dash_sortable_items import SortableGroup, SortableItem

app = dash.Dash(__name__)

item = SortableItem(
    id        = 'item',
    children  = 'This is a row with a dynamic handle',
    handle    = DashIconify(icon='majesticons:hand-pointer-line', width=50, height=50), # Default handle when idle
    handlePos = 'start', # Default position when idle
    dynamicHandle    = {
        'drag' : DashIconify(icon='majesticons:hand-pointer-event-line', width=50, height=50), # Handle when dragging
        'drop' : DashIconify(icon='majesticons:arrows-collapse-full',    width=50, height=50), # Handle when dropping
        'lock' : DashIconify(icon='majesticons:lock',                    width=50, height=50)  # Handle when locked
    },
    dynamicHandlePos = {
        'drag' : 'end',   # Handle's position when dragging
        'drop' : 'start', # Handle's position when dropping
        'lock' : 'end'    # Handle's position when locked
    }
)

button = dash.html.Button('Lock/Unlock', id='button')

group = SortableGroup(
    id            = 'group', 
    children      = [item], 
    dropAnimation = {'duration' : 2000}
)

app.layout = dash.html.Div([group, button])

@app.callback(
    dash.Output('item', 'lock'),
    dash.Input('button', 'n_clicks'),
)
def lock(n_clicks: int | None) -> bool:

    if n_clicks is None: raise dash.exceptions.PreventUpdate

    return n_clicks % 2 == 1

app.run(debug=True)
```
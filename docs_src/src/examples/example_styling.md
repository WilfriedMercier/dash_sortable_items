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

## Custom dynamic styling

For each [`SortableItem`](../API/sortable_item.md), it is possible to provide CSS stylesheets that are applied when the item is being dragged or dropped without using callbacks. The three following style dictionaries can be provided:

- `'styles'` which corresponds to the default style
- `'styles_drag'` which is applied on top of '`styles'` when the item is being dragged
- `'styles_drop'` which is applied on top of '`styles'` when the item is being dropped

Each is a dictionary with the following structure `#!py3 {'div' : ..., 'handle' : ...}` where `#!py3 'div'` styles the parent Div HTML element and `#!py3 'handle'` styles the handle, if provided.

Alternatively, it is also possible to style a dragged component with class name `#!py3 'item'` via CSS stylesheets as follows:

```css
.item[data-dnd-dragging="true"] {
    ...
}
```


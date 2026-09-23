## Showing a clone in the sortable list

It is possible to show a clone of the dragged component inside the list by providing `#!py3 showClone = True` to [`SortableGroup`](../API/sortable_group.md). The clone cannot be styled directly but it is possible to override its default style using CSS stylesheets since it holds the `#!css data-dnd-placeholder="clone"` attribute. For instance, in the example below the background of all the clones of [`SortableItem`](../API/sortable_item.md) components with the `item` class name is set to green, and the background of the specific component with ID `mycustomitem` is set to red:

```css
.item[data-dnd-placeholder="clone"] {
    background-color : green !important;
}

#mycustomitem[data-dnd-placeholder="clone"] {
    background-color : red !important;
}
```

## Customizing the drop animation

When a dragged item is released, it is brought to its final position. By default, no animation is shown but it is possible to define one by providing a couple properties in [`SortableGroup`](../API/sortable_group.md) as follows

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

where `#!py3 'duration'` is the length of the animation in millisecond and `#!py3 'easing'` is a [CSS easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Easing_functions).

## Custom styling when dragging

For each [`SortableItem`](../API/sortable_item.md), one can provide `styles_drag` as an argument which is used specifically to style the component when it is being dragged

It is a dictionary with the following structure `#!py3 {'div' : ..., 'handle' : ...}` where `#!py3 'div'` styles the parent Div HTML element and `#!py3 'handle'` styles the handle, if provided.

Alternatively, it is also possible to style the dragged component via CSS stylesheets as follows

```css
.item[data-dnd-dragging="true"] {
    ...
}
```


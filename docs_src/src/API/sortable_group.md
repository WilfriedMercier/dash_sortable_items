!!! note "Note:"
    `SortableGroup` is technically a placeholder for `_SortableGroup`. For type checkers, one may therefore use as type hint

    ```python
    from dash_sortable_items._SortableGroup import _SortableGroup
    ```

## Keyword arguments

| Name | Description | Type |
| ---- | ----------- | ---- |
| `id`   | Unique identifier for the component in callbacks | `#!py3 str` or a dictionary with structure `#!py3 {'type' : ..., 'index' : ...}` |
| `className` | CSS class name used to style the component via CSS stylesheets | `#!py3 str` |
| `dropAnimation` | Dictionary with keys `#!py3 duration` and `#!py3 easing` where `#!py3 duration` is the length of the animation in millisecond and `#!py3 easing` is a CSS easing function. This is applied by default to all [`SortableItem`](./sortable_item.md) children. | `#!py3 {'duration' : ..., 'easing' : ...}` |
| `showClone` | Whether a clone should be shown in the list when dragging the component or not. This is applied by default to all [`SortableItem`](./sortable_item.md) children. | `#!py3 bool` |
| `style`   | CSS style to apply to this component | `#!py3 dict` |

## Values accessible via callbacks

The arguments below can be used to trigger callbacks or can be updated in callbacks.

| Name | Trigger ? | Updatable ? | Information |
| ---  | :-------: | :---------: | ------  |
| `dropAnimation` | :white_check_mark: | :white_check_mark: | The new `dropAnimation` does not take effect immediately but during the next drop operation. |
| `showClone` | :white_check_mark: | :white_check_mark: | The new `showClone` does not take effect immediately but during the next drag operation. |
| `sortedIds` | :white_check_mark: | :white_check_mark: | Can be used to trigger actions depending on the order of the items. Setting `sortedIds` will not update the visual order unless the children are drawn again in the new order. |
| `style` | :white_check_mark: | :white_check_mark: | The new `style` takes effect immediately. |

## Styles

The following classes are avaible to style the component in a CSS stylesheet:

| CSS selector | Description |
| ----         | ----------- |
| `sortable-group` | Div HTML element containing the [`SortableItem`](./sortable_item.md) children |
!!! note "Note:"
    `SortableItem` is technically a placeholder for `_SortableItem`. For type checkers, one may therefore use as type hint

    ```python
    from dash_sortable_items._SortableItem import _SortableItem
    ```

## Mandatory arguments

The following arguments must always be provided when creating a new `SortableItem` component:

| Name | Description | Type |
| ---- | ----------- | ---- |
| id   | Unique identifier for the component in callbacks and to identify uniquely the component within the [`SortableGroup`](./sortable_group.md) list | `#!py3 str` or a dictionary with structure `#!py3 {'type' : ..., 'index' : ...}` |


## Keyword arguments

| Name | Description | Type |
| ---- | ----------- | ---- |
| className | CSS class name used to style the component via CSS stylesheets | `#!py3 str` |
| handle    | Dash component used as handle. If `#!py3 None`, the entire item is used as handle | `#!py3 dict` or `#!py3 None` |
| handlePos | Position of the handle in the parent HTML Div component. Default value is `#!py3 'start'` | `#!py3 'start'`, `#!py3 'end'`, or `#!py3 None` |
| lock | Whether to lock the item or not. Default is `#!py3 False` | `#!py3 bool` |
| restrict | Whether to restrict the item to vertical or horizontal movement only. Default is no restriction. | `#!py3 'vertical'`, `#!py3 'horizontal'`, or `#!py3 None` |
| styles | Dictionary used to style inner components. Each key identifies a component and each value is a dictionary with camel cased CSS properties. Allowed keys are `#!py3 'div'` to style the parent Div HTML element and `#!py3 'handle'` to style the Div HTML element wrapping the handle, if provided | `#!py3 {'div' : {...}, 'handle' : {...}}` |
| styles_drag | Same as `style` but used when the component is being dragged | `#!py3 {'div' : {...}, 'handle' : {...}}` |

## Styles

The following classes are avaible to style the component in a CSS stylesheet:

| CSS selector  | Description |
| ----          | ----------- |
| sortable-item        | Div HTML element containing the children Dash components |
| sortable-item-handle | Div HTML element wrapping the handle |

## Dynamic styling

It is possible to style differently a `SortableItem` via CSS stylesheets while it is being dragged because when a component is dragged it gets a `#!css data-dnd-dragging="true"` attribute. Additionally, one can also style the clone rendered within the list (if visible) since it gets a `#!css data-dnd-placeholder="clone"` attribute. For instance, see below an example where the background of the dragged component is styled with the color `blue` and the clone with the color `green`:


as follows

```css
.item[data-dnd-dragging="true"] {
    background-color : blue !important;
}

.item[data-dnd-placeholder="clone"] {
    background-color : green !important;
}
```
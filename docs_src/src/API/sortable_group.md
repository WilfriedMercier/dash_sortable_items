!!! note "Note:"
    `SortableGroup` is technically a placeholder for `_SortableGroup`. For type checkers, one may therefore use as type hint

    ```python
    from dash_sortable_items._SortableGroup import _SortableGroup
    ```

## Keyword arguments

| Name | Description | Type |
| ---- | ----------- | ---- |
| id   | Unique identifier for the component in callbacks | `#!py3 str` or a dictionary with structure `#!py3 {'type' : ..., 'index' : ...}` |
| style   | CSS style to apply to this component | `#!py3 dict` |
| className | CSS class name used to style the component via CSS stylesheets | `#!py3 str` |

## Styles

The following classes are avaible to style the component in a CSS stylesheet:

| CSS selector | Description |
| ----         | ----------- |
| sortable-group | Div HTML element containing the `SortableItem` child components |
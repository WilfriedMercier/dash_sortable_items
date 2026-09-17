## Mandatory arguments

The following arguments must always be provided when creating a new `SortableItem` component:

| Name | Description | Type |
| ---- | ----------- | ---- |
| id   | Unique identifier for the component in callbacks and to identify uniquely the component within the `SortableGroup` list | `#!py3 str` or a dictionary with structure `#!py3 {"type" : ..., "index" : ...}` |
| index   | Initial position of the component in the list | `#!py3 int` |


## Keyword arguments

| Name | Description | Type |
| ---- | ----------- | ---- |
| handle    | Dash component used as handle. If `#!py3 None`, the entire `SortableItem` is used as handle | `#!py3 dict` or `#!py3 None` |
| handlePos | Position of the handle in the parent HTML Div component. Default value is `#!py3 'start'` | `#!py3 'start'`, `#!py3 'end'`, or `#!py3 None` |
| restrict | Whether to restrict the item to vertical or horizontal movement only. Default is no restriction. | `#!py3 'vertical'`, `#!py3 'horizontal'`, or `#!py3 None` |
| lock | Whether to lock the item or not. Default is `#!py3 False` | `#!py3 bool` |
| className | CSS class name used to style the component via CSS stylesheets | `#!py3 str` |

## Styles

The following classes are avaible to style the component in a CSS stylesheet:

| CSS selector | Description |
| ----         | ----------- |
| sortable-group | Div HTML element containing the `SortableItem` child components |
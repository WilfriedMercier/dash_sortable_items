## Mandatory arguments

The following arguments must always be provided when creating a new `SortableItem` component:

| Name | Description | Type |
| ---- | ----------- | ---- |
| `id`   | Unique identifier for the component in callbacks and to identify uniquely the component within the [`SortableGroup`](./sortable_group.md) list | `#!py3 str` or a dictionary with structure `#!py3 {'type' : ..., 'index' : ...}` |


## Keyword arguments

| Name | Description | Type |
| ---- | ----------- | ---- |
| `children` | Dash components passed as children | |
| `className` | CSS class name used to style the component via CSS stylesheets | `#!py3 str` |
| `dynamicHandle` | Use `handle` to provide a default handle and then `dynamicHandle` to update it dynamically when the item is dragged, dropped, or locked. `dynamicHandle` is a dictionary with keys `#!py3 'drag'`, `#!py3 'drop'`, and `#!py3 'lock'` with each value a Dash component. If `None`, `handle` is used all the time, if provided. | `#!py3 {'drag' : DashComponent, 'drop' : DashComponent 'lock' : DashComponent}` or `None` |
| `dynamicHandlePos` | Use `handlePos` to provide the default position of the handle and then `dynamicHandlePos` to update it dynamically when the item is dragged, dropped, or locked. `dynamicHandlePos` is a dictionary with keys `#!py3 'drag'`, `#!py3 'drop'`, and `#!py3 'lock'` with each value a boolean flag. If `None`, `handlePos` is used all the time. | `#!py3 {'drag' : bool 'drop' : bool 'lock' : bool}` or `None` |
| `handle`    | Dash component used as handle. If `#!py3 None`, the entire item is used as handle | `DashComponent` or `#!py3 None` |
| `handlePos` | Position of the handle in the parent HTML Div component. Default value is `#!py3 'start'` | `#!py3 'start'` or `#!py3 'end'` |
| `lock` | Whether to lock the item or not. Default is `#!py3 False` | `#!py3 bool` |
| `restrict` | Whether to restrict the item to vertical or horizontal movement only. Default is no restriction. | `#!py3 'vertical'` or `#!py3 'horizontal'` |
| `styles` | Dictionary used to style inner components. Each key identifies a component and each value is a dictionary with camel cased CSS properties. Allowed keys are `#!py3 'div'` to style the parent Div HTML element and `#!py3 'handle'` to style the Div HTML element wrapping the handle, if provided | `#!py3 {'div' : CSSDict, 'handle' : CSSDict}` |
| `stylesDrag` | Same as `style` but used when the component is being dragged | `#!py3 {'div' : CSSDict, 'handle' : CSSDict}` |
| `stylesDrop` | Same as `style` but used when the component is dropped | `#!py3 {'div' : CSSDict, 'handle' : CSSDict}` |
| `stylesLock` | Same as `style` but used when the component is locked | `#!py3 {'div' : CSSDict, 'handle' : CSSDict}` |
| `transitionAnimation` | Dictionary used to customize the animation used when an item transitions from one position to another. `#!py3 None` means there is no transition. If not `#!py3 None`, the following keys are mandatory: `#!py3 'duration'` which indicates how long the transition lasts in millisecond and `#!py3 'easing'` which specifies which CSS easing function to use. | `#!py3 {'duration' : int, 'easing' : str}` |

## Values accessible via callbacks

The arguments below can be used to trigger callbacks or can be updated in callbacks.

| Name | Trigger ? | Updatable ? | Comment |
| ---  | :-------: | :---------: | ------  |
| `dynamicHandle` | :white_check_mark: | :white_check_mark: | For advanced usage when the dynamic styles needs to be updated in a callback. |
| `dynamicHandlePos` | :white_check_mark: | :white_check_mark: | For advanced usage when the dynamic position of the handle needs to be updated in a callback. |
| `handle` | :white_check_mark: | :white_check_mark: | To update the handle when the item is dragged, dropped, or locked, use instead `dynamicHandle` when creating the item. |
| `handlePos` | :white_check_mark: | :white_check_mark: | To update the position of the handle when the item is dragged, dropped, or locked, use instead `dynamicHandlePos` when creating the item. |
| `isDragging` | :white_check_mark: | :x: | Boolean flag specifying whether the item is currently being dragged or not. |
| `isDropping` | :white_check_mark: | :x: | Boolean flag specifying whether the item is currently being dropped or not. Note that the drop animation set in [`SortableGroup`](../API/sortable_group.md) may need to be long enough for it to trigger. |
| `lock` | :white_check_mark: | :white_check_mark: | Can be used to lock/unlock items when pressing a button. |
| `styles` | :white_check_mark: | :white_check_mark: | If used as ouput, the styles are updated immediately. |
| `stylesDrag` | :white_check_mark: | :white_check_mark: | If used as ouput, the styles are updated as soon as the item is dragged. |
| `stylesDrop` | :white_check_mark: | :white_check_mark: | If used as ouput, the styles are updated as soon as the item is dropped. |
| `stylesLock` | :white_check_mark: | :white_check_mark: | If used as ouput, the styles are updated immediately if the item is locked. |
| `transitionAnimation` | :white_check_mark: | :white_check_mark: | Can be used to update the animation depending on the order of the items |


## Styles

The following classes are avaible to style the component in a CSS stylesheet:

| CSS selector  | Description |
| ----          | ----------- |
| `sortable-item`        | Div HTML element containing the children Dash components |
| `sortable-item-handle` | Div HTML element wrapping the handle |

## Dynamic styling with CSS stylesheets

It is possible to style differently a `SortableItem` via CSS stylesheets while it is being dragged because a dragged component gets a `#!css data-dnd-dragging="true"` attribute. Additionally, one can also style the clone rendered within the list (if visible) since it gets a `#!css data-dnd-placeholder="clone"` attribute. For instance, see below an example where the background of the dragged component is styled with the color `blue` and the clone with the color `green`:


as follows

```css
.item[data-dnd-dragging="true"] {
    background-color : blue !important;
}

.item[data-dnd-placeholder="clone"] {
    background-color : green !important;
}
```
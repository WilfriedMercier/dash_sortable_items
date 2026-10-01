import json
from   setuptools import setup

with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

readme = '''
## Basic usage

This python package provides two new Dash components: `SortableGroup` and `SortableItem`. A `SortableGroup` must only contain `SortableItem` components and exposes in callbacks the `sortedIDs` property which can be used to retrieve the order of the children. Each `SortableItem` is a Dash component that can be dragged and sorted within its parent group. See below for a typical example.

**Note:** Drag and drop can be cancelled at any moment by pressing the Esc key

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

Note that **all `SortableItem` component must have `id` provided** as it uniquely identifies the component in its parent group.

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

For more details on `SortableGroup` and `SortableItem` see the [documentation](https://wilfriedmercier.github.io/dash_sortable_items/).
'''

setup(
    name                 = package_name,
    version              = package["version"],
    author               = package['author'],
    packages             = [package_name],
    include_package_data = True,
    license              = package['license'],
    description          = package.get('description', package_name),
    install_requires     = [],
    keywords             = ['dnd-kit', 'plotly-dash'],
    classifiers          = [
        'Framework :: Dash',
    ],
    url                           = package.get('homepage'),
    long_description              = readme,
    long_description_content_type = 'text/markdown',
    project_urls                  = {
        'Issues' : package.get('issuespage'),
        'Documentation' : package.get('docpage')
    }
)

import dash
from   dash_iconify        import DashIconify
from   dash_sortable_items import SortableGroup, SortableItem

app = dash.Dash(__name__, assets_folder='./')

item1 = SortableItem(
    id        = 'item1',
    children  = [dash.html.Label('Row #1')],
    className = 'item'
)

item2 = SortableItem(
    id        = 'item2',
    children  = [dash.html.Label('Row #2')],
    className = 'item'
)

item3 = SortableItem(
    id        = 'item3',
    children  = [dash.html.Label('Row #3')],
    handle    = DashIconify(icon='iconmind:drag-handle-duotone-bold', width=30, height=30),
    className = 'item',
)

group = SortableGroup(
    [item1, item2, item3],
    id        = 'group',
    className = 'group',
    showClone = True
)

label = dash.html.Label('Order:', id='label')

app.layout = dash.html.Div([group, label], className='container')

@app.callback(
    dash.Output('label', 'children'),
    dash.Input('group', 'sortedIds')
)
def _(sortedIDs: list | None) -> str:

    if sortedIDs is None: raise dash.exceptions.PreventUpdate
    return f'Order: {sortedIDs}'

app.run(debug=True)
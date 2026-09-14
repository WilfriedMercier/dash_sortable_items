import dash
from   dash_sortable_items import SortableGroup, SortableItem

app = dash.Dash(__name__, assets_folder='./')

item1 = SortableItem(
    id        = 'item1', 
    index     = 1,
    children  = [dash.html.Label('Row #1')],
    className = 'item'
)

item3 = SortableItem(
    id        = 'item3', 
    index     = 3,
    children  = [dash.html.Label('Row #3')],
    className = 'item'
)

item2 = SortableItem(
    id        = 'item2', 
    index     = 2,
    children  = [dash.html.Label('Row #2')],
    className = 'item'
)

group = SortableGroup(
    id        = 'group',
    children  = [item1, item3, item2],
    className = 'group'
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
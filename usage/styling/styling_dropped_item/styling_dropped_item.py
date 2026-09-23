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
    styles_drop = {
        'div' : {
            'border'  : '3px solid darkgreen',
            'opacity' : 1,
            'rotate' : '180deg'
        },
        'handle' : {
            'width'  : '60px',
            'height' : '60px'
        }
    }
)

group = SortableGroup(
    [item1, item2, item3],
    id        = 'group',
    className = 'group',
    dropAnimation = {'duration' : 2000, 'easing' : 'ease'}
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
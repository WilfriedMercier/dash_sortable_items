import dash
from   dash_iconify                       import DashIconify
from   dash_sortable_items                import SortableGroup, SortableItem
from   dash_sortable_items._SortableGroup import _SortableGroup

app = dash.Dash(__name__, assets_folder='./')

def draw_items() -> _SortableGroup:

    item1 = SortableItem(
        id        = 'ducky',
        children  = [DashIconify(icon='noto:duck', width=50, height=50)]*10,
        className = 'item'
    )

    item2 = SortableItem(
        id        = 'doggo',
        children  = [DashIconify(icon='noto-v1:dog', width=50, height=50)]*10,
        className = 'item'
    )

    item3 = SortableItem(
        id        = 'rosie',
        children  = [DashIconify(icon='noto-v1:rose', width=50, height=50)]*10,
        className = 'item'
    )

    group = SortableGroup(
        id        = 'group',
        items     = [item1, item2, item3],
        className = 'group'
    )

    return group

group           = draw_items()
group_container = dash.html.Div(group, id='group-container', className='group-container')

button = dash.dcc.Button(
    'Click me to reset the list',
    style     = {'maxWidth' : '150px'},
    id        = 'button',
    className = 'button'
)

label = dash.html.Label('Order:', id='label')

app.layout = dash.html.Div([
        dash.html.Div(
            [group_container, button], 
            style = {
                'display'       : 'flex', 
                'flexDirection' : 'row',
                'gap'           : '20px'
        }), 
        label
    ], 
    className='container')

@app.callback(
    dash.Output('label', 'children'),
    dash.Input('group', 'sortedIds')
)
def _(sortedIds: list[str] | None) -> str: 

    if sortedIds is None: raise dash.exceptions.PreventUpdate

    return '/'.join(sortedIds)

@app.callback(
    dash.Output('group-container', 'children'),
    dash.Output('group', 'sortedIds'),
    dash.Input('button', 'n_clicks')
)
def re_order(_) -> tuple[_SortableGroup, list[str]]:

    if _ is None: raise dash.exceptions.PreventUpdate

    return draw_items(), ['ducky', 'doggo', 'rosie']

app.run(debug=True)
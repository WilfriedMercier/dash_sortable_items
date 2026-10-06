import dash
from   dash_iconify        import DashIconify
from   dash_sortable_items import SortableGroup, SortableItem

app = dash.Dash(__name__, assets_folder='./')

item1 = SortableItem(
    id         = {'type' : 'item', 'index' : 1},
    children   = [dash.html.Label('Row #1')],
    lock       = True,
    handle     = DashIconify(icon='iconmind:drag-handle-duotone-bold', width=30, height=30),
    handlePos = 'start',
    stylesLock = {
        'div'    : {'borderColor' : 'red'},
        'handle' : {'border' : 'solid 1px'}
    },
    dynamicHandle = {
        'lock' : DashIconify(icon='ant-design:lock-twotone', width=30, height=30)
    },
    dynamicHandlePos = {
        'lock' : 'end'
    },
    className  = 'item'
)

item2 = SortableItem(
    id        = {'type' : 'item', 'index' : 2},
    lock      = True,
    children  = [dash.html.Label('Row #2')],
    className = 'item'
)

group = SortableGroup(
    children  = [item1, item2],
    id        = 'group',
    className = 'group',
    dropAnimation = {'duration' : 2000, 'easing' : 'ease'}
)

button = dash.html.Button('Lock/Unlock', id='button')

app.layout = dash.html.Div([group, button], className='container')

@app.callback(
    dash.Output({'type' : 'item', 'index' : dash.ALL}, 'lock'),
    dash.Input('button', 'n_clicks')
)
def _(n_clicks: int | None) -> tuple[bool, bool]:

    if n_clicks is None: raise dash.exceptions.PreventUpdate

    if n_clicks % 2 == 0:
        return (True, True)

    return (False, False)

app.run(debug=True)
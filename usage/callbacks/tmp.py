import dash
from   dash_iconify        import DashIconify
from   dash_sortable_items import SortableGroup, SortableItem

app = dash.Dash(__name__)

item = SortableItem(
    id        = 'item',
    children  = 'This is a row with a dynamic handle',
    handle    = DashIconify(icon='majesticons:hand-pointer-line', width=50, height=50), # Default handle when idle
    handlePos = 'start', # Default position when idle
    dynamicHandle    = {
        'drag' : DashIconify(icon='majesticons:hand-pointer-event-line', width=50, height=50), # Handle when dragging
        'drop' : DashIconify(icon='majesticons:arrows-collapse-full',    width=50, height=50), # Handle when dropping
        'lock' : DashIconify(icon='majesticons:lock',                    width=50, height=50)  # Handle when locked
    },
    dynamicHandlePos = {
        'drag' : 'end',   # Handle's position when dragging
        'drop' : 'start', # Handle's position when dropping
        'lock' : 'end'    # Handle's position when locked
    }
)

button = dash.html.Button('Lock/Unlock', id='button')

group = SortableGroup(
    id            = 'group', 
    children      = [item], 
    dropAnimation = {'duration' : 2000}
)

app.layout = dash.html.Div([group, button])

@app.callback(
    dash.Output('item', 'lock'),
    dash.Input('button', 'n_clicks'),
)
def lock(n_clicks: int | None) -> bool:

    if n_clicks is None: raise dash.exceptions.PreventUpdate

    return n_clicks % 2 == 1

app.run(debug=True)
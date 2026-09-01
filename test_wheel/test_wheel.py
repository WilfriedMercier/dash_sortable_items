import dash_sortable_items
import dash

app = dash.Dash()

item1 = dash_sortable_items.SortableItem(
    id        = 'component1', 
    index     = 1,
    children  = [dash.html.Label('First row')],
    className = 'row',
    handle    = dash.html.Label('🟢')
)

item2 = dash_sortable_items.SortableItem(
    id        = 'component2', 
    index     = 0,
    children  = [dash.html.Label('🔒 Second item is locked 🔒'), dash.html.Button('Click me !')],
    className = 'row',
    lock      = True,
    styles    = {'div' : {'opacity' : '0.5'}} # type: ignore
)

item3 = dash_sortable_items.SortableItem(
    id        = 'component3', 
    index     = 2,
    children  = [dash.dcc.Input('Insert text here'), dash.html.Label('Blablabla')],
    className = 'row'
)

item4 = dash_sortable_items.SortableItem(
    id        = 'component4', 
    index     = 3,
    children  = [dash.html.Label('Such a nice handle 🠦')],
    className = 'row',
    handle    = dash.html.Label('🥀'),
    handlePos = 'end'
)


group = dash_sortable_items.SortableGroup(
    id       = 'group',
    children = [item1, item2, item3, item4]
)

button = dash.dcc.Button('click me', id='button')

app.layout = dash.html.Div([group, button])

@app.callback(
    dash.Output('group', 'style'),
    dash.Input('button', 'n_clicks'),
    prevent_initial_callback = True
)
def update_style(_) -> dict[str, str]:

    if _ is None: raise dash.exceptions.PreventUpdate

    print('Clicking !')
    return {'display' : 'flex', 'flexDirection' : 'row', 'backgroundColor' : 'blue'}

if __name__ == '__main__':
    app.run(debug=True)

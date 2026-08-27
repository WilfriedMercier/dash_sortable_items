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

app.layout = group


if __name__ == '__main__':
    app.run(debug=True)

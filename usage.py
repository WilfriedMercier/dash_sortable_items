from   dash_sortable_items import SortableGroup, SortableItem
import dash

app = dash.Dash(__name__)

items = [
    SortableItem(
        id        = f'item{i}', 
        index     = i,
        restrict  = 'horizontal' if i == 0 else None,
        children  = [dash.html.Label(f'Row #{i}')],
        className = 'row'
    )
    for i in range(10)
]

group = SortableGroup(
    id        = 'group',
    className = 'group',
    children  = items,
)

label  = dash.html.Label('', id='label')

app.layout = dash.html.Div([group, label], style={'display' : 'flex'})

if __name__ == '__main__':
    app.run(debug=True)

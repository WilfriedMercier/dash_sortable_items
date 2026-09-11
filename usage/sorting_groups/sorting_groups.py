import dash
from   dash_sortable_items import SortableGroup, SortableItem

app = dash.Dash(__name__, assets_folder='./')

def generate_items(group_name: str) -> list[SortableItem]:

    out = []
    for i in range(2):

        out.append(
            SortableItem(
                id        = f'{group_name}-item{i}', 
                index     = i,
                children  = [dash.html.Label(f'Row #{i} in group {group_name}')],
                className = 'item'
            )
        )

    return out

group1 = SortableItem(
    [
        dash.html.H3('First sortable group'),
        SortableGroup(
            id        = 'group1',
            children  = generate_items('First group'),
            className = 'group'
        )
    ],
    className = 'sortable-group',
    id        = 'group1-item',
    index     = 1
)

group2 = SortableItem(
    [
        dash.html.H3('Second sortable group'),
        SortableGroup(
            id        = 'group2',
            children  = generate_items('Second group'),
            className = 'group'
        )
    ],
    className = 'sortable-group',
    id        = 'group2-item',
    index     = 0
)

app.layout = SortableGroup([group1, group2])

app.run(debug=True)
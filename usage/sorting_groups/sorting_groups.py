import dash
from   dash_sortable_items import SortableGroup, SortableItem

app = dash.Dash(__name__, assets_folder='./')

def generate_items(group_name: str) -> list[SortableItem]:

    out = []
    for i in range(2):

        out.append(
            SortableItem(
                id        = f'{group_name}-item{i}',
                children  = [dash.html.Label(f'Row #{i} in group {group_name}')],
                className = 'item'
            )
        )

    return out

group1 = SortableItem(
    children  = [
        dash.html.H3('First sortable group'),
        SortableGroup(
            id        = 'group1',
            items     = generate_items('First group'),
            className = 'group'
        )
    ],
    className = 'inner-group',
    id        = 'group1-item',
)

group2 = SortableItem(
    children = [
        dash.html.H3('Second sortable group'),
        SortableGroup(
            id        = 'group2',
            items     = generate_items('Second group'),
            className = 'group'
        )
    ],
    className = 'inner-group',
    id        = 'group2-item'
)

app.layout = SortableGroup(items = [group1, group2], id='')

app.run(debug=True)
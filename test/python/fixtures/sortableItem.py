'''Fixtures to test the callbacks of the sortableItem component.'''

import dash
import pytest
from   dash_sortable_items    import SortableGroup, SortableItem

@pytest.fixture
def app_button__item() -> dash.Dash:
    '''Fixture that creates a Dash app with a single group and a button.'''

    app = dash.Dash(__name__)

    item1 = SortableItem(
        id        = 'item1', 
        index     = 0,
        children  = [dash.html.Label('First row')],
        handle    = dash.html.Label('☃'),
        handlePos = 'start',
        styles    = {
            'handle' : {'backgroundColor' : 'red'},
            'div'    : {'backgroundColor' : 'yellow'}
        }, # type: ignore
        className = 'row'
    )
    
    item2 = SortableItem(
        id        = 'item2', 
        index     = 1,
        children  = [dash.html.Label('Second row')],
        className = 'row',
    )

    group = SortableGroup(
        id        = 'group',
        className = 'group',
        children  = [item1, item2]
    )

    button = dash.dcc.Button('Click me !', id = 'button')

    # Store the order the IDs of the items in the group.
    sortedIDs = dash.dcc.Store('sortedIDs', data = None)

    app.layout = dash.html.Div([group, button, sortedIDs], style={'display' : 'flex'})

    return app
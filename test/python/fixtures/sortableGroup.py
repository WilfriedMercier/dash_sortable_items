'''Fixtures to test the callbacks of the sortableGroup component.'''

import dash
import pytest
from   dash_sortable_items    import SortableGroup, SortableItem

@pytest.fixture
def app_button__group() -> dash.Dash:
    '''Fixture that creates a Dash app with a single group and a button.'''

    app = dash.Dash(__name__)

    item1 = SortableItem(
        id        = 'component-locked1', 
        index     = 0,
        children  = [dash.html.Label('First row')],
        lock      = True,
        className = 'row'
    )
    
    item2 = SortableItem(
        id        = 'component-free', 
        index     = 1,
        children  = [dash.html.Label('Second row')],
        className = 'row',
    )

    group = SortableGroup(
        id        = 'group',
        className = 'group',
        children  = [item1, item2],
        style     = {'display' : 'flex', 'flexDirection' : 'column', 'backgroundColor' : 'red'}
    )

    button = dash.dcc.Button('Click me !', id = 'button')

    app.layout = dash.html.Div([group, button], style={'display' : 'flex'})

    return app

@pytest.fixture
def app_label__group() -> dash.Dash:
    '''Fixture that creates a Dash app with a single group and a button.'''

    app = dash.Dash(__name__)

    item1 = SortableItem(
        id        = 'item1', 
        index     = 0,
        children  = [dash.html.Label('First row')],
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
        children  = [item1, item2],
    )

    label  = dash.html.Label('', id='label')

    app.layout = dash.html.Div([group, label], style={'display' : 'flex'})

    return app
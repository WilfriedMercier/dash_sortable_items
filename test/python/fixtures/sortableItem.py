'''Fixtures to test the callbacks of the sortableItem component.'''

import dash
import pytest
from   dash_sortable_items import SortableGroup, SortableItem

@pytest.fixture
def app_button__item() -> dash.Dash:
    '''Fixture that creates a Dash app with a single group and a button.'''

    app = dash.Dash(__name__)

    item1 = SortableItem(
        id        = 'item1',
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
        children  = [dash.html.Label('Second row')],
        className = 'row',
    )

    group = SortableGroup(
        id        = 'group',
        className = 'group',
        items     = [item1, item2]
    )

    button = dash.dcc.Button('Click me !', id = 'button')

    app.layout = dash.html.Div([group, button], style={'display' : 'flex'})

    return app

@pytest.fixture
def app_button_no_handle__item() -> dash.Dash:
    '''Fixture that creates a Dash app with a single group and a button where the layout is vertical.'''

    app = dash.Dash(__name__)

    item1 = SortableItem(
        id        = 'item1',
        restrict  = None,
        children  = [dash.html.Label('First row')],
        className = 'row'
    )
    
    item2 = SortableItem(
        id        = 'item2',
        children  = [dash.html.Label('Second row')],
        className = 'row',
    )

    group = SortableGroup(
        id        = 'group',
        className = 'group',
        items     = [item1, item2]
    )

    button = dash.dcc.Button('Click me !', id = 'button')

    app.layout = dash.html.Div([group, button], style={'display' : 'flex'})

    return app

@pytest.fixture
def app_drag_style__item() -> dash.Dash:
    '''Fixture that creates a Dash app with items whose style changes when being dragged.'''

    app = dash.Dash(__name__)

    item1 = SortableItem(
        id        = 'item1',
        children  = [dash.html.Label('First row')],
        handle    = dash.html.Label('☃'),
        handlePos = 'start',
        styles    = {
            'handle' : {'backgroundColor' : 'red'},
            'div'    : {'backgroundColor' : 'yellow'}
        },
        styles_drag = {
            'handle' : {'backgroundColor' : 'green'},
            'div'    : {'backgroundColor' : 'blue', 'rotate' : '180deg'}
        },
        className = 'row'
    )
    
    item2 = SortableItem(
        id        = 'item2',
        children  = [dash.html.Label('Second row')],
        className = 'row',
    )

    group = SortableGroup(
        id        = 'group',
        className = 'group',
        items     = [item1, item2]
    )

    app.layout = dash.html.Div(group, style={'display' : 'flex'})

    return app

@pytest.fixture
def app_drop_style__item() -> dash.Dash:
    '''Fixture that creates a Dash app with items whose style changes when being dropped.'''

    app = dash.Dash(__name__)

    item1 = SortableItem(
        id        = 'item1',
        children  = [dash.html.Label('First row')],
        handle    = dash.html.Label('☃'),
        handlePos = 'start',
        styles    = {
            'handle' : {'backgroundColor' : 'red'},
            'div'    : {'backgroundColor' : 'yellow'}
        },
        styles_drop = {
            'handle' : {'backgroundColor' : 'green'},
            'div'    : {'backgroundColor' : 'blue', 'rotate' : '180deg'}
        },
        className = 'row'
    )
    
    item2 = SortableItem(
        id        = 'item2',
        children  = [dash.html.Label('Second row')],
        className = 'row',
    )

    group = SortableGroup(
        id            = 'group',
        className     = 'group',
        items         = [item1, item2],
        dropAnimation = {'duration' : 3000, 'easing' : 'ease'}
    )

    app.layout = dash.html.Div(group, style={'display' : 'flex'})

    return app
import dash
import pytest
from   dash_sortable_items import SortableGroup, SortableItem

@pytest.fixture
def app_with_four_items() -> dash.Dash:
    '''Fixture that creates a Dash app with a single group and four sortable items as children.'''

    app = dash.Dash(__name__)
    
    item1 = SortableItem(
        id        = 'component1', 
        index     = 1,
        children  = [dash.html.Label('First row')],
        className = 'row',
        handle    = dash.html.Label('🟢')
    )

    item2 = SortableItem(
        id        = 'component2', 
        index     = 0,
        children  = [dash.html.Label('🔒 Second item is locked 🔒'), dash.html.Button('Click me !')],
        className = 'row',
        lock      = True,
        styles    = {'div' : {'opacity' : '0.5'}} # type: ignore
    )

    item3 = SortableItem(
        id        = 'component3', 
        index     = 2,
        children  = [dash.dcc.Input('Insert text here', style={'width' : '10%'}), dash.html.Label('Blablabla')],
        className = 'row'
    )

    item4 = SortableItem(
        id        = 'component4', 
        index     = 3,
        children  = [dash.html.Label('Such a nice handle 🠦')],
        className = 'row',
        handle    = dash.html.Label('🥀'),
        handlePos = 'end'
    )

    group = SortableGroup(
        id        = 'group',
        className = 'group',
        children  = [item1, item2, item3, item4]
    )

    app.layout = group

    return app

@pytest.fixture
def app_with_two_items() -> dash.Dash:
    '''Fixture that creates a Dash app with a single group containing two items: one with a handle and one without.'''

    app = dash.Dash(__name__)
    
    item1 = SortableItem(
        id        = 'component1', 
        index     = 0,
        children  = [dash.html.Label('First row')],
        className = 'row',
        handle    = dash.html.Label('🟢')
    )

    item2 = SortableItem(
        id        = 'component2', 
        index     = 1,
        children  = [dash.html.Label('Second row')],
        className = 'row'
    )

    group = SortableGroup(
        id        = 'group',
        className = 'group',
        children  = [item1, item2]
    )

    app.layout = group

    return app

@pytest.fixture
def app_with_two_handle_positions() -> dash.Dash:
    '''Fixture that creates a Dash app with one item with a handle on the left-hand side and another one on the right-hand side.'''

    app = dash.Dash(__name__)

    item1 = SortableItem(
        id        = 'component-left', 
        index     = 0,
        children  = [dash.html.Label('First row')],
        handle    = dash.html.Label('☰'),
        handlePos = 'start',
        lock      = True,
        className = 'row'
    )
    
    item2 = SortableItem(
        id        = 'component-right', 
        index     = 1,
        children  = [dash.html.Label('Second row')],
        handle    = dash.html.Label('☰'),
        handlePos = 'end',
        className = 'row',
    )

    group = SortableGroup(
        id        = 'group',
        className = 'group',
        children  = [item1, item2]
    )

    app.layout = group

    return app

@pytest.fixture
def app_with_locked_items() -> dash.Dash:
    '''Fixture that creates a Dash app with a single group containing two free and one locked item.'''

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

    item3 = SortableItem(
        id        = 'component-locked2', 
        index     = 2,
        children  = [dash.html.Label('Third row')],
        lock      = True,
        className = 'row',
        handle    = dash.html.Label('🟢')
    )

    group = SortableGroup(
        id        = 'group',
        className = 'group',
        children  = [item1, item2, item3]
    )

    app.layout = group

    return app
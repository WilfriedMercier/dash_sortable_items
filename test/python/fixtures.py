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

@pytest.fixture
def simple_app_with_button_changing_style() -> dash.Dash:
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

    @app.callback(
        dash.Output('group', 'style'),
        dash.Input('button', 'n_clicks'),
        dash.State('group', 'style'),
        prevent_initial_callback = True
    )
    def update_style(_, old_style: dict[str, str]) -> dict[str, str]:

        if _ is None: raise dash.exceptions.PreventUpdate

        return old_style | {'flexDirection' : 'row', 'backgroundColor' : 'blue'}

    return app

@pytest.fixture
def simple_app_with_label() -> dash.Dash:
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

    @app.callback(
        dash.Output('label', 'children'),
        dash.Input('group', 'sortedIds'),
        prevent_initial_callback = True
    )
    def update_style(ids: list) -> str:

        if ids is None: raise dash.exceptions.PreventUpdate

        return '/'.join(ids)

    return app
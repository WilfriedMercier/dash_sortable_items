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

    @app.callback(
        dash.Output('label', 'children'),
        dash.Input('group', 'sortedIds'),
        prevent_initial_callback = True
    )
    def update_style(ids: list) -> str:

        if ids is None: raise dash.exceptions.PreventUpdate

        return '/'.join(ids)

    return app
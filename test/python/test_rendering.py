'''Integration tests that check that rendering of the SortableGroup and SortableItem components works as expected.'''

import dash
from   dash.testing.composite       import DashComposite
from   selenium.webdriver.common.by import By

from   .fixtures import (
    app_with_four_items,
    app_with_two_handle_positions
)

def test_group_and_items_global_rendering(dash_duo: DashComposite, app_with_four_items: dash.Dash) -> None:
    r'''Checks that a single group element and its item children are all rendered correctly.'''

    dash_duo.start_server(app_with_four_items)

    # Check that the group object is rendered
    element = dash_duo.find_element('group', attribute='ID')
    assert element.get_attribute('id') == 'group'

    # Check that all items are rendered and are children of the group
    rows = element.find_elements(By.CLASS_NAME, 'row')
    assert len(rows) == 4, 'Wrong number of items'

    return

def test_order_of_items(dash_duo: DashComposite, app_with_four_items: dash.Dash) -> None:
    r'''Checks that items are rendered at startup correctly based on their index value.'''

    dash_duo.start_server(app_with_four_items)

    element = dash_duo.find_element('group', attribute='ID')
    rows    = element.find_elements(By.CLASS_NAME, 'row')

    ids_in_order = [f'component{i}' for i in (2, 1, 3, 4)]

    for pos, row in enumerate(rows):
        assert row.get_attribute('id') == ids_in_order[pos], f'Row {pos} does not have the right ID.'

    return

def test_component1_children_rendering(dash_duo: DashComposite, app_with_four_items: dash.Dash) -> None:
    '''Check that the children of the first component are rendered correctly.'''

    dash_duo.start_server(app_with_four_items)

    row = dash_duo.find_element('component1', attribute='ID')

    # Check that the component does not have the dnd-kit button props
    assert row.get_attribute('role') != 'button', 'component1 should not be draggable because it has a handle.'

    children = row.find_elements(By.XPATH, "./child::*")

    # Check that the item has two children, one div and one label
    assert len(children) == 2, 'Wrong number of children found in component1.'

    tags = ['div', 'label']
    for tag, child in zip(tags, children):
        assert child.tag_name == tag

    # Check that the div has the right properties for a dnd-kit handle
    assert children[0].get_attribute('role') == 'button', 'Wrong role for div child in component1.'

    children_of_div = children[0].find_elements(By.XPATH, "./child::*")
    assert len(children_of_div) == 1, 'Wrong number of children found for the handle.'
    assert children_of_div[0].tag_name == 'label', 'Child of the div handle is not a label.'

    return

def test_component2_children_rendering(dash_duo: DashComposite, app_with_four_items: dash.Dash) -> None:
    '''Check that the children of the second component are rendered correctly.'''

    dash_duo.start_server(app_with_four_items)

    row = dash_duo.find_element('component2', attribute='ID')

    # Check that the component does have the dnd-kit button props but is disabled
    assert row.get_attribute('role') == 'button', 'component2 should be draggable because it does not have a handle.'
    assert row.get_attribute('aria-disabled') == 'true', 'component2 is enabled but it should be disabled.'

    children = row.find_elements(By.XPATH, "./child::*")

    # Check that the item has two children, one div and one label
    assert len(children) == 2, 'Wrong number of children found in component2.'

    tags = ['label', 'button']
    for tag, child in zip(tags, children):
        assert child.tag_name == tag

    return

def test_component3_children_rendering(dash_duo: DashComposite, app_with_four_items: dash.Dash) -> None:
    '''Check that the children of the third component are rendered correctly.'''

    dash_duo.start_server(app_with_four_items)

    row = dash_duo.find_element('component3', attribute='ID')

    # Check that the component does have the dnd-kit button props but is disabled
    assert row.get_attribute('role') == 'button', 'component3 should be draggable because it does not have a handle.'
    assert row.get_attribute('aria-disabled') == 'false', 'component2 is disabled but it should be enabled.'

    children = row.find_elements(By.XPATH, "./child::*")

    # Check that the item has two children, one div and one label
    assert len(children) == 2, 'Wrong number of children found in component3.'

    tags = ['div', 'label']
    for tag, child in zip(tags, children):
        assert child.tag_name == tag

    children_of_div = children[0].find_elements(By.XPATH, "./child::*")
    assert len(children_of_div) == 1, 'Wrong number of children found for the first child of component3.'
    assert children_of_div[0].tag_name == 'input', 'Child of the div handle is not an input.'

    return

def test_handle_position(dash_duo: DashComposite, app_with_two_handle_positions: dash.Dash) -> None:
    '''Check that the handle is positioned correctly based on the handlePos props.'''

    dash_duo.start_server(app_with_two_handle_positions)

    # Check that handle is on the left-hand side
    element  = dash_duo.find_element('component-left', attribute='ID')
    children = element.find_elements(By.XPATH, "./child::*")
    assert len(children) == 2, 'Wrong number of children in component-left'
    assert children[0].get_attribute('role') == 'button', 'Handle not correctly placed in component-left'

    # Check that handle is on the right-hand side
    element  = dash_duo.find_element('component-right', attribute='ID')
    children = element.find_elements(By.XPATH, "./child::*")
    assert len(children) == 2, 'Wrong number of children in component-right'
    assert children[1].get_attribute('role') == 'button', 'Handle not correctly placed in component-right'

    return
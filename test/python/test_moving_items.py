import dash
from   dash.testing.composite                  import DashComposite
from   selenium.webdriver.common.action_chains import ActionChains
from   selenium.webdriver.common.by            import By

from   .fixtures.general import (
    app_with_two_items,
    app_with_locked_items
)

def test_moving_unlocked_item_without_handle(dash_duo: DashComposite, app_with_two_items: dash.Dash) -> None:
    '''Check that a SortableItem without a handle can be dragged around.'''

    dash_duo.start_server(app_with_two_items)
    actions = ActionChains(dash_duo.driver)

    source = dash_duo.find_element('component2', attribute='ID')
    target = dash_duo.find_element('component1', attribute='ID')

    initial_locations = {
        'source' : source.location.copy(),
        'target' : target.location.copy()
    }

    # Click and drag + release -> it should move the source to the top and move the target down
    actions.click_and_hold(source)
    actions.pause(0.5)
    actions.move_to_element(target)
    actions.pause(0.5)
    actions.release().perform()

    final_locations = {
        'source' : source.location.copy(),
        'target' : target.location.copy()
    }

    # Check that positions have changed
    assert initial_locations != final_locations, 'Dragging and dropping component2 failed.'
    assert final_locations['source']['y'] < initial_locations['source']['y'], 'source did not move vertically'
    assert final_locations['target']['y'] > initial_locations['target']['y'], 'target did not move vertically'
    assert final_locations['source']['y'] < final_locations['target']['y'], 'source is not above target after drag and drop'

    return

def test_moving_unlocked_item_with_handle(dash_duo: DashComposite, app_with_two_items: dash.Dash) -> None:
    '''Check that a SortableItem with a handle (can) cannot be dragged if clicked (inside) outside of the handle.'''

    dash_duo.start_server(app_with_two_items)
    actions = ActionChains(dash_duo.driver)

    source = dash_duo.find_element('component1', attribute='ID')
    target = dash_duo.find_element('component2', attribute='ID')

    initial_locations = {
        'source' : source.location.copy(),
        'target' : target.location.copy()
    }

    # Check that moving does not work when clicking outside of the handle
    actions.click_and_hold(source)
    actions.pause(0.5)
    actions.move_to_element(target)
    actions.pause(0.5)
    actions.release().perform()

    final_locations = {
        'source' : source.location.copy(),
        'target' : target.location.copy()
    }

    assert initial_locations == final_locations, 'Dragging and dropping should not work outside of handle when provided.'

    # Check that dragging the handle does move the row as expected
    handle = source.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')
    
    actions.click_and_hold(handle)
    actions.pause(0.5)
    actions.move_to_element(target)
    actions.pause(0.5)
    actions.release().perform()

    final_locations = {
        'source' : source.location.copy(),
        'target' : target.location.copy()
    }
    
    assert initial_locations != final_locations, 'Dragging and dropping component1 failed.'
    assert final_locations['source']['y'] > initial_locations['source']['y'], 'source did not move vertically'
    assert final_locations['target']['y'] < initial_locations['target']['y'], 'target did not move vertically'
    assert final_locations['source']['y'] > final_locations['target']['y'], 'source is not below target after drag and drop'

    return

def test_moving_locked_item_without_handle(dash_duo: DashComposite, app_with_locked_items: dash.Dash) -> None:
    '''Check that a SortableItem without a handle that is locked cannot be moved.'''

    dash_duo.start_server(app_with_locked_items)
    actions = ActionChains(dash_duo.driver)

    source = dash_duo.find_element('component-locked1', attribute='ID')
    target = dash_duo.find_element('component-free',    attribute='ID')

    initial_locations = {
        'source' : source.location.copy(),
        'target' : target.location.copy()
    }

    # Check that dragging does not work
    actions.click_and_hold(source)
    actions.pause(0.5)
    actions.move_to_element(target)
    actions.pause(0.5)
    actions.release().perform()

    final_locations = {
        'source' : source.location.copy(),
        'target' : target.location.copy()
    }

    assert initial_locations == final_locations, 'Dragging should not work on locked items.'

    return

def test_moving_locked_item_with_handle(dash_duo: DashComposite, app_with_locked_items: dash.Dash) -> None:
    '''Check that a SortableItem with a handle that is locked cannot be moved.'''

    dash_duo.start_server(app_with_locked_items)
    actions = ActionChains(dash_duo.driver)

    source = dash_duo.find_element('component-locked2', attribute='ID')
    target = dash_duo.find_element('component-free',    attribute='ID')

    initial_locations = {
        'source' : source.location.copy(),
        'target' : target.location.copy()
    }

    handle = source.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')

    # Check that dragging does not work
    actions.click_and_hold(handle)
    actions.pause(0.5)
    actions.move_to_element(target)
    actions.pause(0.5)
    actions.release().perform()

    final_locations = {
        'source' : source.location.copy(),
        'target' : target.location.copy()
    }

    assert initial_locations == final_locations, 'Dragging the handle should not work on locked items.'

    return
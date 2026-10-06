'''Integration tests that check that styling SortableItem components works as expected.'''

import dash
from   dash.testing.composite                  import DashComposite
from   selenium.webdriver.common.by            import By
from   selenium.webdriver.common.action_chains import ActionChains

from   .fixtures.sortableGroup import app_with_clones__group
from   .fixtures.sortableItem  import (
    app_drag_style__item, 
    app_drop_style__item,
    app_lock_style__item
)

def test_drag_style(dash_duo: DashComposite, app_drag_style__item: dash.Dash) -> None:
    r'''Checks that the custom styling applied to item1 when dragged works as expected.'''

    dash_duo.start_server(app_drag_style__item)
    actions = ActionChains(dash_duo.driver)

    source = dash_duo.find_element('item1', attribute='ID')
    handle = source.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')
    target = dash_duo.find_element('item2', attribute='ID')

    # Click and move but do not release
    actions.click_and_hold(handle).pause(0.5)
    actions.move_to_element(target).pause(0.5).perform()

    # Check that the div style is updated dynamically
    style_div = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in source.get_attribute('style').split(";"))
        if v or k.strip()
    }

    assert style_div['background-color'] == 'blue', 'Wrong background color while dragging item1'
    assert style_div['rotate'] == '180deg', 'Wrong rotation angle color while dragging item1'

    # Check that the order of the items changes
    children = source.find_elements(By.XPATH, "./child::*")
    assert (
        children[0].tag_name == 'label' and
        children[1].tag_name == 'div'
    ), 'Label and handle should be swapped when dragging item1.'

    handle = children[1].find_element(By.TAG_NAME, "label")

    # Check that the handle changes
    assert handle.get_attribute('textContent') == '🚀', 'Handle should be changed to a rocket when dragging item1.'

    # Check that the style of the handle changes
    style_handle = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in handle.get_attribute('style').split(";"))
        if v or k.strip()
    }
    
    assert style_handle['background-color'] == 'green', 'Wrong background color for the handle while dragging item1'

    return

def test_clones_and_styling(dash_duo: DashComposite, app_with_clones__group: dash.Dash) -> None:
    r'''Checks that clones are rendered when withClone is True in SortableGroup and that they can be styled with a CSS stylesheet.'''

    dash_duo.start_server(app_with_clones__group)
    actions = ActionChains(dash_duo.driver)

    source = dash_duo.find_element('item1', attribute='ID')
    target = dash_duo.find_element('item2', attribute='ID')

     # Click and move but do not release
    actions.click_and_hold(source).pause(0.5)
    actions.move_to_element(target).pause(0.5).perform()

    # There should be two item1 components now
    sources = dash_duo.find_elements('item1', attribute='ID')
    assert len(sources) == 2, 'There should be two item1 components when withClone is True.'

    # Check that there is exactly one clone
    if (
        sources[0].get_attribute('data-dnd-placeholder') is None and 
        sources[1].get_attribute('data-dnd-placeholder') == 'clone'
    ): idx_placeholder = 1

    elif (
        sources[1].get_attribute('data-dnd-placeholder') == 'clone' and
        sources[0].get_attribute('data-dnd-placeholder') is not None
    ): idx_placeholder = 0

    else: assert False, 'No placeholder clone.'

    # Check that the other component is the dragged component
    assert (
        sources[idx_placeholder].get_attribute('data-dnd-dragging') is None and
        sources[not idx_placeholder].get_attribute('data-dnd-dragging') == 'true'
    ), 'Missing the dragged component.'

    return

def test_drop_style(dash_duo: DashComposite, app_drop_style__item: dash.Dash) -> None:
    r'''Checks that the custom styling applied to item1 when dropped works as expected.'''

    dash_duo.start_server(app_drop_style__item)
    actions = ActionChains(dash_duo.driver)

    source = dash_duo.find_element('item1', attribute='ID')
    handle = source.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')
    target = dash_duo.find_element('item2', attribute='ID')

    # Click and move but do not release
    actions.click_and_hold(handle).pause(0.5)
    actions.move_to_element(target).pause(0.5).release().perform()

    # Assert that the div and handle styles are updated when dropping
    style_div = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in source.get_attribute('style').split(";"))
        if v or k.strip()
    }

    assert style_div['background-color'] == 'blue', 'Wrong background color while dropping item1'
    assert style_div['rotate'] == '180deg', 'Wrong rotation angle while dropping item1'

    handle = source.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')
    style_handle = {
            k.strip(): v.strip()
            for k, _, v in (item.partition(":") for item in handle.get_attribute('style').split(";"))
            if v or k.strip()
        }
    
    assert style_handle['background-color'] == 'green', 'Wrong background color for the handle while dropping item1'

    # Assert that the order of the items changes
    children = source.find_elements(By.XPATH, "./child::*")
    
    assert (
        children[0].tag_name == 'label' and
        children[1].tag_name == 'div'
    ), 'Label and handle should be swapped when dropping item1.'

    handle   = children[1].find_element(By.TAG_NAME, "label")

    # Check that the handle changes
    assert handle.get_attribute('textContent') == '🚀', 'Handle should be changed to a rocket when dropping item1.'

    actions.pause(3.5).perform()

    # Assert that the div and handle styles are reset after dropping
    style_div = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in source.get_attribute('style').split(";"))
        if v or k.strip()
    }
    
    assert style_div['background-color'] != 'blue', 'Wrong background color after dropping stops'
    assert 'rotate' not in style_div, 'Wrong rotation angle after dropping stops'

    handle = source.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')
    style_handle = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in handle.get_attribute('style').split(";"))
        if v or k.strip()
    }
    
    assert style_handle['background-color'] != 'green', 'Wrong background color for the handle after dropping stops'

    # Assert that the order of the items changes back
    children = source.find_elements(By.XPATH, "./child::*")
    
    assert (
        children[0].tag_name == 'div' and
        children[1].tag_name == 'label'
    ), 'Label and handle should be swapped back when dropping stops.'

    handle   = children[0].find_element(By.TAG_NAME, "label")

    # Check that the handle changes
    assert handle.get_attribute('textContent') == '☃', 'Handle should be changed to a rocket when dropping stops.'

    return

def test_lock_style(dash_duo: DashComposite, app_lock_style__item: dash.Dash) -> None:
    r'''Checks that the custom styling applied to item when locked works as expected.'''

    @app_lock_style__item.callback(
        dash.Output('item', 'lock'),
        dash.Input('button', 'n_clicks')
    )
    def lock_unlock(n_clicks: int | None) -> bool:

        if n_clicks is None: raise dash.exceptions.PreventUpdate

        return n_clicks % 2 == 1

    dash_duo.start_server(app_lock_style__item)
    actions = ActionChains(dash_duo.driver)

    button = dash_duo.find_element('button', attribute='ID')

    # Check that the div and handle styles correspond to the unlocked state by default
    item   = dash_duo.find_element('item', attribute='ID')
    handle = item.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')

    actions.pause(0.5).perform()

    style_div = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in item.get_attribute('style').split(";"))
        if v or k.strip()
    }

    style_handle = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in handle.get_attribute('style').split(";"))
        if v or k.strip()
    }

    assert style_div['background-color'] == 'yellow', 'Wrong background color for the div element at startup.'
    assert style_handle['background-color'] == 'red', 'Wrong background color for the handle at startup.'
    assert handle.get_attribute('textContent') == '☃', 'Wrong handle at startup.'

    # Click on the button to lock the item
    actions.click(button).pause(0.5).perform()
    
    item   = dash_duo.find_element('item', attribute='ID')
    handle = item.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')

    style_div = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in item.get_attribute('style').split(";"))
        if v or k.strip()
    }

    style_handle = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in handle.get_attribute('style').split(";"))
        if v or k.strip()
    }

    assert style_div['background-color'] == 'blue', 'Wrong background color for the div element after one click.'
    assert style_handle['background-color'] == 'green', 'Wrong background color for the handle after one click.'
    assert handle.get_attribute('textContent') == '🚀', 'Wrong handle after one click.'

    # Click on the button to unlock the item
    actions.click(button).pause(0.5).perform()

    item   = dash_duo.find_element('item', attribute='ID')
    handle = item.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')

    style_div = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in item.get_attribute('style').split(";"))
        if v or k.strip()
    }

    style_handle = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in handle.get_attribute('style').split(";"))
        if v or k.strip()
    }

    assert style_div['background-color'] == 'yellow', 'Wrong background color for the div element at startup.'
    assert style_handle['background-color'] == 'red', 'Wrong background color for the handle at startup.'
    assert handle.get_attribute('textContent') == '☃', 'Wrong handle at startup.'

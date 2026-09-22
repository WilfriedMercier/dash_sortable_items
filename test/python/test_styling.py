'''Integration tests that check that styling SortableItem components works as expected.'''

import dash
from   dash.testing.composite                  import DashComposite
from   selenium.webdriver.common.by            import By
from   selenium.webdriver.common.action_chains import ActionChains

from   .fixtures.sortableItem  import app_drag_style__item
from   .fixtures.sortableGroup import app_with_clones__group

def test_drag_style(dash_duo: DashComposite, app_drag_style__item: dash.Dash) -> None:
    r'''Checks that the custom styling applied to item1 works as expected.'''

    dash_duo.start_server(app_drag_style__item)
    actions = ActionChains(dash_duo.driver)

    source = dash_duo.find_element('item1', attribute='ID')
    handle = source.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')
    target = dash_duo.find_element('item2', attribute='ID')

    # Click and move but do not release
    actions.click_and_hold(handle).pause(0.5)
    actions.move_to_element(target).pause(0.5).perform()

    style_div = {
        k.strip(): v.strip()
        for k, _, v in (item.partition(":") for item in source.get_attribute('style').split(";"))
        if v or k.strip()
    }

    assert style_div['background-color'] == 'blue', 'Wrong background color while dragging item1'
    assert style_div['rotate'] == '180deg', 'Wrong rotation angle color while dragging item1'

    handle = source.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, 'label')
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
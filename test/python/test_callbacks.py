'''Integration tests that check that the callbacks for the SortableGroup and SortableItem components work as expected.'''

import dash
from   dash.testing.composite                  import DashComposite
from   selenium.webdriver.common.by            import By
from   selenium.webdriver.common.action_chains import ActionChains

from   .fixtures.sortableGroup import (
    app_button__group,
    app_label__group
)

from  .fixtures.sortableItem import (
    app_button__item
)

class Test_SortableGroup:
    r'''Gather all the callback tests relative to the SortableGroup component.'''

    def test_style(self, dash_duo: DashComposite, app_button__group: dash.Dash) -> None:
        r'''Test that the style props can be updated via a callback.'''

        dash_duo.start_server(app_button__group)
        actions = ActionChains(dash_duo.driver)

        button = dash_duo.find_element('button', attribute='ID')
        group  = dash_duo.find_element('group', attribute='ID')

        # Check that the initial style is ok
        style = {
            k.strip(): v.strip()
            for k, _, v in (item.partition(":") for item in group.get_attribute('style').split(";"))
            if v or k.strip()
        }

        assert style['background-color'] == 'red' and style['flex-direction'] == 'column', 'Wrong initial style for the SortableGroup item.'

        # Check that the style after the callback is ok
        actions.pause(0.5)
        actions.click(button)
        actions.pause(0.5)
        actions.release().perform()

        style = {
            k.strip(): v.strip()
            for k, _, v in (item.partition(":") for item in group.get_attribute('style').split(";"))
            if v or k.strip()
        }

        assert style['background-color'] == 'blue' and style['flex-direction'] == 'row', 'Wrong style after callback for the SortableGroup item.'

        return

    def test_sorted_ids(self, dash_duo: DashComposite, app_label__group: dash.Dash) -> None:
        r'''Test that the sortedIDs prop can trigger a callback when one of the items is moved.'''

        dash_duo.start_server(app_label__group)
        actions = ActionChains(dash_duo.driver)

        item1 = dash_duo.find_element('item1', attribute='ID')
        item2 = dash_duo.find_element('item2', attribute='ID')
        label = dash_duo.find_element('label', attribute='ID')

        actions.click_and_hold(item1)
        actions.pause(0.5)
        actions.move_to_element(item2)
        actions.pause(0.5)
        actions.release().perform()

        assert label.text == 'item2/item1', 'Wrong item order at init.'

        return

class Test_SortableItem:
    r'''Gather all the callback tests relative to the SortableItem component.'''

    def test_styles(self, dash_duo: DashComposite, app_button__item: dash.Dash) -> None:
        '''Test that the styles props can be updated via a callback.'''

        dash_duo.start_server(app_button__item)
        actions = ActionChains(dash_duo.driver)

        item1  = dash_duo.find_element('item1', attribute='ID')
        button = dash_duo.find_element('button', attribute='ID')

        actions.click(button)
        actions.pause(0.5)
        actions.release().perform()

        style_div = {
            k.strip(): v.strip()
            for k, _, v in (item.partition(":") for item in item1.get_attribute('style').split(";"))
            if v or k.strip()
        }

        assert style_div['background-color'] == 'magenta', 'Background color of div not updated.'
        assert style_div['padding'] == '100px', 'Padding of div not updated.'

        # Get the label inside the div which corresponds to the handle
        handle = item1.find_elements(By.XPATH, "./child::*")[0].find_elements(By.XPATH, "./child::*")[0]

        style_handle = {
            k.strip(): v.strip()
            for k, _, v in (item.partition(":") for item in handle.get_attribute('style').split(";"))
            if v or k.strip()
        }

        assert style_handle['background-color'] == 'blue', 'Background color of handle not updated.'

        return
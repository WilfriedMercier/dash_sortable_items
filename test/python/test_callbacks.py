'''Integration tests that check that the callbacks for the SortableGroup and SortableItem components work as expected.'''

import dash
from   dash.testing.composite                  import DashComposite
from   selenium.webdriver.common.action_chains import ActionChains
from   .fixtures                               import (
    simple_app_with_button_changing_style,
    simple_app_with_label
)

class Test_SortableGroup:

    def test_style(self, dash_duo: DashComposite, simple_app_with_button_changing_style: dash.Dash) -> None:

        dash_duo.start_server(simple_app_with_button_changing_style)
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

    def test_sorted_ids(self, dash_duo: DashComposite, simple_app_with_label: dash.Dash) -> None:

        dash_duo.start_server(simple_app_with_label)
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
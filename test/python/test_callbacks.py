'''Integration tests that check that the callbacks for the SortableGroup and SortableItem components work as expected.'''

import dash
import typing
from   dash.testing.composite                  import DashComposite
from   selenium.webdriver.common.by            import By
from   selenium.webdriver.common.action_chains import ActionChains

from   .fixtures.sortableGroup import (
    app_button__group,
    app_label__group,
    app_label_with_restrictions__group
)

from  .fixtures.sortableItem import (
    app_button__item,
    app_button_no_handle__item
)

class Test_SortableGroup:
    r'''Gather all the callback tests relative to the SortableGroup component.'''

    def test_style(self, dash_duo: DashComposite, app_button__group: dash.Dash) -> None:
        r'''Test that the style props can be updated via a callback.'''

        @app_button__group.callback(
            dash.Output('group', 'style'),
            dash.Input('button', 'n_clicks'),
            dash.State('group', 'style'),
            prevent_initial_callback = True
        )
        def update_style(_, old_style: dict[str, str]) -> dict[str, str]:
    
            if _ is None: raise dash.exceptions.PreventUpdate
    
            return old_style | {'flexDirection' : 'row', 'backgroundColor' : 'blue'}

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
        actions.click(button).pause(0.5).perform()

        style = {
            k.strip(): v.strip()
            for k, _, v in (item.partition(":") for item in group.get_attribute('style').split(";"))
            if v or k.strip()
        }

        assert style['background-color'] == 'blue' and style['flex-direction'] == 'row', 'Wrong style after callback for the SortableGroup item.'

        return

    def test_sorted_ids(self, dash_duo: DashComposite, app_label__group: dash.Dash) -> None:
        r'''Test that the sortedIDs prop can trigger a callback when one of the items is moved.'''

        @app_label__group.callback(
            dash.Output('label', 'children'),
            dash.Input('group', 'sortedIds'),
            prevent_initial_callback = True
        )
        def update_style(ids: list) -> str:
    
            if ids is None: raise dash.exceptions.PreventUpdate
    
            return '/'.join(ids)

        dash_duo.start_server(app_label__group)
        actions = ActionChains(dash_duo.driver)

        item1 = dash_duo.find_element('item1', attribute='ID')
        item2 = dash_duo.find_element('item2', attribute='ID')
        label = dash_duo.find_element('label', attribute='ID')

        actions.click_and_hold(item1).pause(0.5).move_to_element(item2).pause(0.5).release().perform()

        assert label.text == 'item2/item1', 'Wrong item order.'

        return

    def test_sorted_ids_with_restrict(self, dash_duo: DashComposite, app_label_with_restrictions__group: dash.Dash) -> None:

        pause = 0.5

        @app_label_with_restrictions__group.callback(
            dash.Output('label', 'children'),
            dash.Input('group', 'sortedIds'),
            prevent_initial_callback = True
        )
        def update_style(ids: list) -> str:
    
            if ids is None: raise dash.exceptions.PreventUpdate
    
            return '/'.join(ids)

        dash_duo.start_server(app_label_with_restrictions__group)
        actions = ActionChains(dash_duo.driver)

        item1 = dash_duo.find_element('item1', attribute='ID')
        item2 = dash_duo.find_element('item2', attribute='ID')
        label = dash_duo.find_element('label', attribute='ID')

        # Check that label is empty at first
        assert label.text == '', 'Label not empty at startup.'

        # Check that item1 cannot change position with item2 because of its horizontal movement restriction
        actions.click_and_hold(item1).pause(pause).move_to_element(item2).release().perform()
        assert label.text == 'item1/item2', 'Items should not have swapped order because of movement restriction on item1.'

        # Check that item2 can change position with item1 because it has no constraints on movement
        actions.click_and_hold(item2).pause(pause).move_to_element(item1).release().perform()
        assert label.text == 'item2/item1', 'Items\' order should have changed when moving item2 to item1\' position.'

        return

class Test_SortableItem:
    r'''Gather all the callback tests relative to the SortableItem component.'''

    def test_styles(self, dash_duo: DashComposite, app_button__item: dash.Dash) -> None:
        r'''Test that the styles props can be updated via a callback.'''

        @app_button__item.callback(
            dash.Output('item1', 'styles'),
            dash.Output('item1', 'lock'),
            dash.Input('button', 'n_clicks'),
            dash.State('item1', 'styles'),
            prevent_initial_call = True
        )
        def _(_, old_styles: dict[str, dict[str, str]]) -> tuple[dict[str, dict[str, str]], bool]:
    
            if _ is None: raise dash.exceptions.PreventUpdate
    
            new_styles = {
                'div'    : old_styles['div']    | {'backgroundColor' : 'magenta', 'padding' : '100px'},
                'handle' : old_styles['handle'] | {'backgroundColor' : 'blue'}
            }
    
            return new_styles, True

        dash_duo.start_server(app_button__item)
        actions = ActionChains(dash_duo.driver)

        item1  = dash_duo.find_element('item1', attribute='ID')
        button = dash_duo.find_element('button', attribute='ID')

        actions.click(button).pause(0.5).perform()

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

    def test_lock(self, dash_duo: DashComposite, app_button__item: dash.Dash) -> None:
        r'''Test that the lock props can be updated via a callback.'''

        pause = 0.5

        @app_button__item.callback(
            dash.Output('item1', 'lock'),
            dash.Input('button', 'n_clicks'),
            dash.State('sortedIDs', 'data'),
            prevent_initial_call = True
        )
        def update_styles_and_lock(
            n_clicks: int | None, sortedIDs: int
        ) -> bool:
    
            if n_clicks is None: raise dash.exceptions.PreventUpdate
    
            elif n_clicks == 1: 
    
                assert sortedIDs == ['item2', 'item1'], 'Wrong item order after first click.'
                return True
            
            elif n_clicks == 2: 
    
                assert sortedIDs == ['item2', 'item1'], 'Wrong item order after second click.'
                return False
    
            else: 
            
                assert sortedIDs == ['item1', 'item2'], 'Wrong item order after third click.'
                return True
    
        @app_button__item.callback(
            dash.Output('sortedIDs', 'data'),
            dash.Input('group', 'sortedIDs'),
            prevent_initial_call = True
        )
        def on_order_change(sortedIds: list) -> list: return sortedIds

        dash_duo.start_server(app_button__item)
        actions = ActionChains(dash_duo.driver)

        item1  = dash_duo.find_element('item1', attribute='ID')
        item2  = dash_duo.find_element('item2', attribute='ID')
        button = dash_duo.find_element('button', attribute='ID')

        # This should trigger the on_order_change callback
        actions.click_and_hold(item1).move_to_element(item2)
        actions.pause(pause).release().perform()

        # After first click, order should be item2, item1 and item1 should be locked
        actions.click(button).pause(pause).perform()

        # Item 1 should not move now and order should not change
        actions.click_and_hold(item1)
        actions.move_to_element(item2)
        actions.pause(pause).release().perform()

        # After first click, order should still be item2, item1 and item1 should be unlocked
        actions.click(button).pause(pause).perform()

        # Item 1 should move again and order should change
        actions.click_and_hold(item1)
        actions.move_to_element(item2)
        actions.pause(pause).release().perform()

        # After third click, order should be item1, item2
        actions.click(button).pause(pause).perform()

        return

    def test_handle(self, dash_duo: DashComposite, app_button__item: dash.Dash) -> None:
        r'''Test that the handle props can be updated via a callback.'''

        @app_button__item.callback(
            dash.Output('item1', 'handle'),
            dash.Input('button', 'n_clicks'),
            prevent_initial_call = True
        )
        def _(_):

            if _ is None: raise dash.exceptions.PreventUpdate

            return dash.html.Label('☎️')


        dash_duo.start_server(app_button__item)
        actions = ActionChains(dash_duo.driver)

        button = dash_duo.find_element('button', attribute='ID')
        handle = (
            dash_duo.find_element('item1', attribute='ID')
            .find_elements(By.XPATH, "./child::*")[0]
            .find_elements(By.XPATH, "./child::*")[0]
        )

        assert handle.text == '☃', 'Wrong initial handle.'

        actions.click(button).pause(0.5).perform()

        handle = (
            dash_duo.find_element('item1', attribute='ID')
            .find_elements(By.XPATH, "./child::*")[0]
            .find_elements(By.XPATH, "./child::*")[0]
        )

        assert handle.text == '☎️', 'Wrong handle after callback.'

        return

    def test_handle_pos(self, dash_duo: DashComposite, app_button__item: dash.Dash) -> None:
        r'''Test that the handlePos props can be updated via callback.'''

        @app_button__item.callback(
            dash.Output('item1', 'handlePos'),
            dash.Input('button', 'n_clicks'),
            prevent_initial_call = True
        )
        def _(n_clicks: int | None) -> typing.Literal['start', 'end']:

            if n_clicks is None: raise dash.exceptions.PreventUpdate

            return 'start' if n_clicks % 2 == 0 else 'end'

        dash_duo.start_server(app_button__item)
        actions = ActionChains(dash_duo.driver)

        button         = dash_duo.find_element('button', attribute='ID')

        # Check that children are in the right order at first
        item1_children = dash_duo.find_element('item1', attribute='ID').find_elements(By.XPATH, "./child::*")

        assert (
            (item1_children[0].tag_name == 'div') &
            (item1_children[0].get_attribute('role') == 'button') & 
            (item1_children[1].tag_name == 'label')
        ), 'Wrong initial position for the handle.'

        # Check that children are in the right order after first click
        actions.click(button).pause(0.5).perform()
        item1_children = dash_duo.find_element('item1', attribute='ID').find_elements(By.XPATH, "./child::*")

        assert (
            (item1_children[0].tag_name == 'label') &
            (item1_children[1].get_attribute('role') == 'button') & 
            (item1_children[1].tag_name == 'div')
        ), 'Wrong final position for the handle.'

        # Check that children are in the right order after second click
        actions.click(button).pause(0.5).perform()
        item1_children = dash_duo.find_element('item1', attribute='ID').find_elements(By.XPATH, "./child::*")

        assert (
            item1_children[0].tag_name == 'div' and
            item1_children[0].get_attribute('role') == 'button' and
            item1_children[1].tag_name == 'label'
        ), 'Wrong final position for the handle.'

        return

    def test_restrict(self, dash_duo: DashComposite, app_button_no_handle__item: dash.Dash) -> None:
        r'''Test that the restrict props can be updated via callback when the layout is vertical.'''

        pause = 0.5

        @app_button_no_handle__item.callback(
            dash.Output('item1', 'restrict'),
            dash.Input('button', 'n_clicks'),
            prevent_initial_call = True
        )
        def _(n_clicks: int | None) -> typing.Literal['horizontal', 'vertical']:

            if n_clicks is None: raise dash.exceptions.PreventUpdate

            return 'horizontal' if n_clicks % 2 == 0 else 'vertical'

        dash_duo.start_server(app_button_no_handle__item)
        actions = ActionChains(dash_duo.driver)

        button  = dash_duo.find_element('button', attribute='ID')

        # Check that item1 can move horizontally and vertically at first
        item1   = dash_duo.find_element('item1', attribute='ID')
        
        actions.click_and_hold(item1).pause(pause).perform()
        init_pos = item1.location
        actions.move_by_offset(20, 20).pause(pause).perform()

        assert (
            item1.location['x'] > init_pos['x'] and
            item1.location['y'] > init_pos['y']
        ), 'item1 should be able to move both horizontally and vertically at first.'

        # Check that, vertical movement is restricted after first click
        actions.release().pause(pause).click(button).pause(pause).perform()
        actions.click_and_hold(item1).pause(pause).perform()
        init_pos = item1.location
        actions.move_by_offset(20, 20).perform()

        assert item1.location['x'] == init_pos['x'], 'item1 should not be able to move horizontally after first click.'
        assert item1.location['y'] > init_pos['y'], 'item1 should be able to move vertically after first click.'

        # Check that, vertical movement is restricted after second click
        actions.release().pause(pause).click(button).pause(pause).perform()
        actions.click_and_hold(item1).pause(pause).perform()
        init_pos = item1.location
        actions.move_by_offset(20, 20).perform()


        assert item1.location['x'] > init_pos['x'], 'item1 should be able to move horizontally after second click.'
        assert item1.location['y'] == init_pos['y'], 'item1 should not be able to move vertically after second click.'

        return
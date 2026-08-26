import dash_sortable_items
import dash

app = dash.Dash()

app.layout = dash_sortable_items.DashSortableItems(id='component')


if __name__ == '__main__':
    app.run(debug=True)

# Import libraries
from h2o_wave import ui, Q, app, main, data, site

# Defines dashboard tab logic
def dashboard_view(q, dataframe):
    # Deletes UI elements from other tabs
    del q.page["plot_view"]
    del q.page["table_view"]

    df = dataframe

    q.page["dashboard1"] = ui.form_card(
        box="content",
        items=[
            ui.range_slider(
                name="range_slider",
                label="Select the cities you wish to view data for between two rankings",
                min=1,
            ),
            ui.button(name="show_inputs", label="Submit", primary=True),
        ],
    )

    q.page["dashboard2"] = ui.form_card(
        box="content", items=[ui.text_xl(df.iloc[:, 0:2].to_string())]
    )

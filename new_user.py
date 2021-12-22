# Import libraries
from h2o_wave import ui
import pandas as pd

# Sets up site for new client/user
def new_user_setup(q, dataframe):

    # Loads in dataframe to df variable to set initial x/y variables for the plot view
    df = dataframe

    # Responsive layout and lays out zones for each type of UI element
    q.page["meta"] = ui.meta_card(
        box="",
        theme="neon",
        layouts=[
            ui.layout(
                breakpoint="xs",
                zones=[ui.zone("header"), ui.zone("navigation"), ui.zone("content")],
            )
        ],
    )
    # Header
    q.page["header"] = ui.header_card(
        box="header",
        title="Take Home Task",
        subtitle="Shows users data in visual charts",
    )
    # Navbar
    q.page["navigation"] = ui.tab_card(
        box="navigation",
        items=[
            ui.tab(name="table", label="Table View"),
            ui.tab(name="plot", label="Plot View"),
            ui.tab(name="dashboard", label="Dashboard View"),
        ],
    )

    q.client.x_variable = "city"
    q.client.y_variable = "one_adult_no_kids_living_wage"

    q.client.initialized = True

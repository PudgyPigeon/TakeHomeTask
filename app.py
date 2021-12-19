# Import library for h20wave
from h2o_wave import ui, Q, app, main, data
import pandas as pd

# Main function which serves the site
@app("/")
async def serve(q):

    if not q.client.initialized:
        new_user_setup(q)
        table_view(q)
    elif q.args.table:
        table_view(q)
    elif q.args.plot:
        plot_view(q)
    elif (q.args.x_variable is not None) or (q.args.y_variable is not None):
        q.client.x_variable = q.args.x_variable
        q.client.y_variable = q.args.y_variable
        plot_view(q)

    # Save page
    await q.page.save()


# Sets up site for new client/user
def new_user_setup(q):
    # Responsive layout
    q.page["meta"] = ui.meta_card(
        box="",
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
        title="Aggregated Visualizer",
        subtitle="Allowing users to easily visualize large datasets",
    )
    # Navbar
    q.page["navigation"] = ui.tab_card(
        box="navigation",
        items=[
            ui.tab(name="table", label="Table View"),
            ui.tab(name="plot", label="Plot View"),
        ],
    )

    q.client.x_variable = "c1"
    q.client.y_variable = "c2"

    q.client.initialized = True


# Defines table view logic
def table_view(q):
    del q.page["plot_view"]

    df = aggregated_data()

    q.page["table_view"] = ui.form_card(
        box="content",
        items=[
            ui.text_xl("Table View"),
            ui.table(
                name="aggregated_data_table",
                columns=[
                    ui.table_column(name=col, label=col) for col in df.columns.values
                ],
                rows=[
                    ui.table_row(
                        name=str(i),
                        cells=[str(df[col].values[i]) for col in df.columns.values],
                    )
                    for i in range(len(df))
                ],
                downloadable=True,
            ),
        ],
    )


# Defines plot view logic
def plot_view(q):
    del q.page["table_view"]

    df = aggregated_data()

    q.page["table_view"] = ui.form_card(
        box="content",
        items=[
            ui.text_xl(
                f"Relationship between {q.client.x_variable} and {q.client.y_variable}"
            ),
            ui.inline(
                items=[
                    ui.dropdown(
                        name="x_variable",
                        label="X Variable",
                        choices=[
                            ui.choice(name=col, label=col) for col in df.columns.values
                        ],
                        trigger=True,
                        value=q.client.x_variable,
                    ),
                    ui.dropdown(
                        name="y_variable",
                        label="Y Variable",
                        choices=[
                            ui.choice(name=col, label=col) for col in df.columns.values
                        ],
                        trigger=True,
                        value=q.client.y_variable,
                    ),
                ]
            ),
            ui.visualization(
                data=data(
                    fields=df.columns.tolist(),
                    rows=df.values.tolist(),
                    pack=True,
                ),
                plot=ui.plot(
                    marks=[
                        ui.mark(
                            type="point",
                            x=f"={q.client.x_variable}",
                            x_title="",
                            y=f"={q.client.y_variable}",
                            y_title="",
                            color="=data_type",
                            shape="circle",
                            size="=counts",
                        )
                    ]
                ),
            ),
        ],
    )


# Defines preliminary dataset logic
def aggregated_data():
    df = pd.DataFrame(dict(c1=range(0, 100), c2=range(1, 101), counts=range(2, 102)))
    print(df.head())
    return df

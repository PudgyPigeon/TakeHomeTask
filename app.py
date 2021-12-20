# Import library for h20wave
from h2o_wave import ui, Q, app, main, data
import pandas as pd
import boto3

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
    elif q.args.dashboard:
        dashboard_view(q)    
    elif (q.args.x_variable is not None) or (q.args.y_variable is not None):
        q.client.x_variable = q.args.x_variable
        q.client.y_variable = q.args.y_variable
        plot_view(q)
    

    # Save page
    await q.page.save()


# Sets up site for new client/user
def new_user_setup(q):
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
            ui.tab(name="dashboard", label="Dashboard View")
        ],
    )

    q.client.x_variable = "c1"
    q.client.y_variable = "c2"

    q.client.initialized = True


# Instantiate Boto3 Client to interact with AWS S3 bucket
def server_setup(q):
    
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()


# Defines table view logic
def table_view(q):
    del q.page["plot_view"]
    del q.page["dashboard1"]
    del q.page["dashboard2"]

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
    del q.page["dashboard1"]
    del q.page["dashboard2"]

    df = aggregated_data()

    q.page["plot_view"] = ui.form_card(
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

# Defines dashboard tab logic
def dashboard_view(q):
    #Deletes UI elements from other tabs
    del q.page["plot_view"]
    del q.page["table_view"]
    
    df = aggregated_data()
    
    q.page['dashboard1'] = ui.form_card(box='content', items=[
            ui.slider(name='slider', label='Standard slider', min=0, max=100, step=10, value=30),
            ui.slider(name='slider_zero', label='Origin from zero', min=-10, max=10, step=1, value=-3),
            ui.slider(name='slider_disabled', label='Disabled slider', min=0, max=100, step=10, value=30,
                      disabled=True),
            ui.button(name='show_inputs', label='Submit', primary=True),
        ])
    
    q.page["dashboard2"] = ui.form_card(
        box="content",
        items=[
            ui.text_xl("Hello there ")
        ]
    )

# Defines preliminary dataset logic
def aggregated_data():
    df = pd.DataFrame(dict(c1=range(0, 100), c2=range(1, 101), counts=range(2, 102)))
    print(df.head())
    return df

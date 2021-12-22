from h2o_wave import ui, Q, app, main, data, site

# Defines plot view logic
def plot_view(q, dataframe):
    del q.page["table_view"]
    del q.page["dashboard1"]
    del q.page["dashboard2"]

    #Loads in dataframe into df variable
    df = dataframe

    #Defines logic for plot_view card
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
                        )
                    ]
                ),
            ),
        ],
    )
    
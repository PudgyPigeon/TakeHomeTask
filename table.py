from h2o_wave import ui

# Defines table view logic
def table_view(q, dataframe):

    # Deletes cards from the other tabs
    del q.page["plot_view"]
    del q.page["dashboard1"]
    del q.page["dashboard2"]

    # Assigns Pandas dataset variable, "dataframe" to a more concise variable
    df = dataframe

    # Sets up the main card of the Table View tab
    # Loops through columns and rows to lay them out neatly in a table

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
                # Allows users to download dataset
                downloadable=True,
            ),
        ],
    )

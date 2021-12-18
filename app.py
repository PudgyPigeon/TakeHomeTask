#Import library for h20wave
from h2o_wave import ui, Q, app, main

#Main function which serves the site
@app("/")
async def serve(q):
    
    if not q.client.initialized:
        new_user_setup(q)
    
    #Save page
    await q.page.save()
    
    
#Sets up site for new client/user
def new_user_setup(q):
        #Responsive layout
    q.page["meta"] = ui.meta_card(
        box="",
        layouts=[
            ui.layout(
                breakpoint="xs",
                zones=[
                    ui.zone("header"),
                    ui.zone("navigation"),
                    ui.zone("content")
                ]
            )
        ]
    )

    #Header
    q.page["header"] = ui.header_card(
        box="header",
        title="Aggregated Visualizer",
        subtitle="Allowing users to easily visualize large datasets"
    )
    #Navbar
    q.page["navigation"] = ui.tab_card(
        box="navigation",
        items=[
            ui.tab(name="table", label="Table View"),
            ui.tab(name="plot", label="Plot View")
        ]
    )
    
    q.client.initialized = True

#Defines table view logic
def table_view(q):
    q.page["table_view"] = ui.form_card(
        box="content",
        items=[
            ui.text_xl("Table view")
        ]
    )
    
#Defines plot view logic
def plot_view(q):
    q.page["table_view"] = ui.form_card(
        box="content",
        items=[
            ui.text_xl("Plot view")
        ]
    )
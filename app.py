#Import library for h20wave
from h2o_wave import site, ui

#Set up the base site
page = site['/']

#Responsive layout
page["meta"] = ui.meta_card(
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
page["header"] = ui.header_card(
    box="header",
    title="Aggregated Visualizer",
    subtitle="Allowing users to easily visualize large datasets"
)

#Navbar
page["navigation"] = ui.tab_card(
    box="navigation",
    items=[
        ui.tab(name="table", label="Table View"),
        ui.tab(name="plot", label="Plot View")
    ]
)



page.save()
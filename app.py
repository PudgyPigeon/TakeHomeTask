# Import libraries
from h2o_wave import ui, Q, app, main, data, site
import pandas as pd
import boto3
from dotenv import load_dotenv
import os
import io

#Import custom modules
from backend import load_data
from new_user import new_user_setup
from table import table_view
from plot import plot_view
from dashboard import dashboard_view

#Use custom module to load in dataset from AWS S3
dataframe = load_data()

# Main function which serves the site
@app("/")
async def serve(q):

    #Sets up a new user and presents the table view as the initial UI element
    if not q.client.initialized:
        new_user_setup(q, dataframe)
        table_view(q, dataframe)
        
    #If the query argument changes when user clicks on a tab - call a function that defines
    #the logic that renders the dataset/UI elemeents on the web page
    elif q.args.table:
        table_view(q, dataframe)
    elif q.args.plot:
        plot_view(q,dataframe)
    elif q.args.dashboard:
        dashboard_view(q, dataframe)
    elif (q.args.x_variable is not None) or (q.args.y_variable is not None):
        q.client.x_variable = q.args.x_variable
        q.client.y_variable = q.args.y_variable
        plot_view(q,dataframe)

    # Save page
    await q.page.save()


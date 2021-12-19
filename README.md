# Design Document: H20Wave App 
### Date: December 17, 2021


## Introduction:
-------------
This document will serve as a summary of the considerations and methodologies
involved in creating the application.

The "System Overview" section will cover the general scope of the project, while  
"Design Considerations" will cover the assumptions, goals, and guidelines
that should be considered before development of the application starts.

"Architectural Strategies" will go over preliminary planning and strategies 
that may aid in the development process.


## System Overview
------------------
This program is a containerized application utilizing Docker and Python. Its 
main purpose is to provide the end-user with an app that visualizes traffic
data between two dates in real-time. 

Relevant libraires and packages include Python Black as well as H20Wave.

It will also feature authentication via Gmail account linking.

This project will also attempt to demonstrate proficiency in Git proficiency
as well as adherence to Conventional Commits.

The end result should be a web application that displays easy-to-read 
data through 2-3 visual charts on a dashboard created via H20Wave.
The traffic data will be uploaded to AWS S3.


## Design Considerations
----------------------

#### Assumptions and Dependencies
In order to create this application, creating one container should be more than
enough to run the H20Wave server as well as display the data on localhost.

However, there is a distinct possibility that I may need to create a second container
that handles sending the selected time frame's data to AWS S3. More research needs to 
go into this aspect before development of this particular feature set begins in earnest.

In terms of the web UI for displaying the dashboard, it should be relatively straightforward
as long as the documentation on the H20Wave website is followed.


#### General Constraints
The deadline of a few days may influence removal of more optimized implementations
and design. But due to the small scope of the project, this should not present too
many issues in regards to usability.

One additional constraint would be the developer's relative inexperience with H20Wave
and Dockerized deployment, but that can be solved with effort and additional learning.

#### Goals and Guidelines   
The application should first present the end-user with an authentication prompt of some sort.
Whether it will be a pop up or a separate web page leading to the main dashboard shall be decided
at a later time (addendum: will be updated in this document in later sections).

Once the user is authenticated (Or perhaps if a "skip" button is provided), the
app should display the user with a webpage that asks for input on a chart.
This chart will display all dates ranging from 1 August, 2021 to 1 October, 2021.
The user will then be able to select the dates either through manual input in
a DD-MM-YYYY format or a selectable calendar prompt.

The application should then take this data from "https://data.gov.hk/en-data/dataset/hk-td-sm_1-traffic-speed-map"
and then be uploaded to a deployed AWS S3 server. One challenge that I expect to encounter
is how to manage to convert the XML data into parquet files. Further problems that
may arise in this endeavor would be connecting the Docker container and application to
the AWS S3 server in the first place. Utilization of another container may be necessary.

Then finally, the data downloaded should be presented in 2-3 charts - the nature 
and format of these charts shall be decided at a later point.

Further guidelines that should be adhered to is the Python Black and Conventional Commit
standard. These should be completed in short order and I do not expect any 
troubles in this regard.

--Addendum: 
After further research into parquet files and AWS S3, I can surmise that it will be necessary to create an API with 
Python in order to host the data used by the H20Wave App. AWS Wrangler looks to be the perfect tool for the job.

(Implementation of Dask will be considered if time allows)

#### Development Methods 
Reading supporting documentation and consulting other learning materials will
be instrumental in completing this task.

Aside from this, general remarks on the development method would be to start
with creating the development environment in a Python container first and 
setting up the Dockerfile/Docker-Compose configurations.
-Additional note of concern: Proper set-up of docker-compose will be essential in the
development process due to frequent changes at the start of development.

Once that is accomplished, efforts should shift to granting the Docker container 
the proper environment variables and ensuring that Github pulls and pushes work
seamlessly in order to facilitate workflow and productivity.

Frequent Git commits and versioning will be integral in creating a structured
workflow.

The rest of the application's development process will center mainly on Python and
the H20Wave framework after this point. 

(This section will be expanded on further as development progresses)


## Detailed System Design
------------------------

The main file "app.py" outlines the UI elements show on the page.

At the moment, there is no authentication or hosting of real-time data. Every element
on the website is currently mock data but has allowed me to learn more about the compositional
aspects of the H20 framework.

Each view presently within the app: "Table View" and "Plot View" is defined by their own functions.
Before the DOM renders each respective data chart, the function del q.page[] is used to wipe the
screen clean before the function then proceeds to bring up the respective chart.

From my brief experimentation with the framework, every frontend element encountered so far is 
laid out in a dictionary/array format which simplifies the composotion of the frontend. Further
research into the backend integration in this framework will be needed as development continues.




To be updated as development progresses.



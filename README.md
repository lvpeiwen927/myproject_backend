
# Frontedend
## Frontend code review guide

- `frontend/`

  This is the root folder of application

- `frontend/public`

   The pictures and styles used in this software.
  
- `src/assets`

  The icons used in this software.

- `src/router`

  The glocabl components stored here, like general Router for layout component.

- `src/containers`

  In this folder, structural dashboard components can be managed, like TopBar and SideBar
- `src/dashboard.vue`
    home page for student
    
- `src/views`

  Majority of page components and functional files stored there:

  - `mentor` -> page for mentor
  - `Notification` -> notification for student
  - `pages` -> login, register and 404
  - `project` -> project function for student
  - `team` -> team function for student


- `src/App.js`

  Vue application entry portal
  


## How to install 

### requirement: 
  
node.js v12.18.2
npm 6.14.5
@vue/cli 4.4.6

1.clone the repo
git clone https://github.com/walkenzhong/project_management.git
2.go into app's directory
cd project_management
3.install app's dependencies
npm install
4. serve with hot reload at localhost:8080
npm run serve


# Backend

The data and codes data used in the back-end are in the **backend** folder.


## How to install
We have a guide(**back-end_installation_guide.pdf**). to help with installation.
The project uses **python3.7** and **flask** framework.
The database uses **mysql**.

## API documentation
There are two ways to view API documentation：
1. When the background server is running，use [http://127.0.0.1:5000/docs/api/](http://127.0.0.1:5000/docs/api/)  to see API document；
 2. View **API.pdf** . This is derived from the previous method.

## Backend code review guide
The main function of the project is in **app.py**, so running app.py can run the entire server. The project uses **restful_api** to ensure standardization and modularity.The interfaces are classified into different py files by function.
|   Module name   |   Features                     |
|----------------|--------------------------------|
|DBmodel.py  |  Define data model to facilitate database operations        |
|loginService.py         |   User registration and login       |
|projectService.py      |   Project-related operations: create, view, enroll, etc.      |
|notificationService.py      |   Create and view notifications      |
|teamService.py    |   Team operations: create, join, label, details, etc.     |
|manageService.py     |   Management project: processing phase, task, schedule, etc.      |
|submissionService.py      |   Submit phase deliverable, store files      |
|mentorService.py      |   Provide functions for course managers      |




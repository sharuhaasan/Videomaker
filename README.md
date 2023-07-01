# Videomaker

Project name Videomaker                                  
Audio_Elements - This Django app provides a REST API for managing audio elements in a video editing platform
 
INSTALLATION

Clone the repository: https://github.com/sharuhaasan/Videomaker                  
Navigate to the project directory: cd Videomaker                           
Create a virtual environment: python3 -m venv venv                  
Activate the virtual environment: venv\Scripts\activate                      
Install the dependencies: pip install -r requirements.txt            
Set up the database: python manage.py migrate and python manage.py makemigrations      

USAGE

Start the development server: python manage.py runserver                             
Access the API endpoints: Add audio element: POST /audio-elements/                  
Get audio element by ID: GET /audio-elements/{id}/                              
Update audio element by ID: PUT /audio-elements/{id}/                           
Delete audio element by ID: DELETE /audio-elements/{id}/           
Get Audio Fragments between start-time and end-time : GET /audio-fragments/{id}/{id}/      

SAMPLE API

http://127.0.0.1:8000/audio-elements -- Add audio element        
http://127.0.0.1:8000/audio-elements/3/ -- Get,Udate,Delete audio element by ID         
http://127.0.0.1:8000/audio-fragments/5/15/ -- Get Audio Fragments between start-time and end-time     

DATABASE : I have used Mysql database instead of default sqlite databse.

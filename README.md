 Video Platform: This is a Django-based video platform that allows users to upload, view, and share videos.

 Features
 * User registration and authentication
 * Video upload
 * Video playback with Video.js
 * Pagination for video navigation
 * Share video functionality


 
Installation

1. Clone the repository:
    git clone https://github.com/COBBY07/Project.git

2. Navigate to the project directory:
    cd Project

3. Create a virtual environment:
    python3 -m venv venv

4. Activate the virtual environment:
   On Windows:
        venv\Scripts\activate

   On macOS/Linux:
        source venv/bin/activate

5. Install the required dependencies:
    pip install -r requirements.txt

6. Apply migrations:
    python manage.py migrate

7. Run the development server:
    python manage.py runserver


 Usage
 
1. User Registration and Authentication 
* Users can register and log in to the platform using the built-in Django authentication system.
* Users can reset password when forgotten.
* Users can share video lonk to other via facebook etc.
  
2. Video Upload
* Users can upload videos through the platform.
* The video has previous and next buttons to navigate through the videos.
* If no further video can be loaded when navigating back or forward the previous button or next button are hidden respectively.



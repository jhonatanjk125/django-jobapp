<p align="center">
    <a href="https://github.com/jhonatanjk125/portfolio-web-app/blob/master/images/jobabb-website.png">
        <img src="https://github.com/jhonatanjk125/portfolio-web-app/blob/master/images/jobabb-website.png" height="200" />
    </a>
</p>
<h1 align="center">Django Job App</h1>


<h2 align="center">What is this project?</h2>
<p> A Python-Django app which allows admins to add job postings and they'll automatically be updated and displayed in the job postings list. This is a fully functional website, however it contains dummy data.</p>.

<h2 align="center">How to use this Django Job App?</h2>
<p align="justify"> This project was deployed using DigitalOcean. you should be able to check it at https://seahorse-app-adgn4.ondigitalocean.app/ however, if you have any issues you can always fork
it and run it locally. However you'll need to go to settings.py in the jobapp folder and change the default value of the following two variables to true:<br><br>
DEBUG = os.getenv("DEBUG", "False") == "True"<br>
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"<br><br>
So that they look like this instead:<br><br>
DEBUG = os.getenv("DEBUG", <b>"True"</b>) == "True"<br>
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", <b>"True"</b>) == "True"<br>
Once that's completed you should be able to run the server using "<b>python manage.py runserver</b>"
</p>.

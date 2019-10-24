## IDEA- PITCHING
A web application that allows the users to post pitches, comment and vote on pitches.

# By IKERRIZ
## Description
This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (PickupLines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. The user registers first to complete all the proccess.

## User Stories
* As a user I would like to view the different categories.
* As a user I would like to see the pitches other people have posted.
* As a user I would like to comment on the different pitches and leave feedback.
* As a user I would like to submit a pitch in any category.
* As a user I would like to vote on the pitch they liked and give it a downvote or upvote.
## Specifications

| Behaviour  |	Input       |	  Output      |
|------------|--------------|-----------------|
|Display Various Pitch Categories|	N/A	|Various pitches grouped by categories are displayed|
|Display pitches |	Click on a Category	|A page with a list of pitches from the selected category|
|Add new pitch |	'Click To Pitch' |	User Should register/sign in to add new pitch|
|View Pitches |Click on a pitch	category|View a pitch,add upvote,downvote and comments|

## Prerequisites
Python3.6
## Setup/Installation Requirements
* internet access
* $ git clone https://github.com/IKERRIZ/Idea-Pitching.git
* $ cd Idea-Pitching
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh
## How it works
A user needs to sign up
A user the needs to sign in to vote and post pitches
## Support and Contacts
In case You have any issues using this code please do no hesitate to get in touch with me through kephaokari@gmail.com or leave a commit here on github.

## Known Bugs
No known bugs

## Technologies Used
* Python3.6
* Flask framework
* Bootstrap
* PostgreSQL
## License
MIT (c) 2019 ikerriz
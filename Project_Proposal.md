# Spotify Scrobbling Project Proposal

## The Big Idea:

Music is a huge part of my life. In addition to being an avid music listener, I love creating and learning music, mostly on guitar, piano, and bass. Spotify is my most used app by far and I've always been interested in the massive amount of data collected and tracked by the service. I've been scrobbling my music through last.fm for a couple of years now and love the ability to track habits and metrics quantitatively. In this project, I aim to explore the Spotify Web API as well as the last.fm API to create insights on listening habits, as well as provide specialized metrics for things that aren't readily available from the last.fm dashboard or the Spotify home page. I plan on creating a web app that allows a user to do query-like functions on their last.fm data. In addition, I will use the Spotipy module to create reccomendations and qualitative suggestions for listening.

## Learning Objectives:

The main goal of this project is to get experience in developing a web app. I have working knowledge of HTML/CSS/JS, and working knowledge of Python, but this project will bring those skills together. I have always been interested in music-based data projects, so this will also serve as a launching point for learning music-based APIs.

## Implementation Plan:

I will be using the Spotipy module to call the API and get general artist, album, track information. I have API access to the Spotify Web App and last.fm. I will likely be using Flask for web creation. I have lots of data from my personal last.fm account that I can use for testing, and my aim is to make this app work for anyone who has scrobble-able data from last.fm

## Project Schedule:

I'm splitting the project into sections. While I'm unsure of how much time each one will take, I am relatively sure of the order in which they will be done.

1. Data Exploration
   * The first thing I will do is get familiar with both APIs and the Spotipy module. I need to understand what data is available/accessible, how is it stored, how can I access it, and what data structures it comes in. From there I can formulate the precise functions and outputs that my project will contain.
2. Backend Development 
   * From the information learned in step 1, I will write the main functionality of the app, outside of web context. This will help drive how the frontend should look, what information is needed from the user, and what information needs to be posted to the frontend.
3. Frontend Development
   * Time to make things look pretty. I will put my WebTech skills to the test to create an aesthetically pleasing environment for the user to interact with. Knowing the structure of the webpage helps integrate the front and backends with Flask.
4. Integration
   * Convert my backend shell into a Flask-friendly script so that I can turn the scripts into a proper app.
5. Authentication and Testing
   * I'll use a friends last.fm account to ensure that the app can work well for someone new to the program.

## Collaboration Plan:

Because I am working individually on this project, I have a lot of flexibility in when and how to work on this project. I don't foresee any issues here.

## Risks and Limitations:

The biggest roadblock I can identify right now is authorization. From the last.fm documentation, a user will likely have to go to an external page to authenticate their last.fm data. While the site is public and all last.fm profiles are public, it may require some sort of consent to call the data into a program. I'll have to make sure my callback URLs are working so that the end-user has a fluid experience with the app.

## Additional Course Content:

I think authentication techniques and testing techniques would be the most beneficial addition to the course content for my project. How can I efficiently do QA testing on an app. How can I ensure I'm testing all use cases? How can I efficiently run my program so that testing doesn't cause unnecessary load on my device? These things will help smooth out the more frustrating parts of this project.
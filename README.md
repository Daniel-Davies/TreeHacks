# FLUent
An app designed to assist doctors in making decisions on handing out antibiotic prescriptions

## The Team
<html>
    <img src="https://github.com/Daniel-Davies/TreeHacks/blob/master/68565359_756639748124610_1220692214477225984_n.jpg" alt="Team Photo" width="550">
</html>  

|[Daniel Davies](https://github.com/Daniel-Davies)|[Sophia Shen](https://github.com/sophiaszy)| [Saketh Saxena](https://github.com/sakethsaxena) | [Sarah Gurev](https://www.linkedin.com/in/sarahgurev/)
|--|--|--|--| 

## Awards 🏆
"Most Creative Project" presented by TreeHacks (Stanford University)

## The Project

PhilianthroPoints allows volunteers to find out about charity events in the local area, and upon participating an event, earn points through the app which they can then redeem for giftcards to partnering companies. The experience of volunteering time to a local charity is gamified by keeping a leaderboard (partitioned by location) of who has donated the most of their time to charities for a given time frame.  

Charities post their events on our platform.  
<img src='https://github.com/Daniel-Davies/TreeHacks/blob/master/ezgif-2-d7a1da19f16c.gif' title='PhilanthroPoints App Walkthrough' width='' alt='PhilanthroPoints App Walkthrough' />

Users can look at volunteer events in their area, sign up for events, see what events they are participating in, redeem points, and check their local leaderboard.  

After an event, charities can review statistics on how it went.  
<img src='https://raw.githubusercontent.com/Daniel-Davies/SLOHacks2019/master/gifs/gif2.gif' title='PhilanthroPoints App Walkthrough' width='' alt='PhilanthroPoints App Walkthrough' />

## The Inspiration
Small, local charities form a key part of philanthrophic projects across the globe. Without them, millions of people around the world would be suffering with no one to help them. Volunteering your time at a local charity can be a fulfilling experience that can create a great positive impact in your local community.

In practice however, local charities can find it very difficult to sustain themselves due to the lack of people that many such charities have come through. Since getting volunteers can be hard for these charities, we thought we'd help them out by creating further incentive for people in the community to help with our app, PhilianthroPoints.

This means volunteers now have the feel good factor of helping a good cause, but also upon finding a charity they can connect to on our app, can also challenge themselves against their peers and earn small treats for doing so.

## Implementation

The idea of the project is to have two main platforms for our two main user types: charities that host/ run events, and the volunteers who sign up to these events and redeem the rewards for doing so. 

The website is designed for the charities, so that an organisation can access our resources from, let's say, a work computer, meanwhile the app is designed to be much less formal and can be accessed by anyone on their iOS mobile device.

#### Web Server

The web server has two main goals:

* Enable charities to host events and track their previous events by serving HTML pages
* Act as a centralising data storage and resource unit for the iOS app, which is accessed through supporting API calls

The server itself is written in python flask. More details can be found [here](http://flask.pocoo.org/). API calls for the app are provided as endpoints, as are webpage requests.

The email SMTP client uses the Flask-Mail plugin, which sends messages through an SMTP server. The SMTP server we have used is a google mail account linked to Flask-Mail, and is triggered to send a given message from the "/sendMail" endpoint in our server.

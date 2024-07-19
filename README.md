# BOLDSWAP API

<div align="center"><img src="./resources/bookerLogo.png"></div>

<hr>

https://github.com/jinDeHao/BoldSwap/assets/70861727/377e923d-5bc4-438e-b8b1-c4e12afb5068


## TABLE OF CONTENT
- [Booker explained](#booker-explained)
- [Inspiration](#booker-explained)
- [User stories](#user-stories)
- [Functional requirements](#functional-requirements)
- [Features](#features)
- [Technical specifications](#technical-specifications)
- [Modeling and conception](#modeling-and-conception)
- [Development](#development)
- [Clonning and setup](#clonning-and-setup)
- [Conclusion](#conlusion)
- [Contact](#contact)

## BoldSwap explained

While a random person, in a random area, was struggling with a random illness, they decided to visit a random doctor to end the suffering. The trip to the clinic lasted about 2 hours, which made their health situation even worse.

When the person arrived, to their surprise, a long queue of people waiting to get an appointment to see the doctor, the person waited for what seemed like infinite time, then got an appointment, The person had to hit the road one more time back home until the appointment's date.

This is a typical situation for getting an appointment, thus had I decided to go on a journey to tackle this continuous problem. We introduce `BOLDSWAP`.

BoldSwap is a restful API, that provides booking services and allows industries to create working spaces where their clients can book appointments remotely.

BoldSwap is amazing because it gives great developers the chance to create an interface based on what they think fits their client's needs. The developers can take our API and use it for theirpurposes. The goal was to have an API with simple endpoints that handle different tasks done by regular users that are able to create appointments, and premium users that can own a workspace where to showcase their services and receive appointments, and the administration that handles all the management.

I see BoldSwap as more than just a Restful API; we see it as the future, as it can be used in amazing inventions, and that’s the plan.

## User stories

> As a user, I want to be able to create a new booking or a workspace for my professional activities, view all my bookings and workspaces. Update, cancel, or delete existing ones, and also search for available workspaces based on location, amenities, and availability.

> As a meticulous user, I want to receive confirmation emails for successful bookings.

> As a small business owner, I have been struggling to handle client's requests since they call me on my mobile to book appointments. I haven’t been able to hire an assistant to handle such tasks for me since I have just launched my business, and am not yet able to afford hiring a new employee. With Booker, I pay an affordable monthly fee, and Booker handles client bookings for me. I have a dashboard where I can keep track of the appointments taken, and it gives me the flexibility and the freedom to focus on the work that I do to deliver the best service.

## Functional requirements
BoldSwap provides booking services for users, and workspaces for different industries that occupy various fields.

- User authentication: Users can sign up and manage their accounts. For a user to have access to start creating workspaces, they have to register as a premium user and set up payment information.
- User navigation: Users can navigate through available workspaces, filter based on their demand, and get appointments. Premium users have the right to create workspaces and personalize them based on their schedule and availability.
- Appointment: The user wanting to make an appointment can filter using multiple fields, and then select the proper date based on their availability.
- Developers: As we are working on creating a RESTFUL API, we will ensure that our endpoints are clear for developers to use despite their level of understanding of the API.

## Technical specifications

![Technical specifications](./resources/technologies_infrastructure.png)

## Features

- Authentication
	- Signing up
	- Log in
	- Login out
- Account management
	- Account validation
	- Account upgrade
	- Account deletion
- Profile management
	- Showing profile
	- Updating profile
- Appointment management
	- Creating appointments
	- Listing appointments
	- Canceling appointments
- Workspace management
	- Creating workspace
	- Updating workspace
	- Deleting workspace
	- Listing workspaces
	- Filtering workspaces
- Reviews management
	- Creating review
	- Updating review
	- Liking review
	- Disliking review
	- Deleting review
- Reclaims management
	- Sending reclaim
	- Listing reclaims
- Administration
	- The administration is available for a couple of features so far, and it is under construction.

## Modeling and conception
I have chosen to use the UML (unified modeling language) since it is known for its fitted nature to oriented object programming. It helped us a lot to include this step, and was crucial to some extend.

You can access the UML folder to check out the diagrams separately and go through each.

With UML we were able to create different diagrams each fitted for a purpose starting with the `Use case diagram`.

#### Use case diagram

![UML Use case diagram](./UML/Case_diagram/Png/Booker_diagram_v2.png)

#### Class diagram

![UML Use case diagram](./UML/Class_diagram/Png/Class_diagram_v4.png)

#### Sequence diagram
One example of the use case diagram would be post and get appointment.

![UML Use case diagram](./UML/Sequence_diagram/Png/Post_Get_appointment.png)

The rest of the user sequence diagrams are here [sequence diagrams](/Booker/UML/Sequence_diagram/)

## Development
We created endpoints for every feature. And we have used Swagger to showcase every one of them.

![Swagger](./resources/swagger.jpg)


## Issues
I did face some issues, we had to update the class diagram, It was a learning curve for me. I learned a lot about how to do things the right way.


## Cloning and setup
To test what we have created try to follow this guide:

Cloning the repository
```bash
git clone https://github.com/jinDeHao/Booker.git
```
Navigate to the project
```bash
cd /Booker/API
```

Install the required dependencies
```bash
pip3 install requirements.txt
```

Run the API
```bash
python3 -m run
```

## Conlusion
I had so much fun while working on this project, each time I would refine and update what I have done. I have more to work on but this is the initial version of the API. I would be happy if developers used it to create interfaces.

## Contact
For any ideas or constructive criticism feel free to contact us in our socials.


Dr. Kolapo Adedipe, PhD, OCP, CC, ALX SE Grad

<a href="https://mail.google.com/mail/?view=cm&fs=1&to=adedipebabatundekolapo@gmail.com">
	<img src="./resources/gmail.png" width="3%">
</a>
<a href="https://www.linkedin.com/in/adedipe-kolapo-phd-ocp-cc-220177b2/">
	<img src="./resources/linkedin.png" width="3%">
</a>

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

When our team got together at Treehacks, we wanted to tackle a problem that prevalent in today's society. One such problem is antibiotic resistance: with greater pressure mounting to deliver methods to cut back on unecessary handouts of antibiotics, we wanted to see if we could find an innovative solution in helping the healthcare industry.

We came up with FLUent: FLUent is a Django based web application which uses a SVM model trained on micro-array gene expression data from patients with bacterial and viral infections to predict whether someone has a bacterial or viral infection, meaning that in the case of a viral infection, antiobiotics would have not been handed out unnecessarily.

As an extension, we could model which strains of bacteria would be resistant to a given antibiotic, and hence in the case of one of these infections, could prevent unecessary treatment with antibiotics.

Finally, the app also functions as an information tool, which we can use to send emails to inform patients about antibiotic resistance and why/ why not they were given antibiotics.

<img src='https://github.com/Daniel-Davies/TreeHacks/blob/master/ezgif-2-d7a1da19f16c.gif' title='PhilanthroPoints App Walkthrough' width='' alt='PhilanthroPoints App Walkthrough' />

## Running the code

- Clone this repo
- Install Django
- Enter the TreeHacks directory and type "pip install -r requirements.txt"
- Go into the "mysite" directory and enter "python manage.py runserver" into your terminal
- Visit localhost:8000 to view the site

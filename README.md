# Lean Tech Test
This project has been created in order to identify tax prices for both Canada and the United States

# Technical Requirements
Python v3.10.4
### Libraries:

* **Pandas**: for getting taxe's table and handle data
* **smtplib, ssl**: for connecting with email account and sending emails
* **email.mime.multipart**: for helping to create email message and using html template
* **email.mime.text**: for creating complete message structure
* **pretty_html_table**: for applying style to html tables within email messages
* **decouple**: for using environment variables

## taxes.py
The main script was created in this file and it has the following functions:
* **getTaxes()**: This function uses pandas library for getting the table from on taxes webpage and processing its regarding data according to the given requirements
* **openHtml()**: This function uses **template.html** which has the email design and replaces labels with its regarding information
* **buildMail()**:This function starts the process once it is called and according to the process logical steps, calls the regarding other functions
* **sendMail()**: this functions connect with email account and sends email.

##template.html
This file was created as a email template and is used from openHtml function

## .env
For executing process it should be create an enviroment file with the following variables:

# User Manual
As all automations it is important having in mind that all resources we are using in this solution are not handle by ourselves, the webpage design can be change by its owner and this can affect us.
## Case 1:
Now the web page only has one table that we are using for getting the information we need, but The webpage owner could add another table or more, in this case we would need to identify which of them would be the correct table and check if the procces is using it, now if the process is using another table we would need to indentify its index and change it.

## Case 2:
The webpage owner could changes as well the column titles and this actions could affect our process, now we are using the columns ["State / Province","Rate", "Special Diesel","Biodiesel"]. If we have an error according to these columns names, we would need make a change in its regarding column as the follow image shows

## Case 3:
If you need to use or change other email account such as "from" or "to", within .env file you could make those changes

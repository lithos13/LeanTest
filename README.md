# Lean Tech Test
This project has been created in order to identify tax prices for both Canada and the United States

# Technical Requirements
Python v3.10.4
### Libraries:
![technical_req](https://user-images.githubusercontent.com/68198144/176246642-12ea4348-3f77-4fe3-b7fb-f69f1e3c2cfe.jpg)
* **Pandas**: for getting taxe's table and handle data
* **smtplib, ssl**: for connecting with email account and sending emails
* **email.mime.multipart**: for helping to create email message and using html template
* **email.mime.text**: for creating complete message structure
* **pretty_html_table**: for applying style to html tables within email messages
* **decouple**: for using environment variables

## taxes.py
The main script was created in this file and it has the following functions:
* **getTaxes()**: This function uses pandas library for getting the table from on taxes webpage and processing its regarding data according to the given requirements
![get_Taxes](https://user-images.githubusercontent.com/68198144/176247544-d5722c3c-9032-4208-a889-018f8c396e98.jpg)

* **openHtml()**: This function uses **template.html** which has the email design and replaces labels with its regarding information
![openHTML](https://user-images.githubusercontent.com/68198144/176248285-0b63f09a-f232-4592-9db8-8a42a56b9706.jpg)

* **buildMail()**:This function starts the process once it is called and according to the process logical steps, calls the regarding other functions
![buildEmail](https://user-images.githubusercontent.com/68198144/176248471-d0b394bd-df5a-4a17-88d0-5fc0af6af98d.jpg)

* **sendMail()**: this functions connect with email account and sends email.
![sendMail](https://user-images.githubusercontent.com/68198144/176248396-ebab5fba-d65d-404e-bd83-54ccf51a760b.jpg)

## template.html
This file was created as a email template and is used from openHtml function
![template](https://user-images.githubusercontent.com/68198144/176249088-85739592-285c-4a82-99ec-1998f2a4a2ea.jpg)


## .env
For executing process it should be create an enviroment file with the following variables:
![env](https://user-images.githubusercontent.com/68198144/176249373-c09d2b43-760b-4b57-afed-f563b9982c6a.jpg)

# User Manual
As all automations it is important having in mind that all resources we are using in this solution are not handle by ourselves, the webpage design can be change by its owner and this can affect us.
## Case 1:
Now the web page only has one table that we are using for getting the information we need, but The webpage owner could add another table or more, in this case we would need to identify which of them would be the correct table and check if the procces is using it, therefore if the process is using another table we would need to indentify its index and change it.
![webpage](https://user-images.githubusercontent.com/68198144/176249877-bdc0b017-cf0a-4584-933e-f1508f042a54.jpg)

![getTable](https://user-images.githubusercontent.com/68198144/176250571-9daf8f6f-117f-4ae9-8150-2d507412e642.jpg)

## Case 2:
The webpage owner could changes as well the column titles and this actions could affect our process, now we are using the columns ["State / Province","Rate", "Special Diesel","Biodiesel"]. If we have an error according to these columns names, we would need make a change in its regarding column as the follow image shows
![columnTitles](https://user-images.githubusercontent.com/68198144/176250034-9a0e0d3e-6f94-4888-8330-4018c8ecaffd.jpg)

![keyVariables](https://user-images.githubusercontent.com/68198144/176250825-6a1b777d-5554-4e4b-b48b-84b5866c9f18.jpg)


## Case 3:
If you need to use or change other email account such as "from" or "to", within .env file you could make those changes
![env](https://user-images.githubusercontent.com/68198144/176249373-c09d2b43-760b-4b57-afed-f563b9982c6a.jpg)

# Lean Tech Test
This project has been created in order to identify tax prices for both Canada and the United States.

# Technical Requirements
Python v3.10.4
### Libraries:
![technical_req](https://user-images.githubusercontent.com/68198144/176246642-12ea4348-3f77-4fe3-b7fb-f69f1e3c2cfe.jpg)
* **Pandas**: for obtaining the taxe's table and handling data
* **smtplib, ssl**: for connecting with an email account and sending emails.
* **email.mime.multipart**: for helping to create email messages and using html template
* **email.mime.text**: for creating a complete message structure.
* **pretty_html_table**: for applying style to html tables within email messages.
* **decouple**: for making use of environmental variables.

## .env
For the process to run, an environment file with the following variables should be created:
![env](https://user-images.githubusercontent.com/68198144/176249373-c09d2b43-760b-4b57-afed-f563b9982c6a.jpg)

## taxes.py
This file contains the main script, which performs the following functions:
* **getTaxes()**: This function uses the pandas library for getting the table from the taxes webpage and processing its related data according to the given requirements.\
![get_Taxes](https://user-images.githubusercontent.com/68198144/176247544-d5722c3c-9032-4208-a889-018f8c396e98.jpg)

* **openHtml()**: This function uses **template.html**  which contains the email design and replaces labels such as {{msj}} {{tableMax}} {{tableMin}} {{tableUs}} {{tableCan}} with their relevant information
![openHTML](https://user-images.githubusercontent.com/68198144/176248285-0b63f09a-f232-4592-9db8-8a42a56b9706.jpg)

* **buildMail()**:This function starts the process once it is called and, according to the process logical steps, calls the other functions as well.
![buildEmail](https://user-images.githubusercontent.com/68198144/176248471-d0b394bd-df5a-4a17-88d0-5fc0af6af98d.jpg)

* **sendMail()**: This function connects with an email account and sends email.
![sendMail](https://user-images.githubusercontent.com/68198144/176248396-ebab5fba-d65d-404e-bd83-54ccf51a760b.jpg)

## template.html
This file was created as an email template and is used by the openHtml function.
![template](https://user-images.githubusercontent.com/68198144/176249088-85739592-285c-4a82-99ec-1998f2a4a2ea.jpg)

# User Manual
As with all automation, it is important to keep in mind that all resources we are using in this solution are not handled by ourselves. The webpage design can be changed by its owner and this could affect the process.
## Case 1:
Today, the web page only has one table that we are using for getting the information we need, but the webpage owner could add another table or more.
![webpage](https://user-images.githubusercontent.com/68198144/176249877-bdc0b017-cf0a-4584-933e-f1508f042a54.jpg)

In this case, we would need to identify which of them would be the correct table and check if the process is using it. Therefore, if the process is using another table, we would need to identify its index and change it.\
![getTable](https://user-images.githubusercontent.com/68198144/176250571-9daf8f6f-117f-4ae9-8150-2d507412e642.jpg)

## Case 2:
The web page owner could change the column titles as well, and these actions could affect our process. Currently, we are using the columns ["State / Province","Rate", "Special Diesel","Biodiesel"].
![columnTitles](https://user-images.githubusercontent.com/68198144/176250034-9a0e0d3e-6f94-4888-8330-4018c8ecaffd.jpg)

 If we have an error according to these columns' names, we would need to make a change in its regarding column as the following image shows.
 ![keyVariables](https://user-images.githubusercontent.com/68198144/176250825-6a1b777d-5554-4e4b-b48b-84b5866c9f18.jpg)


## Case 3:
If you need to use or change another email account, such as "from" or "to," you can do so within the **.env** file.
![env](https://user-images.githubusercontent.com/68198144/176249373-c09d2b43-760b-4b57-afed-f563b9982c6a.jpg)

# Final Result


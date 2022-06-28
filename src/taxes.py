from email.message import EmailMessage
from mimetypes import init
import pandas as pd
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pretty_html_table import build_table
from decouple import config

def getTaxes():
    url     = 'https://www.iftach.org/taxmatrix4/Taxmatrix.php'
    table   = pd.read_html(url)[0]
    df      = pd.DataFrame(table)
    df      = df[["State / Province","Rate", "Special Diesel","Biodiesel"]]

    #Canada details
    dfCan  = df.loc[(df['Rate'] == 'Can.')]
    taxCan = build_table(dfCan, 'blue_light') 
    maxCanBio = dfCan["Biodiesel"].max()
    maxCanSpe = dfCan["Special Diesel"].max()
    minCanBio = dfCan["Biodiesel"].min()
    minCanSpe = dfCan["Special Diesel"].min()
           
    #US details
    dfUS    = df.loc[(df['Rate'] == 'U.S.')]
    taxUS   = build_table(dfUS, 'blue_light')
    maxUSBio= dfUS["Biodiesel"].max()
    maxUSSpe= dfUS["Special Diesel"].max()    
    minUSBio= dfUS["Biodiesel"].min()
    minUSSpe= dfUS["Special Diesel"].min()   
    
    
    # Max per country
    maxim   = {'Country'            : ['Canada', 'United States'],
                'Max Diesel Special': [maxCanSpe, maxUSSpe],
                'Max Biodiesel'     : [maxCanBio, maxUSBio]}
    dfMaxim = pd.DataFrame(maxim)
    maxTab      = build_table(dfMaxim, 'blue_light')       

    # Min per country
    minim   = {'Country'            : ['Canada', 'United States'],
                'Min Diesel Special': [minCanSpe, minUSSpe],
                'Min Biodiesel'     : [minCanBio, minUSBio]}
    dfMinim = pd.DataFrame(minim)
    minTab      = build_table(dfMinim, 'blue_light')     


    return [taxCan, taxUS, maxTab, minTab]

def sendMail(email_message: EmailMessage):   
    # Connect to the Gmail SMTP server and Send Email
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login(config('EMAIL_ACCOUNT'), config('EMAIL_PASSWORD'))
    server.sendmail(config('EMAIL_ACCOUNT'), config('SEND_TO'), email_message.as_string())
    server.quit()

def openHtml(tableUs, tableCan, tableMaxim, tableMinim):
    html_data: str = ""
    with open("template.html", mode="r", encoding="utf-8") as data:
        html_data = data.read().replace("\n", "")
        html_data = html_data.replace("{{msj}}", "Hi <br> The following are the fuel taxes for Canada and the United States")
        html_data = html_data.replace("{{tabMax}}", tableMaxim)
        html_data = html_data.replace("{{tabMin}}", tableMinim)
        html_data = html_data.replace("{{tableUS}}", tableUs)
        html_data = html_data.replace("{{tableCan}}", tableCan)      
        return html_data
    
def buildMail():
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

    email_message = MIMEMultipart()
    #email_message['From'] =config('EMAIL_ACCOUNT')
    #email_message['To']   =config('SEND_TO')    
    email_message['Subject'] = f'Fuel taxes for Canada and the United States - {date_str}'

    list=getTaxes()    
    html_data: str = openHtml(list[0], list[1], list[2], list[3])    

    email_message.attach(MIMEText(html_data, "html"))  
    sendMail(email_message=email_message)   

buildMail()      
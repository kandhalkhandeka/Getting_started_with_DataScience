import pymongo
from pymongo import MongoClient
from imbox import Imbox
import os
import traceback
import gridfs
import mysql.connector

connection = MongoClient('localhost',27017)
db = connection.invoices
mysql_db = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd=""
)
mycursor = mysql_db.cursor()
mycursor.execute("use invoices ")
invocieCollection = db.info


with Imbox('imap.gmail.com',
        username='kandaljeet123@gmail.com',
        password='Kandal@123',
        ssl=True,
        ssl_context=None,
        starttls=False) as imbox:
    Messages = imbox.messages(sent_from='sheelakhandeka123@gmail.com')
    
    
    for uid, message in Messages:
        invoiceDetailStr = message.body['plain'][0]
        invoiceDetailStr = invoiceDetailStr.split('\r\n')
        invoiceDetails = list(filter(lambda x: len(x) > 0, invoiceDetailStr))
        attachment = message.attachments
        
        obj ={}
        obj["company"] = invoiceDetails[0]
        obj["dateOrdered"] = invoiceDetails[1][invoiceDetails[1].index(":")+2: ]
        obj["invoiceNum"] = invoiceDetails[2][invoiceDetails[2].index(":")+2: ]
        obj["itemOrdered"] = invoiceDetails[3][invoiceDetails[3].index(":")+2: ]
        obj["billingAddr"] = invoiceDetails[4][invoiceDetails[4].index(":")+2: ]
        
        mycursor.execute(f"""insert into info 
                        values('{obj["company"]}','{obj["dateOrdered"]}','{obj["invoiceNum"]}','{obj["itemOrdered"]}','{obj["billingAddr"]}')
                        """)
        
        mysql_db.commit()
        
        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = attachment.get('filename')
                download_path = f"./GMAIL/{att_fn}"
                with open(download_path, "wb") as fp:
                    fp.write(attachment.get('content').read())
                    
                fileData = open(download_path,"rb")
                data = fileData.read()
                fs = gridfs.GridFS(db)
                fs.put(data, filename=att_fn)
            except:
                print(traceback.print_exc())

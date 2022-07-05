import smtplib
import email.message

def enviar_email(log_erro):  
    log_erro  =  log_erro

    corpo_email = f"""
    <p>Foi encontrado erro no teste: {log_erro}</p>    
    <p>Atenciosamente: report erros automation Jr</p>"""

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'remetente'
    msg['To'] = 'destinatario'
    password = 'senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
import uuid
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def member_confirm_mail(mid, email, username, verification):
	plaintext   = get_template('email/member_register.txt')
	htmly   	= get_template('email/member_register.html')
	code 		= "%s-%s/%s" %(verification, mid, uuid.uuid4())
	ctx 		= Context( {'username':username, 'code': code} )

	text_content = plaintext.render(ctx)
	html_content = htmly.render(ctx)

	subject 	= "KIASU.ME User Registration Confirmation"
	from_email 	= "no-reply@KIASU.ME"
	to_email 	= [email]

	msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def reset_password_mail(email, username, password):
	plaintext   = get_template('email/reset_password.txt')
	htmly   	= get_template('email/reset_password.html')
	ctx 		= Context( {'username':username, 'password': password} )

	text_content = plaintext.render(ctx)
	html_content = htmly.render(ctx)

	subject 	= "KIASU.ME Password Reset"
	from_email 	= "no-reply@KIASU.ME"
	to_email 	= [email]

	msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
	msg.attach_alternative(html_content, "text/html")
	msg.send()
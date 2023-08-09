from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.core.mail import EmailMessage
from .models import Employee, Template, Mail_Logs
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    data = Employee.objects.all()
    return render(request,template_name='email_/home.html', context={'data':data})

@api_view()
def schedule_mail(request):
    object = Employee.objects.all()
    todays_day_and_month =  datetime.today().strftime("%m-%d")
    for obj in object:
        birth_date=obj.birth_date.strftime("%m-%d")
        date_of_join=obj.join_date.strftime("%m-%d")
        if todays_day_and_month == birth_date:
            try :
                template = Template.objects.filter(title='Happy Birthday')
                for temp in template:
                    mail_subject = temp.subject
                    message = temp.message
                to_email = obj.email_id
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()


                employee_id = obj.employee_ID
                message = f"Birthday mail sent successfully to {obj.employee_name}"
                type = "Birthday"
                status = "Successfull"
                message_sent_date = datetime.today().strftime("%Y-%m-%d")
                Mail_Logs.objects.create(employee_ID=employee_id,message=message,mail_sent_date=message_sent_date,mail_type=type,status=status)

            except Exception as e:
                employee_id = obj.employee_ID
                message = f"{e}"
                type = "Birthday"
                status = "Failed"
                message_sent_date = datetime.today().strftime("%Y-%m-%d")
                Mail_Logs.objects.create(employee_ID=employee_id,message=message,mail_sent_date=message_sent_date,mail_type=type,status=status)

        if todays_day_and_month == date_of_join:
            try:
                template = Template.objects.filter(title='Work Anniversary')
                for temp in template:
                    mail_subject = temp.subject
                    message = temp.message
                to_email = obj.email_id
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                
                employee_id = obj.employee_ID
                message = f"Anniversary mail sent successfully to {obj.employee_name}"
                type = "Anniversary"
                status = "Successfull"
                message_sent_date = datetime.today().strftime("%Y-%m-%d")
                Mail_Logs.objects.create(employee_ID=employee_id,message=message,mail_sent_date=message_sent_date,mail_type=type,status=status)
            
            except Exception as e:
                employee_id = obj.employee_ID
                message = f"{e}"
                type = "Anniversary"
                status = "Failed"
                message_sent_date = datetime.today().strftime("%Y-%m-%d")
                Mail_Logs.objects.create(employee_ID=employee_id,message=message,mail_sent_date=message_sent_date,mail_type=type,status=status)
        
        else:
            employee_id = obj.employee_ID
            message = "No Events For Today !!"
            type = "No"
            status = "Not Sent"
            message_sent_date = datetime.today().strftime("%Y-%m-%d")
            Mail_Logs.objects.create(employee_ID=employee_id,message=message,mail_sent_date=message_sent_date,mail_type=type,status=status)
            return Response({"Response":"No Events For Today"})
        return Response({"Response":"mail Sent Successfully"})

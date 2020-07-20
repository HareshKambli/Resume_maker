from django.shortcuts import render, redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io


# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        father_name = request.POST.get("father_name","")
        gender = request.POST.get("gender","")
        dob = request.POST.get("dob", "")
        nationality = request.POST.get("nationality", "")
        language = request.POST.get("language", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        company_name1 = request.POST.get("company_name1", "")
        company_exp1 = request.POST.get("company_exp1", "")
        company_desc1 = request.POST.get("company_desc1", "")
        company_name2 = request.POST.get("company_name2", "")
        company_exp2 = request.POST.get("company_exp2", "")
        company_desc2 = request.POST.get("company_desc2", "")
        degree_course = request.POST.get("degree_course", "")
        degree_university = request.POST.get("degree_university","")
        degree_college_name = request.POST.get("degree_college_name", "")
        degree_pass_year = request.POST.get("degree_pass_year", "")
        degree_percentage = request.POST.get("degree_percentage", "")
        college_name = request.POST.get("college_name", "")
        college_university = request.POST.get("college_university", "")
        college_pass_year = request.POST.get("college_pass_year", "")
        college_percentage = request.POST.get("college_percentage", "")
        school_name = request.POST.get("school_name", "")
        school_university = request.POST.get("school_university", "")
        school_pass_year = request.POST.get("school_pass_year", "")
        school_percentage = request.POST.get("school_percentage", "")
        skills = request.POST.get("skills", "")

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree_course=degree_course, degree_college_name=degree_college_name, degree_university=degree_university,
                          degree_pass_year=degree_pass_year, degree_percentage=degree_percentage, college_name=college_name, college_university=college_university,
                          college_pass_year=college_pass_year, college_percentage=college_percentage, school_name=school_name,
                          school_pass_year=school_pass_year, school_university=school_university, school_percentage=school_percentage,
                          skills=skills, father_name=father_name,gender=gender, nationality=nationality,dob=dob,
                          language=language, company_name1=company_name1, company_exp1=company_exp1, company_desc1=company_desc1,
                          company_name2=company_name2, company_exp2=company_exp2, company_desc2=company_desc2)
        profile.save()
        print(profile.id)
        return redirect('list')
    return render(request, 'pdf/accept.html')

def cv(request, id):
    user_profile= Profile.objects.get(pk=id)
    template = loader.get_template('pdf/cv.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }

    path_wkhtmltopdf = r'C:\wkhtmltox\bin\wkhtmltopdf.exe'
    config=pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html, False, options,configuration=config)
    response= HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response

def view_cv(request, id):
    user_profile = Profile.objects.get(id=id)
    return  render(request, 'pdf/cv.html', {'user_profile':user_profile})

def list(request):
    profile = Profile.objects.all
    return render(request, 'pdf/list.html', {'profile':profile})
from django.shortcuts import render,redirect
from .forms import InstituteForm
from .models import Institute
from django.core.exceptions import ValidationError


# Create your views here.

def add_institute(request):
    form = InstituteForm
    return render(request, "create.html", {"form" : form})

def institute_list(request):
    institute = Institute.objects.all()
    print(institute)
    return render(request, 'tables-datatable.html', {'institute' : institute})

# def create_institute(request):
#     print("##########################******************")
#     if request.method == 'POST':
#         registration_number = request.POST.get('RegistrationNo')
#         institute_name = request.POST.get('InstituteName')
#         branch_name = request.POST.get('BranchName')
#         address1 = request.POST.get('Address1')
#         address2 =request.POST.get('Address2')
#         billing_name = request.POST.get('BillingName')
#         district = request.POST.get('District')
#         pin = request.POST.get('Pin')
#         mobile_number = request.POST.get('mobile1')
#         mobile_number2 = request.POST.get('mobile2')
#         fax_number = request.POST.get('FaxNo')
#         email = request.POST.get('Email')
#         website = request.POST.get('WebsiteName')
#         principal_name = request.POST.get('PrincipalName')
#         acc_start_year = request.POST.get('AcstartYear')
#         session_start_month = request.POST.get('SessionStartMonth')
#         accredited_by = request.POST.get('AccreditedBy')
#         scholar_prefix = request.POST.get('Prefix')
#         scholar_suffix = request.POST.get('Suffix')
#         emp_prefix = request.POST.get('EmpPrefix')
#         no_of_pg_in_tcbook = request.POST.get('nopageintc')
#         auto_enroll_no = request.POST.get('AutoEnrollmentNo') == 'on'
#         std_attd_assignment = request.POST.get('STAppAttAssignment') == 'on'
#         live_class_show_time = request.POST.get('LiveClassShowOnTime') == 'on'
#         allow_edit_emp_attd_time = request.POST.get('EditEmpAttendanceTime') == 'on'
#         show_std_contact_no_app = request.POST.get('ShowStudentMobileInApp') == 'on'
#         auto_admin_number = request.POST.get('AutoAdmissionNo') == 'on'
#         live_class_log_Std = request.POST.get('STAppLogLiveClass') == 'on'
#         suggest_auto_section = request.POST.get('AutoSectionAssign') == 'on'
#         send_Std_wc_msg = request.POST.get('SendWelcomeMsgToClassTeacher') == 'on'
#         auto_scholar_no = request.POST.get('AutoScholarNo') == 'on'
#         change_zoom_url = request.POST.get('ChangeZoomURL') == 'on'
#         single_login = request.POST.get('LoginWithSingleDevice') == 'on'
#         suggest_auto_house = request.POST.get('AutoHouseAssign') == 'on'
#         allow_ss_in_app = request.POST.get('AllowScreenshot') == 'on'
#         auto_emp_no = request.POST.get('AutoEmpCode') == 'on'
#         std_attd_through_live_class = request.POST.get('STAppAttLiveClass') == 'on'
#         login_with_single_device = request.POST.get('LoginWithSingleDevice') == 'on'
#         show_yt_opt_4_app = request.POST.get('ShowYoutube') == 'on'
#         show_teach_mo_no_app = request.POST.get('ShowTeacherMobileInApp') == 'on'
#         show_exam_list_res_wise = request.POST.get('ShowExamComboResultWise') == 'on'
#         profile_image = request.FILES.get('profileImage')
        
#         try:
#             institute = Institute.objects.create(
#                 registration_number = registration_number,
#                 institute_name = institute_name,
#                 branch_name = branch_name,
#                 address1 = address1,
#                 address2 = address2,
#                 billing_name = billing_name,
#                 district = district,
#                 pin = pin,
#                 mobile_number = mobile_number,
#                 mobile_number2 = mobile_number2,
#                 fax_number = fax_number,
#                 email = email,
#                 website = website,
#                 principal_name =principal_name,
#                 acc_start_year = acc_start_year,
#                 session_start_month = session_start_month,
#                 accredited_by = accredited_by,
#                 scholar_prefix = scholar_prefix,
#                 scholar_suffix = scholar_suffix,
#                 emp_prefix = emp_prefix,
#                 no_of_pg_in_tcbook = no_of_pg_in_tcbook,
#                 auto_enroll_no = auto_enroll_no,
#                 std_attd_assignment = std_attd_assignment,
#                 live_class_show_time = live_class_show_time,
#                 allow_edit_emp_attd_time = allow_edit_emp_attd_time,
#                 show_std_contact_no_app = show_std_contact_no_app,
#                 auto_admin_number = auto_admin_number,
#                 live_class_log_Std = live_class_log_Std,
#                 suggest_auto_section = suggest_auto_section,
#                 send_Std_wc_msg = send_Std_wc_msg,
#                 auto_scholar_no = auto_scholar_no,
#                 change_zoom_url = change_zoom_url,
#                 single_login = single_login,
#                 suggest_auto_house = suggest_auto_house,
#                 allow_ss_in_app = allow_ss_in_app,
#                 auto_emp_no = auto_emp_no,
#                 std_attd_through_live_class = std_attd_through_live_class,
#                 login_with_single_device = login_with_single_device,
#                 show_yt_opt_4_app = show_yt_opt_4_app,
#                 show_teach_mo_no_app = show_teach_mo_no_app,
#                 show_exam_list_res_wise = show_exam_list_res_wise,
#                 profile_image = profile_image 
#             )
                
            
#             institute.save()
#             return redirect('institute:institute_list')
            
#         except Exception as e:
#             print("")
#             # return HttpResponseBadRequest("Failed to create institute" + str(e) )
#     else:
#         return render(request, 'create.html')    

def create_institute(request):
    errors = []
    if request.method == 'POST':
        data = request.POST
        institute = Institute(
            registration_number=data.get('RegistrationNo'),
            institute_name=data.get('institute_name'),
            branch_name=data.get('BranchName'),
            address1=data.get('Address1'),
            address2=data.get('Address2'),
            billing_name=data.get('BillingName'),
            district=data.get('District'),
            pin=data.get('Pin'),
            mobile_number=data.get('mobile1'),
            mobile_number2=data.get('mobile_number2'),
            fax_number=data.get('fax_number'),
            email=data.get('email'),
            website=data.get('website'),
            principal_name=data.get('principal_name'),
            acc_start_year=data.get('acc_start_year'),
            session_start_month=data.get('session_start_month'),
            accredited_by=data.get('accredited_by'),
            scholar_prefix=data.get('scholar_prefix'),
            scholar_suffix=data.get('scholar_suffix'),
            emp_prefix=data.get('emp_prefix'),
            no_of_pg_in_tcbook=data.get('no_of_pg_in_tcbook'),
            auto_enroll_no=data.get('auto_enroll_no') == 'on',
            std_attd_assignment=data.get('std_attd_assignment') == 'on',
            live_class_show_time=data.get('live_class_show_time') == 'on',
            allow_edit_emp_attd_time=data.get('allow_edit_emp_attd_time') == 'on',
            show_std_contact_no_app=data.get('show_std_contact_no_app') == 'on',
            auto_admin_number=data.get('auto_admin_number') == 'on',
            live_class_log_Std=data.get('live_class_log_Std') == 'on',
            suggest_auto_section=data.get('suggest_auto_section') == 'on',
            send_Std_wc_msg=data.get('send_Std_wc_msg') == 'on',
            auto_scholar_no=data.get('auto_scholar_no') == 'on',
            change_zoom_url=data.get('change_zoom_url') == 'on',
            single_login=data.get('single_login') == 'on',
            suggest_auto_house=data.get('suggest_auto_house') == 'on',
            allow_ss_in_app=data.get('allow_ss_in_app') == 'on',
            auto_emp_no=data.get('auto_emp_no') == 'on',
            std_attd_through_live_class=data.get('std_attd_through_live_class') == 'on',
            login_with_single_device=data.get('login_with_single_device') == 'on',
            show_yt_opt_4_app=data.get('show_yt_opt_4_app') == 'on',
            show_teach_mo_no_app=data.get('show_teach_mo_no_app') == 'on',
            show_exam_list_res_wise=data.get('show_exam_list_res_wise') == 'on',
        )
        
        try:
            institute.full_clean()
            institute.save()
            return redirect('institute:institute-list')
        except ValidationError as e:
            errors = e.message_dict

    return render(request, 'create.html', {'errors': errors})
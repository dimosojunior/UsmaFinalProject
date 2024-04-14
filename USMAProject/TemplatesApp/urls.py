
from django.urls import path
from . import views


urlpatterns = [
    path('', views.USMAHome, name="USMAHome"),
    path('Universities/', views.UniversitiesView, name="Universities"),



#-------------------------ALL COURSES---------------------------
    path('AllUniversityCourses/<int:id>/', views.AllUniversityCourses, name="AllUniversityCourses"),


   #-------------------------ALL PROJECTS---------------------------
    
    path('AllUniversityProjects/<int:id>/', views.AllUniversityProjects, name="AllUniversityProjects"),
    













#----------------------READ PROJECT-------------------------
    path('ReadProject/<int:id>/', views.ReadProject, name="ReadProject"),











#-----------------------------HOB----------------------------------



	path('Hob/', views.HobsView, name="HobsView"),


	path('AllExperts/<int:id>/', views.AllExperts, name="AllExperts"),
	

 






 #----------------------------ARTICLES----------------------------



 	path('Articles/', views.ArticlesView, name="ArticlesView"),

 	path('AllArticles/<int:id>/', views.AllArticles, name="AllArticles"),
 	




#--------------------------READ ARTICLE----------------------

	path('ReadArticle/<int:id>/', views.ReadArticle, name="ReadArticle"),









#--------------------------ADD ARTICLES----------------------------------------
	path('AddArtcle/', views.AddArtcle, name="AddArtcle"),
	











#----------------------------SEARCH-----------------------------
 	path('search_university_autocomplete/', views.search_university_autocomplete, name="search_university_autocomplete"),


#-------------------------------SEARCH COURSES-------------------
 	path('search_university_autocomplete/', views.search_university_autocomplete, name="search_university_autocomplete"),
 	path('udom_search_university_autocomplete/', views.udom_search_university_autocomplete, name="udom_search_university_autocomplete"),
 	path('must_search_university_autocomplete/', views.must_search_university_autocomplete, name="must_search_university_autocomplete"),
 	path('dit_search_university_autocomplete/', views.dit_search_university_autocomplete, name="dit_search_university_autocomplete"),




#------------------------SEARCH PROJECT-------------------------
	path('project_search_university_autocomplete/', views.project_search_university_autocomplete, name="project_search_university_autocomplete"),


#------------------------SEARCH HOB-------------------------
	path('search_hob_autocomplete/', views.search_hob_autocomplete, name="search_hob_autocomplete"),


#------------------------SEARCH EXPERTS-------------------------
	path('experts_search_autocomplete/', views.experts_search_autocomplete, name="experts_search_autocomplete"),
	path('graphics_experts_search_autocomplete/', views.graphics_experts_search_autocomplete, name="graphics_experts_search_autocomplete"),
	path('mobile_application_experts_search_autocomplete/', views.mobile_application_experts_search_autocomplete, name="mobile_application_experts_search_autocomplete"),
	path('computer_maintenance_experts_search_autocomplete/', views.computer_maintenance_experts_search_autocomplete, name="computer_maintenance_experts_search_autocomplete"),
	path('machine_learning_experts_search_autocomplete/', views.machine_learning_experts_search_autocomplete, name="machine_learning_experts_search_autocomplete"),
	path('computer_vision_experts_search_autocomplete/', views.computer_vision_experts_search_autocomplete, name="computer_vision_experts_search_autocomplete"),
	path('automation_experts_search_autocomplete/', views.automation_experts_search_autocomplete, name="automation_experts_search_autocomplete"),
	path('data_analysis_experts_search_autocomplete/', views.data_analysis_experts_search_autocomplete, name="data_analysis_experts_search_autocomplete"),







#------------------------SEARCH ARTICLES-------------------------
	path('all_articles_search_autocomplete/', views.all_articles_search_autocomplete, name="all_articles_search_autocomplete"),

	path('articles_search_autocomplete/', views.articles_search_autocomplete, name="articles_search_autocomplete"),
	path('Websites_articles_search_autocomplete/', views.Websites_articles_search_autocomplete, name="Websites_articles_search_autocomplete"),
	path('Mobile_App_articles_search_autocomplete/', views.Mobile_App_articles_search_autocomplete, name="Mobile_App_articles_search_autocomplete"),









#------------------CONTACT ME----------------------------
	path('ContactMe/', views.ContactMe, name="ContactMe"),








#----------------------------------READ EXPERT---------------------------
	path('ReadExpert/<int:id>/', views.ReadExpert, name="ReadExpert"),



#-------------------------------ADD PROJECT------------------------


#---------------------------ADD PROJECT-----------------------------
	path('AddProject/', views.AddProject, name="AddProject"),
	


]

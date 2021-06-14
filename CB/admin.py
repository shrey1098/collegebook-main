from django.contrib import admin
from .models import College, UserDetails, CollegeReview, CollegeQuestion, QuestionAnswers, FollowCollege


# Register your models here.


class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "location", "year", "specialization")


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ("user", "college", "user_type")


class CollegeReviewAdmin(admin.ModelAdmin):
    list_display = ("college", "user", "review", "time")


class CollegeQuestionAdmin(admin.ModelAdmin):
    list_display = ("college", "user", "question", "time")


class QuestionAnswersAdmin(admin.ModelAdmin):
    list_display = ("question", "college", "user", "answer", "time")


class FollowCollegeAdmin(admin.ModelAdmin):
    list_display = ("user", "college")


admin.site.register(College, CollegeAdmin)
admin.site.register(UserDetails, UserDetailsAdmin)
admin.site.register(CollegeReview, CollegeReviewAdmin)
admin.site.register(CollegeQuestion, CollegeQuestionAdmin)
admin.site.register(QuestionAnswers, QuestionAnswersAdmin)
admin.site.register(FollowCollege, FollowCollegeAdmin)

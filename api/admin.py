from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    User, Category, Course, CourseEnrollment, Batch, BatchEnrollment,
    Lecture, Note, Assignment, AssignmentSubmission, Attendance,
    Progress, Notification, Doubt, DoubtReply, Payment, FeeReceipt,
    ExamResult, CodingQuestion, Schedule, ChatMessage, Poll, PollOption,
    Quiz, QuizQuestion, QuizAttempt,
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'phone', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active')
    search_fields = ('email', 'name', 'phone')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone', 'avatar')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone', 'password1', 'password2', 'role'),
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'color', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_free', 'is_active', 'total_students')
    list_filter = ('is_active', 'is_free', 'category')
    search_fields = ('title',)


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_free', 'is_active', 'total_students')
    list_filter = ('is_active', 'is_free', 'category')
    search_fields = ('name',)


@admin.register(BatchEnrollment)
class BatchEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'batch', 'enrolled_at')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'subject', 'is_free', 'order')
    list_filter = ('is_free', 'video_type')
    search_fields = ('title',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'subject', 'is_free', 'download_count')
    search_fields = ('title',)


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'batch', 'due_date', 'total_marks')
    search_fields = ('title',)


@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'status', 'submitted_at')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'batch', 'date', 'status')
    list_filter = ('status',)


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'completion_percent', 'certificate_issued')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'type', 'is_read', 'created_at')
    list_filter = ('type', 'is_read')


@admin.register(Doubt)
class DoubtAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'is_resolved', 'created_at')
    list_filter = ('is_resolved',)


@admin.register(DoubtReply)
class DoubtReplyAdmin(admin.ModelAdmin):
    list_display = ('doubt', 'user', 'created_at')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'status', 'created_at')
    list_filter = ('status',)


@admin.register(FeeReceipt)
class FeeReceiptAdmin(admin.ModelAdmin):
    list_display = ('student', 'receipt_number', 'amount', 'status', 'paid_date')
    list_filter = ('status',)


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam_name', 'subject', 'percentage', 'result')
    list_filter = ('result',)


@admin.register(CodingQuestion)
class CodingQuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'language', 'course')
    list_filter = ('difficulty', 'language')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'type', 'start_time', 'end_time', 'is_active')
    list_filter = ('type', 'is_active')


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'course', 'type', 'created_at')


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'course', 'is_active', 'created_at')


@admin.register(PollOption)
class PollOptionAdmin(admin.ModelAdmin):
    list_display = ('poll', 'text', 'votes')


class QuizQuestionInline(admin.TabularInline):
    model = QuizQuestion
    extra = 0


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'course', 'duration', 'total_marks', 'is_active')
    list_filter = ('is_active', 'category')
    search_fields = ('title',)
    inlines = [QuizQuestionInline]


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'percentage', 'passed', 'submitted_at')
    list_filter = ('passed',)

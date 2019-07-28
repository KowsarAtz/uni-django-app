# Generated by Django 2.1.7 on 2019-05-27 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields
import django_jalali.db.models
import users.models
import users.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', django_enumfield.db.fields.EnumField(default=0, enum=users.models.CourseApprovalState)),
                ('deleted_by_carrier', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', django_enumfield.db.fields.EnumField(default=0, enum=users.models.CarrierStatusType)),
                ('admission_type_num', django_enumfield.db.fields.EnumField(default=0, enum=users.models.AdmissionType)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades_status_num', django_enumfield.db.fields.EnumField(default=0, enum=users.models.CourseGradesStatus)),
                ('midterm_exam_date', django_jalali.db.models.jDateTimeField(blank=True, null=True)),
                ('final_exam_date', django_jalali.db.models.jDateTimeField(blank=True, null=True)),
                ('section_number', models.PositiveSmallIntegerField()),
                ('capacity', models.PositiveSmallIntegerField()),
                ('students_gender', django_enumfield.db.fields.EnumField(default=0, enum=users.models.GenderTypeAllowed, verbose_name='Genders allowed to register the course')),
                ('carriers', models.ManyToManyField(blank=True, related_name='registered_courses', through='users.Attend', to='users.Carrier')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practical_units', models.PositiveSmallIntegerField()),
                ('theoritical_units', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DayRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DayTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', django_enumfield.db.fields.EnumField(default=0, enum=users.models.Day)),
                ('day_range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.DayRange')),
            ],
        ),
        migrations.CreateModel(
            name='DayTimeCourseRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Course')),
                ('day_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.DayTime')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='users.College')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('degree', django_enumfield.db.fields.EnumField(default=0, enum=users.models.DegreeType)),
                ('departments', models.ManyToManyField(related_name='fields', to='users.Department')),
                ('head_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_fields', to='users.Department')),
            ],
        ),
        migrations.CreateModel(
            name='FieldCourse',
            fields=[
                ('serial_number', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('corequisites', models.ManyToManyField(blank=True, related_name='corequisite_for', to='users.FieldCourse')),
                ('credit_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_courses', to='users.Credit')),
                ('prerequisites', models.ManyToManyField(blank=True, related_name='prerequisite_for', to='users.FieldCourse')),
            ],
        ),
        migrations.CreateModel(
            name='FieldCourseSubfieldRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggested_term', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('course_type_num', django_enumfield.db.fields.EnumField(default=0, enum=users.models.FieldCourseType)),
                ('field_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.FieldCourse')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_of_twenty', models.FloatField(default=20.0)),
                ('value', models.FloatField(default=0.0)),
                ('base_value', models.FloatField(default=20.0)),
                ('date_examined', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('attend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='users.Attend')),
            ],
        ),
        migrations.CreateModel(
            name='PreliminaryRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_reg_relations', to='users.Carrier')),
                ('field_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.FieldCourse')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('pic', models.ImageField(default='pic_folder/no-img.jpg', upload_to='pic_folder/', validators=[users.utils.validate_image_size])),
            ],
        ),
        migrations.CreateModel(
            name='Subfield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subfields', to='users.Field')),
                ('field_courses', models.ManyToManyField(related_name='subfields', through='users.FieldCourseSubfieldRelation', to='users.FieldCourse')),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', django_jalali.db.models.jDateField()),
                ('end_date', django_jalali.db.models.jDateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_login_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='term',
            unique_together={('start_date', 'end_date')},
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('title', 'place')},
        ),
        migrations.AddField(
            model_name='preliminaryregistration',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Term'),
        ),
        migrations.AddField(
            model_name='fieldcoursesubfieldrelation',
            name='subfield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Subfield'),
        ),
        migrations.AlterUniqueTogether(
            name='dayrange',
            unique_together={('start', 'end')},
        ),
        migrations.AlterUniqueTogether(
            name='credit',
            unique_together={('practical_units', 'theoritical_units')},
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='users.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='departments',
            field=models.ManyToManyField(blank=True, related_name='allowed_courses', to='users.Department', verbose_name='Departments allowed to register the course'),
        ),
        migrations.AddField(
            model_name='course',
            name='field_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='users.FieldCourse'),
        ),
        migrations.AddField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(related_name='courses', through='users.Teach', to='users.Professor'),
        ),
        migrations.AddField(
            model_name='course',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='users.Room'),
        ),
        migrations.AddField(
            model_name='course',
            name='subfields',
            field=models.ManyToManyField(blank=True, related_name='allowed_courses', to='users.Subfield', verbose_name='Subfields allowed to register the course'),
        ),
        migrations.AddField(
            model_name='course',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='users.Term'),
        ),
        migrations.AddField(
            model_name='course',
            name='weekly_schedule',
            field=models.ManyToManyField(related_name='courses', through='users.DayTimeCourseRelation', to='users.DayTime'),
        ),
        migrations.AddField(
            model_name='carrier',
            name='login_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carrier', to='users.UserLoginProfile'),
        ),
        migrations.AddField(
            model_name='carrier',
            name='pre_reg_field_courses',
            field=models.ManyToManyField(blank=True, related_name='carriers', through='users.PreliminaryRegistration', to='users.FieldCourse'),
        ),
        migrations.AddField(
            model_name='carrier',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carriers', to='users.Student'),
        ),
        migrations.AddField(
            model_name='carrier',
            name='subfield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carriers', to='users.Subfield'),
        ),
        migrations.AddField(
            model_name='attend',
            name='carrier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Carrier'),
        ),
        migrations.AddField(
            model_name='attend',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attend_instances', to='users.Course'),
        ),
        migrations.AlterUniqueTogether(
            name='subfield',
            unique_together={('field', 'title')},
        ),
        migrations.AlterUniqueTogether(
            name='fieldcoursesubfieldrelation',
            unique_together={('field_course', 'subfield')},
        ),
        migrations.AlterUniqueTogether(
            name='field',
            unique_together={('head_department', 'title', 'degree')},
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together={('title', 'college')},
        ),
        migrations.AlterUniqueTogether(
            name='daytimecourserelation',
            unique_together={('day_time', 'course')},
        ),
        migrations.AlterUniqueTogether(
            name='daytime',
            unique_together={('day_range', 'day')},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('field_course', 'term', 'section_number')},
        ),
        migrations.AlterUniqueTogether(
            name='attend',
            unique_together={('course', 'carrier')},
        ),
    ]
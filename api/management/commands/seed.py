from django.core.management.base import BaseCommand
from api.models import User, Category, Quiz, QuizQuestion


DEFAULT_CATEGORIES = [
    {'name': 'JEE',             'icon': '⚛️',  'color': '#FF6B35', 'order': 1},
    {'name': 'NEET',            'icon': '🧬',  'color': '#4CAF50', 'order': 2},
    {'name': 'Class 11',        'icon': '📗',  'color': '#2196F3', 'order': 3},
    {'name': 'Class 12',        'icon': '📘',  'color': '#9C27B0', 'order': 4},
    {'name': 'Foundation',      'icon': '🏗️', 'color': '#FF9800', 'order': 5},
    {'name': 'Python',          'icon': '🐍',  'color': '#3776AB', 'order': 6},
    {'name': 'Java',            'icon': '☕',  'color': '#ED8B00', 'order': 7},
    {'name': 'Web Development', 'icon': '🌐',  'color': '#E44D26', 'order': 8},
    {'name': 'Data Science',    'icon': '📊',  'color': '#00BCD4', 'order': 9},
    {'name': 'UPSC',            'icon': '🏛️', 'color': '#795548', 'order': 10},
    {'name': 'Other',           'icon': '📚',  'color': '#607D8B', 'order': 11},
]

QUIZ_DATA = [
    {
        'category': 'Python',
        'title': 'Python Basics',
        'duration': 20,
        'questions': [
            {
                'question': 'Python ma variable declare kem thay?',
                'options': ['var', 'let', 'direct assignment', 'int'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': 'Python ma variable declare karva koi keyword ni jarur nathi, direct assignment thi thay.',
            },
            {
                'question': 'Python file extension su che?',
                'options': ['.java', '.py', '.js', '.html'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Python files .py extension thi save thay.',
            },
            {
                'question': 'Output print karva mate su use thay?',
                'options': ['echo()', 'print()', 'show()', 'display()'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Python ma output print karva print() function use thay.',
            },
            {
                'question': 'Python kai type ni language che?',
                'options': ['compiled', 'interpreted', 'assembly', 'machine'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Python ek interpreted language che.',
            },
            {
                'question': 'Python case sensitive che?',
                'options': ['No', 'Yes'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Python case sensitive che, Name ane name alag variables che.',
            },
            {
                'question': 'Comment kai symbol thi lakhay?',
                'options': ['//', '#', '<!-- -->', '**'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Python ma single line comment # thi sharu thay.',
            },
            {
                'question': 'Input leva mate su use thay?',
                'options': ['scan()', 'get()', 'input()', 'read()'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': 'Python ma user input leva input() function use thay.',
            },
            {
                'question': 'Python ma indentation shu mate?',
                'options': ['decoration', 'syntax', 'comment', 'output'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Python ma indentation syntax nu part che, code block define kare che.',
            },
            {
                'question': 'Python ma keyword example su?',
                'options': ['var', 'if', 'value', 'data'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'if ek Python keyword che jo conditional statement mate use thay.',
            },
            {
                'question': 'Python open source che?',
                'options': ['No', 'Yes'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Python ek free ane open source programming language che.',
            },
        ],
    },
    {
        'category': 'Python',
        'title': 'Python Data Types',
        'duration': 15,
        'questions': [
            {
                'question': 'List kai bracket ma hoy?',
                'options': ['()', '[]', '{}', '<>'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'List square brackets [] ma define thay.',
            },
            {
                'question': 'Tuple kai bracket ma hoy?',
                'options': ['[]', '{}', '()', '<>'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': 'Tuple round brackets () ma define thay.',
            },
            {
                'question': 'Dictionary kai bracket ma hoy?',
                'options': ['[]', '()', '<>', '{}'],
                'correctAnswer': 3,
                'marks': 1,
                'explanation': 'Dictionary curly brackets {} ma define thay.',
            },
            {
                'question': 'String datatype su?',
                'options': ['int', 'float', 'str', 'bool'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': 'String datatype str che.',
            },
            {
                'question': 'Integer datatype su?',
                'options': ['str', 'int', 'float', 'list'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Integer datatype int che.',
            },
            {
                'question': 'Float datatype su?',
                'options': ['int', 'str', 'float', 'bool'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': 'Decimal numbers mate float datatype use thay.',
            },
            {
                'question': 'Boolean value su hoy?',
                'options': ['0/1', 'yes/no', 'True/False', 'on/off'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': 'Boolean ma sirf True ya False value hoy che.',
            },
            {
                'question': 'List mutable che?',
                'options': ['No', 'Yes'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'List mutable che, create karya pachhi pan change kari shakay.',
            },
            {
                'question': 'Tuple mutable che?',
                'options': ['Yes', 'No'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Tuple immutable che, create karya pachhi change nai thay.',
            },
            {
                'question': 'Set duplicate allow kare?',
                'options': ['Yes', 'No'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Set ma duplicate values allow nathi thati.',
            },
        ],
    },
    {
        'category': 'Python',
        'title': 'Python OOP',
        'duration': 20,
        'questions': [
            {
                'question': 'OOP nu full form su che?',
                'options': [
                    'Object Oriented Program',
                    'Object Oriented Programming',
                    'Object Order Program',
                    'None',
                ],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'OOP = Object Oriented Programming.',
            },
            {
                'question': 'Class define karva mate su use thay?',
                'options': ['object', 'class', 'def', 'new'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Python ma class keyword thi class define thay.',
            },
            {
                'question': 'Object su che?',
                'options': ['function', 'variable', 'class nu instance', 'module'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': 'Object ek class nu instance che.',
            },
            {
                'question': 'Constructor kai method che?',
                'options': ['start()', 'create()', '__init__', 'new()'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': '__init__ method constructor che jo object create thay tyare automatically call thay.',
            },
            {
                'question': 'self keyword shu represent kare che?',
                'options': ['global variable', 'class name', 'current object', 'function name'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': 'self current object ne represent kare che.',
            },
            {
                'question': 'Inheritance shu che?',
                'options': ['code delete', 'code reuse', 'code error', 'loop'],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Inheritance thi ek class biji class ni properties reuse kari shake che.',
            },
            {
                'question': 'Ek class bija class ni property use kare te su?',
                'options': ['Encapsulation', 'Polymorphism', 'Inheritance', 'Abstraction'],
                'correctAnswer': 2,
                'marks': 1,
                'explanation': 'Inheritance ma child class parent class ni properties use kare che.',
            },
            {
                'question': 'Encapsulation shu che?',
                'options': ['data hide karvu', 'loop', 'function call', 'variable declare'],
                'correctAnswer': 0,
                'marks': 1,
                'explanation': 'Encapsulation ma data ane methods ne ek sathe bundle kari ne hide karva ma aave che.',
            },
            {
                'question': 'Polymorphism shu che?',
                'options': ['ek name, alag behavior', 'same code', 'loop', 'class'],
                'correctAnswer': 0,
                'marks': 1,
                'explanation': 'Polymorphism ma same method name alag alag class ma alag behavior kare che.',
            },
            {
                'question': 'Abstraction shu che?',
                'options': [
                    'details show karvi',
                    'unnecessary details hide karvi',
                    'loop run karvu',
                    'object banavvu',
                ],
                'correctAnswer': 1,
                'marks': 1,
                'explanation': 'Abstraction ma unnecessary implementation details hide kari ne sirf important part show karva ma aave che.',
            },
        ],
    },
]


class Command(BaseCommand):
    help = 'Seed the database with default categories, admin user, and Python quizzes'

    def handle(self, *args, **options):
        self.stdout.write('🌱 Starting seed...')

        # ── Categories ────────────────────────────────────────────────────────
        cat_count = 0
        for cat_data in DEFAULT_CATEGORIES:
            _, created = Category.objects.update_or_create(
                name=cat_data['name'],
                defaults=cat_data,
            )
            if created:
                cat_count += 1
        self.stdout.write(self.style.SUCCESS(
            f'✅ Categories: {cat_count} created, {len(DEFAULT_CATEGORIES) - cat_count} already existed'
        ))

        # ── Admin user ────────────────────────────────────────────────────────
        admin_email = 'test@pw.com'
        if User.objects.filter(email=admin_email).exists():
            admin_user = User.objects.get(email=admin_email)
            admin_user.role = 'admin'
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.save()
            self.stdout.write(self.style.SUCCESS(f'✅ Admin user updated: {admin_email}'))
        else:
            User.objects.create_superuser(
                email=admin_email,
                name='Admin User',
                phone='9999999999',
                password='123456',
            )
            self.stdout.write(self.style.SUCCESS(f'✅ Admin user created: {admin_email} / 123456'))

        # ── Quizzes ───────────────────────────────────────────────────────────
        quiz_count = 0
        for qd in QUIZ_DATA:
            try:
                category = Category.objects.get(name=qd['category'])
            except Category.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f'⚠️  Category "{qd["category"]}" not found — skipping "{qd["title"]}"'
                ))
                continue

            if Quiz.objects.filter(title=qd['title'], category=category).exists():
                self.stdout.write(f'⏭️  Quiz "{qd["title"]}" already exists — skipping')
                continue

            total_marks = sum(q['marks'] for q in qd['questions'])
            passing_marks = round(total_marks * 0.4)

            quiz = Quiz.objects.create(
                title=qd['title'],
                category=category,
                duration=qd['duration'],
                total_marks=total_marks,
                passing_marks=passing_marks,
                is_active=True,
            )

            for i, q in enumerate(qd['questions']):
                QuizQuestion.objects.create(
                    quiz=quiz,
                    question=q['question'],
                    options=q['options'],
                    correct_answer=q['correctAnswer'],
                    marks=q['marks'],
                    explanation=q['explanation'],
                    order=i,
                )

            self.stdout.write(self.style.SUCCESS(
                f'✅ Quiz added: "{qd["title"]}" ({len(qd["questions"])} questions)'
            ))
            quiz_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'\n🎉 Seed complete! {quiz_count} quizzes added.'
        ))

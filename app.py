from flask import Flask, render_template

app = Flask(__name__)

services = [
    {"icon": "💻", "title": "تصميم المواقع", "desc": "نصمم مواقع احترافية وجذابة تعكس هوية علامتك التجارية.", "features": ["UI/UX Design", "Responsive Design", "Landing Pages"]},
    {"icon": "⚙️", "title": "تطوير المواقع", "desc": "نطور مواقع وتطبيقات ويب بأحدث التقنيات.", "features": ["Frontend & Backend", "E-commerce", "Web Apps"]},
    {"icon": "📱", "title": "إدارة السوشيال ميديا", "desc": "نبني حضورك الرقمي على كل منصات التواصل.", "features": ["Content Creation", "Community Management", "Analytics"]},
    {"icon": "🚀", "title": "التسويق الرقمي", "desc": "نضع استراتيجيات تسويقية تصل لجمهورك المستهدف.", "features": ["Google Ads", "Meta Ads", "SEO & SEM"]},
]

projects = [
    {"title": "منصة تسوق إلكتروني", "category": "تطوير مواقع", "tag": "E-Commerce", "color": "purple", "desc": "متجر إلكتروني متكامل مع نظام دفع ولوحة تحكم."},
    {"title": "حملة تسويقية", "category": "تسويق رقمي", "tag": "Digital Marketing", "color": "blue", "desc": "حملة إعلانية حققت 3x ROI خلال 30 يوم."},
    {"title": "موقع شركة خدمات", "category": "تصميم مواقع", "tag": "Web Design", "color": "teal", "desc": "موقع احترافي مع تجربة مستخدم سلسة."},
    {"title": "إدارة سوشيال ميديا", "category": "سوشيال ميديا", "tag": "Social Media", "color": "pink", "desc": "نمو 200% في المتابعين خلال 3 أشهر."},
]

stats = [
    {"number": "50+", "label": "مشروع منجز"},
    {"number": "30+", "label": "عميل سعيد"},
    {"number": "3x",  "label": "متوسط ROI"},
    {"number": "24/7","label": "دعم فني"},
]

@app.route("/")
def home():
    return render_template("index.html", services=services, projects=projects, stats=stats)

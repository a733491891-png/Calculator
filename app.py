from flask import Flask, render_template_string

app = Flask(__name__)

# كود الإعلان المشترك الذي سيفتح مع كل ضغطة زر
AD_SCRIPT = """
<script>
function openAdAndNavigate(url) {
    // فتح الإعلان في نافذة جديدة خلفية (Pop-under)
    window.open("https://www.effectivecpmnetwork.com/ini6wd4r?key=2310fbd3cc6aadd5c14d9bbf226e1075", "_blank");
    // الانتقال للصفحة المطلوبة بداخل الموقع فوراً
    window.location.href = url;
}
</script>
"""

# الستايل المشترك لجميع الصفحات (Dark Cyber Theme)
SHARED_STYLE = """
<style>
    :root {
        --bg-main: #0a0b10;
        --bg-card: #141622;
        --accent-neon: #00ffcc;
        --accent-blue: #0077ff;
        --text-main: #f5f6f9;
        --text-muted: #8a8f9f;
    }
    body {
        background-color: var(--bg-main);
        color: var(--text-main);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding-bottom: 50px;
    }
    .navbar-brand {
        font-weight: 800;
        color: var(--accent-neon) !important;
    }
    .calculator-card {
        background-color: var(--bg-card);
        border: 1px solid rgba(0, 255, 204, 0.1);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-top: 40px;
    }
    .form-control, .form-select {
        background-color: #1a1d2f !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: var(--text-main) !important;
        border-radius: 10px;
        padding: 12px;
    }
    .btn-calc {
        background: linear-gradient(135deg, var(--accent-neon) 0%, var(--accent-blue) 100%);
        color: var(--bg-main);
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 14px;
        transition: 0.3s;
    }
    .btn-calc:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0, 255, 204, 0.3);
    }
    .btn-back {
        background-color: #1a1d2f;
        color: var(--text-main);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 10px 20px;
        text-decoration: none;
        transition: 0.3s;
    }
    .btn-back:hover {
        background-color: var(--accent-neon);
        color: var(--bg-main);
    }
    .result-box {
        background-color: #1a1d2f;
        border-right: 4px solid var(--accent-neon);
        border-radius: 10px;
        padding: 20px;
        margin-top: 25px;
        display: none;
    }
    .result-value {
        color: var(--accent-neon);
        font-size: 1.5rem;
        font-weight: 700;
    }
    /* ستايل المنيو الرئيسي */
    .menu-card {
        background-color: var(--bg-card);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 20px;
        cursor: pointer;
        transition: 0.3s;
    }
    .menu-card:hover {
        border-color: var(--accent-neon);
        transform: translateY(-5px);
        box-shadow: 0px 5px 15px rgba(0, 255, 204, 0.2);
    }
</style>
"""

# ----------------- 1. الصفحة الرئيسية (قائمة الخيارات) -----------------
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🧮 المنصة المالية الذكية | الرئيسية</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """ + SHARED_STYLE + AD_SCRIPT + """
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark pt-3">
    <div class="container">
        <a class="navbar-brand" href="#"><i class="fa-solid fa-wallet me-2"></i> SMART FINANCE</a>
    </div>
</nav>

<div class="container text-center mt-5">
    <h1 class="fw-bold mb-3">المنصة المالية الذكية 🧮</h1>
    <p class="text-muted fs-5 mb-5">اختر الأداة المناسبة لك لبدء الحسابات الدقيقة فوراً. (كل خيار يفتح صفحة مستقلة وإعلان جديد)</p>
    
    <div class="row g-4 justify-content-center">
        <div class="col-md-4 col-sm-6">
            <div class="menu-card" onclick="openAdAndNavigate('/car')">
                <i class="fa-solid fa-car fa-3x mb-3 text-info"></i>
                <h4>حاسبة قرض السيارة</h4>
                <p class="text-muted small">احسب قسط التمويل والفائدة</p>
            </div>
        </div>
        <div class="col-md-4 col-sm-6">
            <div class="menu-card" onclick="openAdAndNavigate('/mortgage')">
                <i class="fa-solid fa-house fa-3x mb-3 text-warning"></i>
                <h4>حاسبة الرهن العقاري</h4>
                <p class="text-muted small">حساب قروض البيوت والعقارات</p>
            </div>
        </div>
        <div class="col-md-4 col-sm-6">
            <div class="menu-card" onclick="openAdAndNavigate('/insurance')">
                <i class="fa-solid fa-shield-halved fa-3x mb-3 text-success"></i>
                <h4>حاسبة قسط التأمين</h4>
                <p class="text-muted small">تقدير تكاليف التأمين الشامل</p>
            </div>
        </div>
        <div class="col-md-4 col-sm-6">
            <div class="menu-card" onclick="openAdAndNavigate('/zakat')">
                <i class="fa-solid fa-hand-holding-dollar fa-3x mb-3 text-danger"></i>
                <h4>حاسبة الزكاة الشرعية</h4>
                <p class="text-muted small">احسب زكاة مالك بدقة 2.5%</p>
            </div>
        </div>
        <div class="col-md-4 col-sm-6">
            <div class="menu-card" onclick="openAdAndNavigate('/savings')">
                <i class="fa-solid fa-piggy-bank fa-3x mb-3" style="color: #ff00ff;"></i>
                <h4>حاسبة الادخار والتقاعد</h4>
                <p class="text-muted small">خطط لثروتك المستقبلية المركبة</p>
            </div>
        </div>
    </div>
</div>

</body>
</html>
"""

# ----------------- الـ Routes (التوجيهات لباقي الصفحات المنفصلة) -----------------

@app.route("/")
def home():
    return render_template_string(HOME_TEMPLATE)

@app.route("/car")
def car():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl"><head><meta charset="UTF-8"><title>حاسبة قرض السيارة</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """ + SHARED_STYLE + """</head><body>
    <div class="container row justify-content-center mx-auto">
        <div class="col-md-8 calculator-card">
            <a href="/" class="btn-back"><i class="fa-solid fa-arrow-right me-2"></i>العودة للرئيسية</a>
            <h3 class="mt-4 mb-4 text-center text-info"><i class="fa-solid fa-car me-2"></i> حاسبة تمويل وقروض السيارات</h3>
            <div class="row g-3">
                <div class="col-md-6"><label class="form-label">سعر السيارة الكلي ($)</label><input type="number" id="carPrice" class="form-control" value="20000"></div>
                <div class="col-md-6"><label class="form-label">الدُفعة الأولى ($)</label><input type="number" id="carDownPayment" class="form-control" value="4000"></div>
                <div class="col-md-6"><label class="form-label">نسبة الفائدة السنوية (%)</label><input type="number" id="carInterest" class="form-control" value="4.5" step="0.1"></div>
                <div class="col-md-6"><label class="form-label">مدة القرض (بالسنوات)</label><select id="carYears" class="form-select"><option value="3">3 سنوات</option><option value="5" selected>5 سنوات</option></select></div>
                <button onclick="calculateCarLoan()" class="btn btn-calc w-100 mt-4">🚀 إحسب القسط الشهري</button>
            </div>
            <div id="carResult" class="result-box"><p class="mb-1 text-muted">القسط الشهري المتوقع:</p><div id="carMonthlyPay" class="result-value">$0.00</div></div>
        </div>
    </div>
    <script>
    function calculateCarLoan() {
        let price = parseFloat(document.getElementById('carPrice').value) || 0;
        let down = parseFloat(document.getElementById('carDownPayment').value) || 0;
        let interest = parseFloat(document.getElementById('carInterest').value) || 0;
        let years = parseFloat(document.getElementById('carYears').value) || 5;
        let principal = price - down;
        let monthlyInterest = (interest / 100) / 12;
        let totalMonths = years * 12;
        let monthlyPay = (monthlyInterest === 0) ? (principal / totalMonths) : (principal * monthlyInterest * Math.pow(1 + monthlyInterest, totalMonths)) / (Math.pow(1 + monthlyInterest, totalMonths) - 1);
        document.getElementById('carMonthlyPay').innerText = "$" + monthlyPay.toFixed(2);
        document.getElementById('carResult').style.display = 'block';
    }
    </script>
    </body></html>
    """)

@app.route("/mortgage")
def mortgage():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl"><head><meta charset="UTF-8"><title>حاسبة الرهن العقاري</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """ + SHARED_STYLE + """</head><body>
    <div class="container row justify-content-center mx-auto">
        <div class="col-md-8 calculator-card">
            <a href="/" class="btn-back"><i class="fa-solid fa-arrow-right me-2"></i>العودة للرئيسية</a>
            <h3 class="mt-4 mb-4 text-center text-warning"><i class="fa-solid fa-house me-2"></i> حاسبة الرهن العقاري</h3>
            <div class="row g-3">
                <div class="col-md-6"><label class="form-label">قيمة العقار ($)</label><input type="number" id="homePrice" class="form-control" value="150000"></div>
                <div class="col-md-6"><label class="form-label">المقدمة المدفوعة ($)</label><input type="number" id="homeDownPayment" class="form-control" value="30000"></div>
                <div class="col-md-6"><label class="form-label">الفائدة الثابتة (%)</label><input type="number" id="homeInterest" class="form-control" value="5.0" step="0.1"></div>
                <div class="col-md-6"><label class="form-label">مدة الرهن</label><select id="homeYears" class="form-select"><option value="15">15 سنة</option><option value="30" selected>30 سنة</option></select></div>
                <button onclick="calculateMortgage()" class="btn btn-calc w-100 mt-4">🚀 احسب تكلفة الرهن</button>
            </div>
            <div id="mortgageResult" class="result-box"><p class="mb-1 text-muted">الدفع الشهري:</p><div id="mortgageMonthlyPay" class="result-value">$0.00</div></div>
        </div>
    </div>
    <script>
    function calculateMortgage() {
        let price = parseFloat(document.getElementById('homePrice').value) || 0;
        let down = parseFloat(document.getElementById('homeDownPayment').value) || 0;
        let interest = parseFloat(document.getElementById('homeInterest').value) || 0;
        let years = parseFloat(document.getElementById('homeYears').value) || 30;
        let principal = price - down;
        let monthlyInterest = (interest / 100) / 12;
        let totalMonths = years * 12;
        let monthlyPay = (principal * monthlyInterest * Math.pow(1 + monthlyInterest, totalMonths)) / (Math.pow(1 + monthlyInterest, totalMonths) - 1);
        document.getElementById('mortgageMonthlyPay').innerText = "$" + monthlyPay.toFixed(2);
        document.getElementById('mortgageResult').style.display = 'block';
    }
    </script>
    </body></html>
    """)

@app.route("/insurance")
def insurance():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl"><head><meta charset="UTF-8"><title>حاسبة التأمين</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """ + SHARED_STYLE + """</head><body>
    <div class="container row justify-content-center mx-auto">
        <div class="col-md-8 calculator-card">
            <a href="/" class="btn-back"><i class="fa-solid fa-arrow-right me-2"></i>العودة للرئيسية</a>
            <h3 class="mt-4 mb-4 text-center text-success"><i class="fa-solid fa-shield-halved me-2"></i> حاسبة قسط التأمين التقديرية</h3>
            <div class="row g-3">
                <div class="col-md-6"><label class="form-label">عمر المتقدم</label><input type="number" id="insAge" class="form-control" value="25"></div>
                <div class="col-md-6"><label class="form-label">نوع التأمين</label><select id="insType" class="form-select"><option value="100">تأمين صحي شامل</option><option value="150">تأمين سيارة شامل</option></select></div>
                <button onclick="calculateInsurance()" class="btn btn-calc w-100 mt-4">🚀 احسب القسط</button>
            </div>
            <div id="insResult" class="result-box"><p class="mb-1 text-muted">القسط الشهري المقدر:</p><div id="insMonthlyPay" class="result-value">$0.00</div></div>
        </div>
    </div>
    <script>
    function calculateInsurance() {
        let age = parseFloat(document.getElementById('insAge').value) || 25;
        let baseRate = parseFloat(document.getElementById('insType').value);
        let ageModifier = age < 25 ? 1.2 : 1.0;
        document.getElementById('insMonthlyPay').innerText = "$" + (baseRate * ageModifier).toFixed(2);
        document.getElementById('insResult').style.display = 'block';
    }
    </script>
    </body></html>
    """)

@app.route("/zakat")
def zakat():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl"><head><meta charset="UTF-8"><title>حاسبة الزكاة</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """ + SHARED_STYLE + """</head><body>
    <div class="container row justify-content-center mx-auto">
        <div class="col-md-8 calculator-card">
            <a href="/" class="btn-back"><i class="fa-solid fa-arrow-right me-2"></i>العودة للرئيسية</a>
            <h3 class="mt-4 mb-4 text-center text-danger"><i class="fa-solid fa-hand-holding-dollar me-2"></i> حاسبة الزكاة الشرعية</h3>
            <div class="row g-3">
                <div class="col-md-12"><label class="form-label">إجمالي الأموال والمدخرات ($ أو دينار)</label><input type="number" id="zakatMoney" class="form-control" value="10000"></div>
                <button onclick="calculateZakat()" class="btn btn-calc w-100 mt-4">🚀 احسب مقدار الزكاة الواجبة (2.5%)</button>
            </div>
            <div id="zakatResult" class="result-box"><p class="mb-1 text-muted">مقدار الزكاة الواجب إخراجها:</p><div id="zakatValue" class="result-value">0.00</div></div>
        </div>
    </div>
    <script>
    function calculateZakat() {
        let money = parseFloat(document.getElementById('zakatMoney').value) || 0;
        document.getElementById('zakatValue').innerText = (money * 0.025).toFixed(2);
        document.getElementById('zakatResult').style.display = 'block';
    }
    </script>
    </body></html>
    """)

@app.route("/savings")
def savings():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl"><head><meta charset="UTF-8"><title>حاسبة الادخار والتقاعد</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """ + SHARED_STYLE + """</head><body>
    <div class="container row justify-content-center mx-auto">
        <div class="col-md-8 calculator-card">
            <a href="/" class="btn-back"><i class="fa-solid fa-arrow-right me-2"></i>العودة للرئيسية</a>
            <h3 class="mt-4 mb-4 text-center" style="color: #ff00ff;"><i class="fa-solid fa-piggy-bank me-2"></i> حاسبة مخطط التقاعد والادخار</h3>
            <div class="row g-3">
                <div class="col-md-6"><label class="form-label">المبلغ المدخر شهرياً ($)</label><input type="number" id="saveMonthly" class="form-control" value="200"></div>
                <div class="col-md-6"><label class="form-label">العائد السنوي المتوقع (%)</label><input type="number" id="saveReturn" class="form-control" value="6" step="0.1"></div>
                <div class="col-md-12"><label class="form-label">عدد سنوات الادخار</label><input type="number" id="saveYears" class="form-control" value="20"></div>
                <button onclick="calculateSavings()" class="btn btn-calc w-100 mt-4">🚀 احسب إجمالي الثروة</button>
            </div>
            <div id="savingsResult" class="result-box"><p class="mb-1 text-muted">إجمالي مدخراتك المتوقعة:</p><div id="savingsTotal" class="result-value">$0.00</div></div>
        </div>
    </div>
    <script>
    function calculateSavings() {
        let monthly = parseFloat(document.getElementById('saveMonthly').value) || 0;
        let rate = parseFloat(document.getElementById('saveReturn').value) || 0;
        let years = parseFloat(document.getElementById('saveYears').value) || 0;
        let monthlyRate = (rate / 100) / 12;
        let months = years * 12;
        let total = 0;
        for(let i=0; i<months; i++) { total = (total + monthly) * (1 + monthlyRate); }
        document.getElementById('savingsTotal').innerText = "$" + total.toFixed(2);
        document.getElementById('savingsResult').style.display = 'block';
    }
    </script>
    </body></html>
    """)

if __name__ == "__main__":
    app.run(debug=True)

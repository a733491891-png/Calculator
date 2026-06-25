from flask import Flask, render_template_string

app = Flask(__name__)

# الواجهة الرسومية الخرافية (Dark Cybernetic Premium Theme)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🧮 المنصة المالية الذكية | Smart Finance Hub</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
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
            letter-spacing: 1px;
        }
        .hero-section {
            text-align: center;
            padding: 40px 0;
            background: linear-gradient(180deg, rgba(0,255,204,0.05) 0%, rgba(10,11,16,0) 100%);
        }
        /* تصميم التبويبات الفخم */
        .nav-pills .nav-link {
            color: var(--text-muted);
            background-color: var(--bg-card);
            border: 1px solid rgba(255,255,255,0.05);
            margin: 5px;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .nav-pills .nav-link.active, .nav-pills .nav-link:hover {
            color: var(--bg-main) !important;
            background-color: var(--accent-neon) !important;
            box-shadow: 0px 0px 15px rgba(0, 255, 204, 0.4);
        }
        /* تصميم الكارد والحاسبات */
        .calculator-card {
            background-color: var(--bg-card);
            border: 1px solid rgba(0, 255, 204, 0.1);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .form-control, .form-select {
            background-color: #1a1d2f !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            color: var(--text-main) !important;
            border-radius: 10px;
            padding: 12px;
        }
        .form-control:focus, .form-select:focus {
            border-color: var(--accent-neon) !important;
            box-shadow: 0 0 10px rgba(0, 255, 204, 0.2) !important;
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
            color: var(--bg-main);
        }
        .result-box {
            background-color: #1a1d2f;
            border-right: 4px solid var(--accent-neon);
            border-radius: 10px;
            padding: 20px;
            margin-top: 25px;
            display: none; /* تظهر فقط بعد الحساب */
        }
        .result-value {
            color: var(--accent-neon);
            font-size: 1.5rem;
            font-weight: 700;
        }
    </style>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark pt-3">
    <div class="container">
        <a class="navbar-brand" href="#"><i class="fa-solid fa-wallet me-2"></i> SMART FINANCE</a>
    </div>
</nav>

<div class="hero-section">
    <div class="container">
        <h1 class="fw-bold mb-2">المنصة المالية الذكية 🧮</h1>
        <p class="text-muted fs-5">أدوات تفاعلية متقدمة لحساب القروض، الرهن، التأمين، والزكاة بدقة متناهية وبضغطة زر.</p>
    </div>
</div>

<div class="container mt-4">
    <ul class="nav nav-pills justify-content-center mb-5" id="financeTabs" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link active" id="car-tab" data-bs-toggle="pill" data-bs-target="#car" type="button" role="tab"><i class="fa-solid fa-car list-icon me-2"></i>قرض السيارة</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="mortgage-tab" data-bs-toggle="pill" data-bs-target="#mortgage" type="button" role="tab"><i class="fa-solid fa-house me-2"></i>الرهن العقاري</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="insurance-tab" data-bs-toggle="pill" data-bs-target="#insurance" type="button" role="tab"><i class="fa-solid fa-shield-halved me-2"></i>التأمين</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="zakat-tab" data-bs-toggle="pill" data-bs-target="#zakat" type="button" role="tab"><i class="fa-solid fa-hand-holding-dollar me-2"></i>حاسبة الزكاة</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link" id="savings-tab" data-bs-toggle="pill" data-bs-target="#savings" type="button" role="tab"><i class="fa-solid fa-piggy-bank me-2"></i>الادخار والتقاعد</button>
        </li>
    </ul>

    <div class="tab-content row justify-content-center" id="financeTabsContent">
        
        <div class="tab-pane fade show active col-md-8" id="car" role="tabpanel">
            <div class="calculator-card">
                <h3 class="mb-4 text-center text-info"><i class="fa-solid fa-car me-2"></i> حاسبة تمويل وقروض السيارات</h3>
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label">سعر السيارة الكلي ($)</label>
                        <input type="number" id="carPrice" class="form-control" value="20000">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">الدُفعة الأولى ($)</label>
                        <input type="number" id="carDownPayment" class="form-control" value="4000">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">نسبة الفائدة السنوية (%)</label>
                        <input type="number" id="carInterest" class="form-control" value="4.5" step="0.1">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">مدة القرض (بالسنوات)</label>
                        <select id="carYears" class="form-select">
                            <option value="3">3 سنوات</option>
                            <option value="5" selected>5 سنوات</option>
                            <option value="7">7 سنوات</option>
                        </select>
                    </div>
                    <button onclick="calculateCarLoan()" class="btn btn-calc w-100 mt-4">🚀 إحسب القسط الشهري الأفضل</button>
                </div>
                <div id="carResult" class="result-box">
                    <p class="mb-1 text-muted">القسط الشهري المتوقع:</p>
                    <div id="carMonthlyPay" class="result-value">$0.00</div>
                </div>
            </div>
        </div>

        <div class="tab-pane fade col-md-8" id="mortgage" role="tabpanel">
            <div class="calculator-card">
                <h3 class="mb-4 text-center text-warning"><i class="fa-solid fa-house me-2"></i> حاسبة الرهن العقاري والبيوت</h3>
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label">قيمة العقار ($)</label>
                        <input type="number" id="homePrice" class="form-control" value="150000">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">المقدمة المدفوعة ($)</label>
                        <input type="number" id="homeDownPayment" class="form-control" value="30000">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">الفائدة الثابتة (%)</label>
                        <input type="number" id="homeInterest" class="form-control" value="5.0" step="0.1">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">مدة الرهن</label>
                        <select id="homeYears" class="form-select">
                            <option value="15">15 سنة</option>
                            <option value="20">20 سنة</option>
                            <option value="30" selected>30 سنة</option>
                        </select>
                    </div>
                    <button onclick="calculateMortgage()" class="btn btn-calc w-100 mt-4">🚀 احسب تكلفة الرهن</button>
                </div>
                <div id="mortgageResult" class="result-box">
                    <p class="mb-1 text-muted">الدفع الشهري للرهن العقاري:</p>
                    <div id="mortgageMonthlyPay" class="result-value">$0.00</div>
                </div>
            </div>
        </div>

        <div class="tab-pane fade col-md-8" id="insurance" role="tabpanel">
            <div class="calculator-card">
                <h3 class="mb-4 text-center text-success"><i class="fa-solid fa-shield-halved me-2"></i> حاسبة قسط التأمين التقديرية</h3>
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label">عمر المتقدم للتأمين</label>
                        <input type="number" id="insAge" class="form-control" value="25">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">نوع التأمين المطلوب</label>
                        <select id="insType" class="form-select">
                            <option value="100">تأمين صحي شامل</option>
                            <option value="150">تأمين سيارة شامل</option>
                            <option value="80">تأمين على الممتلكات</option>
                        </select>
                    </div>
                    <div class="col-md-12">
                        <label class="form-label">هل السجل يحتوي على حوادث سابقة؟</label>
                        <select id="insHistory" class="form-select">
                            <option value="1.0">سجل نظيف بالكامل (لا توجد حوادث)</option>
                            <option value="1.3">توجد حوادث سابقة (مخاطر متوسطة)</option>
                        </select>
                    </div>
                    <button onclick="calculateInsurance()" class="btn btn-calc w-100 mt-4">🚀 احسب القسط التقديري اليومي/الشهري</button>
                </div>
                <div id="insResult" class="result-box">
                    <p class="mb-1 text-muted">قسط التأمين الشهري المقدر:</p>
                    <div id="insMonthlyPay" class="result-value">$0.00</div>
                </div>
            </div>
        </div>

        <div class="tab-pane fade col-md-8" id="zakat" role="tabpanel">
            <div class="calculator-card">
                <h3 class="mb-4 text-center text-danger"><i class="fa-solid fa-hand-holding-dollar me-2"></i> حاسبة الزكاة الشرعية الدقيقة</h3>
                <div class="row g-3">
                    <div class="col-md-12">
                        <label class="form-label">إجمالي الأموال والمدخرات التي دار عليها الحول ($ أو دينار)</label>
                        <input type="number" id="zakatMoney" class="form-control" value="10000">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">قيمة الذهب المعد للتجارة (إن وجد)</label>
                        <input type="number" id="zakatGold" class="form-control" value="0">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">قيمة الفضة أو الأسهم (إن وجد)</label>
                        <input type="number" id="zakatSilver" class="form-control" value="0">
                    </div>
                    <button onclick="calculateZakat()" class="btn btn-calc w-100 mt-4">🚀 احسب مقدار الزكاة الواجبة (2.5%)</button>
                </div>
                <div id="zakatResult" class="result-box">
                    <p class="mb-1 text-muted">مقدار الزكاة الواجب إخراجها فوراً:</p>
                    <div id="zakatValue" class="result-value">0.00</div>
                </div>
            </div>
        </div>

        <div class="tab-pane fade col-md-8" id="savings" role="tabpanel">
            <div class="calculator-card">
                <h3 class="mb-4 text-center" style="color: #ff00ff;"><i class="fa-solid fa-piggy-bank me-2"></i> حاسبة مخطط التقاعد والادخار الذكي</h3>
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label">المبلغ المدخر شهرياً ($)</label>
                        <input type="number" id="saveMonthly" class="form-control" value="200">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">العائد السنوي المتوقع المتراكم (%)</label>
                        <input type="number" id="saveReturn" class="form-control" value="6" step="0.1">
                    </div>
                    <div class="col-md-12">
                        <label class="form-label">عدد سنوات الادخار حتى التقاعد</label>
                        <input type="number" id="saveYears" class="form-control" value="20">
                    </div>
                    <button onclick="calculateSavings()" class="btn btn-calc w-100 mt-4">🚀 احسب إجمالي ثروتك المستقبلية</button>
                </div>
                <div id="savingsResult" class="result-box">
                    <p class="mb-1 text-muted">إجمالي مدخراتك المتراكمة مع الأرباح المركبة:</p>
                    <div id="savingsTotal" class="result-value">$0.00</div>
                </div>
            </div>
        </div>

    </div>
</div>

<script>
function triggerPopunder() {
    // كود فتح إعلانك المنبثق في صفحة ثانية عند كل عملية حسابية
    window.open("https://www.effectivecpmnetwork.com/ini6wd4r?key=2310fbd3cc6aadd5c14d9bbf226e1075", "_blank");
}

function calculateCarLoan() {
    triggerPopunder();
    let price = parseFloat(document.getElementById('carPrice').value) || 0;
    let down = parseFloat(document.getElementById('carDownPayment').value) || 0;
    let interest = parseFloat(document.getElementById('carInterest').value) || 0;
    let years = parseFloat(document.getElementById('carYears').value) || 5;
    
    let principal = price - down;
    let monthlyInterest = (interest / 100) / 12;
    let totalMonths = years * 12;
    
    let monthlyPay = 0;
    if (monthlyInterest === 0) {
        monthlyPay = principal / totalMonths;
    } else {
        monthlyPay = (principal * monthlyInterest * Math.pow(1 + monthlyInterest, totalMonths)) / (Math.pow(1 + monthlyInterest, totalMonths) - 1);
    }
    
    document.getElementById('carMonthlyPay').innerText = "$" + monthlyPay.toFixed(2);
    document.getElementById('carResult').style.display = 'block';
}

function calculateMortgage() {
    triggerPopunder();
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

function calculateInsurance() {
    triggerPopunder();
    let age = parseFloat(document.getElementById('insAge').value) || 25;
    let baseRate = parseFloat(document.getElementById('insType').value);
    let historyModifier = parseFloat(document.getElementById('insHistory').value);
    
    // معادلة بسيطة: الصغار في السن يدفعون أكثر للمخاطر
    let ageModifier = age < 25 ? 1.2 : 1.0;
    let totalInsurance = baseRate * historyModifier * ageModifier;
    
    document.getElementById('insMonthlyPay').innerText = "$" + totalInsurance.toFixed(2);
    document.getElementById('insResult').style.display = 'block';
}

function calculateZakat() {
    triggerPopunder();
    let money = parseFloat(document.getElementById('zakatMoney').value) || 0;
    let gold = parseFloat(document.getElementById('zakatGold').value) || 0;
    let silver = parseFloat(document.getElementById('zakatSilver').value) || 0;
    
    let totalZakat = (money + gold + silver) * 0.025;
    
    document.getElementById('zakatValue').innerText = totalZakat.toFixed(2);
    document.getElementById('zakatResult').style.display = 'block';
}

function calculateSavings() {
    triggerPopunder();
    let monthly = parseFloat(document.getElementById('saveMonthly').value) || 0;
    let rate = parseFloat(document.getElementById('saveReturn').value) || 0;
    let years = parseFloat(document.getElementById('saveYears').value) || 0;
    
    let monthlyRate = (rate / 100) / 12;
    let months = years * 12;
    let total = 0;
    
    for(let i=0; i<months; i++) {
        total = (total + monthly) * (1 + monthlyRate);
    }
    
    document.getElementById('savingsTotal').innerText = "$" + total.toFixed(2);
    document.getElementById('savingsResult').style.display = 'block';
}
</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)

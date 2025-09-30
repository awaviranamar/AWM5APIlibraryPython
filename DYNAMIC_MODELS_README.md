# 🔄 מדריך לטעינה דינמית של מודלים

## 📖 סקירה כללית

הספרייה תומכת כעת בטעינה דינמית של מודלים מותאמים אישית. זה מאפשר למתכנתים ליצור מודלים מותאמים אישית שיחליפו את הפונקציות הסטנדרטיות ב-endpoints.

## 🏗️ איך זה עובד?

1. **בדיקה אוטומטית**: כאשר נוצר אובייקט `endpoints`, המערכת בודקת אוטומטית את תיקיית `models/`
2. **זיהוי מודלים**: המערכת מחפשת קבצי Python שמכילים קלאסים המסתיימים ב-`Model`
3. **החלפה דינמית**: פונקציות שמתחילות בשם המודל מוחלפות אוטומטית

## 📁 מבנה התיקיות

```
project/
│
├── models/                    # תיקיית המודלים המותאמים
│   ├── __init__.py
│   ├── Accidents.py          # מודל מותאם עבור Accidents
│   ├── Assets.py             # מודל מותאם עבור Assets (אופציונלי)
│   └── WorkOrders.py         # מודל מותאם עבור WorkOrders (אופציונלי)
│
├── endpoints.py              # קובץ ה-endpoints המעודכן
├── ApiClient.py
└── ...
```

## 🛠️ יצירת מודל מותאם אישית

### שלב 1: יצירת קובץ המודל

צור קובץ חדש בתיקיית `models/` עם השם של ה-endpoint (לדוגמה: `Accidents.py`):

```python
'''
    Custom Accidents Model - מודל מותאם אישית עבור Accidents
'''

class AccidentsModel:
    def __init__(self, ApiClient):
        self.ApiClient = ApiClient

    def Accidents_Get(self):
        """פונקציה מותאמת אישית לקבלת תאונות"""
        print("🚗 משתמש במודל מותאם אישית עבור Accidents_Get")
        # הוסף לוגיקה מותאמת אישית כאן
        return self.ApiClient.getAPI('/accidents')

    def Accidents_GetWithDetails(self, accident_id):
        """פונקציה חדשה שלא קיימת ב-endpoints המקורי"""
        print(f"🚗 פונקציה חדשה: קבלת תאונה עם פרטים: {accident_id}")
        return self.ApiClient.getAPI(f'/accidents/{accident_id}')
```

### שלב 2: כללי שמות

- **שם הקובץ**: חייב להתאים לשם ה-endpoint (לדוגמה: `Accidents.py`)
- **שם הקלאס**: חייב להסתיים ב-`Model` (לדוגמה: `AccidentsModel`)
- **שמות הפונקציות**: חייבים להתחיל בשם ה-endpoint + `_` (לדוגמה: `Accidents_Get`)

## 🎯 דוגמאות שימוש

### דוגמה 1: החלפת פונקציה קיימת

```python
# במודל המותאם (models/Accidents.py)
def Accidents_Get(self):
    print("🔄 משתמש בגרסה מותאמת אישית")
    # הוסף לוגיקה מותאמת (לוגים, ולידציה, וכו')
    return self.ApiClient.getAPI('/accidents')

# בקוד הראשי
from ApiClient import ApiClient

client = ApiClient()
result = client.API.Accidents_Get()  # ישתמש בגרסה המותאמת
```

### דוגמה 2: הוספת פונקציה חדשה

```python
# במודל המותאם (models/Assets.py)
class AssetsModel:
    def __init__(self, ApiClient):
        self.ApiClient = ApiClient
    
    def Assets_GetWithMaintenanceHistory(self, asset_id):
        """פונקציה חדשה שמחזירה נכס עם היסטוריית תחזוקה"""
        asset_data = self.ApiClient.getAPI(f'/assets/{asset_id}')
        maintenance_data = self.ApiClient.getAPI(f'/assets/{asset_id}/maintenance')
        return {
            'asset': asset_data,
            'maintenance_history': maintenance_data
        }

# בקוד הראשי
result = client.API.Assets_GetWithMaintenanceHistory(123)
```

## 🔍 בדיקת הטעינה

הרץ את קובץ הבדיקה כדי לוודא שהמודלים נטענים כראוי:

```bash
python test_dynamic_models.py
```

## ⚡ יתרונות

1. **גמישות**: אפשרות להתאים פונקציות לצרכים ספציפיים
2. **הרחבה**: הוספת פונקציות חדשות ללא שינוי הקוד הבסיסי
3. **תחזוקה**: קל לעדכן ולתחזק מודלים נפרדים
4. **בדיקות**: אפשרות ליצור מודלי בדיקה (mock) בקלות

## 🚨 הערות חשובות

1. **שמות קבצים**: חייבים להתאים בדיוק לשם ה-endpoint
2. **מבנה הקלאס**: חייב לכלול `__init__(self, ApiClient)`
3. **שמות פונקציות**: חייבים להתחיל בשם ה-endpoint
4. **טיפול בשגיאות**: המערכת תמשיך לעבוד גם אם יש שגיאה בטעינת מודל

## 🔧 פתרון בעיות

### בעיה: המודל לא נטען
- ✅ בדוק שהקובץ נמצא בתיקיית `models/`
- ✅ בדוק ששם הקובץ תואם לשם ה-endpoint
- ✅ בדוק ששם הקלאס מסתיים ב-`Model`

### בעיה: הפונקציה לא מוחלפת
- ✅ בדוק ששם הפונקציה מתחיל בשם ה-endpoint + `_`
- ✅ בדוק שהפונקציה לא מתחילה ב-`_` (פונקציות פרטיות)

## 📞 תמיכה

לשאלות ותמיכה, פנה אל Aviran Amar - API Support Engineer at AssetWorks
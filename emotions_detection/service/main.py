from fastapi import FastAPI 
from service.api.api import main_router
import onnxruntime as rt 

app = FastAPI(project_name="Emotions Detection")
app.include_router(main_router) ## This router contain emo_router and test_router

providers = ['CPUExecutionProvider']
m_q = rt.InferenceSession(
        "service/core/logic/zidan.onnx", providers=providers)

@app.get("/")
def root():
    return {"hello":"world"}



""""
async the function in detect.py + test.py + main.py

تخيّل إنك نشرت الـ اي بي أي تبعك، وصار عندك 20 مستخدمًا يرفعون صورًا في نفس الوقت لتصنيف المشاعر

إذا شغّلت التطبيق بطريقة بسيطة باستخدام يوفي كورن، فقد تكون تعمل بعملية واحدة فقط.
 أما باستخدام جونيكورن مع عدة وركورس، فتقدر تشغّل عدة عمليات مستقلة من التطبيق لمعالجة الطلبات.
gunicorn service main.app --workers 2 --worker-class uvicorn.workers.UvicornWorker

"""
from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')

def predictor(request):
    return render(request,'main.html')

def formInfo(request):
    task = request.GET['task']  
    experience = request.GET['experience']

    y_pred=model.predict([[task,experience]])
    if y_pred[0]==1:
        y_pred='Ayush'
    
    elif y_pred[0]==2:
        y_pred='Parth'
    
    elif y_pred[0]==3:
        y_pred='Devansh'
    elif y_pred[0]==4:
        y_pred='Aradhya'
    elif y_pred[0]==5:
        y_pred='Astha'
    elif y_pred[0]==6:
        y_pred='Devika'
    elif y_pred[0]==7:
        y_pred='Kritika'
    elif y_pred[0]==8:
        y_pred='Tanmay'
    elif y_pred[0]==9:
        y_pred='Tarun'
    elif y_pred[0]==10:
        y_pred='Anurag'
    elif y_pred[0]==11:
        y_pred='Charu'
    elif y_pred[0]==12:
        y_pred='Janvi'
    elif y_pred[0]==13:
        y_pred='Himani'
    elif y_pred[0]==14:
        y_pred='Pranjal'
    elif y_pred[0]==15:
        y_pred='Ashish'
    elif y_pred[0]==16:
        y_pred='Aditya'
    elif y_pred[0]==17:
        y_pred='Abhimanyu'
    elif y_pred[0]==18:
        y_pred='Ram'
    elif y_pred[0]==19:
        y_pred='Daksh'
    elif y_pred[0]==20:
        y_pred='Shiv'
    elif y_pred[0]==21:
        y_pred='Juhi'
    elif y_pred[0]==22:
        y_pred='Vanya'
    elif y_pred[0]==23:
        y_pred='Disha'
    elif y_pred[0]==24:
        y_pred='Aniket'
    elif y_pred[0]==25:
        y_pred='Abhishek'
    elif y_pred[0]==26:
        y_pred='Saloni'
    elif y_pred[0]==27:
        y_pred='Tanya'
    elif y_pred[0]==28:
        y_pred='Pari'
    elif y_pred[0]==29:
        y_pred='Prateek'
    elif y_pred[0]==30:
        y_pred='Lavanya'
    elif y_pred[0]==31:
        y_pred='Ankur'
    elif y_pred[0]==31:
        y_pred='Anjali'
    elif y_pred[0]==32:
        y_pred='Krishna'
    elif y_pred[0]==33:
        y_pred='Arjun'
    elif y_pred[0]==34:
        y_pred='Mukesh'
    elif y_pred[0]==35:
        y_pred='Pal'
    elif y_pred[0]==36:
        y_pred='Suman'
    elif y_pred[0]==37:
        y_pred='Kusum'
    elif y_pred[0]==38:
        y_pred='Rajpal'
    elif y_pred[0]==39:
        y_pred='Megha'
    elif y_pred[0]==40:
        y_pred='Neeru'
    elif y_pred[0]==41:
        y_pred='Anand'
    elif y_pred[0]==42:
        y_pred='Ashok'
    elif y_pred[0]==43:
        y_pred='Anuradha'
    elif y_pred[0]==44:
        y_pred='Mohit'
    elif y_pred[0]==45:
        y_pred='Divyansh'
    elif y_pred[0]==46:
        y_pred='Himanshu'
    elif y_pred[0]==47:
        y_pred='Chirag'
    elif y_pred[0]==48:
        y_pred='Isha'
    elif y_pred[0]==49:
        y_pred='Jasleen'
    else:
        y_pred='Invalid'
    
        
    return render(request,'result.html', {'result' : y_pred})
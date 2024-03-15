from fastapi import FastAPI
from fastapi import FastAPI,Request,Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,JSONResponse
from database import SessionLocal
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import models
from fastapi import Form

app = FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")



def get_db():
    db=None
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()




@app.get('/update') 
def get_form(request:Request,db:Session = Depends(get_db)):
    new_user=db.query(models.New).filter(models.New.status=="ACTIVE").all()
    return templates.TemplateResponse("test.html",context={"request":request,"new_id":new_user})

@app.get("/delete/{id}")
def create_data(id:int,request:Request,db:Session=Depends(get_db)):
    db.query(models.New).filter(models.New.id==id,models.New.status=="ACTIVE").update({"status":"INACTIVE"})
    db.commit()
    return RedirectResponse("/update",status_code=302)

# @app.get('/insert')
# def dashboard(request:Request,db:Session = Depends(get_db)):
#     return templates.TemplateResponse("add.html",context={"request":request})
#chart
@app.get('/chart')
def get_chart(id: int, request: Request, db: Session = Depends(get_db)):
    new_night = 80  # Placeholder value, replace with your actual logic
    new_day = 20    # Placeholder value, replace with your actual logic

    print("New night:", new_night)
    print("New day:", new_day)

    return templates.TemplateResponse("dashboard.html", context={"request": request, "new_day": new_day, "new_night": new_night})



@app.post('/add')
def create(request:Request,db:Session = Depends(get_db),ename:str=Form(...),session:str=Form(...),logindate:str=Form(...),logintime:str=Form(...),logouttime:str=Form(...)):
    status1="Active"
    find=db.query(models.SignUp).filter(models.New.ename==ename).first()
    if find is None:
        body=models.New(ename=ename,session=session,logindate=logindate,logintime=logintime,logouttime=logouttime,status=status1)
        db.add(body)
        db.commit()
        error="Done"
        #return RedirectResponse("/update")
        return get_form(request, db=db)
    else:
        error="Already Exists"


@app.put("/edit_emp/{id}")
def edit_emp(id:int,request:Request,db:Session=Depends(get_db)):
    data=db.query(models.New).filter(models.New.id==id,models.New.status=="ACTIVE").first()
    content=jsonable_encoder(data)
    return JSONResponse(content=content)


@app.post("/updatedata")
def create_data(request:Request,db:Session=Depends(get_db),edit_id:int=Form(...),edit_name:str=Form(...),edit_session:str=Form(...),edit_logindate:str=Form(...),edit_logintime:str=Form(...),edit_logouttime:str=Form(...)):
    find=db.query(models.New).filter(models.New.id!=edit_id,models.New.ename==edit_name,models.New.status =="ACTIVE").first()
    if find is None:
        db.query(models.New).filter(models.New.id==edit_id).update({"ename":edit_name,"session":edit_session,"logindate":edit_logindate,"logintime":edit_logintime,"logouttime":edit_logouttime})
        db.commit()
        error = "Done"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error = "Already this name Exist"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    


#Dashboard
@app.get('/dashboard') 
def get_dash(request:Request,db:Session = Depends(get_db)):
    return templates.TemplateResponse("dashboard.html",context={"request":request})



#Signup
# @app.get('/signup')
# def get_user(request:Request,db:Session = Depends(get_db)):
#     return templates.TemplateResponse("signup.html",context={"request":request})


# @app.post('/newuser')
# def create(request:Request,db:Session = Depends(get_db),name:str=Form(...),username:str=Form(...),email:str=Form(...),gender:str=Form(...),number:str=Form(...),password:str=Form(...)):
#     status1="Active"
#     find=db.query(models.SignUp).filter(models.SignUp.username==username).first()
#     if find is None:
#         body=models.SignUp(name=name,username=username,email=email,gender=gender,number=number,password=password,status=status1)
#         db.add(body)
#         db.commit()
#         error="Done"
#         #return RedirectResponse("/update")
#         return get_login(request, db=db)
#     else:
#         error="Already Exists"


#login
@app.get('/login')
def get_login(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/logcheck")
def logcheck(request:Request,db:Session=Depends(get_db),login_user:str=Form(...),login_password:str=Form(...)):
    print(login_user,login_password)
    find=db.query(models.SignUp).filter(models.SignUp.username==login_user,models.SignUp.password==login_password).first()
    if find is None:
        error= "Invalid Creditional"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error= "Done"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)

# @app.post('/loginuser')
# def login(request: Request, db: Session = Depends(get_db), username: str = Form(...), password: str = Form(...)):
#     user = db.query(models.SignUp).filter(models.SignUp.username == username, models.SignUp.password == password).first()
#     if user:
#         return JSONResponse(content={"status": "success"})
#     else:
#         return JSONResponse(content={"status": "failure"})




# Card Files
@app.get('/card') 
def get_card(request:Request,db:Session = Depends(get_db)):
    new_user=db.query(models.Card).filter(models.Card.cname=="Zoho").first()
    return templates.TemplateResponse("card.html",context={"request":request,"new_name":new_user})




#card loop 
@app.get('/loop')
def loop_card(request:Request,db:Session = Depends(get_db)):
    new_card = db.query(models.Col).all()
    print(new_card)
    return templates.TemplateResponse("loop.html",context={"request":request,"new_card":new_card})

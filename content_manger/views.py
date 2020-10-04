from django.shortcuts import render
import pymysql
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def connection():
    try:
        db=pymysql.connect("localhost","root1","Sahil@19970","blogs" )
        cursor=db.cursor()
        return cursor
    except Exception as e:
        print("there is an exception in creating the cursor",e)

def dashboard(request):
    try:
        cursor=connection()
        try:
            cursor.execute("SELECT Title,id,date,SUBSTRING(description,1 , 100) FROM posts ")
            results=cursor.fetchall()
            data=[]
            for i in range(len(results)):
                data.append(results[i])
            paginator=Paginator(data,4)
            page_number=request.GET.get('page',1)
            print(page_number)
            print(paginator)
            page_obj = paginator.get_page(page_number)
            print(page_obj)
            print(data)
            return render(request,"dashboard.html",{'pages':page_obj})
        except Exception as e:
            print("there is an exception in database",e)
    except Exception as e:
        print("there is an exception in database",e)
    return render(request,'base.html')

def archieve(request):
    cursor=connection()
    try:
        cursor.execute("Select monthname(date),id,year(date) from posts")
        results=cursor.fetchall()

        dict_data={}
     

        try:
            r=0
            for j in range(len(results)):
                try:
                    cursor.execute("Select count(title) from posts where monthname(date)='"+results[j][0]+"'")
                    results1=cursor.fetchone()
                  
                    dict_data[results[j][2]]=set()
                except Exception as e:
                    print("there  is an exception in fetching archieve main data",e)      
 
            print(dict_data)
            for r in range(len(results)):
                for key in dict_data:
                    if key == results[r][2]:
                        for f in range(len(results)):
                            try:
                                cursor.execute("Select count(title) from posts where monthname(date)='"+results[r][0]+"'AND year(date)='"+str(results[r][2])+"' ")
                                results1=cursor.fetchone()
                            except Exception as e:
                                print("there is an exception in getting count data for archieve",e)
                        dict_data[key].add((results[r][0],results1[0]))         
            print(dict_data)   
     
            
            return render(request,"archieve.html",{'data':dict_data})
        except Exception as e:
            print("exception in getting count ",e)
    except Exception as e:
        print("Exception in archieve getting data",e)

    return render(request,"archieve.html")

def tags(request):
    cursor=connection()
    try:
        cursor.execute("SELECT  tags.id,tags.name  from tags INNER JOIN posts ON posts.tags_id =tags.id ")
        results=cursor.fetchall()
        print("these are results_________",results)
        tag_data={}
        j=0
        for i in results:
            tag_data[i[0]]=i[1]
            j=j+1
        print(tag_data)

    except Exception as e:
        tag_data={}
        print("there is an exception in tags",e)
    
    return render(request,"tags.html",{'results':tag_data})

def blog_view(request,id):
    try:
        if id!="":
            try:
                cursor=connection()
                cursor.execute("select * from posts where id='"+str(id)+"'")
                results=cursor.fetchall()
                dict_data={}
                date=""
                for i in results:
                    date=i[4]
                    dict_data[i[0]]={i[1]:i[2]}
                print(dict_data)
                print(date)
                return render(request,"blog.html",{'data':dict_data,'date':date})
            except Exception as e:
                print("error in fetching data",e)

    except Exception as e:
        print("there is an error in blog_view",e)


    
def tag_list(request,id):
    try:
        if id!="":
            try:
                cursor=connection()
                cursor.execute("select id,title,date from posts where tags_id='"+str(id)+"'")
                results=cursor.fetchall()
                dict_data={}
                for i in results:
                
                    dict_data[i[0]]={i[2]:i[1]}
                print(dict_data)
                try:
                    cursor.execute("SELECT name from tags where id='"+str(id)+"'")
                    results=cursor.fetchone()
                    names=results[0]
                    if names:
                        return render(request,"tag_list.html",{'data':dict_data,'names':names})
                    else:
                        try:
                            cursor.execute("SELECT month from tags where id='"+str(id)+"'")
                            results=cursor.fetchone()
                            date=results[0]
                        except Exception as e:
                            return render(request,"tag_list.html",{'data':dict_data})
                            print("error in fetching data of tags",e)
                except Exception as e:
                    return render(request,"tag_list.html",{'data':dict_data})
                    print("error in fetching data of tags",e)
                    
                
            except Exception as e:
                print("there is an error in tag_list",e)
    except Exception as e:
        print(e)

def year_list(request,year):
    if year!="":
        try:
            cursor=connection()
            cursor.execute("Select id,title,date from posts where year(date)='"+year+"'")
            results=cursor.fetchall()
            dict_data={}
            print(results)
            for i in results: 
                dict_data[i[0]]={i[2]:i[1]}

            return render(request,"month-list.html",{'data':dict_data})
        except Exception as e:
            return render(request,"month-list.html")
            print("there is an exception",e)
def month_list(request,year,month):
    if month!="" and year!="":
        try:
            cursor=connection()
            cursor.execute("Select id,title,date from posts where monthname(date)='"+month+"' AND year(date)='"+year+"'")
            results=cursor.fetchall()
            dict_data={}
            print(results)
            for i in results: 
                    dict_data[i[0]]={i[2]:i[1]}
            return render(request,"month-list.html",{'data':dict_data})
        except Exception as e:
            return render(request,"month-based.html")
            print("there is an exception",e)







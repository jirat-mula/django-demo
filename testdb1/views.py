from distutils.command.build_scripts import first_line_re
from unittest import result
from django.db import connection
from django.dispatch import receiver
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Blue
from testdb.models import Student
import psycopg2

# Create your views here.


def viewdata(request):
    data = Student.objects.using('dbtest2').all()

    return render(request,"view.html",{"data":data})

class Add(CreateView):
    model = Blue
    fields = ('title','content')
    template_name = 'add.html'
    success_url = '/testdb1/'
    

def connect():
    conn = psycopg2.connect(dbname="testget", user="postgres", password="079108104")
    cur = conn.cursor()
    cur.callproc('accounts', (1))
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()
    # close the communication with the PostgreSQL database server
    cur.close()
    conn.close()


def store_proc(request):
    ps_connection = psycopg2.connect(user="postgres",
                                     password="079108104",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="dbtest")
    cursor = ps_connection.cursor()
    try:
        cursor.callproc('get_film')
        result = cursor.fetchall()
        return render(request,"view.html",{"data":result})
    finally:
        cursor.close()
        ps_connection.close()

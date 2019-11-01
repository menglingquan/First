
from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)
student=[
    ['zhang','001','物理'],
    ['li','002','化学']
]
def findnumber(Num):
    for i in range(len(student)):
        if student[i][1]==Num:
            return i
    return -1
def save(stu):
    studentfile = open('student.txt','w')
    for i in stu:
        for j in i:
            str = j
            studentfile.write(str)
            studentfile.write(' '*4)
        studentfile.write('\n')
    studentfile.close()


@app.route('/')
def index():
    save(student)
    return render_template('index.html',student=student)
@app.route('/delstu',methods=['GET','POST'])
def delstu():
    if request.method == 'POST':
        delnumber = request.form.get('delnumber')
        if findnumber(delnumber) == -1:
            return '学生不存在'
        else:
            del student[findnumber(delnumber)]
            save(student)
            return redirect(url_for('index'))
    return render_template('delstu.html',student=student)
@app.route('/addstu',methods=['GET','POST'])
def addstu():
    if request.method == 'POST':
        addnumber = request.form.get('addnumber')
        if findnumber(addnumber) !=-1:
            return '学号已存在a'
        else:
            addname = request.form.get('addname')
            adddepartment = request.form.get('adddepartment')
            if addname != None and adddepartment and addnumber !=None:
                student.append([addname,addnumber,adddepartment])
                save(student)
                return redirect(url_for('index'))
    return render_template('addstu.html')
@app.route('/altstu',methods=['GET','POST'])
def altstu():
    if request.method == 'POST':
        altnumber = request.form.get('altnumber')
        altdep = request.form.get('altdepartment')
        altname = request.form.get('altname')
        if findnumber(altnumber)==-1:
            return '学号bu已存在a'
        else:
            if altdep:
                student[findnumber(altdep)][2]=altdep
            if altname:
                student[findnumber(altname)][0]=altname
                save(student)
            return render_template('index.html',student=student)
    return render_template('altstu.html')
@app.route('/searchstu',methods=['GET','POST'])
def searchstu():
    if request.method=='POST':
        number = request.form.get('number')
        if findnumber(number) == -1:
            return '不存在啊'
        else:
            find=student[findnumber(number)]
            return render_template('searchstu.html',find=find)
    return render_template('searchstu.html',student=student)
if __name__ == '__main__':
    app.run(debug=True)
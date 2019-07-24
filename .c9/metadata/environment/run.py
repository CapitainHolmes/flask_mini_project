{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":43,"column":23},"action":"remove","lines":["import os","import json","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","    ","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","    ","    return render_template(\"member.html\", member=member)","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1},{"start":{"row":0,"column":0},"end":{"row":47,"column":23},"action":"insert","lines":["import os","import json","from flask import Flask, render_template, request","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","   ","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","   ","    return render_template(\"member.html\", member=member)","","","@app.route('/contact', methods=[\"GET\", \"POST\"])","def contact():","    if request.method == \"POST\":","        print(request.form)","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":0,"column":0},"end":{"row":47,"column":23},"action":"remove","lines":["import os","import json","from flask import Flask, render_template, request","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","   ","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","   ","    return render_template(\"member.html\", member=member)","","","@app.route('/contact', methods=[\"GET\", \"POST\"])","def contact():","    if request.method == \"POST\":","        print(request.form)","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":2},{"start":{"row":0,"column":0},"end":{"row":50,"column":23},"action":"insert","lines":["import os","import json","from flask import Flask, render_template, request, flash","","app = Flask(__name__)","app.secret_key = 'some_secret'","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    data = []","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","    return render_template(\"about.html\", page_title=\"About\", company=data)","","","@app.route('/about/<member_name>')","def about_member(member_name):","    member = {}","   ","    with open(\"data/company.json\", \"r\") as json_data:","        data = json.load(json_data)","        for obj in data:","            if obj[\"url\"] == member_name:","                member = obj","   ","    return render_template(\"member.html\", member=member)","","","@app.route('/contact', methods=[\"GET\", \"POST\"])","def contact():","    if request.method == \"POST\":","        flash(\"Thanks {}, we have received your message\".format(","            request.form[\"name\"]","        ))","    return render_template(\"contact.html\", page_title=\"Contact\")","","","@app.route('/careers')","def careers():","    return render_template(\"careers.html\", page_title=\"Careers\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}]]},"ace":{"folds":[],"scrolltop":482.234375,"scrollleft":0,"selection":{"start":{"row":50,"column":23},"end":{"row":50,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":21,"state":"start","mode":"ace/mode/python"}},"timestamp":1563970402514,"hash":"04eb8481214ff2eb12de44d3e8fe8d43296af289"}
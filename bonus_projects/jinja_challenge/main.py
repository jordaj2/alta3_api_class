#!/usr/bin/env python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)
app.secret_key = "dunamis_power"

groups = [{"hostname": "hostA", "ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]


@app.route('/', methods=['POST', 'GET'])
def print_hostfile_text_version():
    if "username" in session:
        web_render =  render_template("template.html", groups=groups)
    else:
        web_render = render_template("template_noadd.html", groups=groups)
    return web_render

@app.route('/form')
def display_form():
    return render_template("host_form.html")

@app.route('/add', methods=['POST', 'GET'])
def add_hosts():
    if request.method == 'POST':
        hostname = request.form.get('hn')
        ip = request.form.get('ip')
        fqdn = request.form.get('fqdn')
        #my have something in there for all 3 values in order for it to save.
        if (hostname and ip and fqdn):
            groups.append({'hostname': hostname, 'ip': ip, 'fqdn': fqdn})
    return redirect(url_for('print_hostfile_text_version'))

@app.route("/login", methods = ["GET", "POST"])
def login():
    ## if you sent us a POST because you clicked the login button
    if request.method == "POST":
        ## request.form["xyzkey"]: use indexing if you know the key exists
        ## request.form.get("xyzkey"): use get if the key might not exist
        session["username"] = request.form.get("username")
        return redirect(url_for("print_hostfile_text_version"))
    return """
   <form action ="" method = "post">
      <p><input type="text" name="username"></p>
      <p><input type="submit" value="Login"></p>
   </form>
  """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

from flask import Flask, render_template,request
import requests
app = Flask(__name__)
import smtplib

email_id = "sagulpragadeesh@gmail.com"
email_password = "prec ghqw xuim mgur"

second_email = "pragadeeeh@gmail.com"

blog_endpoint = "https://api.npoint.io/efb5c79167653e8ea71d"
response = requests.get(blog_endpoint).json()

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_msg(data["name"],data["email"],data["phone"],data["message"])
        return render_template("contact.html",user=True)
    return render_template("contact.html",user=False )
def send_msg(name,email,phone,message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(email_id, email_password)
        connection.sendmail(email_id,email_id, email_message)

@app.route("/")
def web():
    return render_template("index.html", blogdata=response)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request
from supabase import create_client
import hashlib

app = Flask(__name__)

name = ""
@app.route("/login/<username>/<password>", methods=["GET"])
def get_user(username, password):
    supabase = create_client("https://uynwrkkrrstgckbwteeu.supabase.co",
                             "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV5bndya2tycnN0Z2NrYnd0ZWV1Iiwicm9sZSI6ImFub"
                             "24iLCJpYXQiOjE3MjUxMzA0ODksImV4cCI6MjA0MDcwNjQ4OX0.yzwuN4B2b2QijXWxR72H4A4Q6PCWI-h6LYUVjXIkze0")
    response = (
        supabase.table("users")
        .select("subjects")
        .eq("username", username)
        .eq("password", hashlib.sha256(password.encode()).hexdigest())
        .execute())

    if response.data:
        global name
        name = username

        return jsonify(response.data), 200
    else:
        return jsonify([])


@app.route("/register/<username>/<password>", methods=["POST"])
def add_user(username, password):
    supabase = create_client("https://uynwrkkrrstgckbwteeu.supabase.co",
                             "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV5bndya2tycnN0Z2NrYnd0ZWV1Iiwicm9sZSI6ImFub"
                             "24iLCJpYXQiOjE3MjUxMzA0ODksImV4cCI6MjA0MDcwNjQ4OX0.yzwuN4B2b2QijXWxR72H4A4Q6PCWI-h6LYUVjXIkze0")

    user = (
        supabase.table("users")
        .select("subjects")
        .eq("username", username)
        .execute())

    print(user.data)
    if len(user.data) == 0:
        response = (
            supabase.table("users")
            .insert({"username": username, "password": str(hashlib.sha256(password.encode()).hexdigest()), "subjects": []})
            .execute())

        global name
        name = username

        return jsonify(response.data), 200
    else:
        return jsonify([])


@app.route("/save", methods=["PUT"])
def upload():
    supabase = create_client("https://uynwrkkrrstgckbwteeu.supabase.co",
                             "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV5bndya2tycnN0Z2NrYnd0ZWV1Iiwicm9sZSI6ImFub"
                             "24iLCJpYXQiOjE3MjUxMzA0ODksImV4cCI6MjA0MDcwNjQ4OX0.yzwuN4B2b2QijXWxR72H4A4Q6PCWI-h6LYUVjXIkze0")

    data = request.get_json()

    response = (
        supabase.table("users")
        .update({"subjects": data})
        .eq("username", name)
        .execute()
    )

    print(data)
    return jsonify(response.data), 200


if __name__ == "__main__":
    app.run(host="localhost")

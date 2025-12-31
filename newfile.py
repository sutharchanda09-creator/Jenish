from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Maine aapka naam yahan pehle se likh diya hai
    jenish_ka_naam = "Jenish" 
    
    return f"""
    <html>
    <head>
        <title>{jenish_ka_naam} ki Website</title>
        <style>
            body {{ 
                background: linear-gradient(135deg, #1e3c72, #2a5298); 
                color: white; 
                text-align: center; 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                padding-top: 80px;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                display: inline-block;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            }}
            h1 {{ font-size: 45px; margin-bottom: 10px; color: #00d4ff; }}
            h2 {{ font-weight: 300; }}
            .btn {{
                background: #00d4ff;
                color: #051937;
                border: none;
                padding: 15px 30px;
                font-size: 18px;
                border-radius: 50px;
                cursor: pointer;
                font-weight: bold;
                margin-top: 20px;
                transition: 0.3s;
            }}
            .btn:hover {{ background: #ffffff; transform: scale(1.1); }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Suno Doston! 📢</h1>
            <h2>Yeh Website <b style="color:white; text-shadow: 0 0 10px #00d4ff;">{jenish_ka_naam}</b> ne banayi hai!</h2>
            <p style="font-size: 18px; opacity: 0.8;">Jenish ab ek Pro Python Coder ban gaya hai. 🚀</p>
            <button class="btn" onclick="alert('Dhanyawad! Jenish ki mehnat rang layi!')">Mera Power Dekho</button>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Isse aapka local server mobile par chalu hoga
    app.run(host='0.0.0.0', port=5000)

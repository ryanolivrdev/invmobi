import json
from flask import jsonify, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User, Scenario, historic
from app.calc.calculation import comparando_tempo, valores_pago


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        
        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email já cadastrado")
            return redirect(url_for("signup"))

        if name and email and password:
            user = User(email=email, password=password, name=name)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("signin"))

        flash("Preencha todos os campos")

    if current_user.is_authenticated:
      return redirect("/simul")

    return render_template("signUp.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            flash("Verifique os dados e tente novamente")
            return redirect(url_for('signin'))

        login_user(user)
        return redirect("/simul")

    if current_user.is_authenticated:
        return redirect("/simul")
    return render_template("signIn.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/historic", methods=["GET"])
@login_required
def historicRoute():
    data = historic.query.filter_by(user_id=current_user.id).all()
    
    return render_template("historic.html", data=data)

@app.route("/simul", methods=["GET"])
@login_required
def simul():
    return render_template("simul.html")

@app.route("/calc", methods=["POST"])
@login_required
def calc():
    print(request)
    data = request.get_json()
    valor_aluguel_imovel = float(data["valor_aluguel_imovel"])
    valor_compra_imovel = float(data["valor_compra_imovel"])
    entrada_imovel = float(data["entrada_imovel"])
    tempo_imovel = int(data["tempo_imovel"])
    cenario = int(data["cenarios"])
  
    # FUNCAO VALORES PAGO
    valores_pago_mes = [valor_aluguel_imovel]
    
    query = Scenario.query.get(cenario)
    
    if not query:
      return json.dumps({"status":"error","message":"Cenario não encontrado"})
    
    
    taxa = query.property_valuation
    variacao = query.financing_rate

   
    somatorio_aluguel = valores_pago(valores_pago_mes,tempo_imovel,taxa)
    
    comparacao_tempo = comparando_tempo(valor_aluguel_imovel,valor_compra_imovel,entrada_imovel,variacao,taxa,tempo_imovel)

    opcao = "Alugar"

    if somatorio_aluguel >= comparacao_tempo[1]:
        opcao = "Comprar"
  
    historic_d = historic(user_id= current_user.id,
                          scenario_id=cenario,
                          valor_aluguel_imovel=valor_aluguel_imovel,
                          valor_compra_imovel=valor_compra_imovel,
                          entrada_imovel=entrada_imovel,
                          tempo_imovel=tempo_imovel,
                          soma_aluguel= comparacao_tempo[0],
                          total_pago_pela_compra= comparacao_tempo[1],
                          compensar_aluguel=comparacao_tempo[2],
                          opcao=opcao,
                          somatorio_aluguel= somatorio_aluguel,
                          )

    db.session.add(historic_d)
    db.session.commit()

    return json.dumps({"somatorio_aluguel": somatorio_aluguel, "comparacao_tempo":comparacao_tempo,"status":"ok","opcao": opcao})


app.run(debug=True)

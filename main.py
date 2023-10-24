from flask import Flask,flash, render_template, request, redirect, send_file
# from scripts import generate_plotly_graph
import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input

### Lembrar de Colocar no diagrama de casos de uso a Criacao de conta.

app = Flask(__name__)
app.secret_key = "super secret key"


df = pd.read_csv('forhealth_data.csv')
df["sintomas"] = [eval(sintomas) for sintomas in df["sintomas"]]
print(df.sintomas.iloc[0][0])

@app.route("/")
def index():
    return redirect('/login')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Capturar os dados do formulário submetidos pelo usuário
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        crm = request.form['crm']
        email = request.form['email']
        senha = request.form['password']
        
        # Aqui você pode processar os dados, armazená-los em um banco de dados, etc.
        # Neste exemplo, vamos apenas exibi-los de volta para o usuário.
        # flash('Usuário criado com sucesso!')
        return redirect('/')
    
    # Se a solicitação for GET, exibir o formulário
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Capturar os dados do formulário submetidos pelo usuário
        email = request.form['email']
        senha = request.form['password']
        if email == 'admin' and senha == 'admin':
            return redirect('insights')
        
        else:
            # flash('Login Realizado!')
            return redirect('consulta')
    return render_template('login.html')

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    if request.method == 'POST':
        # Capturar os dados do formulário submetidos pelo usuário
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        data_de_nascimento = request.form['data_de_nascimento']
        bairro = request.form['bairro']
        email = request.form['email']
        antecedentes_pessoais = request.form['antecedentes_pessoais']
        cirurgias_previas = request.form['cirurgias_previas']
        antecedentes_ginecologicos = request.form['antecedentes_ginecologicos']
        medicacoes_em_uso = request.form['medicacoes_em_uso']
        queixa_principal = request.form['queixa_principal']
        exame_fisico = request.form['exame_fisico']
        hda = request.form['hda']
        hipotese = request.form['hipotese']
        tipo_sanguineo = request.form['tipo_sanguineo']
        peso = request.form['peso']
        altura = request.form['altura']
        alergias = request.form['alergias']
        doencas_cronicas = request.form['doencas_cronicas']
        prescricao = request.form['prescricao']
        exame = request.form['exame']
        # data_de_validade_da_prescricao = request.form['data_de_validade_da_prescricao']
       
        # Aqui você pode processar os dados, armazená-los em um banco de dados, etc. 
        # flash('Consulta Realizada!')
        return redirect('consulta')
    return render_template('consulta.html')


# @app.route('/insights', methods=['GET'])
# def insights():

#     all_symptoms = [symptom for sublist in df['sintomas'] for symptom in sublist]
#     symptom_counts = pd.Series(all_symptoms).value_counts().reset_index()
#     symptom_counts.columns = ['Sintoma', 'Contagem']

#     # Gerar dados para gráfico 1
#     fig1 = px.scatter(symptom_counts, x='Sintoma', y='Contagem', title='Gráfico 1')
#     div1 = fig1.to_html(full_html=False)

#     # Gerar dados para gráfico 2
#     fig2 = px.scatter(df, x='x', y='y', title='Gráfico 2')
#     div2 = fig2.to_html(full_html=False)

#     # Gerar dados para gráfico 3 (por exemplo, um gráfico de barras)
#     fig3 = px.bar(df, x='x', y='y', title='Gráfico 3')
#     div3 = fig3.to_html(full_html=False)

#     return render_template('insights.html', plot_div1=div1, plot_div2=div2, plot_div3=div3)

#     # plot_divs = [generate_plotly_graph(df, data['title']) for data in graficos_data]
#     # return render_template('insights.html', plot_divs=plot_divs)


@app.route('/dynamic-insigths', methods=['GET'])
def dynamic_insigths():
    unique_months = df['mes'].unique()

    selected_month = request.args.get('month', unique_months[0])

    filtered_df = df[df['mes'] == selected_month]

    all_symptoms = [symptom for sublist in filtered_df['sintomas'] for symptom in sublist]
    symptom_counts = pd.Series(all_symptoms).value_counts().reset_index()
    symptom_counts.columns = ['Sintoma', 'Contagem']

    fig = px.bar(symptom_counts, x='Sintoma', y='Contagem', title=f'Contagem de Sintomas em {selected_month}')
    plot_div = fig.to_html(full_html=False)

    hipotese_counts = pd.Series(filtered_df['hipotese']).value_counts().reset_index()
    hipotese_counts.columns = ['Doença', 'Contagem']

    # fig = px.line(df, x="mes", y="lifeExp", title='Life expectancy in Canada')
    fig1 = px.bar(hipotese_counts, x='Doença', y='Contagem', title=f'Total de doenças em {selected_month}')
    div1 = fig1.to_html(full_html=False)

    return render_template('dynamic.html', 
    plot_div=plot_div, 
    plot_div2=div1, 
    # plot_div3=plot_div, 
    # plot_div4=plot_div, 
    unique_months=unique_months, 
    selected_month=selected_month)


if __name__ == '__main__':
    app.run(debug=True)
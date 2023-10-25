from flask import Flask,flash, render_template, request, redirect, send_file
# from scripts import generate_plotly_graph
import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input

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
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        crm = request.form['crm']
        email = request.form['email']
        senha = request.form['password']
        
        
        return redirect('/')
    
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']
        if email == 'admin' and senha == 'admin':
            return redirect('insights-anuais')
        
        else:
            return redirect('consulta')
    return render_template('login.html')

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    if request.method == 'POST':
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
        # exame = request.form['exame']
        
        columns_df = ['bairro','antecedentes pessoais','cirurgias previas','antecedentes ginecologicos','medicacoes em uso','queixa_principal','exame fisico','hda','hipotese','tipo sanguineo','alergias','doencas cronicas','prescricao','exame']

        form_df = pd.DataFrame(list(zip(
        bairro,
        antecedentes_pessoais,
        cirurgias_previas,
        antecedentes_ginecologicos,
        medicacoes_em_uso,
        queixa_principal,
        exame_fisico,
        hda,
        hipotese,
        tipo_sanguineo,
        alergias,
        doencas_cronicas,
        prescricao,
        # exame
        )),columns = columns_df)
        # print(form_df_teste.bairro)
        # form_df_teste.to_csv('forhealth_real_data.csv', index=False)

        return redirect('consulta')
    return render_template('consulta.html')


@app.route('/insights-anuais', methods=['GET'])
def insights_anuais():
    todos_os_sintomas = [sintoma for sublist in df['sintomas'] for sintoma in sublist]
    sintoma_counts = pd.Series(todos_os_sintomas).value_counts().reset_index()
    sintoma_counts.columns = ['Sintomas', 'Contagem']

    hipotese_counts = pd.Series(df['hipotese']).value_counts().reset_index()
    hipotese_counts.columns = ['Doenças', 'Contagem']

    tratamento_counts = pd.Series(df['tratamento']).value_counts().reset_index()
    tratamento_counts.columns = ['Tratamentos', 'Contagem']

    bairro_counts = pd.Series(df['bairro']).value_counts().reset_index()
    bairro_counts.columns = ['Bairros', 'Contagem']

    meses_counts = pd.Series(df['mes']).value_counts().reset_index()
    meses_counts.columns = ['Meses', 'Contagem']
    
    fig1 = px.bar(sintoma_counts, x='Sintomas', y='Contagem', title='Sintomas em alta')
    div1 = fig1.to_html(full_html=False)

    fig2 = px.bar(hipotese_counts, x='Doenças', y='Contagem', title='Doenças mais Frequentes')
    div2 = fig2.to_html(full_html=False)

    fig3 = px.bar(tratamento_counts, x='Tratamentos', y='Contagem', title='Tratamentos mais recorrentes')
    div3 = fig3.to_html(full_html=False)

    fig4 = px.histogram(df, x='queixa', color='mes', title='Queixas principais mais ocorrentes')
    div4 = fig4.to_html(full_html=False)

    fig5 = px.bar(meses_counts, x='Meses', y='Contagem', title='Quantidade de casos por mês')
    div5 = fig5.to_html(full_html=False)

    fig6 = px.bar(bairro_counts, x='Bairros', y='Contagem', title='Bairros com maiores números de casos')
    div6 = fig6.to_html(full_html=False)

    return render_template('insights-anuais.html', 
    plot_div1=div1, 
    plot_div2=div2, 
    plot_div3=div3, 
    plot_div4=div4, 
    plot_div5=div5,
    plot_div6=div6,
    )


@app.route('/insights-mensais', methods=['GET'])
def insigths_mensais():
    unique_months = df['mes'].unique()

    selected_month = request.args.get('month', unique_months[0])
    df['index'] = df.index
    filtered_df = df[df['mes'] == selected_month]

    hipotese_counts = pd.Series(filtered_df['hipotese']).value_counts().reset_index()
    hipotese_counts.columns = ['Doenças', 'Contagem']

    tratamento_counts = pd.Series(filtered_df['tratamento']).value_counts().reset_index()
    tratamento_counts.columns = ['Tratamentos', 'Contagem']

    all_symptoms = [symptom for sublist in filtered_df['sintomas'] for symptom in sublist]
    symptom_counts = pd.Series(all_symptoms).value_counts().reset_index()
    symptom_counts.columns = ['Sintomas', 'Contagem']

    bairro_counts = pd.Series(filtered_df['bairro']).value_counts().reset_index()
    bairro_counts.columns = ['Bairros', 'Contagem']

    hipotese_queixa_counts = filtered_df.groupby(['hipotese','queixa'])['index'].count().sort_values(ascending=False).reset_index()
    hipotese_queixa_counts.columns = ['Doença', 'Queixa','Contagem']
    print(hipotese_queixa_counts.index)


    # fig = px.line(df, x="mes", y="lifeExp", title='Life expectancy in Canada')
    fig1 = px.bar(hipotese_counts, x='Doenças', y='Contagem', title=f'Total de doenças em {selected_month}')
    div1 = fig1.to_html(full_html=False)

    fig2 = px.bar(symptom_counts, x='Sintomas', y='Contagem', title=f'Contagem de Sintomas em {selected_month}')
    div2 = fig2.to_html(full_html=False)

    fig3 = px.bar(hipotese_counts, x='Doenças', y='Contagem', title=f'Total de doenças em {selected_month}')
    div3 = fig3.to_html(full_html=False)

    fig4 = px.bar(tratamento_counts, x='Tratamentos', y='Contagem',title=f'Tratamentos realizados em {selected_month}')
    div4 = fig4.to_html(full_html=False)

    fig5 = px.bar(bairro_counts, x='Bairros', y='Contagem', title=f'Bairros com maior ocorrência de casos em {selected_month}')
    div5 = fig5.to_html(full_html=False)

    fig6 = px.bar(hipotese_counts, x='Doenças', y='Contagem', title=f'Total de doenças em {selected_month}')
    div6 = fig6.to_html(full_html=False)

    return render_template('insights-mensais.html', 
    plot_div1=div1, 
    plot_div2=div2, 
    plot_div3=div3, 
    plot_div4=div4, 
    plot_div5=div5,
    plot_div6=div6,
    unique_months=unique_months, 
    selected_month=selected_month)


if __name__ == '__main__':
    app.run(debug=True)
from faker import Faker
from faker.providers import DynamicProvider
import math
import numpy as np

## Criando os metodos para gerar as doenças e sintomas
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho','Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# nomes_medicos_provider = DynamicProvider(
#      provider_name="medical_profession",
#      elements=["dr."],
# )

dengue_sintomas_provider = DynamicProvider(
    provider_name='dengue_sintomas',
    elements=['Febra alta', 'Vômitos', 'Náuseas', 'Cefaleia', 'Dor retro-orbital',
              'Dor muscular', 'Dor nas articulações e ossos', 'Perda do apetite',
              'Fraqueza e cansaço', 'Rash de pele'
              ]
)

dengue_tratamento_provider = DynamicProvider(
    provider_name='dengue_tratamento',
    elements=['Repouso e remédios para tratar sintomas (Dipirona e Paracetamol)']
)

esporotricose_sintomas_provider = DynamicProvider(
    provider_name='esporotricose_sintomas',
    elements=['Contato com animais infectados', 'Lesões cutâneas em forma de caroços/nódulos', 'Pode evoluir para uma úlcera piogênica/purulenta (com pus)', 'Prurido / coceira', 'Linfonodomegalia / Aumento dos Linfonodos', 'Febre']
)

esporotricose_tratamento_provider = DynamicProvider(
    provider_name='esporotricose_tratamento',
    elements=['Itraconazol']
)

diabetes_dm2_sintomas_provider = DynamicProvider(
    provider_name='diabetes_dm2_sintomas',
    elements=['Poliúria / Liberação de urina em excesso', 'Polidipsia / Sede em excesso', 'Poliacúria / Micção frequente', 'Distúrbios na cicatrização de feridas', 'Fadiga', 'Polifagia / Fome em excesso', 'Visão turva']
)

diabetes_dm2_tratamento_provider = DynamicProvider(
    provider_name='diabetes_dm2_tratamento',
    elements=['Glifage XR (Metformina)']
)

ascaridiase_sintomas_provider = DynamicProvider(
    provider_name='ascaridiase_sintomas',
    elements=['Dispneia / Dificuldade em respirar', 'Distensão abdominal', 'Dor abdominal', 'Constipação', 'Tosse seca', 'Vômitos', 'Náuseas', 'Regurgitação dos vermes']
)

ascaridiase_tratamento_provider = DynamicProvider(
    provider_name='ascaridiase_tratamento',
    elements=['Albendazol']
)

esquistossomose_sintomas_provider = DynamicProvider(
    provider_name='esquistossomose_sintomas',
    elements=['Hepatomegalia', 'Esplenomegalia', 'Diarreia', 'Varizes esofágicas', 'Ascite', 'Anemia']
)

esquistossomose_tratamento_provider = DynamicProvider(
    provider_name='esquistossomose_tratamento',
    elements=['Praziquantel']
)

oxiuriase_sintomas_provider = DynamicProvider(
    provider_name='oxiuriase_sintomas',
    elements=['Prurido anal', 'Presença de vermes nas fezes', 'Presença de vermes na região perianal']
)

oxiuriase_tratamento_provider = DynamicProvider(
    provider_name='oxiuriase_tratamento',
    elements=['Albendazol']
)

teniase_sintomas_provider = DynamicProvider(
    provider_name='teniase_sintomas',
    elements=['Dor abdominal', 'Diarreias', 'Fraqueza muscular', 'Polifagia', 'Perda de peso', 'Náuseas', 'Vômitos', 'Distensão abdominal', 'Tontura', 'Presença de proglotes nas fezes']
)

teniase_tratamento_provider = DynamicProvider(
    provider_name='teniase_tratamento',
    elements=['Albendazol']
)

catapora_sintomas_provider = DynamicProvider(
    provider_name = 'catapora_sintomas',
    elements=['Manchas vermelhas / Lesões cutâneas', 'Fadiga', 'Coceira / Prurido', 'Cefaleia']
)

catapora_tratamento_provider = DynamicProvider(
    provider_name='catapora_tratamento',
    elements=['Paracetamol', 'Dipirona', 'Loratadina']
)

obesidade_sintomas_provider = DynamicProvider(
    provider_name='obesidade_sintomas',
    elements=['Gordura em excesso']
)

obesidade_tratamento_provider = DynamicProvider(
    provider_name='obesidade_tratamento',
    elements=['Basicamente dieta e exercício', 'Semeglutida (Ozempic) off label', 'Topiramato', 'Sibutramina']
)

hanseniase_sintomas_provider = DynamicProvider(
    provider_name='hanseniase_sintomas',
    elements=['Perda de sensibilidade na pele', 'Dormência', 'Formigamento', 'Fraqueza Muscular', 'Manchas esbranquiçadas']
)

hanseniase_tratamento_provider = DynamicProvider(
    provider_name='hanseniase_tratamento',
    elements=['Associação de 3 medicamentos: Rifampicina, Dapsona e Clofazimina']
)

itu_sintomas_provider = DynamicProvider(
    provider_name='itu_sintomas',
    elements=['Dor lombar', 'Dor no pé da barriga', 'Disúria / Dor ao urinar', 'Poliúria / Liberação de urina em excesso', 'Poliacúria / Micção com maior frequência', 'Febre']
)

itu_tratamento_provider = DynamicProvider(
    provider_name='itu_tratamento',
    elements=['Cefalexina', 'Nitrofurantoína']
)

has_sintomas_provider = DynamicProvider(
    provider_name='has_sintomas',
    elements=['Cefaleia', 'Tontura', 'Náuseas', 'Síncope / desmaio', 'Pressão arterial média maior que 140/90 mmHg']
)

has_tratamento_provider = DynamicProvider(
    provider_name='has_tratamento',
    elements=['Losartana', 'Captopril', 'Enalapril']
)

rinossinusite_viral_sintomas_provider = DynamicProvider(
    provider_name='rinossinusite_viral_sintomas',
    elements=['Coriza', 'Tosse cheia', 'Febre', 'Cefaleia', 'Faringite']
)

rinossinusite_viral_tratamento_provider = DynamicProvider(
    provider_name='rinossinusite_viral_tratamento',
    elements=['Dipirona', 'Lavagem nasal']
)

rinossinusite_bacteriana_sintomas_provider = DynamicProvider(
    provider_name='rinossinusite_bacteriana_sintomas',
    elements=['Coriza', 'Tosse cheia', 'Febre', 'Cefaleia', 'Faringite']
)

rinossinusite_bacteriana_tratamento_provider = DynamicProvider(
    provider_name='rinossinusite_bacteriana_tratamento',
    elements=['Dipirona', 'Lavagem nasal', 'Amoxicilina', 'Clavulin']
)

asma_leve_sintomas_provider = DynamicProvider(
    provider_name='asma_leve_sintomas',
    elements=['Dispnéia / falta de ar', 'Tosse seca', 'Sibilo difusos na ausculta pulmonar']
)

asma_leve_tratamento_provider = DynamicProvider(
    provider_name='asma_leve_tratamento',
    elements=['Salmeterol', 'Formoterol']
)

vaginose_bacteriana_sintomas_provider = DynamicProvider(
    provider_name='vaginose_bacteriana_sintomas',
    elements=['Corrimento branco-acinzentado', 'Piora do odor durante o período menstrual e na relação sexual']
)

vaginose_bacteriana_tratamento_provider = DynamicProvider(
    provider_name='vaginose_bacteriana_tratamento',
    elements=['Metronidazol']
)

candidiase_sintomas_provider = DynamicProvider(
    provider_name='candidiase_sintomas',
    elements=['Corrimento branco aderido e grumoso', 'Prurido genital', 'Ardor vulvar intenso', 'Dispareunia / dor nas relações sexuais']
)

candidiase_tratamento_provider = DynamicProvider(
    provider_name='candidiase_tratamento',
    elements=['Miconazol creme vaginal']
)

tricomoníase_sintomas_provider = DynamicProvider(
    provider_name='tricomoníase_sintomas',
    elements=['Corrimento amarelo esverdeado e bolhoso', 'Odor desagradável', 'Prurido genital', 'Disúria / Dor ao urinar']
)

tricomoníase_tratamento_provider = DynamicProvider(
    provider_name='tricomoníase_tratamento',
    elements=['Metronidazol']
)

clamidia_sintomas_provider = DynamicProvider(
    provider_name='clamidia_sintomas',
    elements=['Dor forte na região genital', 'Ardência ao urinar', 'Poliaciúria / Micção com maior frequência', 'Disúria / Dor ao urinar', 'Secreção de pus através da uretra', 'Dispareunia / dor nas relações sexuais']
)

clamidia_tratamento_provider = DynamicProvider(
    provider_name='clamidia_tratamento',
    elements=['Azitromicina']
)

gonorreia_sintomas_provider = DynamicProvider(
    provider_name='gonorreia_sintomas',
    elements=['Corrimento amarelado', 'Dor na região inferior do abdome', 'Dor e ardência ao urinar', 'Dor pélvica', 'Dor e sangramento durante a relação sexual']
)

gonorreia_tratamento_provider = DynamicProvider(
    provider_name='gonorreia_tratamento',
    elements=['Ceftriaxona']
)

sifilis_sintomas_provider = DynamicProvider(
    provider_name='sifilis_sintomas',
    elements=['cancro duro (úlcera única, indolor, que some)',
              'lesão cutânea plana e ulcerada', 'lesões palmares e plantares', 'febre', 'mal-estar', 'cefaleia',
              'lesões cutâneas', 'lesões ósseas', 'lesões cardiovasculares', 'lesões neurológicas']
)

sifilis_tratamento_provider = DynamicProvider(
    provider_name='sifilis_tratamento',
    elements=['Penicilina G Benzatina']
)

herpes_genital_sintomas_provider = DynamicProvider(
    provider_name='herpes_genital_sintomas',
    elements=['Vesículas (pequenas bolhas) em região genital', 'úlceras dolorosas e limpas na região genital', 'crostas na região genital', 'Adenopatia dolorosa que não fistuliza']
)

herpes_genital_tratamento_provider = DynamicProvider(
    provider_name='herpes_genital_tratamento',
    elements=['Aciclovir']
)

conjuntivite_viral_sintomas_provider = DynamicProvider(
    provider_name='conjuntivite_viral_sintomas',
    elements=['Fotofobia - se acometer a córnea', 'Lacrimejamento', 'Secreção clara ou esbranquiçada, fluida, aquosa e serosa em pequena quantidade em um ou ambos os olhos']
)

conjuntivite_viral_tratamento_provider = DynamicProvider(
    provider_name='conjuntivite_viral_tratamento',
    elements=['Hyabak', 'Compressas frias']
)

conjuntivite_bacteriana_sintomas_provider = DynamicProvider(
    provider_name='conjuntivite_bacteriana_sintomas',
    elements=['Conjuntivite unilateral com secreção purulenta', 'Conjuntivite bilateral', 'Início agudo com hiperemia', 'Sensação de corpo estranho', 'Ardor', 'Pálpebras inchadas e coladas ao acordar']
)

conjuntivite_bacteriana_tratamento_provider = DynamicProvider(
    provider_name='conjuntivite_bacteriana_tratamento',
    elements=['Tobramicina']
)

glaucoma_angulo_fechado_sintomas_provider = DynamicProvider(
    provider_name='glaucoma_angulo_fechado_sintomas',
    elements=['Quadro de embaçamento da visão', 'Fotofobia', 'Dor ocular', 'Cefaleia intensa', 'Visão de halos coloridos', 'Náuseas', 'Vômitos']
)

glaucoma_angulo_fechado_tratamento_provider = DynamicProvider(
    provider_name='glaucoma_angulo_fechado_tratamento',
    elements=['Acetazolamida', 'Pilocarpina 2%', 'Manitol 20%']
)

glaucoma_angulo_aberto_cronico_sintomas_provider = DynamicProvider(
    provider_name='glaucoma_angulo_aberto_cronico_sintomas',
    elements=['Perda do campo visual periférico', 'cegueira total']
)

glaucoma_angulo_aberto_cronico_tratamento_provider = DynamicProvider(
    provider_name='glaucoma_angulo_aberto_cronico_tratamento',
    elements=['Timolol']
)

amigdalite_bacteriana_sintomas_provider = DynamicProvider(
    provider_name='amigdalite_bacteriana_sintomas',
    elements=['Dor ao deglutir', 'Inchaço/aumento de tamanho das amígdalas', 'Amígdalas avermelhadas']
)

amigdalite_bacteriana_tratamento_provider = DynamicProvider(
    provider_name='amigdalite_bacteriana_tratamento',
    elements=['Amoxicilina']
)

amigdalite_viral_sintomas_provider = DynamicProvider(
    provider_name='amigdalite_viral_sintomas',
    elements=['Dor ao deglutir', 'Inchaço/aumento de tamanho das amígdalas', 'Amígdalas avermelhadas']
)

amigdalite_viral_tratamento_provider = DynamicProvider(
    provider_name='amigdalite_viral_tratamento',
    elements=['Dipirona', 'Ibuprofeno']
)

caxumba_sintomas_provider = DynamicProvider(
    provider_name='caxumba_sintomas',
    elements=['Inchaço nas glândulas salivares', 'Febre', 'Cefaleia', 'Calafrio']
)

caxumba_tratamento_provider = DynamicProvider(
    provider_name='caxumba_tratamento',
    elements=['dipirona', 'paracetamol']
)

escabiose_sintomas_provider = DynamicProvider(
    provider_name='escabiose_sintomas',
    elements=['Prurido intenso', 'Lesões cutâneas avermelhadas com crostas']
)

escabiose_tratamento_provider = DynamicProvider(
    provider_name='escabiose_tratamento',
    elements=['Permetrina']
)

pneumonia_bacteriana_sintomas_provider = DynamicProvider(
    provider_name='pneumonia_bacteriana_sintomas',
    elements=['Dispneia (dificuldade a respirar)', 'Falta de ar', 'Dor no peito', 'Tosse seca ou produtiva', 'Febre', 'Fadiga']
)

pneumonia_bacteriana_tratamento_provider = DynamicProvider(
    provider_name='pneumonia_bacteriana_tratamento',
    elements=['amoxicilina','salbutamol (broncodilatador)']
)

pneumonia_viral_sintomas_provider = DynamicProvider(
    provider_name='pneumonia_viral_sintomas',
    elements=['Dispneia (dificuldade a respirar)', 'Falta de ar', 'Dor no peito', 'Tosse seca ou produtiva', 'Febre', 'Fadiga']
)

pneumonia_viral_tratamento_provider = DynamicProvider(
    provider_name='pneumonia_viral_tratamento',
    elements=['dipirona', 'paracetamol', 'salbutamol (broncodilatador)']
)

tuberculose_sintomas_provider = DynamicProvider(
    provider_name='tuberculose_sintomas',
    elements=['Dispneia (dificuldade em respirar)', 'Falta de ar', 'Tosse seca ou produtiva', 'Febre', 'Fadiga', 'Dor torácica']
)

tuberculose_tratamento_provider = DynamicProvider(
    provider_name='tuberculose_tratamento',
    elements=['Associação de 4 medicamentos: rifampicina, isoniazida, etambutol e pirazinamida']
)

pitiriase_sintomas_provider = DynamicProvider(
    provider_name='ptiriase_sintomas',
    elements=['Lesões na pele hipopigmentadas (esbranquiçadas)','Lesões na pele hiperpigmentadas (avermelhadas amarronzadas)', 'Prurido']
)

pitiriase_tratamento_provider = DynamicProvider(
    provider_name='ptiriase_tratamento',
    elements=['Antifúngico como cetoconazol']
)

refluxo_gastroesofagico_sintomas_provider = DynamicProvider(
    provider_name='refluxo_gastroesofagico_sintomas',
    elements=['Tosse crônica e seca que aumenta após alimentação', 'Azia (queimação no peito)', 'Pigarro', 'Regurgitação', 'Arrotos frequentes (principalmente após alimentação)']
)

refluxo_gastroesofagico_tratamento_provider = DynamicProvider(
    provider_name='refluxo_gastroesofagico_tratamento',
    elements=['Omeprazol']
)


fake = Faker()
fake.add_provider(nomes_medicos_provider)

fake.add_provider(dengue_sintomas_provider)
fake.add_provider(dengue_tratamento_provider)

fake.add_provider(esporotricose_sintomas_provider)
fake.add_provider(esporotricose_tratamento_provider)

fake.add_provider(diabetes_dm2_sintomas_provider)
fake.add_provider(diabetes_dm2_tratamento_provider)

fake.add_provider(ascaridiase_sintomas_provider)
fake.add_provider(ascaridiase_tratamento_provider)

fake.add_provider(esquistossomose_sintomas_provider)
fake.add_provider(esquistossomose_tratamento_provider)

fake.add_provider(oxiuriase_sintomas_provider)
fake.add_provider(oxiuriase_tratamento_provider)

fake.add_provider(teniase_sintomas_provider)
fake.add_provider(teniase_tratamento_provider)

fake.add_provider(catapora_sintomas_provider)
fake.add_provider(catapora_tratamento_provider)

fake.add_provider(hanseniase_sintomas_provider)
fake.add_provider(hanseniase_tratamento_provider)

fake.add_provider(obesidade_sintomas_provider)
fake.add_provider(obesidade_tratamento_provider)

fake.add_provider(itu_sintomas_provider)
fake.add_provider(itu_tratamento_provider)

fake.add_provider(has_sintomas_provider)
fake.add_provider(has_tratamento_provider)

fake.add_provider(rinossinusite_viral_sintomas_provider)
fake.add_provider(rinossinusite_viral_tratamento_provider)

fake.add_provider(rinossinusite_bacteriana_sintomas_provider)
fake.add_provider(rinossinusite_bacteriana_tratamento_provider)

fake.add_provider(asma_leve_sintomas_provider)
fake.add_provider(asma_leve_tratamento_provider)

fake.add_provider(vaginose_bacteriana_sintomas_provider)
fake.add_provider(vaginose_bacteriana_tratamento_provider)

fake.add_provider(candidiase_sintomas_provider)
fake.add_provider(candidiase_tratamento_provider)

fake.add_provider(tricomoníase_sintomas_provider)
fake.add_provider(tricomoníase_tratamento_provider)

fake.add_provider(clamidia_sintomas_provider)
fake.add_provider(clamidia_tratamento_provider)

fake.add_provider(gonorreia_sintomas_provider)
fake.add_provider(gonorreia_tratamento_provider)

fake.add_provider(sifilis_sintomas_provider)
fake.add_provider(sifilis_tratamento_provider)

fake.add_provider(herpes_genital_sintomas_provider)
fake.add_provider(herpes_genital_tratamento_provider)

fake.add_provider(conjuntivite_viral_sintomas_provider)
fake.add_provider(conjuntivite_viral_tratamento_provider)

fake.add_provider(conjuntivite_bacteriana_sintomas_provider)
fake.add_provider(conjuntivite_bacteriana_tratamento_provider)

fake.add_provider(glaucoma_angulo_fechado_sintomas_provider)
fake.add_provider(glaucoma_angulo_fechado_tratamento_provider)

fake.add_provider(glaucoma_angulo_aberto_cronico_sintomas_provider)
fake.add_provider(glaucoma_angulo_aberto_cronico_tratamento_provider)

fake.add_provider(amigdalite_bacteriana_sintomas_provider)
fake.add_provider(amigdalite_bacteriana_tratamento_provider)

fake.add_provider(amigdalite_viral_sintomas_provider)
fake.add_provider(amigdalite_viral_tratamento_provider)

fake.add_provider(caxumba_sintomas_provider)
fake.add_provider(caxumba_tratamento_provider)

fake.add_provider(escabiose_sintomas_provider)
fake.add_provider(escabiose_tratamento_provider)

fake.add_provider(pneumonia_bacteriana_sintomas_provider)
fake.add_provider(pneumonia_bacteriana_tratamento_provider)

fake.add_provider(pneumonia_viral_sintomas_provider)
fake.add_provider(pneumonia_viral_tratamento_provider)

fake.add_provider(tuberculose_sintomas_provider)
fake.add_provider(tuberculose_tratamento_provider)

fake.add_provider(pitiriase_sintomas_provider)
fake.add_provider(pitiriase_tratamento_provider)

fake.add_provider(refluxo_gastroesofagico_sintomas_provider)
fake.add_provider(refluxo_gastroesofagico_tratamento_provider)

# Doenças muito raras: Menos de 15.000 casos pro ano no Brasil - 59 casos por ano (0,0039 * 15.000), 5 casos por mês.
# Utilizando como base que são 59 casos por ano, utilizarei adicionarei 15% a mais de casos para o limite superior que será 68(59 + 9)
# e como limite inferior 50(59 - 9) casos por ano. Intervalo [50, 68]
# Doenças: Hanseníase, Esporiotricose

# Doenças raras: Menos de 150.000 (assumi 100.000) casos por ano no Brasil = 390 casos por ano (0,0039 * 100.000), 33 casos por mês.
# Utilizando como base que são 390 casos por ano, utilizarei adicionarei 15% a mais de casos para o limite superior que será 449(390 + 59)
# e como limite inferior 331(390 - 59) casos por ano. Intervalo [331, 449]
# Doenças: Caxumba, Tuberculose, Sífilis, Oxiuriase

# Doenças comuns: Mais de 150.000 (assumi 175.000) casos por ano no Brasil = 683 casos por ano (0,0039 * 175.000), 49 casos por mês.
# Utilizando como base que são 683 casos por ano, utilizarei adicionarei 15% a mais de casos para o limite superior que será 785(683 + 102)
# e como limite inferior 581(683 - 102) casos por ano. Intervalo [581, 785]
# Doenças: Catapora, Dengue, Escabiose, Esquistossomose, Teniase, Glaucoma (Angulo aberto e fechado), Clamídia, Ascaridiase

# Doenças muito comuns: Mais de 2 milhões cassos por ano no Brasil - 7800 casos por ano (0,0039 * 2.000.000), 650 casos por mês.
# Utilizando como base que são 7800 casos por ano, utilizarei adicionarei 15% a mais de casos para o limite superior que será 8970(7800 + 1170)
# e como limite inferior 6630(7800 - 1170) casos por ano. Intervalo [6630, 8970]
# Doenças: Hipertensão arterial sistêmica, Asma leve, Vaginose Bacteriana, Amigdalite, Pneumonia(juntas viral e bacteriana), Doença do Refluxo Gastroesofágico,
# Obesidade, Diabetes tipo 2, Infecção do trato urinário (ITU), Tricomoníase, Gonorreia, Herpes Genital, Conjuntivite (viral e bacteriana), candidiase, rinossinusite

patiente_names = [fake.unique.name() for i in range(10000)]
bairros = [
    "Água Fria","Aeroclube","Altiplano","Alto do Céu","Alto do Mateus","Anatólia",
    "Bairro das Indústrias","Bairro dos Estados","Bairro dos Ipês","Bairro dos Novais",
    "Bancários","Barra de Gramame","Bessa","Jardim Brisamar","Cabo Branco",
    "Castelo Branco","Centro","Cidade dos Colibris","Costa do Sol","Costa e Silva",
    "Cristo Redentor","Cruz das Armas","Cuiá","Distrito Industrial","Ernesto Geisel",
    "Ernâni Sátiro","Expedicionários","Funcionários II","Gramame","Grotão",
    "Ilha do Bispo","Jaguaribe","Jardim 13 de Maio","Jardim Cidade Universitária",
    "Jardim Esther","Jardim Luna","Jardim Mangueira","Jardim Oceania",
    "Jardim Planalto","Jardim São Paulo","Jardim Veneza","José Américo",
    "João Agripino","João Paulo II","Manaíra","Mandacaru","Mangabeira",
    "Mata do Buraquinho","Miramar","Mumbaba","Mussuré","Muçumagro",
    "Oitizeiro","Padre Zé","Paratibe","Pedro Gondim","Penha","Planalto da Boa Esperança",
    "Ponta dos Seixas","Portal do Sol","Quadramares","Rangel","Róger",
    "São José","Tambaú","Tambauzinho","Tambiá","Torre","Trincheiras",
    "Valentina Figueiredo","Varadouro","Varjão"
]







# Gerando as doenças muito raras
hanseniase_sintomas = [list({fake.hanseniase_sintomas() for i in range(math.ceil(len(fake.hanseniase_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(50,68))]
hanseniase_tratamento  = [fake.hanseniase_tratamento() for i in range(len(hanseniase_sintomas))]
hanseniase_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(hanseniase_sintomas))]
hanseniase_queixa_principal = [hanseniase_sintomas[i][np.random.randint(len(hanseniase_sintomas[i]))] for i in range(len(hanseniase_sintomas))]
hanseniase_hipotese = ['Hanseníase' for i in range(len(hanseniase_sintomas))]
hanseniase_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(hanseniase_sintomas))
hanseniase_casos_mensais = transformar_em_meses(hanseniase_lista_de_ocorrencias_mensais)

esporotricose_sintomas = [list({fake.esporotricose_sintomas() for i in range(math.ceil(len(fake.esporotricose_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(50,68))]
esporotricose_tratamento  = [fake.esporotricose_tratamento() for i in range(len(esporotricose_sintomas))]
esporotricose_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(esporotricose_sintomas))]
esporotricose_queixa_principal = [esporotricose_sintomas[i][np.random.randint(len(esporotricose_sintomas[i]))] for i in range(len(esporotricose_sintomas))]
esporotricose_hipotese = ['Esporotricose' for i in range(len(esporotricose_sintomas))]
esporotricose_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(esporotricose_sintomas))
esporotricose_casos_mensais = transformar_em_meses(esporotricose_lista_de_ocorrencias_mensais)

# Gerando as doenças raras
caxumba_sintomas = [list({fake.caxumba_sintomas() for i in range(math.ceil(len(fake.caxumba_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(331,449))]
caxumba_tratamento = [fake.caxumba_tratamento() for i in range(len(caxumba_sintomas))]
caxumba_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(caxumba_sintomas))]
caxumba_queixa_principal = [caxumba_sintomas[i][np.random.randint(len(caxumba_sintomas[i]))] for i in range(len(caxumba_sintomas))]
caxumba_hipotese = ['Caxumba' for i in range(len(caxumba_sintomas))]
caxumba_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(caxumba_sintomas))
caxumba_casos_mensais = transformar_em_meses(caxumba_lista_de_ocorrencias_mensais)

tuberculose_sintomas = [list({fake.tuberculose_sintomas() for i in range(math.ceil(len(fake.tuberculose_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(331, 449))]
tuberculose_tratamento = [fake.tuberculose_tratamento() for i in range(len(tuberculose_sintomas))]
tuberculose_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(tuberculose_sintomas))]
tuberculose_queixa_principal = [tuberculose_sintomas[i][np.random.randint(len(tuberculose_sintomas[i]))] for i in range(len(tuberculose_sintomas))]
tuberculose_hipotese = ['Tuberculose' for i in range(len(tuberculose_sintomas))]
tuberculose_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(tuberculose_sintomas))
tuberculose_casos_mensais = transformar_em_meses(tuberculose_lista_de_ocorrencias_mensais)

sifilis_sintomas = [list({fake.sifilis_sintomas() for i in range(math.ceil(len(fake.sifilis_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(331, 449))]
sifilis_tratamento = [fake.sifilis_tratamento() for i in range(len(sifilis_sintomas))]
sifilis_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(sifilis_sintomas))]
sifilis_queixa_principal = [sifilis_sintomas[i][np.random.randint(len(sifilis_sintomas[i]))] for i in range(len(sifilis_sintomas))]
sifilis_hipotese = ['Sífilis ' for i in range(len(sifilis_sintomas))]
sifilis_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(sifilis_sintomas))
sifilis_casos_mensais = transformar_em_meses(sifilis_lista_de_ocorrencias_mensais)


oxiuriase_sintomas = [list({fake.oxiuriase_sintomas() for i in range(math.ceil(len(fake.oxiuriase_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(331, 449))]
oxiuriase_tratamento = [fake.oxiuriase_tratamento() for i in range(len(oxiuriase_sintomas))]
oxiuriase_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(oxiuriase_sintomas))]
oxiuriase_queixa_principal = [oxiuriase_sintomas[i][np.random.randint(len(oxiuriase_sintomas[i]))] for i in range(len(oxiuriase_sintomas))]
oxiuriase_hipotese = ['Oxiuríase' for i in range(len(oxiuriase_sintomas))]
oxiuriase_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(oxiuriase_sintomas))
oxiuriase_casos_mensais = transformar_em_meses(oxiuriase_lista_de_ocorrencias_mensais)


# Gerando as doenças comuns
dengue_sintomas = [list({fake.dengue_sintomas() for i in range(math.ceil(len(fake.dengue_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(581,785))]
dengue_tratamento  = [fake.dengue_tratamento() for i in range(len(dengue_sintomas))]
dengue_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(dengue_sintomas))]
dengue_queixa_principal = [dengue_sintomas[i][np.random.randint(len(dengue_sintomas[i]))] for i in range(len(dengue_sintomas))]
dengue_hipotese = ['Dengue' for i in range(len(dengue_sintomas))]
dengue_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(dengue_sintomas))
dengue_casos_mensais = transformar_em_meses(dengue_lista_de_ocorrencias_mensais)


catapora_sintomas = [list({fake.catapora_sintomas() for i in range(math.ceil(len(fake.catapora_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(581, 785))]
catapora_tratamento = [fake.catapora_tratamento() for i in range(len(catapora_sintomas))]
catapora_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(catapora_sintomas))]
catapora_queixa_principal = [catapora_sintomas[i][np.random.randint(len(catapora_sintomas[i]))] for i in range(len(catapora_sintomas))]
catapora_hipotese = ['Catapora' for i in range(len(catapora_sintomas))]
catapora_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(catapora_sintomas))
catapora_casos_mensais = transformar_em_meses(catapora_lista_de_ocorrencias_mensais)


escabiose_sintomas = [list({fake.escabiose_sintomas() for i in range(math.ceil(len(fake.escabiose_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(581, 785))]
escabiose_tratamento = [fake.escabiose_tratamento() for i in range(len(escabiose_sintomas))]
escabiose_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(escabiose_sintomas))]
escabiose_queixa_principal = [escabiose_sintomas[i][np.random.randint(len(escabiose_sintomas[i]))] for i in range(len(escabiose_sintomas))]
escabiose_hipotese = ['Escabiose' for i in range(len(escabiose_sintomas))]
escabiose_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(escabiose_sintomas))
escabiose_casos_mensais = transformar_em_meses(escabiose_lista_de_ocorrencias_mensais)


esquistossomose_sintomas = [list({fake.esquistossomose_sintomas() for i in range(math.ceil(len(fake.esquistossomose_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(581, 785))]
esquistossomose_tratamento = [fake.esquistossomose_tratamento() for i in range(len(esquistossomose_sintomas))]
esquistossomose_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(esquistossomose_sintomas))]
esquistossomose_queixa_principal = [esquistossomose_sintomas[i][np.random.randint(len(esquistossomose_sintomas[i]))] for i in range(len(esquistossomose_sintomas))]
esquistossomose_hipotese = ['Esquistossomose' for i in range(len(esquistossomose_sintomas))]
esquistossomose_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(esquistossomose_sintomas))
esquistossomose_casos_mensais = transformar_em_meses(esquistossomose_lista_de_ocorrencias_mensais)


teniase_sintomas = [list({fake.teniase_sintomas() for i in range(math.ceil(len(fake.teniase_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(581, 785))]
teniase_tratamento = [fake.teniase_tratamento() for i in range(len(teniase_sintomas))]
teniase_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(teniase_sintomas))]
teniase_queixa_principal = [teniase_sintomas[i][np.random.randint(len(teniase_sintomas[i]))] for i in range(len(teniase_sintomas))]
teniase_hipotese = ['Teníase' for i in range(len(teniase_sintomas))]
teniase_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(teniase_sintomas))
teniase_casos_mensais = transformar_em_meses(teniase_lista_de_ocorrencias_mensais)


glaucoma_angulo_aberto_cronico_sintomas = [list({fake.glaucoma_angulo_aberto_cronico_sintomas() for i in range(math.ceil(len(fake.glaucoma_angulo_aberto_cronico_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(581, 785))]
glaucoma_angulo_aberto_cronico_tratamento = [fake.glaucoma_angulo_aberto_cronico_tratamento() for i in range(len(glaucoma_angulo_aberto_cronico_sintomas))]
glaucoma_angulo_aberto_cronico_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(glaucoma_angulo_aberto_cronico_sintomas))]
glaucoma_angulo_aberto_cronico_queixa_principal = [glaucoma_angulo_aberto_cronico_sintomas[i][np.random.randint(len(glaucoma_angulo_aberto_cronico_sintomas[i]))] for i in range(len(glaucoma_angulo_aberto_cronico_sintomas))]
glaucoma_angulo_aberto_cronico_hipotese = ['Glaucoma ângulo aberto crônico' for i in range(len(glaucoma_angulo_aberto_cronico_sintomas))]
glaucoma_angulo_aberto_cronico_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(glaucoma_angulo_aberto_cronico_sintomas))
glaucoma_angulo_aberto_cronico_casos_mensais = transformar_em_meses(glaucoma_angulo_aberto_cronico_lista_de_ocorrencias_mensais)


glaucoma_angulo_fechado_sintomas = [list({fake.glaucoma_angulo_fechado_sintomas() for i in range(math.ceil(len(fake.glaucoma_angulo_fechado_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(581, 785))]
glaucoma_angulo_fechado_tratamento = [fake.glaucoma_angulo_fechado_tratamento() for i in range(len(glaucoma_angulo_fechado_sintomas))]
glaucoma_angulo_fechado_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(glaucoma_angulo_fechado_sintomas))]
glaucoma_angulo_fechado_queixa_principal = [glaucoma_angulo_fechado_sintomas[i][np.random.randint(len(glaucoma_angulo_fechado_sintomas[i]))] for i in range(len(glaucoma_angulo_fechado_sintomas))]
glaucoma_angulo_fechado_hipotese = ['Glaucoma ângulo fechado' for i in range(len(glaucoma_angulo_fechado_sintomas))]
glaucoma_angulo_fechado_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(glaucoma_angulo_fechado_sintomas))
glaucoma_angulo_fechado_casos_mensais = transformar_em_meses(glaucoma_angulo_fechado_lista_de_ocorrencias_mensais)


clamidia_sintomas = [list({fake.clamidia_sintomas() for i in range(math.ceil(len(fake.clamidia_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(581, 785))]
clamidia_tratamento = [fake.clamidia_tratamento() for i in range(len(clamidia_sintomas))]
clamidia_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(clamidia_sintomas))]
clamidia_queixa_principal = [clamidia_sintomas[i][np.random.randint(len(clamidia_sintomas[i]))] for i in range(len(clamidia_sintomas))]
clamidia_hipotese = ['Clamídia' for i in range(len(clamidia_sintomas))]
clamidia_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(clamidia_sintomas))
clamidia_casos_mensais = transformar_em_meses(clamidia_lista_de_ocorrencias_mensais)


ascaridiase_sintomas = [list({fake.ascaridiase_sintomas() for i in range(math.ceil(len(fake.ascaridiase_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(581, 785))]
ascaridiase_tratamento = [fake.ascaridiase_tratamento() for i in range(len(ascaridiase_sintomas))]
ascaridiase_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(ascaridiase_sintomas))]
ascaridiase_queixa_principal = [ascaridiase_sintomas[i][np.random.randint(len(ascaridiase_sintomas[i]))] for i in range(len(ascaridiase_sintomas))]
ascaridiase_hipotese = ['Ascaridíase' for i in range(len(ascaridiase_sintomas))]
ascaridiase_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(ascaridiase_sintomas))
ascaridiase_casos_mensais = transformar_em_meses(ascaridiase_lista_de_ocorrencias_mensais)


# Gerando doenças muito comuns
amigdalite_viral_sintomas = [list({fake.amigdalite_viral_sintomas() for i in range(math.ceil(len(fake.amigdalite_viral_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(3315, 4485))]
amigdalite_viral_tratamento  = [fake.amigdalite_viral_tratamento() for i in range(len(amigdalite_viral_sintomas))]
amigdalite_viral_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(amigdalite_viral_sintomas))]
amigdalite_viral_queixa_principal = [amigdalite_viral_sintomas[i][np.random.randint(len(amigdalite_viral_sintomas[i]))] for i in range(len(amigdalite_viral_sintomas))]
amigdalite_viral_hipotese = ['Amigdalite' for i in range(len(amigdalite_viral_sintomas))]
amigdalite_viral_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(amigdalite_viral_sintomas))
amigdalite_viral_casos_mensais = transformar_em_meses(amigdalite_viral_lista_de_ocorrencias_mensais)


amigdalite_bacteriana_sintomas = [list({fake.amigdalite_bacteriana_sintomas() for i in range(math.ceil(len(fake.amigdalite_bacteriana_sintomas())/(np.random.randint(2,3))))}) for i in range(np.random.randint(3315, 4485))]
amigdalite_bacteriana_tratamento  = [fake.amigdalite_bacteriana_tratamento() for i in range(len(amigdalite_bacteriana_sintomas))]
amigdalite_bacteriana_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(amigdalite_bacteriana_sintomas))]
amigdalite_bacteriana_queixa_principal = [amigdalite_bacteriana_sintomas[i][np.random.randint(len(amigdalite_bacteriana_sintomas[i]))] for i in range(len(amigdalite_bacteriana_sintomas))]
amigdalite_bacteriana_hipotese = ['Amigdalite' for i in range(len(amigdalite_bacteriana_sintomas))]
amigdalite_bacteriana_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(amigdalite_bacteriana_sintomas))
amigdalite_bacteriana_casos_mensais = transformar_em_meses(amigdalite_bacteriana_lista_de_ocorrencias_mensais)


has_sintomas = [list({fake.has_sintomas() for i in range(math.ceil(len(fake.has_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
has_tratamento = [fake.has_tratamento() for i in range(len(has_sintomas))]
has_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(has_sintomas))]
has_queixa_principal = [has_sintomas[i][np.random.randint(len(has_sintomas[i]))] for i in range(len(has_sintomas))]
has_hipotese = ['Hipertensão Arterial Sistêmica (HAS)' for i in range(len(has_sintomas))]
has_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(has_sintomas))
has_casos_mensais = transformar_em_meses(has_lista_de_ocorrencias_mensais)


asma_leve_sintomas = [list({fake.asma_leve_sintomas() for i in range(math.ceil(len(fake.asma_leve_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
asma_leve_tratamento = [fake.asma_leve_tratamento() for i in range(len(asma_leve_sintomas))]
asma_leve_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(asma_leve_sintomas))]
asma_leve_queixa_principal = [asma_leve_sintomas[i][np.random.randint(len(asma_leve_sintomas[i]))] for i in range(len(asma_leve_sintomas))]
asma_leve_hipotese = ['Asma leve' for i in range(len(asma_leve_sintomas))]
asma_leve_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(asma_leve_sintomas))
asma_leve_casos_mensais = transformar_em_meses(asma_leve_lista_de_ocorrencias_mensais)


vaginose_bacteriana_sintomas = [list({fake.vaginose_bacteriana_sintomas() for i in range(math.ceil(len(fake.vaginose_bacteriana_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
vaginose_bacteriana_tratamento = [fake.vaginose_bacteriana_tratamento() for i in range(len(vaginose_bacteriana_sintomas))]
vaginose_bacteriana_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(vaginose_bacteriana_sintomas))]
vaginose_bacteriana_principal = [vaginose_bacteriana_sintomas[i][np.random.randint(len(vaginose_bacteriana_sintomas[i]))] for i in range(len(vaginose_bacteriana_sintomas))]
vaginose_bacteriana_hipotese = ['Vaginose Bacteriana' for i in range(len(vaginose_bacteriana_sintomas))]
vaginose_bacteriana_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(vaginose_bacteriana_sintomas))
vaginose_bacteriana_casos_mensais = transformar_em_meses(vaginose_bacteriana_lista_de_ocorrencias_mensais)


pneumonia_viral_sintomas = [list({fake.pneumonia_viral_sintomas() for i in range(math.ceil(len(fake.pneumonia_viral_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(3315, 4485))]
pneumonia_viral_tratamento = [fake.pneumonia_viral_tratamento() for i in range(len(pneumonia_viral_sintomas))]
pneumonia_viral_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(pneumonia_viral_sintomas))]
pneumonia_viral_queixa_principal = [pneumonia_viral_sintomas[i][np.random.randint(len(pneumonia_viral_sintomas[i]))] for i in range(len(pneumonia_viral_sintomas))]
pneumonia_viral_hipotese = ['Pneumonia' for i in range(len(pneumonia_viral_sintomas))]
pneumonia_viral_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(pneumonia_viral_sintomas))
pneumonia_viral_casos_mensais = transformar_em_meses(pneumonia_viral_lista_de_ocorrencias_mensais)


pneumonia_bacteriana_sintomas = [list({fake.pneumonia_bacteriana_sintomas() for i in range(math.ceil(len(fake.pneumonia_bacteriana_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(3315, 4485))]
pneumonia_bacteriana_tratamento = [fake.pneumonia_bacteriana_tratamento() for i in range(len(pneumonia_bacteriana_sintomas))]
pneumonia_bacteriana_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(pneumonia_bacteriana_sintomas))]
pneumonia_bacteriana_queixa_principal = [pneumonia_bacteriana_sintomas[i][np.random.randint(len(pneumonia_bacteriana_sintomas[i]))] for i in range(len(pneumonia_bacteriana_sintomas))]
pneumonia_bacteriana_hipotese = ['Pneumonia' for i in range(len(pneumonia_bacteriana_sintomas))]
pneumonia_bacteriana_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(pneumonia_bacteriana_sintomas))
pneumonia_bacteriana_casos_mensais = transformar_em_meses(pneumonia_bacteriana_lista_de_ocorrencias_mensais)


refluxo_gastroesofagico_sintomas = [list({fake.refluxo_gastroesofagico_sintomas() for i in range(math.ceil(len(fake.refluxo_gastroesofagico_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
refluxo_gastroesofagico_tratamento = [fake.refluxo_gastroesofagico_tratamento() for i in range(len(refluxo_gastroesofagico_sintomas))]
refluxo_gastroesofagico_tratamento_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(refluxo_gastroesofagico_sintomas))]
refluxo_gastroesofagico_queixa_principal = [refluxo_gastroesofagico_sintomas[i][np.random.randint(len(refluxo_gastroesofagico_sintomas[i]))] for i in range(len(refluxo_gastroesofagico_sintomas))]
refluxo_gastroesofagico_hipotese = ['Doença do Refluxo Gastroesofágico' for i in range(len(refluxo_gastroesofagico_sintomas))]
refluxo_gastroesofagico_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(refluxo_gastroesofagico_sintomas))
refluxo_gastroesofagico_casos_mensais = transformar_em_meses(refluxo_gastroesofagico_lista_de_ocorrencias_mensais)


obesidade_sintomas = [list({fake.obesidade_sintomas() for i in range(math.ceil(len(fake.obesidade_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
obesidade_tratamento = [fake.obesidade_tratamento() for i in range(len(obesidade_sintomas))]
obesidade_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(obesidade_sintomas))]
obesidade_queixa_principal = [obesidade_sintomas[i][np.random.randint(len(obesidade_sintomas[i]))] for i in range(len(obesidade_sintomas))]
obesidade_hipotese = ['Obesidade' for i in range(len(obesidade_sintomas))]
obesidade_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(obesidade_sintomas))
obesidade_casos_mensais = transformar_em_meses(obesidade_lista_de_ocorrencias_mensais)


diabetes_dm2_sintomas = [list({fake.diabetes_dm2_sintomas() for i in range(math.ceil(len(fake.diabetes_dm2_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
diabetes_dm2_tratamento = [fake.diabetes_dm2_tratamento() for i in range(len(diabetes_dm2_sintomas))]
diabetes_dm2_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(diabetes_dm2_sintomas))]
diabetes_dm2_queixa_principal = [diabetes_dm2_sintomas[i][np.random.randint(len(diabetes_dm2_sintomas[i]))] for i in range(len(diabetes_dm2_sintomas))]
diabetes_dm2_hipotese = ['Diabetes DM-2' for i in range(len(diabetes_dm2_sintomas))]
diabetes_dm2_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(diabetes_dm2_sintomas))
diabetes_dm2_casos_mensais = transformar_em_meses(diabetes_dm2_lista_de_ocorrencias_mensais)


itu_sintomas = [list({fake.itu_sintomas() for i in range(math.ceil(len(fake.itu_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
itu_tratamento = [fake.itu_tratamento() for i in range(len(itu_sintomas))]
itu_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(itu_sintomas))]
itu_queixa_principal = [itu_sintomas[i][np.random.randint(len(itu_sintomas[i]))] for i in range(len(itu_sintomas))]
itu_hipotese = ['Infecção do Trato Urinário' for i in range(len(itu_sintomas))]
itu_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(itu_sintomas))
itu_casos_mensais = transformar_em_meses(itu_lista_de_ocorrencias_mensais)


tricomoníase_sintomas = [list({fake.tricomoníase_sintomas() for i in range(math.ceil(len(fake.tricomoníase_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
tricomoníase_tratamento = [fake.tricomoníase_tratamento() for i in range(len(tricomoníase_sintomas))]
tricomoníase_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(tricomoníase_sintomas))]
tricomoníase_queixa_principal = [tricomoníase_sintomas[i][np.random.randint(len(tricomoníase_sintomas[i]))] for i in range(len(tricomoníase_sintomas))]
tricomoníase_hipotese = ['Tricomoníase' for i in range(len(tricomoníase_sintomas))]
tricomoníase_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(tricomoníase_sintomas))
tricomoníase_casos_mensais = transformar_em_meses(tricomoníase_lista_de_ocorrencias_mensais)


gonorreia_sintomas = [list({fake.gonorreia_sintomas() for i in range(math.ceil(len(fake.gonorreia_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
gonorreia_tratamento = [fake.gonorreia_tratamento() for i in range(len(gonorreia_sintomas))]
gonorreia_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(gonorreia_sintomas))]
gonorreia_queixa_principal = [gonorreia_sintomas[i][np.random.randint(len(gonorreia_sintomas[i]))] for i in range(len(gonorreia_sintomas))]
gonorreia_hipotese = ['Gonorreia' for i in range(len(gonorreia_sintomas))]
gonorreia_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(gonorreia_sintomas))
gonorreia_casos_mensais = transformar_em_meses(gonorreia_lista_de_ocorrencias_mensais)


herpes_genital_sintomas = [list({fake.herpes_genital_sintomas() for i in range(math.ceil(len(fake.herpes_genital_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
herpes_genital_tratamento = [fake.herpes_genital_tratamento() for i in range(len(herpes_genital_sintomas))]
herpes_genital_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(herpes_genital_sintomas))]
herpes_genital_queixa_principal = [herpes_genital_sintomas[i][np.random.randint(len(herpes_genital_sintomas[i]))] for i in range(len(herpes_genital_sintomas))]
herpes_genital_hipotese = ['Herpes Genital' for i in range(len(herpes_genital_sintomas))]
herpes_genital_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(herpes_genital_sintomas))
herpes_genital_casos_mensais = transformar_em_meses(herpes_genital_lista_de_ocorrencias_mensais)


conjuntivite_viral_sintomas = [list({fake.conjuntivite_viral_sintomas() for i in range(math.ceil(len(fake.conjuntivite_viral_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(3315, 4485))]
conjuntivite_viral_tratamento = [fake.conjuntivite_viral_tratamento() for i in range(len(conjuntivite_viral_sintomas))]
conjuntivite_viral_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(conjuntivite_viral_sintomas))]
conjuntivite_viral_queixa_principal = [conjuntivite_viral_sintomas[i][np.random.randint(len(conjuntivite_viral_sintomas[i]))] for i in range(len(conjuntivite_viral_sintomas))]
conjuntivite_viral_hipotese = ['Conjuntivite' for i in range(len(conjuntivite_viral_sintomas))]
conjuntivite_viral_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(conjuntivite_viral_sintomas))
conjuntivite_viral_casos_mensais = transformar_em_meses(conjuntivite_viral_lista_de_ocorrencias_mensais)


conjuntivite_bacteriana_sintomas = [list({fake.conjuntivite_bacteriana_sintomas() for i in range(math.ceil(len(fake.conjuntivite_bacteriana_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(3315, 4485))]
conjuntivite_bacteriana_tratamento = [fake.conjuntivite_bacteriana_tratamento() for i in range(len(conjuntivite_bacteriana_sintomas))]
conjuntivite_bacteriana_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(conjuntivite_bacteriana_sintomas))]
conjuntivite_bacteriana_principal = [conjuntivite_bacteriana_sintomas[i][np.random.randint(len(conjuntivite_bacteriana_sintomas[i]))] for i in range(len(conjuntivite_bacteriana_sintomas))]
conjuntivite_bacteriana_hipotese = ['Conjuntivite' for i in range(len(conjuntivite_bacteriana_sintomas))]
conjuntivite_bacteriana_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(conjuntivite_bacteriana_sintomas))
conjuntivite_bacteriana_casos_mensais = transformar_em_meses(conjuntivite_bacteriana_lista_de_ocorrencias_mensais)


candidiase_sintomas = [list({fake.candidiase_sintomas() for i in range(math.ceil(len(fake.candidiase_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(6630, 8970))]
candidiase_tratamento = [fake.candidiase_tratamento() for i in range(len(candidiase_sintomas))]
candidiase_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(candidiase_sintomas))]
candidiase_queixa_principal = [candidiase_sintomas[i][np.random.randint(len(candidiase_sintomas[i]))] for i in range(len(candidiase_sintomas))]
candidiase_hipotese = ['Candidíase' for i in range(len(candidiase_sintomas))]
candidiase_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(candidiase_sintomas))
candidiase_casos_mensais = transformar_em_meses(candidiase_lista_de_ocorrencias_mensais)

rinossinusite_viral_sintomas = [list({fake.rinossinusite_viral_sintomas() for i in range(math.ceil(len(fake.rinossinusite_viral_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(3315, 4485))]
rinossinusite_viral_tratamento = [fake.rinossinusite_viral_tratamento() for i in range(len(rinossinusite_viral_sintomas))]
rinossinusite_viral_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(rinossinusite_viral_sintomas))]
rinossinusite_viral_queixa_principal = [rinossinusite_viral_sintomas[i][np.random.randint(len(rinossinusite_viral_sintomas[i]))] for i in range(len(rinossinusite_viral_sintomas))]
rinossinusite_viral_hipotese = ['Rinossinusite' for i in range(len(rinossinusite_viral_sintomas))]
rinossinusite_viral_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(rinossinusite_viral_sintomas))
rinossinusite_viral_casos_mensais = transformar_em_meses(rinossinusite_viral_lista_de_ocorrencias_mensais)


rinossinusite_bacteriana_sintomas = [list({fake.rinossinusite_bacteriana_sintomas() for i in range(math.ceil(len(fake.rinossinusite_bacteriana_sintomas()) / (np.random.randint(2, 3))))}) for i in range(np.random.randint(3315, 4485))]
rinossinusite_bacteriana_tratamento = [fake.rinossinusite_bacteriana_tratamento() for i in range(len(rinossinusite_bacteriana_sintomas))]
rinossinusite_bacteriana_bairro = [bairros[np.random.randint(len(bairros))] for i in range(len(rinossinusite_bacteriana_sintomas))]
rinossinusite_bacteriana_queixa_principal = [rinossinusite_bacteriana_sintomas[i][np.random.randint(len(rinossinusite_bacteriana_sintomas[i]))] for i in range(len(rinossinusite_bacteriana_sintomas))]
rinossinusite_bacteriana_hipotese = ['Rinossinusite' for i in range(len(rinossinusite_bacteriana_sintomas))]
rinossinusite_bacteriana_lista_de_ocorrencias_mensais = dividir_valor_mensalmente(len(rinossinusite_bacteriana_sintomas))
rinossinusite_bacteriana_casos_mensais = transformar_em_meses(rinossinusite_bacteriana_lista_de_ocorrencias_mensais)


df = pd.DataFrame(list(zip(x, y, z)), columns=['teste1', 'teste2', 'teste3'] )

columns_df = ['mes', 'sintomas', 'tratamento', 'bairro', 'queixa', 'hipotese']
hanseniase_df = pd.DataFrame(list(zip(
    rinossinusite_bacteriana_casos_mensais,
    rinossinusite_bacteriana_sintomas, 
    rinossinusite_bacteriana_tratamento, 
    rinossinusite_bacteriana_bairro, 
    rinossinusite_bacteriana_queixa_principal, 
    rinossinusite_bacteriana_hipotese)), columns=columns_df)




hanseniase_df = pd.DataFrame(list(zip(
    hanseniase_casos_mensais,
    hanseniase_sintomas,
    hanseniase_tratamento,
    hanseniase_bairro,
    hanseniase_queixa_principal,
    hanseniase_hipotese
)),columns = columns_df)
esporotricose_df = pd.DataFrame(list(zip(
    esporotricose_casos_mensais,
    esporotricose_sintomas,
    esporotricose_tratamento,
    esporotricose_bairro,
    esporotricose_queixa_principal,
    esporotricose_hipotese
)),columns = columns_df)
caxumba_df = pd.DataFrame(list(zip(
    caxumba_casos_mensais,
    caxumba_sintomas,
    caxumba_tratamento,
    caxumba_bairro,
    caxumba_queixa_principal,
    caxumba_hipotese
)),columns = columns_df)
tuberculose_df = pd.DataFrame(list(zip(
    tuberculose_casos_mensais,
    tuberculose_sintomas,
    tuberculose_tratamento,
    tuberculose_bairro,
    tuberculose_queixa_principal,
    tuberculose_hipotese
)),columns = columns_df)
sifilis_df = pd.DataFrame(list(zip(
    sifilis_casos_mensais,
    sifilis_sintomas,
    sifilis_tratamento,
    sifilis_bairro,
    sifilis_queixa_principal,
    sifilis_hipotese
)),columns = columns_df)
oxiuriase_df = pd.DataFrame(list(zip(
    oxiuriase_casos_mensais,
    oxiuriase_sintomas,
    oxiuriase_tratamento,
    oxiuriase_bairro,
    oxiuriase_queixa_principal,
    oxiuriase_hipotese
)),columns = columns_df)
dengue_df = pd.DataFrame(list(zip(
    dengue_casos_mensais,
    dengue_sintomas,
    dengue_tratamento,
    dengue_bairro,
    dengue_queixa_principal,
    dengue_hipotese
)),columns = columns_df)
catapora_df = pd.DataFrame(list(zip(
    catapora_casos_mensais,
    catapora_sintomas,
    catapora_tratamento,
    catapora_bairro,
    catapora_queixa_principal,
    catapora_hipotese
)),columns = columns_df)
escabiose_df = pd.DataFrame(list(zip(
    escabiose_casos_mensais,
    escabiose_sintomas,
    escabiose_tratamento,
    escabiose_bairro,
    escabiose_queixa_principal,
    escabiose_hipotese
)),columns = columns_df)
esquistossomose_df = pd.DataFrame(list(zip(
    esquistossomose_casos_mensais,
    esquistossomose_sintomas,
    esquistossomose_tratamento,
    esquistossomose_bairro,
    esquistossomose_queixa_principal,
    esquistossomose_hipotese
)),columns = columns_df)
teniase_df = pd.DataFrame(list(zip(
    teniase_casos_mensais,
    teniase_sintomas,
    teniase_tratamento,
    teniase_bairro,
    teniase_queixa_principal,
    teniase_hipotese
)),columns = columns_df)
glaucoma_angulo_aberto_cronico_df = pd.DataFrame(list(zip(
    glaucoma_angulo_aberto_cronico_casos_mensais,
    glaucoma_angulo_aberto_cronico_sintomas,
    glaucoma_angulo_aberto_cronico_tratamento,
    glaucoma_angulo_aberto_cronico_bairro,
    glaucoma_angulo_aberto_cronico_queixa_principal,
    glaucoma_angulo_aberto_cronico_hipotese
)),columns = columns_df)
glaucoma_angulo_fechado_df = pd.DataFrame(list(zip(
    glaucoma_angulo_fechado_casos_mensais,
    glaucoma_angulo_fechado_sintomas,
    glaucoma_angulo_fechado_tratamento,
    glaucoma_angulo_fechado_bairro,
    glaucoma_angulo_fechado_queixa_principal,
    glaucoma_angulo_fechado_hipotese
)),columns = columns_df)
clamidia_df = pd.DataFrame(list(zip(
    clamidia_casos_mensais,
    clamidia_sintomas,
    clamidia_tratamento,
    clamidia_bairro,
    clamidia_queixa_principal,
    clamidia_hipotese
)),columns = columns_df)
ascaridiase_df = pd.DataFrame(list(zip(
    ascaridiase_casos_mensais,
    ascaridiase_sintomas,
    ascaridiase_tratamento,
    ascaridiase_bairro,
    ascaridiase_queixa_principal,
    ascaridiase_hipotese
)),columns = columns_df)
amigdalite_viral_df = pd.DataFrame(list(zip(
    amigdalite_viral_casos_mensais,
    amigdalite_viral_sintomas,
    amigdalite_viral_tratamento,
    amigdalite_viral_bairro,
    amigdalite_viral_queixa_principal,
    amigdalite_viral_hipotese
)),columns = columns_df)
amigdalite_bacteriana_df = pd.DataFrame(list(zip(
    amigdalite_bacteriana_casos_mensais,
    amigdalite_bacteriana_sintomas,
    amigdalite_bacteriana_tratamento,
    amigdalite_bacteriana_bairro,
    amigdalite_bacteriana_queixa_principal,
    amigdalite_bacteriana_hipotese
)),columns = columns_df)
has_df = pd.DataFrame(list(zip(
    has_casos_mensais,
    has_sintomas,
    has_tratamento,
    has_bairro,
    has_queixa_principal,
    has_hipotese
)),columns = columns_df)
asma_leve_df = pd.DataFrame(list(zip(
    asma_leve_casos_mensais,
    asma_leve_sintomas,
    asma_leve_tratamento,
    asma_leve_bairro,
    asma_leve_queixa_principal,
    asma_leve_hipotese
)),columns = columns_df)
vaginose_bacteriana_df = pd.DataFrame(list(zip(
    vaginose_bacteriana_casos_mensais,
    vaginose_bacteriana_sintomas,
    vaginose_bacteriana_tratamento,
    vaginose_bacteriana_bairro,
    vaginose_bacteriana_queixa_principal,
    vaginose_bacteriana_hipotese
)),columns = columns_df)
pneumonia_viral_df = pd.DataFrame(list(zip(
    pneumonia_viral_casos_mensais,
    pneumonia_viral_sintomas,
    pneumonia_viral_tratamento,
    pneumonia_viral_bairro,
    pneumonia_viral_queixa_principal,
    pneumonia_viral_hipotese
)),columns = columns_df)
pneumonia_bacteriana_df = pd.DataFrame(list(zip(
    pneumonia_bacteriana_casos_mensais,
    pneumonia_bacteriana_sintomas,
    pneumonia_bacteriana_tratamento,
    pneumonia_bacteriana_bairro,
    pneumonia_bacteriana_queixa_principal,
    pneumonia_bacteriana_hipotese
)),columns = columns_df)
refluxo_gastroesofagico_df = pd.DataFrame(list(zip(
    refluxo_gastroesofagico_casos_mensais,
    refluxo_gastroesofagico_sintomas,
    refluxo_gastroesofagico_tratamento,
    refluxo_gastroesofagico_bairro,
    refluxo_gastroesofagico_queixa_principal,
    refluxo_gastroesofagico_hipotese
)),columns = columns_df)
obesidade_df = pd.DataFrame(list(zip(
    obesidade_casos_mensais,
    obesidade_sintomas,
    obesidade_tratamento,
    obesidade_bairro,
    obesidade_queixa_principal,
    obesidade_hipotese
)),columns = columns_df)
diabetes_dm2_df = pd.DataFrame(list(zip(
    diabetes_dm2_casos_mensais,
    diabetes_dm2_sintomas,
    diabetes_dm2_tratamento,
    diabetes_dm2_bairro,
    diabetes_dm2_queixa_principal,
    diabetes_dm2_hipotese
)),columns = columns_df)
itu_df = pd.DataFrame(list(zip(
    itu_casos_mensais,
    itu_sintomas,
    itu_tratamento,
    itu_bairro,
    itu_queixa_principal,
    itu_hipotese
)),columns = columns_df)
tricomoníase_df = pd.DataFrame(list(zip(
    tricomoníase_casos_mensais,
    tricomoníase_sintomas,
    tricomoníase_tratamento,
    tricomoníase_bairro,
    tricomoníase_queixa_principal,
    tricomoníase_hipotese
)),columns = columns_df)
gonorreia_df = pd.DataFrame(list(zip(
    gonorreia_casos_mensais,
    gonorreia_sintomas,
    gonorreia_tratamento,
    gonorreia_bairro,
    gonorreia_queixa_principal,
    gonorreia_hipotese
)),columns = columns_df)
herpes_genital_df = pd.DataFrame(list(zip(
    herpes_genital_casos_mensais,
    herpes_genital_sintomas,
    herpes_genital_tratamento,
    herpes_genital_bairro,
    herpes_genital_queixa_principal,
    herpes_genital_hipotese
)),columns = columns_df)
conjuntivite_viral_df = pd.DataFrame(list(zip(
    conjuntivite_viral_casos_mensais,
    conjuntivite_viral_sintomas,
    conjuntivite_viral_tratamento,
    conjuntivite_viral_bairro,
    conjuntivite_viral_queixa_principal,
    conjuntivite_viral_hipotese
)),columns = columns_df)
conjuntivite_bacteriana_df = pd.DataFrame(list(zip(
    conjuntivite_bacteriana_casos_mensais,
    conjuntivite_bacteriana_sintomas,
    conjuntivite_bacteriana_tratamento,
    conjuntivite_bacteriana_bairro,
    conjuntivite_bacteriana_queixa_principal,
    conjuntivite_bacteriana_hipotese
)),columns = columns_df)
candidiase_df = pd.DataFrame(list(zip(
    candidiase_casos_mensais,
    candidiase_sintomas,
    candidiase_tratamento,
    candidiase_bairro,
    candidiase_queixa_principal,
    candidiase_hipotese
)),columns = columns_df)
rinossinusite_viral_df = pd.DataFrame(list(zip(
    rinossinusite_viral_casos_mensais,
    rinossinusite_viral_sintomas,
    rinossinusite_viral_tratamento,
    rinossinusite_viral_bairro,
    rinossinusite_viral_queixa_principal,
    rinossinusite_viral_hipotese
)),columns = columns_df)
rinossinusite_bacteriana_df = pd.DataFrame(list(zip(
    rinossinusite_bacteriana_casos_mensais,
    rinossinusite_bacteriana_sintomas,
    rinossinusite_bacteriana_tratamento,
    rinossinusite_bacteriana_bairro,
    rinossinusite_bacteriana_queixa_principal,
    rinossinusite_bacteriana_hipotese
)),columns = columns_df)

x = pd.concat([hanseniase_df,
esporotricose_df,
caxumba_df,
tuberculose_df,
sifilis_df,
oxiuriase_df,
dengue_df,
catapora_df,
escabiose_df,
esquistossomose_df,
teniase_df,
glaucoma_angulo_aberto_cronico_df,
glaucoma_angulo_fechado_df,
clamidia_df,
ascaridiase_df,
amigdalite_viral_df,
amigdalite_bacteriana_df,
has_df,
asma_leve_df,
vaginose_bacteriana_df,
pneumonia_viral_df,
pneumonia_bacteriana_df,
refluxo_gastroesofagico_df,
obesidade_df,
diabetes_dm2_df,
itu_df,
tricomoníase_df,
gonorreia_df,
herpes_genital_df,
conjuntivite_viral_df,
conjuntivite_bacteriana_df,
candidiase_df,
rinossinusite_viral_df,
rinossinusite_bacteriana_df])
'''
Função para Adicionar um Novo Filme;
Usa o gerenciador de contexto para abrir o 
arquivo no modo 'a' (Append);

'''
def adicionar_filme(ano, titulo, tema, sinopse):
    """
    Adiciona um novo filme ao final do arquivo 'catalogo_filmes.txt'.
    Cada campo é separado por ponto e vírgula (;).
    """
    ## Criamos o arquivo.
    nome_arquivo = "catalogo_filmes.txt"
   
    ## Montar a linha de dados para o arquivo
    nova_linha = f"{ano};{titulo};{tema};{sinopse}\n"

    ## Carregamento do arquivo,modo portugues brasil ('utf-8')
    try:
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(nova_linha)
        print(f"✅ Filme '{titulo}' adicionado ao catálogo com sucesso!")

    except Exception as e:
        # Tratamento de erro básico
        print(f"❌ Ocorreu um erro ao salvar o filme: {e}")


    """
    Demonstração de Uso:    
    """

adicionar_filme(
    ano="2020",
    titulo="O Homem Invisível",
    tema="Terror / Ficção Científica",
    sinopse="Uma mulher tenta provar que está sendo perseguida por seu ex-namorado, um cientista que desenvolveu um traje de invisibilidade."
)
adicionar_filme(
    ano="2020",
    titulo="O Céu da Meia-Noite",
    tema="Ficção Científica",
    sinopse="Um cientista solitário no Ártico tenta impedir que uma equipe de astronautas retorne à Terra após um desastre global, enquanto enfrenta as consequências da solidão e do fim do mundo."
)
adicionar_filme(
    ano="2020",
    titulo="Bad Boys Para Sempre",
    tema="Ação / Comédia",
    sinopse="Os policiais Mike e Marcus se juntam a recém-criada equipe de elite do departamento de polícia de Miami para derrubar o líder de um cartel de drogas da cidade."
)
adicionar_filme(
    ano="2017",
    titulo="Jogador N° 1",
    tema="Ficção Científica",
    sinopse="Em um futuro onde as pessoas ficam muito tempo na realidade virtual, existe uma guerra para achar um easter egg e herdar toda realidade."
)
adicionar_filme(
    ano="2010",
    titulo="A Origem",
    tema="Ficção Científica / Thriller",
    sinopse="Thriller de ficção científica que explora sonhos e a manipulação da mente."
)

adicionar_filme(
    ano="1999", 
    titulo="Matrix", 
    tema="Ficção Científica", 
    sinopse="Um hacker descobre que a realidade é uma simulação controlada por máquinas."
)
adicionar_filme(
    ano="2008", 
    titulo="Batman: O Cavaleiro das Trevas", 
    tema="Ação / Super-Herói", 
    sinopse="Batman enfrenta o Coringa, um criminoso anárquico que ameaça Gotham City."
)
adicionar_filme(
    ano="1985",
    titulo="De Volta para o Futuro",
    tema="Ficção Científica",
    sinopse="Um adolescente viaja acidentalmente para 1955 na máquina do tempo DeLorean e precisa garantir que seus pais se apaixonem para salvar sua própria existência."
)
adicionar_filme(
    ano="1994",
    titulo="Forrest Gump",
    tema="Drama / Comédia",
    sinopse="A vida extraordinária de Forrest Gump, um homem com QI baixo que, apesar de suas limitações, influencia eventos históricos e vive aventuras incríveis."
)
adicionar_filme(
    ano="2000",
    titulo="X-Men",
    tema="Ficção Científica",
    sinopse="Mutantes com poderes extraordinários se dividem entre a visão pacífica do Professor Xavier e o plano de dominação mundial de Magneto, com Wolverine e Rogue no centro do conflito."
) 
adicionar_filme(
    ano="2000",
    titulo="Gladiador",
    tema="Épico Histórico / Vingança",
    sinopse="Um general romano, traído e escravizado após o assassinato do imperador, se torna um gladiador famoso em busca de vingança contra o novo imperador, Commodus."
)
adicionar_filme(
    ano="2014",
    titulo="Interestelar",
    tema="Ficção Científica",
    sinopse="Um grupo de astronautas viaja por um buraco de minhoca em busca de um novo lar para a humanidade, enquanto o tempo e o amor desafiam as leis da física."
    )
adicionar_filme(
    ano="2017",
    titulo="Blade Runner 2049",
    tema="Ficção Científica",
    sinopse="Um novo caçador de androides descobre um segredo enterrado há décadas que pode mudar o destino da humanidade e dos replicantes."
)
adicionar_filme(
    ano="2020",
    titulo="Tenet",
    tema="Ação e Ficção Científica",
    sinopse="Um agente é recrutado para impedir a Terceira Guerra Mundial usando uma tecnologia que inverte o fluxo do tempo."
)
adicionar_filme(
    ano="2020",
    titulo="Sonic: O Filme",
    tema="Aventura e Comédia",
    sinopse="Sonic, um ouriço veloz de outro planeta, se une a um policial para escapar do Dr. Robotnik e salvar o mundo."
    )
adicionar_filme(
    ano="2020", 
    titulo="Soul", 
    tema="Animação/Aventura", 
    sinopse="Um músico de jazz em Nova York luta para reunir sua alma e seu corpo."
)

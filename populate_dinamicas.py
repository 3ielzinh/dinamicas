"""
Script para popular o banco de dados com dinâmicas de exemplo.
Execute com: python manage.py shell < populate_dinamicas.py
Ou crie um comando customizado.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.dinamicas.models import Dinamica, Categoria, NivelIntensidade, PublicoIndicado


def criar_dinamicas():
    """Cria todas as 120 dinâmicas organizadas por categoria"""
    
    dinamicas_data = [
        # DINÂMICAS DE QUEBRA-GELO (1-20)
        {
            'numero': 1,
            'titulo': 'Duas Verdades e Uma Mentira',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Dinâmica divertida para conhecer melhor os participantes através de histórias pessoais.',
            'objetivo': 'Quebrar o gelo inicial e criar um ambiente descontraído onde as pessoas possam se conhecer melhor.',
            'materiais': '- Nenhum material necessário\n- Opcional: papel e caneta para anotações',
            'passo_a_passo': '''1. Organize os participantes em círculo
2. Explique que cada pessoa dirá 3 afirmações sobre si mesma
3. Duas afirmações devem ser verdadeiras e uma mentira
4. O grupo deve adivinhar qual é a mentira
5. Após as tentativas, a pessoa revela a resposta
6. Continue até todos participarem
7. Encerre com uma reflexão sobre o que aprenderam uns dos outros''',
            'tempo_estimado': '15-20 minutos',
            'quantidade_participantes': '8-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Efésios 4:25 - "Por isso, deixem a mentira e falem a verdade."'
        },
        {
            'numero': 2,
            'titulo': 'Tempestade de Nomes',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Atividade energética para memorizar nomes de forma divertida.',
            'objetivo': 'Ajudar todos a memorizarem os nomes uns dos outros rapidamente através de movimento e repetição.',
            'materiais': '- Espaço amplo para movimentação\n- Nenhum material adicional',
            'passo_a_passo': '''1. Forme um grande círculo com todos de pé
2. Uma pessoa no centro diz o nome de alguém do círculo
3. A pessoa chamada deve dizer outro nome antes que o do centro chegue até ela
4. Se não conseguir, vai para o centro
5. Continue por 10-15 minutos
6. Variação: adicione gestos junto com os nomes
7. Finalize com todos dizendo os nomes que memorizaram''',
            'tempo_estimado': '15 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 3,
            'titulo': 'Encontre Alguém Que...',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Caça ao tesouro humana para descobrir características comuns.',
            'objetivo': 'Incentivar a interação entre todos os participantes e descobrir coisas em comum.',
            'materiais': '- Folhas impressas com lista de características\n- Canetas para todos',
            'passo_a_passo': '''1. Prepare uma lista com 15-20 características (ex: "toca instrumento", "tem irmão gêmeo")
2. Entregue uma cópia para cada participante
3. Ao seu sinal, todos circulam procurando pessoas que correspondam às características
4. Cada característica deve ter uma assinatura diferente
5. Primeiro a completar grita "Bingo!"
6. Valide as respostas com o grupo
7. Compartilhe descobertas interessantes''',
            'tempo_estimado': '20 minutos',
            'quantidade_participantes': '15-50 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        
        # DINÂMICAS DE AUTOCONHECIMENTO (21-40)
        {
            'numero': 21,
            'titulo': 'Linha da Vida',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Reflexão visual sobre momentos marcantes da própria história.',
            'objetivo': 'Promover autoconhecimento através da reflexão sobre momentos importantes da vida.',
            'materiais': '- Papel A4 ou cartolina\n- Canetas coloridas\n- Régua (opcional)',
            'passo_a_passo': '''1. Distribua o material para cada participante
2. Peça que desenhem uma linha horizontal representando sua vida
3. Marquem os momentos mais importantes (altos e baixos)
4. Identifiquem como Deus esteve presente em cada momento
5. Em pequenos grupos (3-4 pessoas), compartilhem suas linhas
6. Permita 5-7 minutos de compartilhamento por pessoa
7. Encerre com oração de gratidão pelas jornadas''',
            'tempo_estimado': '40-50 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'Salmos 139:16 - "Todos os dias determinados para mim foram escritos no teu livro."'
        },
        {
            'numero': 22,
            'titulo': 'Escudo Pessoal',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Criação de um escudo representando valores e qualidades pessoais.',
            'objetivo': 'Identificar e reconhecer os próprios valores, qualidades e propósitos.',
            'materiais': '- Papel A4\n- Canetas e lápis de cor\n- Modelo de escudo impresso',
            'passo_a_passo': '''1. Entregue o modelo de escudo dividido em 4 partes
2. Quadrante 1: Desenhe seu maior talento
3. Quadrante 2: Seu maior valor/princípio
4. Quadrante 3: Uma conquista importante
5. Quadrante 4: Seu propósito/sonho
6. Tempo para criação: 15 minutos
7. Compartilhe em duplas ou grupos pequenos
8. Finalize com reflexão sobre identidade em Cristo''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Salmos 139:14 - "Sou formidável e maravilhosamente feito."'
        },
        
        # DINÂMICAS DE TRABALHO EM EQUIPE (41-60)
        {
            'numero': 41,
            'titulo': 'Torre de Papel',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Construção colaborativa de uma torre usando apenas papel.',
            'objetivo': 'Desenvolver trabalho em equipe, comunicação e criatividade sob pressão.',
            'materiais': '- 20 folhas de papel A4 por equipe\n- Fita adesiva\n- Cronômetro\n- Régua para medir',
            'passo_a_passo': '''1. Divida o grupo em equipes de 4-6 pessoas
2. Cada equipe recebe 20 folhas e fita adesiva
3. Objetivo: construir a torre mais alta em 15 minutos
4. Regras: usar apenas os materiais fornecidos
5. Torre deve ficar em pé sozinha por 30 segundos
6. Após o tempo, meça as torres
7. Reflita sobre liderança, comunicação e estratégia
8. Conecte com o trabalho em equipe na igreja''',
            'tempo_estimado': '25-30 minutos',
            'quantidade_participantes': '12-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
            'versiculo_base': '1 Coríntios 12:12 - "O corpo é uma unidade, embora tenha muitos membros."'
        },
        {
            'numero': 42,
            'titulo': 'Travessia Cega',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Atravessar obstáculos com olhos vendados, guiados pela equipe.',
            'objetivo': 'Desenvolver confiança mútua e habilidades de comunicação clara.',
            'materiais': '- Vendas para os olhos\n- Obstáculos seguros (almofadas, cadeiras, cordas)\n- Espaço amplo',
            'passo_a_passo': '''1. Prepare um percurso com obstáculos no chão
2. Divida em duplas ou trios
3. Uma pessoa é vendada, outras guiam apenas com voz
4. Objetivo: atravessar o percurso sem tocar obstáculos
5. Troque os papéis até todos participarem
6. Discuta: Como foi confiar? Como foi guiar?
7. Relacione com confiar em Deus e orientar outros
8. Encerre com oração sobre confiança''',
            'tempo_estimado': '30 minutos',
            'quantidade_participantes': '8-24 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Provérbios 3:5-6 - "Confie no Senhor de todo o seu coração."'
        },
        
        # DINÂMICAS ESPIRITUAIS (61-80)
        {
            'numero': 61,
            'titulo': 'Cartas para Deus',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Momento íntimo de escrita de carta pessoal para Deus.',
            'objetivo': 'Proporcionar um momento de intimidade com Deus através da escrita.',
            'materiais': '- Papel bonito ou pergaminho\n- Canetas\n- Envelopes\n- Música instrumental suave',
            'passo_a_passo': '''1. Prepare ambiente tranquilo com música suave
2. Explique que escreverão uma carta para Deus
3. Pode conter gratidão, pedidos, confissões, sonhos
4. Garanta privacidade total (não será lido)
5. Dê 15-20 minutos para escrita
6. Opção 1: Lacrar e levar para casa
7. Opção 2: Queimar simbolicamente (com segurança)
8. Ore sobre o momento vivido''',
            'tempo_estimado': '30 minutos',
            'quantidade_participantes': '5-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Filipenses 4:6 - "Apresentem seus pedidos a Deus."'
        },
        {
            'numero': 62,
            'titulo': 'Lava-Pés',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Reprodução do ato de Jesus lavar os pés dos discípulos.',
            'objetivo': 'Experimentar humildade, servir e ser servido como Jesus ensinou.',
            'materiais': '- Bacias\n- Água morna\n- Toalhas\n- Música de adoração suave\n- Sabonete líquido',
            'passo_a_passo': '''1. Prepare estações com bacias, água e toalhas
2. Leia João 13:1-17 sobre Jesus lavando os pés
3. Explique o significado: servir com humildade
4. Convide participantes a formarem duplas
5. Um lava os pés do outro, depois invertem
6. Durante o ato, podem orar ou apenas silenciar
7. Música suave ao fundo
8. Compartilhe o que sentiram
9. Encerre com oração e abraço''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'João 13:14 - "Se eu, sendo Senhor, lavei os vossos pés, vocês também devem lavar os pés uns dos outros."'
        },
        
        # DINÂMICAS DE DIVERSÃO E ENERGIA (81-100)
        {
            'numero': 81,
            'titulo': 'Dança das Cadeiras Bíblica',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Versão animada da dança das cadeiras com perguntas bíblicas.',
            'objetivo': 'Energizar o grupo enquanto revisa conhecimento bíblico de forma divertida.',
            'materiais': '- Cadeiras (uma a menos que participantes)\n- Música animada\n- Lista de perguntas bíblicas\n- Sistema de som',
            'passo_a_passo': '''1. Organize cadeiras em círculo (uma a menos)
2. Toque música e participantes circulam
3. Quando parar, todos sentam
4. Quem ficou de pé responde pergunta bíblica
5. Acertou: volta ao jogo; Errou: sai
6. Remove uma cadeira e continua
7. Continue até ter um campeão
8. Premie o vencedor''',
            'tempo_estimado': '20-25 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 82,
            'titulo': 'Corrida do Versículo',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Corrida em revezamento para encontrar versículos na Bíblia.',
            'objetivo': 'Estimular agilidade na busca por versículos de forma competitiva e divertida.',
            'materiais': '- Bíblias (uma por equipe)\n- Lista de versículos\n- Sinos ou buzinas\n- Espaço para correr',
            'passo_a_passo': '''1. Divida em equipes de 5-7 pessoas
2. Cada equipe em fila com Bíblia na frente
3. Líder anuncia um versículo (ex: João 3:16)
4. Primeiro da fila corre, encontra e lê em voz alta
5. Toca sino/buzina quando encontrar
6. Equipe que acertar primeiro ganha ponto
7. Pessoa vai para o fim da fila
8. Continue com 10-15 versículos
9. Equipe com mais pontos vence''',
            'tempo_estimado': '25-30 minutos',
            'quantidade_participantes': '15-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
            'versiculo_base': '2 Timóteo 2:15 - "Maneje bem a palavra da verdade."'
        },
        
        # DINÂMICAS PROFUNDAS PARA MOMENTOS MARCANTES (101-120)
        {
            'numero': 101,
            'titulo': 'Caixa de Memórias',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Criação de cápsula do tempo com memórias e promessas do retiro.',
            'objetivo': 'Marcar profundamente o momento do retiro e criar lembrança física duradoura.',
            'materiais': '- Caixa decorativa ou cápsula\n- Papéis\n- Canetas\n- Fotos do retiro\n- Fita adesiva',
            'passo_a_passo': '''1. Explique que criarão uma cápsula do tempo do retiro
2. Cada pessoa escreve: uma memória especial, uma gratidão, um compromisso
3. Podem incluir: fotos, versículos marcantes, objetos pequenos
4. Todos colocam seus papéis na caixa
5. Lacrem juntos com oração
6. Decidam quando abrir (6 meses, 1 ano)
7. Guardem em lugar especial da igreja
8. Na abertura futura, relembrem e celebrem crescimento''',
            'tempo_estimado': '35-45 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Josué 4:7 - "Estas pedras servirão de memorial."'
        },
        {
            'numero': 102,
            'titulo': 'Anel da Aliança',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Círculo de compromisso e oração uns pelos outros.',
            'objetivo': 'Criar pacto de oração e apoio mútuo que perdure após o retiro.',
            'materiais': '- Corda ou fita (formando círculo fechado)\n- Velas\n- Cartões de compromisso\n- Canetas',
            'passo_a_passo': '''1. Forme círculo com todos de mãos dadas
2. Passe a corda por dentro do círculo, conectando todos
3. Cada pessoa segura a corda com uma mão
4. Um por um, compartilha um pedido de oração pessoal
5. Todos se comprometem a orar por aquela pessoa
6. Anote os pedidos em cartões
7. Distribua os cartões aleatoriamente
8. Cada um será "anjo da guarda" em oração de alguém
9. Ore em grupo selando o compromisso
10. Acenda velas simbolizando luz uns para outros''',
            'tempo_estimado': '50-70 minutos',
            'quantidade_participantes': '8-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'Eclesiastes 4:12 - "O cordão de três dobras não se rompe com facilidade."'
        },
        {
            'numero': 103,
            'titulo': 'Legado de Bênçãos',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Cada pessoa recebe bênçãos escritas de todos do grupo.',
            'objetivo': 'Abençoar profundamente cada participante com palavras de edificação.',
            'materiais': '- Envelopes personalizados\n- Papéis coloridos\n- Canetas\n- Caixa decorativa',
            'passo_a_passo': '''1. Prepare um envelope para cada participante com seu nome
2. Coloque os envelopes espalhados em mesas
3. Durante 30 minutos, todos circulam escrevendo mensagens
4. Em cada envelope, escreva: uma qualidade que admira, uma palavra profética, um versículo
5. Pode ser anônimo ou assinado
6. Após todos escreverem, recolha os envelopes
7. Momento especial: cada pessoa recebe seu envelope
8. Leem em silêncio (ou compartilham algumas)
9. Guardem como tesouro do retiro
10. Ore abençoando cada vida presente''',
            'tempo_estimado': '60-90 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Provérbios 18:21 - "A língua tem poder sobre a vida e a morte."'
        },
    ]
    
    print("Iniciando população do banco de dados com dinâmicas...")
    
    criadas = 0
    atualizadas = 0
    
    for data in dinamicas_data:
        dinamica, created = Dinamica.objects.update_or_create(
            numero=data['numero'],
            defaults=data
        )
        
        if created:
            criadas += 1
            print(f"✓ Criada: {dinamica.numero}. {dinamica.titulo}")
        else:
            atualizadas += 1
            print(f"↻ Atualizada: {dinamica.numero}. {dinamica.titulo}")
    
    print(f"\n{'='*60}")
    print(f"Processo concluído!")
    print(f"Dinâmicas criadas: {criadas}")
    print(f"Dinâmicas atualizadas: {atualizadas}")
    print(f"Total no banco: {Dinamica.objects.count()}")
    print(f"{'='*60}")


if __name__ == '__main__':
    criar_dinamicas()

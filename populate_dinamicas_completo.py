"""
Script para popular o banco de dados com TODAS as 120 dinâmicas.
Execute com: python populate_dinamicas_completo.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.dinamicas.models import Dinamica, Categoria, NivelIntensidade, PublicoIndicado


def criar_todas_dinamicas():
    """Cria todas as 120 dinâmicas do sistema"""
    
    dinamicas_data = [
        # DINÂMICAS DE QUEBRA-GELO (1-20)
        {
            'numero': 1,
            'titulo': 'Teia da Amizade com Barbante',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Dinâmica visual que cria uma teia conectando todos os participantes através de um rolo de barbante.',
            'objetivo': 'Demonstrar visualmente como todos estão conectados no corpo de Cristo e iniciar o processo de integração.',
            'materiais': '- Rolo de barbante ou lã\n- Espaço para formar círculo',
            'passo_a_passo': '''1. Forme um círculo com todos os participantes
2. Uma pessoa segura a ponta do barbante e se apresenta brevemente
3. Joga o rolo para alguém, mantendo a ponta do fio
4. A pessoa que recebeu se apresenta e joga para outra
5. Continue até todos participarem
6. Ao final, terá uma teia visual conectando todos
7. Reflita sobre como somos conectados
8. Para desfazer: fazer o caminho inverso''',
            'tempo_estimado': '15-20 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': '1 Coríntios 12:27 - "Vocês são o corpo de Cristo."'
        },
        {
            'numero': 2,
            'titulo': 'Entrevista em Duplas e Apresentação Cruzada',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Participantes se entrevistam mutuamente e depois apresentam o parceiro para o grupo.',
            'objetivo': 'Incentivar a escuta ativa e ajudar os participantes a se conhecerem de forma mais profunda.',
            'materiais': '- Lista de perguntas sugeridas (opcional)\n- Canetas e papéis (opcional)',
            'passo_a_passo': '''1. Divida o grupo em duplas aleatórias
2. Dê 5 minutos para cada um entrevistar o outro
3. Perguntas sugeridas: maior sonho, momento marcante, maior desafio
4. Após 10 minutos, reúna todos em círculo
5. Cada pessoa apresenta seu parceiro (não a si mesmo)
6. Incentive apresentações criativas e divertidas
7. Finalize com uma rodada de aplausos''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 3,
            'titulo': 'Bingo Humano',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Caça ao tesouro humana onde participantes procuram pessoas com características específicas.',
            'objetivo': 'Descobrir afinidades e características interessantes dos participantes de forma divertida.',
            'materiais': '- Cartelas de bingo personalizadas\n- Canetas para todos\n- Prêmio simbólico (opcional)',
            'passo_a_passo': '''1. Prepare cartelas com características variadas (ex: toca violão, já fez missão, tem irmão gêmeo)
2. Distribua uma cartela e caneta para cada pessoa
3. Ao seu sinal, todos circulam procurando pessoas que se encaixem
4. Cada característica deve ter uma assinatura diferente
5. Primeiro a completar uma linha grita "Bingo!"
6. Valide as respostas com o grupo
7. Continue até ter 3 vencedores ou tempo esgotar
8. Compartilhe descobertas interessantes''',
            'tempo_estimado': '15-20 minutos',
            'quantidade_participantes': '15-60 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 4,
            'titulo': 'Duas Verdades e Uma Mentira',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Cada pessoa conta três histórias sobre si, sendo duas verdadeiras e uma falsa.',
            'objetivo': 'Conhecer histórias interessantes dos participantes de forma lúdica e surpreendente.',
            'materiais': '- Nenhum material necessário\n- Papéis para anotações (opcional)',
            'passo_a_passo': '''1. Organize o grupo em círculo
2. Explique que cada um dirá 3 afirmações sobre si
3. Duas devem ser verdadeiras, uma mentira
4. A mentira deve ser plausível (não óbvia)
5. O grupo tenta adivinhar qual é a mentira
6. Após as tentativas, revelam a verdade
7. Continue com todos os participantes
8. Finalize destacando as histórias mais surpreendentes''',
            'tempo_estimado': '15-25 minutos',
            'quantidade_participantes': '8-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 5,
            'titulo': 'Mapa do Nome',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Cada participante compartilha o significado e história por trás de seu nome.',
            'objetivo': 'Valorizar a identidade única de cada pessoa e a história que carrega em seu nome.',
            'materiais': '- Dicionário de nomes bíblicos (opcional)\n- Papel e canetas coloridas',
            'passo_a_passo': '''1. Peça que todos pesquisem o significado do nome (pode ser antes ou durante)
2. Cada pessoa compartilha: significado, quem escolheu, por que esse nome
3. Se houver conexão bíblica, explore
4. Opção: desenhar o nome de forma criativa
5. Compartilhe em círculo ou pequenos grupos
6. Ore pelos nomes e significados
7. Finalize valorizando a identidade única de cada um''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Isaías 43:1 - "Eu o chamei pelo nome; você é meu."'
        },
        {
            'numero': 6,
            'titulo': 'Linha do Tempo da Vida em 3 Minutos',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Cada pessoa tem 3 minutos para contar sua história de vida resumida.',
            'objetivo': 'Conhecer rapidamente a trajetória dos participantes de forma dinâmica.',
            'materiais': '- Cronômetro\n- Sino ou buzina para sinalizar tempo',
            'passo_a_passo': '''1. Explique que cada um terá exatamente 3 minutos
2. Devem contar: onde nasceu, infância, momento marcante, presente
3. Use cronômetro visível
4. Avise quando faltar 30 segundos
5. Toque sino/buzina quando acabar o tempo
6. Sem interrupções durante a fala
7. Próximo continua imediatamente
8. Ao final, destaque a diversidade de histórias''',
            'tempo_estimado': '30-60 minutos (depende do grupo)',
            'quantidade_participantes': '10-20 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 7,
            'titulo': 'Quem Sou Eu? (Nome Bíblico na Testa)',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Adesivo com nome de personagem bíblico na testa, descobrir fazendo perguntas.',
            'objetivo': 'Revisar conhecimento bíblico de forma divertida enquanto quebra o gelo.',
            'materiais': '- Etiquetas adesivas\n- Caneta\n- Lista de personagens bíblicos',
            'passo_a_passo': '''1. Prepare etiquetas com nomes bíblicos variados
2. Cole um nome na testa de cada pessoa (sem ver)
3. Explique: só podem fazer perguntas sim/não
4. Todos circulam perguntando aos outros
5. Exemplos: "Sou do Velho Testamento?" "Sou mulher?"
6. Quando descobrir, pode ajudar os outros
7. Continue até todos descobrirem
8. Discuta características dos personagens''',
            'tempo_estimado': '15-20 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 8,
            'titulo': 'Jogo das Afinidades',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Participantes se agrupam rapidamente por características anunciadas.',
            'objetivo': 'Descobrir afinidades comuns e promover movimentação e risadas.',
            'materiais': '- Espaço amplo\n- Lista de características variadas',
            'passo_a_passo': '''1. Todos em pé no centro da sala
2. Líder anuncia uma característica (ex: "mês de aniversário")
3. Pessoas com mesma característica se agrupam
4. Grupos pequenos fazem desafio/pergunta extra
5. Retornam ao centro
6. Nova característica é anunciada
7. Varie: sérias (sonhos) e engraçadas (sabor de sorvete)
8. Finalize com reflexão sobre diversidade e unidade''',
            'tempo_estimado': '15-20 minutos',
            'quantidade_participantes': '15-50 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 9,
            'titulo': 'Perguntas Aleatórias Dentro de Balões',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Perguntas interessantes dentro de balões coloridos que são estourados.',
            'objetivo': 'Gerar conversas espontâneas e divertidas através de perguntas aleatórias.',
            'materiais': '- Balões coloridos\n- Papéis com perguntas\n- Alfinetes ou palitos',
            'passo_a_passo': '''1. Prepare balões com perguntas dentro (uma por balão)
2. Encha todos os balões
3. Espalhe pelo ambiente ou distribua
4. Cada pessoa pega um balão
5. Estoura o balão e lê a pergunta
6. Responde para o grupo ou pequeno grupo
7. Perguntas variadas: sérias, engraçadas, profundas
8. Continue até acabarem os balões''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 10,
            'titulo': 'Corrente de Elogios',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Cada pessoa elogia genuinamente a pessoa ao lado, criando corrente positiva.',
            'objetivo': 'Criar ambiente de valorização e positividade desde o início.',
            'materiais': '- Nenhum material necessário',
            'passo_a_passo': '''1. Forme um círculo com todos sentados
2. Explique: cada um elogiará a pessoa à direita
3. Elogios devem ser sinceros e específicos
4. Não vale elogios genéricos ("legal", "legal")
5. Observe algo positivo real: atitude, característica, ação
6. Comece você dando exemplo
7. Continue no sentido horário
8. Finalize agradecendo a atmosfera criada''',
            'tempo_estimado': '10-15 minutos',
            'quantidade_participantes': '8-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Efésios 4:29 - "Falem apenas o que é bom para edificação."'
        },
        {
            'numero': 11,
            'titulo': 'Objeto que Me Representa',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Cada pessoa escolhe um objeto que a representa e explica o porquê.',
            'objetivo': 'Expressar personalidade e valores de forma criativa através de objetos.',
            'materiais': '- Objetos diversos espalhados (ou pedir que tragam de casa)\n- Pode ser simbólico/imaginário',
            'passo_a_passo': '''1. Opção 1: Espalhe objetos variados pela sala
2. Opção 2: Peça que tragam algo de casa
3. Opção 3: Objetos imaginários/simbólicos
4. Cada pessoa escolhe seu objeto
5. Explica por que aquele objeto a representa
6. Pode ser característica física ou simbólica
7. Grupo pode fazer perguntas
8. Guarde alguns objetos como memorial do retiro''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '10-25 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 12,
            'titulo': 'História em Uma Palavra',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Construção colaborativa de história onde cada pessoa contribui com uma palavra.',
            'objetivo': 'Estimular criatividade, trabalho coletivo e gerar muitas risadas.',
            'materiais': '- Nenhum (ou gravador para registrar)',
            'passo_a_passo': '''1. Sente o grupo em círculo
2. Líder começa: "Era uma vez..."
3. Próxima pessoa adiciona UMA palavra
4. Continue em círculo construindo a história
5. História deve fazer algum sentido (mínimo!)
6. Risadas são bem-vindas
7. Após 2-3 voltas completas, finalize a história
8. Alguém relê a história completa
9. Opção: gravar e ouvir depois''',
            'tempo_estimado': '10-15 minutos',
            'quantidade_participantes': '8-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 13,
            'titulo': 'Jogo do Sorriso',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Desafio de não rir enquanto outros tentam fazer você sorrir sem tocar.',
            'objetivo': 'Quebrar tensão inicial através de diversão e risadas genuínas.',
            'materiais': '- Nenhum material necessário',
            'passo_a_passo': '''1. Uma pessoa vai para o centro (voluntário)
2. Deve ficar sério(a) por 1 minuto
3. Os outros tentam fazê-la sorrir/rir
4. Regras: não pode tocar, apenas caretas/sons
5. Se sorrir, sai e outro entra
6. Se aguentar 1 minuto, escolhe próximo
7. Continue por 10-15 minutos
8. Prêmio simbólico para quem resistir mais''',
            'tempo_estimado': '15-20 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 14,
            'titulo': 'Corrida de Perguntas Rápidas',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Perguntas rápidas em sequência para conhecer preferências e opiniões.',
            'objetivo': 'Conhecer preferências e personalidades de forma rápida e dinâmica.',
            'materiais': '- Lista de perguntas preparadas\n- Cronômetro',
            'passo_a_passo': '''1. Prepare lista com 20-30 perguntas rápidas
2. Exemplos: "Praia ou montanha?" "Café ou chá?" "Cantor favorito?"
3. Faça perguntas para o grupo todo
4. Pessoas respondem levantando mão ou gritando
5. Não há certo ou errado
6. Mantenha ritmo acelerado
7. Perguntas mais profundas no final
8. Observe e comente padrões interessantes''',
            'tempo_estimado': '10-15 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 15,
            'titulo': 'Desafio do Aperto de Mão Criativo',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Duplas criam apertos de mão exclusivos e únicos.',
            'objetivo': 'Promover criatividade e conexão física apropriada entre participantes.',
            'materiais': '- Espaço amplo\n- Música animada (opcional)',
            'passo_a_passo': '''1. Divida em duplas aleatórias
2. Cada dupla cria um aperto de mão único
3. Pode incluir: palmas, estalos, movimentos
4. Dê 3 minutos para criar e ensaiar
5. Cada dupla apresenta seu cumprimento
6. Grupo tenta imitar
7. Vote no mais criativo
8. Opcional: criar um cumprimento coletivo final''',
            'tempo_estimado': '15-20 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 16,
            'titulo': 'Desafio dos 30 Segundos de Conexão',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Duplas têm 30 segundos para encontrar algo em comum.',
            'objetivo': 'Descobrir pontos de conexão rapidamente e valorizar semelhanças.',
            'materiais': '- Cronômetro\n- Apito ou sino',
            'passo_a_passo': '''1. Todos circulam pela sala
2. Ao sinal, formam duplas aleatórias
3. Têm 30 segundos para encontrar algo em comum
4. Não vale respostas óbvias (ser humano, estar no retiro)
5. Ao sinal, compartilham com grupo próximo
6. Formam novas duplas
7. Repita 5-7 vezes
8. Finalize compartilhando conexões mais inusitadas''',
            'tempo_estimado': '10-15 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 17,
            'titulo': 'Foto Imaginária',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Grupos criam poses criativas para "fotos" temáticas imaginárias.',
            'objetivo': 'Estimular criatividade e trabalho em equipe de forma lúdica.',
            'materiais': '- Câmera ou celular para fotos reais (opcional)',
            'passo_a_passo': '''1. Divida em grupos de 5-7 pessoas
2. Líder anuncia tema da foto (ex: "Salvação", "Adoração")
3. Grupos têm 1 minuto para criar pose coletiva
4. Podem usar corpo, expressões, formações
5. "Fotógrafo" (líder) tira foto imaginária
6. Opcional: tirar fotos reais para memória
7. Temas variados: 5-8 rodadas
8. Compartilhe fotos depois no grupo''',
            'tempo_estimado': '15-20 minutos',
            'quantidade_participantes': '15-50 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 18,
            'titulo': 'Histórias Improváveis',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Cada pessoa conta uma história real inacreditável que viveu.',
            'objetivo': 'Compartilhar experiências únicas e surpreender o grupo.',
            'materiais': '- Nenhum material necessário',
            'passo_a_passo': '''1. Explique: cada um contará algo inacreditável mas real
2. Histórias curtas (2-3 minutos)
3. Pode ser: coincidência, livramento, momento engraçado
4. Grupo pode fazer perguntas após
5. Histórias devem ser verdadeiras
6. Incentive detalhes que provem veracidade
7. Vote na história mais inacreditável
8. Conecte com providência divina''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '8-20 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 19,
            'titulo': 'Cartão com Talentos Escondidos',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Participantes escrevem talentos que ninguém sabe que têm.',
            'objetivo': 'Descobrir habilidades ocultas e valorizar a diversidade de dons.',
            'materiais': '- Cartões ou papéis\n- Canetas\n- Caixa ou chapéu',
            'passo_a_passo': '''1. Distribua cartões para todos
2. Escrevam um talento que poucos conhecem
3. Não assinem, mantenham anônimo
4. Coloquem na caixa
5. Líder sorteia e lê em voz alta
6. Grupo tenta adivinhar de quem é
7. Pessoa se revela e demonstra (se possível)
8. Continue até acabarem os cartões
9. Ore pelos dons e talentos presentes''',
            'tempo_estimado': '20-25 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': '1 Pedro 4:10 - "Cada um exerça o dom que recebeu."'
        },
        {
            'numero': 20,
            'titulo': 'Construindo Torre com Papel',
            'categoria': Categoria.QUEBRA_GELO,
            'descricao': 'Equipes competem para construir a torre mais alta usando apenas papel.',
            'objetivo': 'Incentivar trabalho em equipe, criatividade e competição saudável.',
            'materiais': '- Folhas de papel A4 (20 por equipe)\n- Fita adesiva\n- Régua para medir',
            'passo_a_passo': '''1. Divida em equipes de 4-6 pessoas
2. Cada equipe recebe 20 folhas e fita
3. Objetivo: torre mais alta em 10 minutos
4. Torre deve ficar em pé sozinha por 30 segundos
5. Só podem usar materiais fornecidos
6. Ao final, meça as torres
7. Discuta estratégias usadas
8. Relacione com construção do Reino''',
            'tempo_estimado': '20-25 minutos',
            'quantidade_participantes': '12-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },

        # DINÂMICAS DE AUTOCONHECIMENTO (21-40)
        {
            'numero': 21,
            'titulo': 'Carta para Si Mesmo no Futuro',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Escrever carta para si mesmo para ser aberta em 6 meses ou 1 ano.',
            'objetivo': 'Promover reflexão sobre presente e projetar transformações desejadas.',
            'materiais': '- Papel bonito ou carta\n- Envelopes\n- Canetas\n- Selos (se for enviar)',
            'passo_a_passo': '''1. Ambiente tranquilo com música suave
2. Explique que escreverão para seu "eu futuro"
3. Sugestões: como está hoje, o que espera mudar, promessas a Deus
4. Dê 15-20 minutos para escrita
5. Lacrem em envelope
6. Opção 1: Guardar e entregar depois
7. Opção 2: Enviar por correio
8. Ore sobre os desejos expressos''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '5-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 22,
            'titulo': 'Espelho da Identidade - Quem Sou Eu em Deus?',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Reflexão profunda sobre identidade em Cristo versus identidade social.',
            'objetivo': 'Confrontar identidade falsa com identidade verdadeira em Cristo.',
            'materiais': '- Espelhos pequenos ou um grande\n- Papéis\n- Canetas\n- Versículos sobre identidade impressos',
            'passo_a_passo': '''1. Cada pessoa olha no espelho por 1 minuto
2. Escreva: "O mundo diz que eu sou..."
3. Leia versículos sobre identidade (Ef 1, 2 Co 5:17)
4. Escreva: "Deus diz que eu sou..."
5. Compare as duas listas
6. Compartilhe em grupos pequenos
7. Rasguem ou queimem a primeira lista
8. Guardem a segunda como memorial''',
            'tempo_estimado': '40-50 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
            'versiculo_base': '2 Coríntios 5:17 - "Nova criatura é; as coisas velhas passaram."'
        },
        {
            'numero': 23,
            'titulo': 'Árvore da Vida (Raízes, Frutos, Sonhos)',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Desenhar árvore representando origem, presente e futuro.',
            'objetivo': 'Visualizar trajetória de vida e projetar crescimento futuro.',
            'materiais': '- Papel grande ou cartolina\n- Canetas coloridas\n- Lápis de cor\n- Modelo de árvore (opcional)',
            'passo_a_passo': '''1. Cada pessoa desenha uma árvore
2. Raízes: família, origem, fundamentos
3. Tronco: quem você é hoje, forças
4. Galhos: relacionamentos importantes
5. Frutos: conquistas e resultados
6. Flores: sonhos e potencial
7. Tempo para desenho: 20 minutos
8. Compartilhe em pequenos grupos
9. Exponha as árvores (opcional)''',
            'tempo_estimado': '40-60 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 24,
            'titulo': 'Linha da Graça',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Mapear momentos de intervenção divina clara na vida.',
            'objetivo': 'Reconhecer e agradecer pela providência e cuidado de Deus.',
            'materiais': '- Papel longo ou cartolina\n- Canetas\n- Adesivos ou marcadores coloridos',
            'passo_a_passo': '''1. Desenhe linha horizontal representando vida
2. Marque momentos de intervenção divina clara
3. Pode incluir: livramentos, cura, provisão, conversão
4. Use cores diferentes para tipos de graça
5. Escreva breve descrição em cada ponto
6. Reflita sobre a fidelidade de Deus
7. Compartilhe os mais marcantes
8. Ore em gratidão''',
            'tempo_estimado': '35-45 minutos',
            'quantidade_participantes': '8-25 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Salmos 103:2 - "Não te esqueças de nenhuma de suas bênçãos."'
        },
        {
            'numero': 25,
            'titulo': 'Mochila da Vida - O Que Carrego?',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Identificar pesos emocionais e espirituais que carregamos.',
            'objetivo': 'Conscientizar sobre fardos desnecessários e aprender a entregá-los.',
            'materiais': '- Mochila real\n- Pedras ou objetos pesados\n- Etiquetas\n- Canetas',
            'passo_a_passo': '''1. Mostre mochila vazia ao grupo
2. Explique: todos carregamos "pesos"
3. Liste tipos: mágoa, medo, culpa, preocupação
4. Cada pessoa escreve seus pesos em etiquetas
5. Voluntários colocam objetos na mochila (simbolizando)
6. Alguém tenta carregar a mochila
7. Reflita: como é carregar tudo isso?
8. Tire objetos um a um, entregando a Deus
9. Ore sobre cada área''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Mateus 11:28 - "Venham a mim, todos os que estão cansados e sobrecarregados."'
        },
        {
            'numero': 26,
            'titulo': 'Pedras e Flores',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Identificar dificuldades (pedras) e bênçãos (flores) do último ano.',
            'objetivo': 'Equilibrar perspectiva entre desafios enfrentados e graças recebidas.',
            'materiais': '- Pedras pequenas\n- Flores (reais ou papel)\n- Cestas ou vasos\n- Papéis pequenos',
            'passo_a_passo': '''1. Distribua pedras e flores para todos
2. Em uma pedra, escrevam maior dificuldade recente
3. Em uma flor, maior bênção recente
4. Crie dois espaços: jardim (flores) e vale (pedras)
5. Um por um, coloca pedra no vale e compartilha
6. Depois coloca flor no jardim e agradece
7. Observe que geralmente há mais flores
8. Ore pelas pedras e agradeça pelas flores''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 27,
            'titulo': 'Máscaras - O Que Mostro vs. O Que Sinto',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Criar máscaras que representam exterior (fachada) e interior (real).',
            'objetivo': 'Confrontar inautenticidade e encorajar vulnerabilidade.',
            'materiais': '- Máscaras brancas de papel\n- Tintas ou canetas\n- Pincéis\n- Espelho',
            'passo_a_passo': '''1. Cada pessoa recebe 2 máscaras
2. Máscara 1 (externa): como me mostro ao mundo
3. Máscara 2 (interna): como realmente me sinto
4. Tempo para criar: 20 minutos
5. Compartilhe em grupos pequenos (seguro)
6. Discuta: por que usamos máscaras?
7. Simbolicamente "tire" as máscaras
8. Compromisso de ser mais autêntico''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-25 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 28,
            'titulo': 'Diário de Silêncio Guiado',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Momento prolongado de silêncio com perguntas guiadas para reflexão.',
            'objetivo': 'Praticar silêncio, ouvir Deus e processar pensamentos internos.',
            'materiais': '- Diários ou cadernos\n- Canetas\n- Lista de perguntas reflexivas\n- Música instrumental suave',
            'passo_a_passo': '''1. Explique importância do silêncio
2. Distribua diários e lista de perguntas
3. Perguntas: "O que temo?", "O que espero de Deus?", "Onde preciso mudar?"
4. Silêncio total por 30 minutos
5. Música ambiente muito baixa
6. Líderes permanecem em oração
7. Após, opcional: compartilhar descobertas
8. Não force; respeite privacidade''',
            'tempo_estimado': '40-50 minutos',
            'quantidade_participantes': '5-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 29,
            'titulo': 'Teste dos Talentos Espirituais',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Questionário para identificar dons espirituais predominantes.',
            'objetivo': 'Ajudar a identificar e validar dons espirituais para uso no Reino.',
            'materiais': '- Teste impresso (baseado em Rm 12, 1Co 12, Ef 4)\n- Canetas\n- Folha de resultados',
            'passo_a_passo': '''1. Explique dons espirituais biblicamente
2. Distribua teste (30-50 perguntas)
3. Responda honestamente, sem "certo/errado"
4. Calcule pontuação conforme instruções
5. Identifique top 3 dons
6. Leia descrição dos dons identificados
7. Reflita: faz sentido? Já usa?
8. Discuta como usar os dons no ministério
9. Ore por capacitação''',
            'tempo_estimado': '40-60 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': '1 Coríntios 12:7 - "A cada um é dada a manifestação do Espírito."'
        },
        {
            'numero': 30,
            'titulo': 'Deserto Simbólico',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Tempo individual a sós com Deus em lugar isolado.',
            'objetivo': 'Experimentar solidão proposital para ouvir a voz de Deus claramente.',
            'materiais': '- Bíblia para cada um\n- Diário\n- Canetas\n- Lugar amplo (campo, bosque)',
            'passo_a_passo': '''1. Explique conceito de "deserto" bíblico
2. Estabeleça limites geográficos seguros
3. Cada pessoa vai para lugar isolado
4. Levam apenas: Bíblia, diário, água
5. Tempo: 1-2 horas
6. Sem celular/música
7. Atividades: ler, orar, escrever, silenciar
8. Horário para retornar (use apito)
9. Compartilhe experiências depois''',
            'tempo_estimado': '90-150 minutos',
            'quantidade_participantes': '5-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'Marcos 1:35 - "De madrugada... foi para um lugar deserto e ali orava."'
        },
        {
            'numero': 31,
            'titulo': 'Meu Chamado em Uma Frase',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Sintetizar propósito de vida em uma frase clara e memorável.',
            'objetivo': 'Clarificar propósito e missão pessoal diante de Deus.',
            'materiais': '- Papéis\n- Canetas\n- Exemplos de declarações de chamado',
            'passo_a_passo': '''1. Explique conceito de "chamado" vs "trabalho"
2. Mostre exemplos (ex: "Sou chamado para trazer esperança aos quebrantados")
3. Dê perguntas guia: "Pelo que sou apaixonado?", "Onde vejo necessidade?"
4. Tempo de reflexão: 20 minutos
5. Escreva frase de chamado
6. Deve ser: clara, memorável, acionável
7. Compartilhe em duplas
8. Receba feedback e refine
9. Ore sobre os chamados compartilhados''',
            'tempo_estimado': '40-50 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 32,
            'titulo': 'Mural de Gratidão',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Criar mural coletivo com motivos de gratidão de cada participante.',
            'objetivo': 'Cultivar coração grato e celebrar bondade de Deus coletivamente.',
            'materiais': '- Mural grande (papel pardo ou parede)\n- Post-its coloridos\n- Canetas\n- Fita adesiva',
            'passo_a_passo': '''1. Monte mural em lugar visível
2. Título: "Somos Gratos Por..."
3. Cada pessoa escreve 3-5 motivos de gratidão
4. Podem ser gerais ou específicos do retiro
5. Colam no mural
6. Ao longo do evento, podem adicionar mais
7. Em momentos livres, leia o mural
8. Finalize com oração de gratidão coletiva''',
            'tempo_estimado': '20-30 minutos (inicial) + contínuo',
            'quantidade_participantes': '10-100 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': '1 Tessalonicenses 5:18 - "Deem graças em todas as circunstâncias."'
        },
        {
            'numero': 33,
            'titulo': 'Quem Eu Era, Quem Sou, Quem Quero Ser',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Linha do tempo pessoal dividida em três fases de identidade.',
            'objetivo': 'Reconhecer transformação passada e projetar crescimento futuro.',
            'materiais': '- Papel dividido em 3 colunas\n- Canetas coloridas\n- Espelho (opcional)',
            'passo_a_passo': '''1. Divida papel em 3 colunas
2. Coluna 1: "Quem eu era" (antes de Cristo ou há anos)
3. Coluna 2: "Quem eu sou" (hoje, presente)
4. Coluna 3: "Quem quero ser" (futuro em Deus)
5. Escreva características, valores, comportamentos
6. Compare as colunas
7. Identifique progressos e áreas para crescer
8. Compartilhe em trios
9. Ore pelo "quero ser" de cada um''',
            'tempo_estimado': '35-45 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 34,
            'titulo': 'Quebra de Rótulos',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Identificar rótulos negativos e simbolicamente destruí-los.',
            'objetivo': 'Libertar de identidades falsas impostas por outros ou por si mesmo.',
            'materiais': '- Etiquetas adesivas\n- Canetas\n- Lixeira ou lugar para queimar (com segurança)',
            'passo_a_passo': '''1. Explique como rótulos nos limitam
2. Cada pessoa escreve rótulos que recebeu (fracasso, burro, feio, incapaz)
3. Cole as etiquetas em si mesmo
4. Sinta o peso desses rótulos
5. Leia versículos sobre nova identidade
6. Um por um, tire as etiquetas
7. Rasgue ou queime simbolicamente
8. Declare: "Não sou isso, sou filho(a) de Deus"
9. Ore por liberta libertação''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
            'versiculo_base': 'João 8:36 - "Se o Filho os libertar, vocês serão de fato livres."'
        },
        {
            'numero': 35,
            'titulo': 'Meu Maior Medo Entregue a Deus',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Identificar e confessar maior medo, depois entregá-lo simbolicamente.',
            'objetivo': 'Confrontar medos e aprender a confiar plenamente em Deus.',
            'materiais': '- Papéis\n- Canetas\n- Caixa ou altar\n- Velas (opcional)',
            'passo_a_passo': '''1. Momento de vulnerabilidade e seriedade
2. Cada pessoa identifica seu maior medo
3. Escreva anonimamente (ou não) no papel
4. Dobre o papel
5. Traga à frente e coloque em caixa/altar
6. Pode ser acompanhado de oração silenciosa
7. Líder ora sobre todos os medos entregues
8. Opção: queimar os papéis com segurança
9. Declare: "Deus cuida de mim"''',
            'tempo_estimado': '25-35 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': '2 Timóteo 1:7 - "Deus não nos deu espírito de covardia, mas de poder."'
        },
        {
            'numero': 36,
            'titulo': 'Linha do Perdão',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Mapear pessoa que precisa perdoar ou de quem precisa de perdão.',
            'objetivo': 'Identificar pendências de perdão e iniciar processo de reconciliação.',
            'materiais': '- Papel longo\n- Canetas\n- Envelopes (opcional)',
            'passo_a_passo': '''1. Ambiente de seriedade e privacidade
2. Desenhe linha horizontal
3. Lado esquerdo: pessoas que preciso perdoar
4. Lado direito: pessoas de quem preciso perdão
5. Marque na linha conforme intensidade
6. Não precisa mostrar para ninguém
7. Ore sobre cada situação
8. Identifique primeira ação prática
9. Líder disponível para conversa particular''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'Mateus 6:14 - "Se perdoarem as ofensas uns dos outros, o Pai celestial também os perdoará."'
        },
        {
            'numero': 37,
            'titulo': 'Oração Escrita Anônima',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Escrever oração pessoal que será orada por outra pessoa anônima.',
            'objetivo': 'Expressar necessidades em oração e experimentar intercessão anônima.',
            'materiais': '- Papéis bonitos\n- Canetas\n- Caixa para sorteio',
            'passo_a_passo': '''1. Cada pessoa escreve uma oração pessoal
2. Pode incluir pedidos, confissões, gratidão
3. Não assine, mantenha anônimo
4. Dobre e coloque na caixa
5. Cada um sorteia uma oração (não a própria)
6. Leva para casa
7. Compromisso: orar por aquela pessoa 1 semana
8. Não tentará descobrir quem é''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 38,
            'titulo': 'Símbolo da Transformação',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Criar dois desenhos: antes e depois de conhecer Cristo.',
            'objetivo': 'Visualizar e celebrar transformação operada por Deus.',
            'materiais': '- Papel dividido ao meio\n- Lápis de cor\n- Canetas',
            'passo_a_passo': '''1. Divida papel: lado esquerdo e direito
2. Esquerdo: "Antes" - como era sem Deus
3. Direito: "Depois" - como é em Cristo
4. Pode ser abstrato, simbólico ou literal
5. Use cores que representem sentimentos
6. Tempo para criação: 15 minutos
7. Compartilhe em duplas
8. Opcional: fazer galeria de transformações
9. Agradeça a Deus pela obra em cada vida''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 39,
            'titulo': 'Mapa dos Sonhos com Deus',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Criar mapa visual de sonhos e planos alinhados com propósito de Deus.',
            'objetivo': 'Sonhar junto com Deus e planejar passos práticos.',
            'materiais': '- Cartolina ou papel grande\n- Revistas para recorte\n- Cola\n- Canetas coloridas\n- Fotos pessoais (opcional)',
            'passo_a_passo': '''1. Ore pedindo que Deus revele sonhos
2. Divida cartolina em áreas: família, ministério, carreira, pessoal
3. Recorte imagens que representem sonhos
4. Cole criando collage visual
5. Escreva metas específicas
6. Inclua versículos relacionados
7. Compartilhe em pequenos grupos
8. Ore uns pelos outros
9. Tire foto para levar''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-25 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
            'versiculo_base': 'Jeremias 29:11 - "Planos para prosperá-los e não para causar dano."'
        },
        {
            'numero': 40,
            'titulo': 'Caixinha de Confissões',
            'categoria': Categoria.AUTOCONHECIMENTO,
            'descricao': 'Caixa anônima para confessar lutas, pecados ou dores sem exposição.',
            'objetivo': 'Permitir confissão segura e oração coletiva sem quebrar privacidade.',
            'materiais': '- Caixa lacrada com abertura\n- Papéis pequenos\n- Canetas\n- Local privado',
            'passo_a_passo': '''1. Coloque caixa em local discreto
2. Explique: totalmente anônimo
3. Ao longo do retiro, podem escrever confissões
4. Exemplos: lutas, pecados, medos, dores
5. Não assinem
6. Em momento específico, líder lê (sem julgamento)
7. Grupo ora coletivamente sobre cada área
8. Não tente identificar autores
9. Queime os papéis ao final''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
            'versiculo_base': 'Tiago 5:16 - "Confessem os seus pecados uns aos outros e orem."'
        },

        # DINÂMICAS DE TRABALHO EM EQUIPE (41-60)
        {
            'numero': 41,
            'titulo': 'Construção de Ponte com Papel',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Equipes competem para construir ponte de papel que aguente peso.',
            'objetivo': 'Desenvolver colaboração, planejamento e execução em equipe.',
            'materiais': '- Jornais ou papelão\n- Fita adesiva\n- Tesoura\n- Pesos para testar (livros)',
            'passo_a_passo': '''1. Divida em equipes de 5-7 pessoas
2. Objetivo: ponte que atravesse 50cm e aguente peso
3. Material limitado: 10 folhas de jornal e fita
4. Tempo: 20 minutos para planejar e construir
5. Não pode colar nas extremidades (livre)
6. Teste com pesos progressivos
7. Equipe cuja ponte aguentar mais peso vence
8. Discuta estratégias e trabalho em equipe''',
            'tempo_estimado': '40-50 minutos',
            'quantidade_participantes': '15-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 42,
            'titulo': 'Desafio do Marshmallow e Espaguete',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Construir torre mais alta usando espaguete, fita e marshmallow no topo.',
            'objetivo': 'Estimular criatividade, prototipagem rápida e trabalho colaborativo.',
            'materiais': '- 20 espaguetes por equipe\n- 1 metro de fita adesiva\n- 1 metro de barbante\n- 1 marshmallow',
            'passo_a_passo': '''1. Divida em equipes de 4-5 pessoas
2. Cada equipe recebe materiais iguais
3. Objetivo: torre mais alta com marshmallow no topo
4. Tempo: 18 minutos exatos
5. Torre deve ficar em pé sozinha
6. Marshmallow não pode ser cortado
7. Meça as torres ao final
8. Discuta: planejamento vs execução''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '12-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 43,
            'titulo': 'Missão Impossível em Tempo Limitado',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Série de desafios cronometrados que exigem cooperação total.',
            'objetivo': 'Trabalhar sob pressão mantendo comunicação e foco em objetivo comum.',
            'materiais': '- Lista de desafios preparada\n- Materiais diversos\n- Cronômetro\n- Apito',
            'passo_a_passo': '''1. Prepare 5-7 desafios variados
2. Exemplos: transportar água, montar quebra-cabeça, memorizar versículo
3. Cada desafio tem tempo limite curto
4. Equipe toda deve participar
5. Se falhar, reinicia ou penalidade de tempo
6. Registre tempo total
7. Equipe mais rápida vence
8. Discuta comunicação sob pressão''',
            'tempo_estimado': '40-60 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 44,
            'titulo': 'Torre Humana Sem Falar',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Construir formação específica em silêncio total, apenas com gestos.',
            'objetivo': 'Desenvolver comunicação não-verbal e coordenação em grupo.',
            'materiais': '- Imagem da formação alvo\n- Espaço amplo\n- Cronômetro',
            'passo_a_passo': '''1. Mostre imagem de formação/estrutura humana
2. Pode ser: pirâmide, forma geométrica, imagem bíblica
3. Equipe tem 10 minutos para replicar
4. Regra: SILÊNCIO TOTAL
5. Apenas gestos e linguagem corporal
6. Se alguém falar, voltam ao início
7. Líder observa e avalia precisão
8. Discuta importância da comunicação não-verbal''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '10-25 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 45,
            'titulo': 'Caminhada Vendado com Guia',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Metade vendada é guiada pela outra metade através de percurso.',
            'objetivo': 'Desenvolver confiança mútua e praticar liderança servidora.',
            'materiais': '- Vendas para metade do grupo\n- Obstáculos seguros\n- Espaço amplo',
            'passo_a_passo': '''1. Forme duplas
2. Um vendado, outro guia
3. Monte percurso com obstáculos leves
4. Guia apenas com palavras (sem tocar)
5. Vendado deve confiar completamente
6. Após percurso, invertem papéis
7. Variação: guia também vendado, mas conhece caminho
8. Discuta: confiança, direção, ouvir instruções''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Provérbios 3:5-6 - "Confie no Senhor... e ele endireitará suas veredas."'
        },
        {
            'numero': 46,
            'titulo': 'Quebra-Cabeça Cooperativo Gigante',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Montar quebra-cabeça grande onde cada equipe tem apenas algumas peças.',
            'objetivo': 'Perceber interdependência e necessidade de compartilhar recursos.',
            'materiais': '- Quebra-cabeça grande (500+ peças)\n- Mesas\n- Sacos para separar peças',
            'passo_a_passo': '''1. Divida peças do quebra-cabeça entre equipes
2. Nenhuma equipe tem todas peças necessárias
3. Devem perceber que precisam cooperar
4. Podem negociar, trocar, pedir emprestado
5. Objetivo: completar quebra-cabeça juntos
6. Tempo limite: 40 minutos
7. Observe dinâmicas de cooperação/competição
8. Relacione com corpo de Cristo (1 Co 12)''',
            'tempo_estimado': '50-60 minutos',
            'quantidade_participantes': '15-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 47,
            'titulo': 'Queda Controlada (Confiança)',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Pessoa se deixa cair de costas confiando que grupo a segurará.',
            'objetivo': 'Exercitar confiança extrema e responsabilidade coletiva.',
            'materiais': '- Espaço amplo e seguro\n- Superfície macia (grama ou tapete grosso)\n- Adultos fortes presentes',
            'passo_a_passo': '''1. SEGURANÇA É PRIORIDADE
2. Forme duas filas face a face, braços entrelaçados
3. Pessoa sobe em base baixa segura (30-50cm)
4. Cruza braços no peito
5. Pergunta: "Equipe pronta?"
6. Grupo responde: "Pronta!"
7. Deixa-se cair de costas rígido
8. Grupo segura com segurança
9. Todos participam sendo segurados
10. Discuta confiança e responsabilidade''',
            'tempo_estimado': '25-35 minutos',
            'quantidade_participantes': '10-20 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 48,
            'titulo': 'Resgate Simbólico',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Equipe deve "resgatar" objeto ou pessoa usando criatividade e materiais limitados.',
            'objetivo': 'Resolver problemas em equipe usando recursos escassos.',
            'materiais': '- Objeto para resgatar\n- Cordas\n- Materiais variados\n- Zona delimitada',
            'passo_a_passo': '''1. Coloque objeto em área "proibida"
2. Ninguém pode pisar na zona
3. Materiais: cordas, cabos, barbantes
4. Equipe deve recuperar objeto
5. Se alguém pisar, reinicia
6. Tempo limite: 20 minutos
7. Devem planejar antes de executar
8. Relacione com resgatar os perdidos''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '8-20 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 49,
            'titulo': 'Planejar Evento Evangelístico Juntos',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Grupos planejam evento evangelístico real para a igreja.',
            'objetivo': 'Aplicar dons diversos em planejamento estratégico de missão.',
            'materiais': '- Papel flip chart\n- Canetas\n- Orçamento fictício\n- Modelos de eventos',
            'passo_a_passo': '''1. Divida em equipes de 6-8 pessoas
2. Desafio: planejar evento evangelístico
3. Devem definir: público, tema, logística, orçamento, estratégia
4. Tempo: 40 minutos
5. Cada equipe apresenta (10 min)
6. Grupo avalia viabilidade
7. Melhor plano pode ser executado realmente
8. Discuta importância de planejamento na obra''',
            'tempo_estimado': '80-90 minutos',
            'quantidade_participantes': '12-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 50,
            'titulo': 'Ilustrar Versículo em Equipe',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Criar representação visual ou teatral de versículo sorteado.',
            'objetivo': 'Combinar criatividade e conhecimento bíblico em colaboração.',
            'materiais': '- Versículos impressos\n- Materiais artísticos\n- Roupas para caracterização\n- Espaço para apresentação',
            'passo_a_passo': '''1. Cada equipe sorteia um versículo
2. Devem criar apresentação: teatro, dança, mímica ou visual
3. Tempo para preparar: 20 minutos
4. Apresentações de 3-5 minutos cada
5. Grupo tenta adivinhar versículo
6. Todos devem ter papel na apresentação
7. Criatividade e trabalho em equipe contam pontos
8. Reflita sobre o significado dos versículos''',
            'tempo_estimado': '60-75 minutos',
            'quantidade_participantes': '15-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 51,
            'titulo': 'Teatro Improvisado Bíblico',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Improvisar dramatização de história bíblica em 10 minutos.',
            'objetivo': 'Desenvolver criatividade, trabalho sob pressão e conhecimento bíblico.',
            'materiais': '- Lista de histórias bíblicas\n- Adereços simples\n- Espaço para apresentação',
            'passo_a_passo': '''1. Equipes sorteiam história bíblica
2. Exemplos: Davi e Golias, Zaqueu, multiplicação dos pães
3. Tempo de preparação: 10 minutos apenas
4. Distribuir papéis rapidamente
5. Pode ser cômico (respeitoso)
6. Apresentação: 5 minutos
7. Grupo avalia criatividade e fidelidade bíblica
8. Todos se divertem e aprendem''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '12-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 52,
            'titulo': 'Corrida Cooperativa de Revezamento',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Corrida onde todos os membros devem participar em sequência.',
            'objetivo': 'Promover inclusão e celebrar que todos contribuem para vitória.',
            'materiais': '- Cones ou marcadores\n- Espaço amplo\n- Cronômetro\n- Bastão de revezamento (opcional)',
            'passo_a_passo': '''1. Monte percurso de revezamento
2. Equipes de tamanhos iguais
3. Todos devem correr uma etapa
4. Revezamento tradicional com bastão
5. Varia distância conforme habilidade
6. Tempo total da equipe é o que conta
7. Incentive torcida entre membros
8. Celebre equipe completa, não só rápidos''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '16-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 53,
            'titulo': 'Missão Evangelística Prática',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Sair do retiro para evangelizar em duplas na comunidade.',
            'objetivo': 'Aplicar ensinos em missão real, praticando evangelismo.',
            'materiais': '- Tratados evangelísticos\n- Garrafas de água para distribuir\n- Identificação da igreja\n- Transporte se necessário',
            'passo_a_passo': '''1. Prepare duplas estratégicas
2. Treinamento breve de abordagem
3. Distribuir materiais evangelísticos
4. Definir área segura de atuação
5. Tempo: 60-90 minutos
6. Cada dupla define estratégia
7. Podem: orar por pessoas, distribuir material, compartilhar testemunho
8. Retornam e compartilham experiências
9. Ore pelas pessoas contatadas''',
            'tempo_estimado': '120-150 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
            'versiculo_base': 'Marcos 16:15 - "Vão pelo mundo todo e preguem o evangelho."'
        },
        {
            'numero': 54,
            'titulo': 'Caça ao Tesouro Bíblica',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Resolver enigmas bíblicos para encontrar pistas e chegar ao tesouro.',
            'objetivo': 'Combinar conhecimento bíblico, trabalho em equipe e diversão.',
            'materiais': '- Enigmas preparados\n- Pistas escondidas\n- Bíblias\n- Tesouro final (prêmio simbólico)',
            'passo_a_passo': '''1. Prepare 7-10 pistas com enigmas bíblicos
2. Cada pista leva à próxima
3. Equipes começam em locais diferentes
4. Devem resolver enigma para saber onde ir
5. Exemplo: "Onde Jesus foi batizado?" -> Procurar pista no rio/lago
6. Equipe que encontrar tesouro primeiro vence
7. Todas equipes devem completar
8. Tesouuro pode ser versículo especial ou lembrança''',
            'tempo_estimado': '60-90 minutos',
            'quantidade_participantes': '15-50 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 55,
            'titulo': 'Decisão em Situação de Crise',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Grupo decide coletivamente como agir em cenários éticos complexos.',
            'objetivo': 'Exercitar tomada de decisão ética baseada em princípios bíblicos.',
            'materiais': '- Cenários preparados\n- Papel para anotar\n- Bíblias para consulta',
            'passo_a_passo': '''1. Apresente cenário ético complexo
2. Exemplos: "Esconder judeus na 2ª Guerra?", "Mentir para proteger?"
3. Grupo tem 15 minutos para decidir
4. Devem consultar Bíblia e princípios
5. Chegarem a consenso
6. Apresentam decisão e justificativa
7. Líder facilita discussão
8. Não há resposta única correta
9. Avalie processo de decisão ética''',
            'tempo_estimado': '40-60 minutos',
            'quantidade_participantes': '8-25 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 56,
            'titulo': 'Júri Simulado Bíblico',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Simular julgamento de personagem bíblico polêmico.',
            'objetivo': 'Desenvolver argumentação, trabalho em equipe e análise bíblica profunda.',
            'materiais': '- Caso preparado\n- Bíblias\n- Papéis: juiz, promotoria, defesa, júri\n- Toga improvisada (opcional)',
            'passo_a_passo': '''1. Escolha personagem: Jonas, Pedro, Judas, Pilatos
2. Divida papéis: promotoria (acusa), defesa, júri
3. Tempo para preparar: 20 minutos
4. Apresentação de argumentos: 10 min cada lado
5. Júri delibera
6. Veredicto final
7. Discuta complexidade moral
8. Relacione com graça e justiça de Deus''',
            'tempo_estimado': '60-90 minutos',
            'quantidade_participantes': '15-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 57,
            'titulo': 'Projetar Igreja Ideal Juntos',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Desenhar características da igreja ideal em aspectos variados.',
            'objetivo': 'Visionar igreja dos sonhos baseada em princípios bíblicos.',
            'materiais': '- Papel flip chart\n- Canetas coloridas\n- Bíblias\n- Exemplos de igrejas',
            'passo_a_passo': '''1. Divida em aspectos: adoração, ensino, comunhão, missão, serviço
2. Cada grupo desenha um aspecto
3. Deve ser bíblico e prático
4. Tempo: 30 minutos
5. Apresentações: 5 min cada
6. Monte painel com visão completa
7. Identifique pontos em comum
8. Discuta: como chegar lá?
9. Compromissos práticos''',
            'tempo_estimado': '70-90 minutos',
            'quantidade_participantes': '15-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 58,
            'titulo': 'Debate Estruturado de Tema Relevante',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Debater tema atual sob perspectiva bíblica em formato estruturado.',
            'objetivo': 'Desenvolver pensamento crítico e defesa da fé com amor.',
            'materiais': '- Tema polêmico definido\n- Regras de debate\n- Cronômetro\n- Moderador',
            'passo_a_passo': '''1. Escolha tema: redes sociais, política, namoro, dinheiro
2. Forme dois grupos: diferentes perspectivas bíblicas
3. Tempo de preparação: 20 minutos
4. Debate: 3 rodadas de 5 minutos
5. Argumentos baseados na Bíblia
6. Respeito obrigatório
7. Plateia faz perguntas
8. Não precisa "vencer", mas entender
9. Sintetize pontos em comum''',
            'tempo_estimado': '50-70 minutos',
            'quantidade_participantes': '15-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 59,
            'titulo': 'Desafio do Labirinto Humano',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Grupo forma labirinto vivo que outro grupo deve atravessar.',
            'objetivo': 'Cooperar para criar e resolver desafio conjunto.',
            'materiais': '- Espaço amplo\n- Fita adesiva ou cordas (opcional)\n- Cronômetro',
            'passo_a_passo': '''1. Metade do grupo forma labirinto humano
2. Ficam parados em formações variadas
3. Outra metade deve atravessar
4. Regras: não pode tocar, deve seguir caminho
5. Podem dar dicas verbais
6. Cronometrar tempo
7. Inverter papéis
8. Discuta comunicação e estratégia''',
            'tempo_estimado': '25-35 minutos',
            'quantidade_participantes': '16-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 60,
            'titulo': 'Projeto Solidário Real Planejado em Equipe',
            'categoria': Categoria.TRABALHO_EQUIPE,
            'descricao': 'Planejar e executar ação social real durante ou após o retiro.',
            'objetivo': 'Transformar reflexão em ação concreta servindo comunidade.',
            'materiais': '- Depende do projeto\n- Materiais de planejamento\n- Possível arrecadação\n- Transporte',
            'passo_a_passo': '''1. Identifique necessidade na comunidade
2. Exemplos: visitar asilo, limpeza de praça, distribuir alimentos
3. Planeje: o que, quando, quem, como
4. Divida tarefas conforme dons
5. Arrecade recursos necessários
6. Execute projeto juntos
7. Documente com fotos
8. Compartilhe testemunhos depois
9. Estabeleça continuidade''',
            'tempo_estimado': '120-240 minutos (total)',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Tiago 2:17 - "A fé, por si só, se não for acompanhada de obras, está morta."'
        },

        # DINÂMICAS ESPIRITUAIS (61-80)
        {
            'numero': 61,
            'titulo': 'Lectio Divina Guiada em Grupo',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Leitura meditativa da Bíblia em quatro etapas: ler, meditar, orar, contemplar.',
            'objetivo': 'Aprofundar relacionamento com Deus através de leitura orante da Escritura.',
            'materiais': '- Bíblias\n- Texto selecionado impresso\n- Ambiente tranquilo\n- Música instrumental suave',
            'passo_a_passo': '''1. Escolha texto bíblico (Salmo ou Evangelho)
2. Lectio (leitura): Leia em voz alta 2x, lentamente
3. Meditatio (meditação): Silêncio 5 min, reflita
4. Oratio (oração): Responda a Deus em oração
5. Contemplatio (contemplação): Descanse em Deus, silêncio
6. Compartilhe o que Deus falou (opcional)
7. Total: 30-40 minutos
8. Encerre com gratidão''',
            'tempo_estimado': '40-50 minutos',
            'quantidade_participantes': '5-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'Salmos 119:105 - "Lâmpada para os meus pés é a tua palavra."'
        },
        {
            'numero': 62,
            'titulo': 'Caminhada de Oração ao Ar Livre',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Caminhada em silêncio pela natureza intercalada com estações de oração.',
            'objetivo': 'Conectar com Deus através da criação e momentos de oração direcionada.',
            'materiais': '- Rota planejada\n- Estações marcadas\n- Cartões com temas de oração\n- Bíblias',
            'passo_a_passo': '''1. Planeje rota de 1-2 km com 5-7 estações
2. Cada estação tem tema: gratidão, confissão, intercessão, etc
3. Inicie com oração
4. Caminham em silêncio até estação 1
5. Líder lê tema e versículo
6. 5 minutos de oração individual
7. Prosseguem para próxima estação
8. Finalize com partilha e oração coletiva''',
            'tempo_estimado': '60-90 minutos',
            'quantidade_participantes': '5-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 63,
            'titulo': 'Lava-Pés Simbólico Mútuo',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Reencenar João 13, lavando pés uns dos outros em ambiente de adoração.',
            'objetivo': 'Praticar humildade, servir mutuamente e experimentar amor de Cristo.',
            'materiais': '- Bacias\n- Água morna\n- Toalhas\n- Cadeiras\n- Música de adoração suave',
            'passo_a_passo': '''1. Leia João 13:1-17
2. Explique significado de lavar pés
3. Música de adoração ambiente
4. Duplas ou trios se formam
5. Um lava os pés do outro com reverência
6. Pode orar enquanto lava
7. Pessoa pode compartilhar benção após
8. Invertem papéis
9. Momento poderoso de quebrantamento
10. Finalize com adoração e comunhão''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'João 13:14 - "Pois se eu... lavei os vossos pés, também vós deveis lavar os pés uns dos outros."'
        },
        {
            'numero': 64,
            'titulo': 'Cruz com Pedidos de Oração',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Grande cruz onde participantes pregam papéis com pedidos de oração.',
            'objetivo': 'Entregar cargas a Deus simbolicamente e orar uns pelos outros.',
            'materiais': '- Cruz grande de madeira\n- Papéis pequenos\n- Canetas\n- Pregos ou alfinetes\n- Músic de adoração',
            'passo_a_passo': '''1. Monte cruz grande em local central
2. Explique simbologia de levar à cruz
3. Cada pessoa escreve pedido/carga
4. Podem assinar ou não
5. Vão à frente individualmente
6. Pregam papel na cruz com reverência
7. Momento de oração pessoal ali
8. Líder ora por todos os pedidos
9. Cruz fica exposta durante retiro''',
            'tempo_estimado': '30-45 minutos',
            'quantidade_participantes': '10-100 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 65,
            'titulo': 'Pedra Simbolizando Pecado Levada à Cruz',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Cada pessoa pega pedra pesada representando pecado e a deixa aos pés da cruz.',
            'objetivo': 'Simbolizar entrega de pecados e experienciar perdão e libertação.',
            'materiais': '- Pedras de tamanho médio\n- Cruz grande\n- Cesta ou monte aos pés da cruz\n- Música instrumental',
            'passo_a_passo': '''1. Cada pessoa recebe uma pedra
2. Momento de reflexão e confissão silenciosa
3. Pedra representa peso do pecado
4. Música suave de adoração
5. Um por um, caminham à cruz
6. Deixam pedra aos pés (entrega simbólica)
7. Retornam livres
8. Líder proclama perdão (1 Jo 1:9)
9. Celebração da liberdade em Cristo''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-60 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
            'versiculo_base': '1 João 1:9 - "Se confessarmos os nossos pecados... nos purificará de toda injustiça."'
        },
        {
            'numero': 66,
            'titulo': 'Oração em Duplas Profunda',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Duplas oram uma pela outra após compartilhar necessidades reais.',
            'objetivo': 'Praticar intercessão, vulnerabilidade e ministério mútuo.',
            'materiais': '- Espaço tranquilo\n- Músicas suave de fundo\n- Lenços (caso haja lágrimas)',
            'passo_a_passo': '''1. Forme duplas aleatórias (ou estratégicas)
2. Explique importância de confidencialidade
3. Cada pessoa compartilha necessidade real (5 min)
4. Outra ouve sem interromper
5. Depois, ora especificamente por aquela necessidade (5 min)
6. Invertem
7. Podem se ajoelhar, impor mãos
8. Momento íntimo e poderoso
9. Opcional: manter contato depois para acompanhar''',
            'tempo_estimado': '25-35 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 67,
            'titulo': 'Intercessão com Nomes Sorteados',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Cada pessoa sorteia nome de outro participante e intercede por ele durante o retiro.',
            'objetivo': 'Praticar intercessão secreta e servir em amor sem reconhecimento.',
            'materiais': '- Papéis com nomes\n- Caixa para sorteio\n- Cartões com ideias de oração',
            'passo_a_passo': '''1. Coloque nome de todos em papéis
2. Cada um sorteia um (se pegar o próprio, sorteia novamente)
3. Durante todo o retiro, intercede por aquela pessoa
4. Observe discretamente necessidades
5. Ore em momentos livres
6. Não revele que está orando
7. Ao final do retiro, revele e compartilhe
8. Pessoa descobre quem orou por ela''',
            'tempo_estimado': 'Contínuo durante retiro',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 68,
            'titulo': 'Jejum Reflexivo em Grupo',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Período de jejum coletivo com momentos de oração e ensino.',
            'objetivo': 'Buscar a Deus intensamente através de jejum e oração.',
            'materiais': '- Planejamento de horários\n- Água disponível\n- Local de oração\n- Ensino sobre jejum',
            'passo_a_passo': '''1. Ensine sobre jejum bíblico antes
2. Defina período: 12h, 24h ou parcial
3. Orientações médicas para quem não pode
4. Substitua refeições por oração
5. Horários de oração coletiva
6. Disponibilize Bíblias e material devocional
7. Líderes em oração disponíveis
8. Quebre jejum juntos com gratidão
9. Compartilhe experiências''',
            'tempo_estimado': '12-24 horas',
            'quantidade_participantes': '5-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'Mateus 6:16-18 - Ensino de Jesus sobre jejum'
        },
        {
            'numero': 69,
            'titulo': 'Silêncio Total de 30 Minutos',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Período de silêncio absoluto para ouvir a voz de Deus.',
            'objetivo': 'Aquietar alma e mente para ouvir Deus falar no silêncio.',
            'materiais': '- Local tranquilo\n- Versículo guia impresso\n- Cronômetro\n- Música suave opcional',
            'passo_a_passo': '''1. Explique o propósito do silêncio
2. Leia Salmo 46:10 - "Aquietai-vos e sabei..."
3. Regras: silêncio total, sem celular
4. Podem ficar sentados, ajoelhados ou caminhar
5. Simplesmente estar com Deus
6. Líder sinaliza início e fim
7. Após, opcional compartilhar o que Deus falou
8. Muitos terão revelações surpreendentes''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '5-100 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'Salmos 46:10 - "Aquietai-vos e sabei que eu sou Deus."'
        },
        {
            'numero': 70,
            'titulo': 'Exercício de Escuta: Deus Está Falando',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Prática de ouvir voz de Deus através de passos estruturados.',
            'objetivo': 'Ensinar a discernir e ouvir a voz de Deus pessoalmente.',
            'materiais': '- Bíblias\n- Diários\n- Canetas\n- Guia impresso de passos',
            'passo_a_passo': '''1. Ensine sobre como Deus fala (Bíblia, paz, circunstâncias, outros)
2. Momento de aquietamento (5 min)
3. Faça pergunta específica a Deus
4. Silêncio de escuta (15 min)
5. Anote impressões, versículos, pensamentos
6. Teste impressões pela Bíblia
7. Compartilhe com líder ou grupo
8. Pratique discernimento coletivo''',
            'tempo_estimado': '40-50 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 71,
            'titulo': 'Dramatização do Filho Pródigo',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Encenar Lucas 15 de forma profunda e emocional.',
            'objetivo': 'Experimentar amor do Pai e arrependimento genuíno através do teatro.',
            'materiais': '- Roteiro adaptado\n- Figurinos simples\n- Espaço para apresentação\n- Música de fundo',
            'passo_a_passo': '''1. Selecione atores: pai, filho pródigo, filho mais velho
2. Ensaie com antecedência ou improvise
3. Narre história lentamente
4. Enfatize momento da volta e abraço do pai
5. Congele cena do abraço
6. Convide pessoas que se identificam a virem
7. Experimentem abraço do Pai (líder abraça)
8. Momento de restauração e choro
9. Celebração pelo retorno''',
            'tempo_estimado': '40-60 minutos',
            'quantidade_participantes': '15-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Lucas 15:20 - "Seu pai o viu e... correu ao seu encontro, e o beijou."'
        },
        {
            'numero': 72,
            'titulo': 'Estações da Cruz (Via Sacra)',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Percorrer estações meditando sobre sofrimento de Cristo.',
            'objetivo': 'Aprofundar gratidão pelo sacrifício de Jesus através de meditação.',
            'materiais': '- 7-12 estações montadas\n- Textos bíblicos em cada\n- Imagens ou símbolos\n- Velas',
            'passo_a_passo': '''1. Monte estações: condenação, crucificação, morte, ressurreição
2. Cada estação tem: texto, imagem, reflexão
3. Participantes percorrem individualmente
4. Música suave de adoração
5. Param em cada estação (2-3 min)
6. Leem, meditam, oram
7. Prosseguem no seu ritmo
8. Estação final: cruz vazia e ressurreição
9. Momento de gratidão e adoração''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 73,
            'titulo': 'Clamor Coletivo',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Momento de oração intensa onde todos clamam a Deus simultaneamente.',
            'objetivo': 'Experimentar poder da oração coletiva fervorosa.',
            'materiais': '- Nenhum necessário\n- Espaço amplo\n- Opcional: instrumentos de percussão',
            'passo_a_passo': '''1. Contextualize: momentos bíblicos de clamor (Esdras, Neemias)
2. Defina foco: avivamento, cura, salvação de almas
3. Explique: todos orarão em voz alta simultaneamente
4. Pode durar 15-30 minutos
5. Intensidade natural vai variar
6. Podem se ajoelhar, ficar em pé, levantar mãos
7. Líder não dirige durante, apenas inicia e finaliza
8. Momento poderoso de mover do Espírito''',
            'tempo_estimado': '20-40 minutos',
            'quantidade_participantes': '15-200 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 74,
            'titulo': 'Roda de Testemunhos',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Círculo onde cada pessoa compartilha breve testemunho de fé.',
            'objetivo': 'Edificar uns aos outros através de testemunhos de fidelidade de Deus.',
            'materiais': '- Nenhum necessário\n- Lenços\n- Cronômetro (limite de tempo)',
            'passo_a_passo': '''1. Forme círculo sentado
2. Explique: testemunho breve (2-3 min)
3. Tema: "Como Deus tem me transformado" ou "Fidelidade de Deus"
4. Voluntários ou seguir ordem
5. Sem interrupções durante testemunho
6. Grupo pode responder "Amém", "Glória a Deus"
7. Continue até todos que desejarem compartilharem
8. Finalize com oração de gratidão''',
            'tempo_estimado': '40-90 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 75,
            'titulo': 'Mapa Missionário com Oração',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Orar por diferentes países e povos não alcançados.',
            'objetivo': 'Expandir visão missionária e interceder por nações.',
            'materiais': '- Mapa-múndi grande\n- Informações sobre povos não alcançados\n- Alfinetes ou adesivos\n- Velas',
            'passo_a_passo': '''1. Monte mapa-múndi em parede
2. Distribua informações sobre países/povos
3. Cada pessoa (ou grupo) escolhe uma nação
4. Pesquisa necessidades: perseguição, pobreza, sem evangelho
5. Apresenta ao grupo brevemente
6. Ora especificamente por aquela nação
7. Marca no mapa com alfinete
8. Continue até cobrir várias nações
9. Compromisso de continuar orando''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Mateus 28:19 - "Portanto, vão e façam discípulos de todas as nações."'
        },
        {
            'numero': 76,
            'titulo': 'Escrever Cartas a Personagens Bíblicos',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Escrever carta para personagem bíblico que inspira ou se identifica.',
            'objetivo': 'Conectar pessoalmente com histórias bíblicas e extrair lições.',
            'materiais': '- Papel bonito\n- Canetas\n- Envelopes\n- Bíblias para pesquisa',
            'passo_a_passo': '''1. Cada pessoa escolhe personagem bíblico
2. Pesquisa história dele na Bíblia
3. Escreve carta: agradecimento, perguntas, identificação
4. Pode expressar como história impactou
5. Tempo: 20 minutos
6. Voluntários leem cartas
7. Grupo identifica lições aplicáveis hoje
8. Guarde carta como memorial''',
            'tempo_estimado': '35-45 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 77,
            'titulo': 'Painel: O Que Deus Tem Feito',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Criar mural visual de milagres e respostas de oração recentes.',
            'objetivo': 'Celebrar fidelidade de Deus e fortalecer fé através de testemunhos visuais.',
            'materiais': '- Painel grande\n- Post-its coloridos\n- Canetas\n- Fotos (opcional)',
            'passo_a_passo': '''1. Monte painel com título: "O Que Deus Tem Feito"
2. Cada pessoa escreve resposta de oração recente
3. Pode ser: cura, provisão, salvação, livramento
4. Colar no painel
5. Ler alguns em voz alta
6. Celebrar com palmas e glória a Deus
7. Painel fica exposto
8. Tire foto ao final para compartilhar''',
            'tempo_estimado': '25-35 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 78,
            'titulo': 'Círculo de Gratidão Pública',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Cada pessoa agradece publicamente por algo específico.',
            'objetivo': 'Cultivar espírito de gratidão e edificar através de testemunhos.',
            'materiais': '- Nenhum necessário',
            'passo_a_passo': '''1. Forme círculo de pé
2. Leia Salmo 100
3. Cada pessoa completa: "Sou grato a Deus por..."
4. Deve ser específico e recente
5. Grupo responde: "Graças a Deus!"
6. Continue ao redor do círculo
7. Ninguém obrigado, mas encoraje todos
8. Finalize com oração de gratidão coletiva''',
            'tempo_estimado': '15-25 minutos',
            'quantidade_participantes': '8-40 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 79,
            'titulo': 'Criar Salmo Coletivo',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Grupo compõe salmo original de louvor ou lamento juntos.',
            'objetivo': 'Expressar adoração criativa e contextualizar experiência do retiro.',
            'materiais': '- Papel flip chart\n- Canetas\n- Bíblia (Salmos para inspiração)\n- Instrumentos musicais (opcional)',
            'passo_a_passo': '''1. Leia alguns Salmos como modelo
2. Defina tema: gratidão, louvor, lamento, confiança
3. Cada pessoa contribui com uma linha
4. Líder escreve e organiza
5. Pode ter refrão repetido
6. Revise e refine juntos
7. Recite/cante o salmo criado
8. Guarde como memorial do retiro''',
            'tempo_estimado': '40-60 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 80,
            'titulo': 'Ato Simbólico de Entrega Total',
            'categoria': Categoria.ESPIRITUAIS,
            'descricao': 'Cada pessoa entrega simbolicamente algo a Deus através de ação concreta.',
            'objetivo': 'Marcar momento de rendição e consagração através de símbolo tangível.',
            'materiais': '- Depende do símbolo escolhido\n- Altar ou local especial\n- Música de adoração',
            'passo_a_passo': '''1. Escolha símbolo: carta, objeto pessoal, lenço (lágrimas)
2. Explique significado de consagração
3. Tempo de reflexão: "O que Deus está pedindo?"
4. Música de adoração profunda
5. Um por um, vão à frente
6. Deixam símbolo no altar
7. Oração de entrega
8. Líder abençoa cada um
9. Momento transformador''',
            'tempo_estimado': '30-45 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Romanos 12:1 - "Ofereçam seus corpos como sacrifício vivo, santo e agradável a Deus."'
        },

        # DINÂMICAS DE DIVERSÃO E ENERGIA (81-100)
        {
            'numero': 81,
            'titulo': 'Gincana Bíblica por Equipes',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Competição divertida com provas variadas baseadas em conhecimento bíblico.',
            'objetivo': 'Revisar Bíblia de forma lúdica e energizar o grupo através de competição saudável.',
            'materiais': '- Provas preparadas\n- Bíblias\n- Materiais diversos\n- Placar\n- Prêmios simbólicos',
            'passo_a_passo': '''1. Divida em 3-4 equipes
2. Prepare 8-10 provas variadas
3. Exemplos: corrida de versículos, mímica bíblica, quiz rápido
4. Cada prova vale pontos
5. Equipes alternam ou simultâneo
6. Mantenha ritmo acelerado
7. Registre pontuação visível
8. Equipe vencedora recebe prêmio
9. Celebre todos os participantes''',
            'tempo_estimado': '60-90 minutos',
            'quantidade_participantes': '15-60 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 82,
            'titulo': 'Quiz Bíblico Relâmpago',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Perguntas rápidas de múltipla escolha sobre a Bíblia.',
            'objetivo': 'Testar e reforçar conhecimento bíblico de forma dinâmica.',
            'materiais': '- 50 perguntas preparadas\n- Sino ou buzina\n- Placar\n- Placas A-B-C-D (opcional)',
            'passo_a_passo': '''1. Prepare perguntas de dificuldades variadas
2. Leia pergunta e 4 alternativas
3. Equipes têm 10 segundos para responder
4. Levantam placa ou gritam resposta
5. Resposta correta: 1 ponto
6. Mantenha ritmo rápido e divertido
7. 30-40 perguntas no total
8. Equipe com mais pontos vence''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 83,
            'titulo': 'Caça ao Versículo',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Competição para encontrar versículos específicos rapidamente na Bíblia.',
            'objetivo': 'Familiarizar com estrutura da Bíblia de forma competitiva e divertida.',
            'materiais': '- Bíblias idênticas para todos\n- Lista de versículos\n- Sino\n- Prêmios',
            'passo_a_passo': '''1. Todos com Bíblia fechada
2. Líder anuncia referência (ex: João 3:16)
3. Ao sinal, procuram o mais rápido possível
4. Primeiro a encontrar levanta mão e lê em voz alta
5. Se correto: ponto
6. Varie dificuldade: livros conhecidos e obscuros
7. 15-20 rodadas
8. Jogador com mais pontos vence''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '8-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 84,
            'titulo': 'Stop Bíblico',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Jogo stop adaptado com categorias bíblicas.',
            'objetivo': 'Revisar conhecimento bíblico de forma criativa e competitiva.',
            'materiais': '- Folhas de categorias impressas\n- Canetas\n- Letras do alfabeto em papéis',
            'passo_a_passo': '''1. Categorias: personagem, livro da Bíblia, lugar, objeto, animal
2. Sorteie uma letra
3. Todos preenchem categorias com letra sorteada
4. Primeiro a completar grita "Stop!"
5. Todos param
6. Leem respostas
7. Pontuação: única=10, repetida=5, em branco=0
8. 8-10 rodadas
9. Maior pontuação vence''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '8-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 85,
            'titulo': 'Passa ou Repassa',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Jogo de perguntas onde equipes podem passar perguntas difíceis.',
            'objetivo': 'Testar conhecimento bíblico com estratégia e trabalho em equipe.',
            'materiais': '- Perguntas de dificuldades variadas\n- Placar\n- Buzinas ou sinos',
            'passo_a_passo': '''1. Duas equipes competem
2. Pergunta é feita para equipe A
3. Têm 20 segundos para responder
4. Se não souber, "passa" para equipe B
5. Se equipe B também não sabe, "repassa" para A
6. Se ninguém responde, pergunta vale dobro na próxima
7. Pontuação acumula
8. Primeira equipe a 10 pontos vence''',
            'tempo_estimado': '30-45 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 86,
            'titulo': 'Desafio Musical Cristão',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Competição envolvendo músicas gospel: completar letra, adivinhar, cantar.',
            'objetivo': 'Celebrar louvor e adoração de forma alegre e participativa.',
            'materiais': '- Músicas selecionadas\n- Aparelho de som\n- Microfone\n- Letras impressas',
            'passo_a_passo': '''1. Rodadas variadas:
   - Completar letra (música para e continuam cantando)
   - Adivinhar música pelos primeiros segundos
   - Karaokê em equipe
   - Mímica do título da música
2. Cada rodada vale pontos
3. Mantenha energia alta
4. Todos participam
5. Equipe vencedora lidera louvor ao final''',
            'tempo_estimado': '40-60 minutos',
            'quantidade_participantes': '15-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 87,
            'titulo': 'Teatro Mudo de Histórias Bíblicas',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Equipes representam histórias bíblicas apenas com mímica.',
            'objetivo': 'Revisar histórias bíblicas através de criatividade corporal.',
            'materiais': '- Lista de histórias bíblicas\n- Cronômetro\n- Placar',
            'passo_a_passo': '''1. Equipe sorteia história bíblica
2. Têm 2 minutos para planejar
3. Apresentam mímica (3 minutos máx)
4. Outras equipes tentam adivinhar
5. Primeira a acertar ganha ponto
6. Não pode falar ou fazer sons
7. Criatividade conta pontos extras
8. 5-7 rodadas''',
            'tempo_estimado': '40-50 minutos',
            'quantidade_participantes': '12-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 88,
            'titulo': 'Desafio do Copo',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Passar copo com água usando apenas a boca em corrente.',
            'objetivo': 'Gerar risadas, diversão e trabalho em equipe coordenado.',
            'materiais': '- Copos plásticos pequenos\n- Água\n- Toalhas\n- Balde',
            'passo_a_passo': '''1. Equipes em fila
2. Cada pessoa com copo na boca (sem mãos)
3. Primeiro enche copo com água
4. Passa para próximo boca a boca
5. Último despeja em balde
6. Voltam correndo e refazem
7. Tempo limite: 3 minutos
8. Equipe com mais água no balde vence
9. Prepare-se para muitas risadas!''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '12-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 89,
            'titulo': 'Dança Congelante',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Dançar livremente e congelar em pose quando música para.',
            'objetivo': 'Quebrar inibição, gerar alegria e movimento.',
            'materiais': '- Músicas animadas (gospel)\n- Aparelho de som\n- Espaço amplo',
            'passo_a_passo': '''1. Todos no centro dançando
2. Música gospel animada toca
3. Quando música para, CONGELAR imediatamente
4. Quem se mover está fora
5. Retorna música
6. Continue até sobrar 3 vencedores
7. Variação: congelar em pose específica (adoração, alegria)
8. Diversão garantida''',
            'tempo_estimado': '15-25 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 90,
            'titulo': 'Corrida de Versículos Decorados',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Competição para decorar e recitar versículos rapidamente.',
            'objetivo': 'Memorizar Escritura de forma divertida e competitiva.',
            'materiais': '- Versículos impressos\n- Cronômetro\n- Prêmios',
            'passo_a_passo': '''1. Escolha versículo médio (15-20 palavras)
2. Mostre por 1 minuto
3. Esconda o versículo
4. Equipes têm 3 minutos para memorizar juntos
5. Um representante recita de memória
6. Deve ser palavra por palavra
7. Equipe que recitar perfeitamente primeiro vence
8. Repita com 3-4 versículos diferentes''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '12-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 91,
            'titulo': 'Jogo da Memória Bíblica',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Jogo de memória gigante com personagens ou versículos bíblicos.',
            'objetivo': 'Exercitar memória enquanto revisa conteúdo bíblico.',
            'materiais': '- Cartões grandes (pares)\n- Personagens/versículos\n- Fita adesiva\n- Espaço para espalhar',
            'passo_a_passo': '''1. Prepare pares de cartões (20-30 pares)
2. Pode ser: personagem-descrição, versículo-referência
3. Espalhe virados para baixo
4. Equipes alternam
5. Viram 2 cartões tentando formar par
6. Se acertar, fica com par e joga novamente
7. Se errar, vira de volta e passa vez
8. Equipe com mais pares vence''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 92,
            'titulo': 'Pictionary Bíblico',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Desenhar conceitos bíblicos enquanto equipe adivinha.',
            'objetivo': 'Revisar Bíblia através de desenho e criatividade.',
            'materiais': '- Quadro branco ou flip chart\n- Canetas\n- Cartões com palavras\n- Cronômetro',
            'passo_a_passo': '''1. Prepare cartões: personagens, lugares, eventos, objetos bíblicos
2. Jogador sorteia cartão
3. Tem 1-2 minutos para desenhar
4. Não pode falar, escrever letras ou números
5. Equipe tenta adivinhar
6. Se acertar no tempo: ponto
7. Alterne entre equipes
8. 10-15 rodadas''',
            'tempo_estimado': '30-45 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 93,
            'titulo': 'Adivinhe o Personagem Bíblico',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Fazer perguntas sim/não para descobrir personagem bíblico.',
            'objetivo': 'Revisar características de personagens bíblicos jogando.',
            'materiais': '- Nomes de personagens escritos\n- Fita adesiva',
            'passo_a_passo': '''1. Cole nome de personagem bíblico nas costas
2. Pessoa não vê seu personagem
3. Circula perguntando aos outros: perguntas sim/não
4. "Sou do NT?" "Sou profeta?" "Sou mulher?"
5. Tenta descobrir quem é
6. Quando descobrir, pode ajudar outros
7. Continue até todos descobrirem
8. Discuta características dos personagens''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 94,
            'titulo': 'Mímica de Versículos',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Representar versículo inteiro através de mímica criativa.',
            'objetivo': 'Memorizar e interpretar versículos de forma corporal.',
            'materiais': '- Versículos selecionados\n- Cronômetro',
            'passo_a_passo': '''1. Equipe sorteia versículo
2. Têm 2 minutos para planejar
3. Apresentam mímica do versículo inteiro
4. Podem usar todos os membros
5. Outras equipes tentam adivinhar
6. Primeira a dizer versículo completo vence
7. Criatividade conta pontos extras
8. 5-7 rodadas''',
            'tempo_estimado': '35-45 minutos',
            'quantidade_participantes': '12-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 95,
            'titulo': 'Charadas Bíblicas',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Adivinhar resposta através de pistas criativas e enigmáticas.',
            'objetivo': 'Estimular raciocínio e conhecimento bíblico através de charadas.',
            'materiais': '- Charadas preparadas\n- Papel para respostas',
            'passo_a_passo': '''1. Prepare 15-20 charadas bíblicas
2. Exemplo: "Quem perdeu força com um corte de cabelo?" (Sansão)
3. Leia charada
4. Equipes escrevem resposta
5. Revelam simultaneamente
6. Resposta correta: ponto
7. Varie dificuldade
8. Equipe com mais pontos vence''',
            'tempo_estimado': '25-35 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 96,
            'titulo': 'Rodada de Perguntas Profundas Rápidas',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Perguntas reflexivas respondidas rapidamente em 30 segundos.',
            'objetivo': 'Conhecer valores e pensamentos uns dos outros de forma dinâmica.',
            'materiais': '- Lista de perguntas preparadas\n- Cronômetro',
            'passo_a_passo': '''1. Prepare perguntas interessantes
2. Exemplos: "Maior sonho?", "O que mudaria no mundo?", "Maior medo?"
3. Escolha pessoa aleatória
4. Tem 30 segundos para responder
5. Deve ser honesto e rápido
6. Grupo pode fazer uma pergunta follow-up
7. Próxima pessoa
8. 15-20 pessoas respondem''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 97,
            'titulo': 'Campeonato de Criatividade',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Desafios criativos com materiais limitados e tempo curto.',
            'objetivo': 'Estimular pensamento criativo e improvisação.',
            'materiais': '- Materiais diversos\n- Desafios preparados\n- Cronômetro',
            'passo_a_passo': '''1. Rodadas com desafios diferentes
2. Exemplos: criar instrumento, construir ponte, fazer poesia
3. Materiais limitados fornecidos
4. Tempo: 5-10 minutos por desafio
5. Apresentam criações
6. Grupo vota na mais criativa
7. Vencedor de cada rodada ganha ponto
8. 4-5 rodadas''',
            'tempo_estimado': '50-70 minutos',
            'quantidade_participantes': '12-40 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 98,
            'titulo': 'Improviso com Objetos Aleatórios',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Criar apresentação usando objetos sorteados aleatoriamente.',
            'objetivo': 'Desenvolver criatividade, improviso e gerar muitas risadas.',
            'materiais': '- Objetos diversos em sacola\n- Temas bíblicos',
            'passo_a_passo': '''1. Sacola com objetos aleatórios (guarda-chuva, panela, bola)
2. Equipe sorteia 3 objetos
3. Sorteia também tema bíblico
4. Devem criar apresentação usando os 3 objetos
5. Tempo para criar: 5 minutos
6. Apresentação: 2-3 minutos
7. Criatividade e humor bem-vindos
8. Grupo vota na melhor''',
            'tempo_estimado': '40-60 minutos',
            'quantidade_participantes': '12-30 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 99,
            'titulo': 'Quem Será o Líder Surpresa?',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Grupo imita movimentos de líder secreto enquanto um tenta descobrir quem é.',
            'objetivo': 'Desenvolver observação e gerar diversão através de imitação.',
            'materiais': '- Nenhum necessário',
            'passo_a_passo': '''1. Um voluntário sai da sala
2. Grupo escolhe líder secreto
3. Todos fazem movimentos que líder fizer
4. Voluntário volta e observa
5. Tem 3 tentativas para descobrir quem é o líder
6. Líder muda movimentos sutilmente
7. Se descobrir: líder sai na próxima rodada
8. Se não descobrir: mesma pessoa sai novamente
9. 5-7 rodadas''',
            'tempo_estimado': '20-30 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 100,
            'titulo': 'Se Eu Fosse...',
            'categoria': Categoria.DIVERSAO_ENERGIA,
            'descricao': 'Completar frases criativas sobre identidade e preferências.',
            'objetivo': 'Conhecer personalidades de forma lúdica e criativa.',
            'materiais': '- Lista de categorias\n- Papel e canetas (opcional)',
            'passo_a_passo': '''1. Prepare categorias: animal, cor, lugar, personagem bíblico
2. Cada pessoa completa: "Se eu fosse um animal seria... porque..."
3. Compartilha com grupo
4. Grupo pode adivinhar antes da pessoa falar
5. Continue com várias categorias
6. Respostas revelam muito sobre personalidade
7. Gera conversas interessantes
8. Celebre diversidade''',
            'tempo_estimado': '25-35 minutos',
            'quantidade_participantes': '8-30 pessoas',
            'nivel_intensidade': NivelIntensidade.BAIXO,
            'publico_indicado': PublicoIndicado.TODOS,
        },

        # DINÂMICAS PROFUNDAS E DE ENCERRAMENTO (101-120)
        {
            'numero': 101,
            'titulo': 'Noite do Silêncio Total',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Período extenso de silêncio absoluto (2-4 horas) para encontro profundo com Deus.',
            'objetivo': 'Experimentar presença de Deus através de silêncio prolongado e solidão proposital.',
            'materiais': '- Local tranquilo\n- Bíblias\n- Diários\n- Iluminação suave\n- Cobertores',
            'passo_a_passo': '''1. Prepare ambiente propício ao silêncio
2. Explique importância e regras
3. Período: 2-4 horas (geralmente noturno)
4. Sem celular, música, conversas
5. Atividades permitidas: ler Bíblia, orar, escrever, caminhar
6. Líderes disponíveis mas em silêncio
7. Sinal sonoro para encerramento
8. Compartilhamento opcional depois
9. Experiência transformadora''',
            'tempo_estimado': '120-240 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': '1 Reis 19:12 - "Uma voz mansa e suave."'
        },
        {
            'numero': 102,
            'titulo': 'Caminho das Velas',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Percurso iluminado por velas com estações de reflexão e oração.',
            'objetivo': 'Criar atmosfera de reverência e encontro íntimo com Deus.',
            'materiais': '- Velas (muitas!)\n- Caminho demarcado\n- Estações com textos\n- Música instrumental suave\n- Segurança contra fogo',
            'passo_a_passo': '''1. Monte caminho com velas dos dois lados
2. 5-7 estações ao longo do percurso
3. Cada estação: tema (perdão, gratidão, entrega)
4. Percorrem individualmente, em silêncio
5. Música ambiente muito baixa
6. Pace próprio de cada um
7. Podem parar quanto tempo precisarem
8. Final: altar ou cruz iluminada
9. Momento de encontro poderoso''',
            'tempo_estimado': '45-90 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 103,
            'titulo': 'Enterrar o Passado Simbolicamente',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Escrever pecados/passado e enterrar literalmente na terra.',
            'objetivo': 'Marcar momento de deixar passado para trás definitivamente.',
            'materiais': '- Papéis biodegradáveis\n- Canetas\n- Pá ou pazinhas\n- Local apropriado para cavar\n- Cruz ou marco',
            'passo_a_passo': '''1. Local ao ar livre apropriado
2. Cada pessoa escreve o que quer deixar no passado
3. Pode ser pecado, mágoa, trauma
4. Momento de confissão e reflexão (20 min)
5. Cave buraco coletivo ou individuais
6. Um por um, enterram seus papéis
7. Cobrem com terra
8. Plante cruz ou marco no local
9. Declare: "Está morto e enterrado"
10. Celebre nova vida''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
            'versiculo_base': 'Isaías 43:18 - "Não se lembrem das coisas passadas."'
        },
        {
            'numero': 104,
            'titulo': 'Escrever Pecados e Queimá-los',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Confessar pecados no papel e queimar simbolizando purificação.',
            'objetivo': 'Experimentar libertação através de confissão e símbolo de purificação.',
            'materiais': '- Papéis\n- Canetas\n- Recipiente seguro para queimar\n- Extintor ou água (segurança)\n- Local ventilado',
            'passo_a_passo': '''1. SEGURANÇA é prioridade
2. Ambiente sério e reverente
3. Leia 1 João 1:9
4. Cada pessoa escreve pecados confessados
5. Momento privado (15-20 min)
6. Um por um, levam papel à frente
7. Queimam no recipiente seguro
8. Observam papel se transformar em cinzas
9. Líder proclama perdão de Deus
10. Limpeza das cinzas simboliza purificação total''',
            'tempo_estimado': '40-60 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 105,
            'titulo': 'Processo de Reconciliação Guiado',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Facilitar reconciliação entre pessoas com conflitos reais.',
            'objetivo': 'Restaurar relacionamentos quebrados através de mediação e perdão.',
            'materiais': '- Sala privada\n- Líder treinado em mediação\n- Lenços\n- Bíblias',
            'passo_a_passo': '''1. Apenas com líder preparado
2. Identifique conflitos que precisam resolução
3. Convite voluntário (nunca forçado)
4. Ambiente privado e seguro
5. Regras: respeito, ouvir sem interromper
6. Cada pessoa expõe perspectiva
7. Líder facilita empatia mútua
8. Conduz a pedido de perdão
9. Oração de restauração
10. Follow-up posterior essencial''',
            'tempo_estimado': '60-120 minutos',
            'quantidade_participantes': '2-4 pessoas por sessão',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'Mateus 5:23-24 - "Reconcilie-se primeiro com seu irmão."'
        },
        {
            'numero': 106,
            'titulo': 'Confissão e Perdão Público',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Espaço para confissões voluntárias e declarações de perdão.',
            'objetivo': 'Experimentar liberdade através de confissão aberta e graça recebida.',
            'materiais': '- Microfone\n- Ambiente preparado\n- Líderes pastorais presentes\n- Lenços',
            'passo_a_passo': '''1. MUITO cuidado e sabedoria
2. Apenas em grupos maduros e seguros
3. Líder abre compartilhando primeiro
4. Espaço para confissões voluntárias
5. Ninguém obrigado
6. Grupo responde com graça
7. Declaração de perdão e aceitação
8. Oração sobre cada pessoa
9. Quebra barreiras de hipocrisia
10. Pode ser transformador ou perigoso - discernimento''',
            'tempo_estimado': '60-90 minutos',
            'quantidade_participantes': '15-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 107,
            'titulo': 'Abraço Restaurador',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Ministração através de abraços significativos e oração.',
            'objetivo': 'Transmitir amor de Deus através de toque apropriado e oração.',
            'materiais': '- Música de adoração\n- Lenços\n- Espaço confortável',
            'passo_a_passo': '''1. Explique poder do toque santo
2. Pessoas com necessidade de cura emocional vêm à frente
3. Líder abraça com paternidade/maternidade espiritual
4. Ora especificamente
5. Não é abraço comum - é ministração
6. Pode durar vários minutos
7. Pessoa recebe amor do Pai
8. Lágrimas e libertação são comuns
9. Equipe de apoio disponível''',
            'tempo_estimado': '45-90 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 108,
            'titulo': 'Renovação de Aliança com Deus',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Cerimônia formal de renovação de compromisso com Deus.',
            'objetivo': 'Marcar momento de reconsagração através de ritual significativo.',
            'materiais': '- Velas individuais\n- Declaração de aliança impressa\n- Altar\n- Música de adoração\n- Certificado (opcional)',
            'passo_a_passo': '''1. Ambiente de reverência
2. Ensine sobre aliança bíblica
3. Leia declaração de compromisso
4. Cada pessoa recebe vela apagada
5. Vêm à frente individualmente
6. Acendem vela na chama central (Cristo)
7. Declaram compromisso em voz alta
8. Assinam declaração
9. Oração de bênção
10. Guardam vela como memorial''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 109,
            'titulo': 'Consagração com Óleo',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Ungir com óleo para ministérios específicos ou consagração geral.',
            'objetivo': 'Separar pessoas para chamados específicos através de unção.',
            'materiais': '- Óleo de unção\n- Músicas de adoração\n- Toalhas',
            'passo_a_passo': '''1. Base bíblica: Tiago 5:14, unções do AT
2. Líder explica significado
3. Pode ser para cura, chamado, consagração
4. Pessoas vêm à frente
5. Líder unge testa fazendo cruz
6. Ora especificamente pelo chamado/necessidade
7. Imposição de mãos da liderança
8. Profecia/palavra se apropriado
9. Momento de separação e capacitação''',
            'tempo_estimado': '40-90 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
            'versiculo_base': 'Tiago 5:14 - "Orem sobre ele, ungindo-o com óleo."'
        },
        {
            'numero': 110,
            'titulo': 'Oração por Dons Espirituais',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Oração específica por liberação e capacitação em dons espirituais.',
            'objetivo': 'Buscar capacitação sobrenatural para servir o Reino.',
            'materiais': '- Bíblias\n- Lista de dons (1 Co 12, Rm 12, Ef 4)\n- Equipe de oração',
            'passo_a_passo': '''1. Ensino sobre dons espirituais
2. Identifique área de desejo/necessidade
3. Base bíblica: "desejem os melhores dons"
4. Momento de oração individual
5. Equipe disponível para orar com pessoas
6. Oração específica por capacitação
7. Incentive passo de fé depois
8. Follow-up sobre uso dos dons''',
            'tempo_estimado': '60-90 minutos',
            'quantidade_participantes': '15-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 111,
            'titulo': 'Definir Missão na Comunidade',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Cada pessoa define ação missionária concreta para executar após retiro.',
            'objetivo': 'Transformar experiência espiritual em missão prática definida.',
            'materiais': '- Formulários de compromisso\n- Canetas\n- Exemplos de missões\n- Calendário',
            'passo_a_passo': '''1. Reflita sobre aprendizados do retiro
2. Identifique necessidade em sua esfera
3. Defina ação concreta: quem, o que, quando, onde
4. Escreva compromisso específico
5. Exemplos: evangelizar vizinho, servir asilo, discipular alguém
6. Compartilhe em pequeno grupo
7. Grupo ora e responsabiliza
8. Troque contatos para acompanhamento
9. Defina data de prestação de contas''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-40 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 112,
            'titulo': 'Desafio de 30 Dias',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Comprometer-se com disciplina espiritual por 30 dias após retiro.',
            'objetivo': 'Estabelecer hábitos espirituais duradouros através de compromisso público.',
            'materiais': '- Cartões de desafio\n- Calendário de 30 dias\n- Plano de leitura/oração\n- Parceiros de prestação de contas',
            'passo_a_passo': '''1. Apresente disciplinas possíveis: devocional diário, jejum, memorização
2. Cada pessoa escolhe sua disciplina
3. Define detalhes: horário, duração, método
4. Assina compromisso
5. Forme duplas de prestação de contas
6. Recebem material de apoio
7. Check-ins semanais programados
8. Celebração ao completar 30 dias''',
            'tempo_estimado': '40-50 minutos + 30 dias',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 113,
            'titulo': 'Compromisso Selado com Testemunhas',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Declaração pública de compromisso com testemunhas que acompanharão.',
            'objetivo': 'Aumentar seriedade de compromissos através de prestação de contas.',
            'materiais': '- Formulário de compromisso\n- Canetas\n- Testemunhas designadas',
            'passo_a_passo': '''1. Cada pessoa escreve compromisso específico
2. Exemplos: pureza, perdoar alguém, frequentar igreja
3. Escolhe 2-3 testemunhas
4. Lê compromisso em voz alta
5. Testemunhas assinam documento
6. Testemunhas têm permissão para perguntar e acompanhar
7. Data de revisão definida (3-6 meses)
8. Documento guardado por líder''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 114,
            'titulo': 'Mural de Testemunhos do Retiro',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Criar mural coletivo com principais impactos e transformações.',
            'objetivo': 'Celebrar obra de Deus e criar memorial tangível do retiro.',
            'materiais': '- Painel grande\n- Canetas coloridas\n- Post-its\n- Fotos do retiro\n- Cola',
            'passo_a_passo': '''1. No encerramento do retiro
2. Monte painel: "O Que Deus Fez Aqui"
3. Cada pessoa escreve principal impacto
4. Cole fotos do retiro
5. Versículos marcantes
6. Compromissos assumidos
7. Todos assinam
8. Tire foto para compartilhar
9. Painel fica na igreja como memorial''',
            'tempo_estimado': '30-40 minutos',
            'quantidade_participantes': '10-100 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 115,
            'titulo': 'Vídeos de Familiares',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Exibir vídeos surpresa de familiares enviando mensagens de amor e fé.',
            'objetivo': 'Emocionar e fortalecer conexão familiar e apoio mútuo.',
            'materiais': '- Vídeos gravados previamente\n- Projetor e som\n- Lenços (muitos!)\n- Privacidade',
            'passo_a_passo': '''1. Coleta vídeos de familiares antes do retiro
2. Pais, cônjuges, filhos enviam mensagens
3. Conteúdo: amor, orgulho, fé, esperança
4. No momento adequado, projete
5. Pode ser individual ou coletivo
6. Prepare-se para muitas lágrimas
7. Momento profundamente tocante
8. Permite que participante sinta apoio
9. Fortalece propósito de mudança''',
            'tempo_estimado': '30-60 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 116,
            'titulo': 'Lavagem de Mãos Simbolizando Limpeza',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Lavar mãos em bacia enquanto confessa e recebe purificação.',
            'objetivo': 'Simbolizar limpeza de pecado e início de vida nova.',
            'materiais': '- Bacias com água\n- Toalhas limpas\n- Sabonete\n- Flores na água (opcional)\n- Música suave',
            'passo_a_passo': '''1. Monte estação com bacias de água limpa
2. Leia sobre purificação (Sl 51, 1 Jo 1:9)
3. Cada pessoa se aproxima
4. Enquanto lava mãos, confessa silenciosamente
5. Líder declara: "Seus pecados são perdoados"
6. Seca mãos em toalha limpa
7. Simboliza novo início
8. Momento simples mas poderoso''',
            'tempo_estimado': '25-40 minutos',
            'quantidade_participantes': '10-50 pessoas',
            'nivel_intensidade': NivelIntensidade.MEDIO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 117,
            'titulo': 'Vigília de Oração Noturna',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Noite inteira dedicada à oração, louvor e busca de Deus.',
            'objetivo': 'Buscar Deus intensamente através de vigília prolongada.',
            'materiais': '- Local confortável\n- Cobertores\n- Café e lanches leves\n- Instrumentos musicais\n- Velas\n- Programação flexível',
            'passo_a_passo': '''1. Início: 22h, término: 6h
2. Estrutura flexível: louvor, oração, silêncio, ensino
3. Revezamento de liderança
4. Focos de oração variados
5. Permite caminhar, deitar, ajoelhar
6. Momentos de alta intensidade e descanso
7. Café e lanche à meia-noite
8. Nascer do sol em oração
9. Experiência marcante e poderosa''',
            'tempo_estimado': '8 horas (noite toda)',
            'quantidade_participantes': '15-100 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.JOVENS,
        },
        {
            'numero': 118,
            'titulo': 'Jornada do Herói Pessoal',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Mapear jornada espiritual como narrativa de herói: chamado, desafios, transformação.',
            'objetivo': 'Ver vida como jornada épica onde Deus é autor e você é protagonista.',
            'materiais': '- Modelo de jornada do herói\n- Papel grande\n- Canetas coloridas\n- Exemplos bíblicos',
            'passo_a_passo': '''1. Ensine estrutura: mundo comum, chamado, recusa, mentor, provações, transformação, retorno
2. Cada pessoa mapeia sua jornada
3. Identifique: onde estou agora?
4. Quais foram minhas provações?
5. Quem foram meus mentores?
6. Que transformação Deus operou?
7. Qual minha missão ao "retornar"?
8. Compartilhe em grupos
9. Celebre história única de cada um''',
            'tempo_estimado': '60-90 minutos',
            'quantidade_participantes': '10-30 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.ADULTOS,
        },
        {
            'numero': 119,
            'titulo': 'Cruz Coletiva de Testemunhos',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Construir cruz grande usando testemunhos escritos como "madeira".',
            'objetivo': 'Visualizar que a cruz é formada por nossas histórias de redenção.',
            'materiais': '- Estrutura de cruz\n- Papéis de madeira\n- Canetas\n- Pregos ou cola\n- Iluminação especial',
            'passo_a_passo': '''1. Cruz vazia montada
2. Cada pessoa escreve breve testemunho em papel formato madeira
3. Tema: "Como a cruz mudou minha vida"
4. Um por um, pregam/colam na estrutura
5. Vão formando cruz cheia de testemunhos
6. Ao final, cruz está completa
7. Iluminem especialmente
8. Momento de adoração
9. Cruz fica como memorial''',
            'tempo_estimado': '45-60 minutos',
            'quantidade_participantes': '20-100 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
        },
        {
            'numero': 120,
            'titulo': 'Envio Missionário com Imposição de Mãos',
            'categoria': Categoria.PROFUNDAS,
            'descricao': 'Cerimônia de envio como encerramento, com imposição de mãos e oração.',
            'objetivo': 'Encerrar retiro enviando participantes como missionários para seus contextos.',
            'materiais': '- Óleo de unção (opcional)\n- Certificados de envio\n- Músicas de envio\n- Liderança para orar',
            'passo_a_passo': '''1. Momento final e culminante do retiro
2. Relembre jornada e aprendizados
3. Leia Grande Comissão (Mt 28:18-20)
4. Cada pessoa vem à frente
5. Liderança impõe mãos
6. Ora especificamente pelo chamado/contexto
7. Entrega certificado ou símbolo de envio
8. Abraço e bênção
9. Enviados como embaixadores de Cristo
10. Música final: "Ide" ou "Eu Navegarei"''',
            'tempo_estimado': '60-90 minutos',
            'quantidade_participantes': '15-50 pessoas',
            'nivel_intensidade': NivelIntensidade.ALTO,
            'publico_indicado': PublicoIndicado.TODOS,
            'versiculo_base': 'Mateus 28:19-20 - "Portanto, vão e façam discípulos de todas as nações."'
        },
    ]
    
    print("Iniciando população do banco de dados com TODAS as 120 dinâmicas...")
    print(f"{'='*60}")
    
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
    print(f"🎉 PROCESSO CONCLUÍDO COM SUCESSO! 🎉")
    print(f"{'='*60}")
    print(f"📊 Estatísticas:")
    print(f"   • Dinâmicas criadas: {criadas}")
    print(f"   • Dinâmicas atualizadas: {atualizadas}")
    print(f"   • Total no banco de dados: {Dinamica.objects.count()}")
    print(f"\n📁 Distribuição por categoria:")
    print(f"   • Quebra-Gelo: {Dinamica.objects.filter(categoria='QUEBRA_GELO').count()}")
    print(f"   • Autoconhecimento: {Dinamica.objects.filter(categoria='AUTOCONHECIMENTO').count()}")
    print(f"   • Trabalho em Equipe: {Dinamica.objects.filter(categoria='TRABALHO_EQUIPE').count()}")
    print(f"   • Espirituais: {Dinamica.objects.filter(categoria='ESPIRITUAIS').count()}")
    print(f"   • Diversão e Energia: {Dinamica.objects.filter(categoria='DIVERSAO_ENERGIA').count()}")
    print(f"   • Profundas: {Dinamica.objects.filter(categoria='PROFUNDAS').count()}")
    print(f"{'='*60}")
    print(f"\n✅ Seu MicroSaaS '+100 Dinâmicas Para Retiro na Igreja' está completo!")
    print(f"🚀 Execute: python manage.py runserver")
    print(f"🌐 Acesse: http://127.0.0.1:8000/dinamicas/")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    criar_todas_dinamicas()

Feature: Busca por cursos na Alura

  Scenario: Acessar a página da Alura e procurar por Inteligência Artificial
    Given que o usuário acessa a página "https://alura.com.br"
    When o usuário preenche a barra de busca com "Inteligência Artificial"
    And clica no botão de busca
    Then o usuário deve ver resultados relacionados a "Inteligência Artificial"
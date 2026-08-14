# Refatoração e Revisão Arquitetural

## Refatorando de Camadas para Hexagonal

1. Escolha um caso de uso real, não uma entidade.
2. Escreva o comportamento esperado em linguagem de negócio.
3. Extraia um input port que represente a capacidade do domínio.
4. Mova regra de negócio do controller, service procedural, DAO ou stored procedure para o domínio/application.
5. Identifique tudo que o domínio pede ao mundo externo.
6. Crie output ports para essas necessidades.
7. Faça adaptadores implementarem os output ports.
8. Faça controllers, consumers e jobs chamarem input ports.
9. Introduza DTOs/resources na borda.
10. Trave dependências com teste arquitetural ou módulo separado.

## Perguntas de Revisão

- O nome da porta comunica uma intenção de negócio?
- O domínio compila sem Spring Boot?
- Uma mudança de banco exigiria mudança no domínio?
- Uma mudança de JSON exigiria mudança no domínio?
- Existe regra relevante em controller, listener, repository ou mapper?
- O adaptador converte formatos externos sujos antes de chamar o domínio?
- A persistência está guiando o modelo ou apenas armazenando o modelo?
- Os testes de regra rodam sem subir contexto Spring?

## Sinais de Mau Design

- `@Entity`, `@Table`, `@JsonProperty`, `@RestController`, `@Service` ou `@Autowired` no domínio.
- `ResponseEntity`, `Pageable`, `ConsumerRecord`, `EntityManager`, `JdbcTemplate` ou `WebClient` atravessando portas.
- Porta com assinatura CRUD genérica quando o domínio fala em intenção.
- Mapper fazendo regra de negócio.
- Repository decidindo política de negócio.
- Controller chamando vários repositories diretamente.
- Teste de regra exigindo banco real, container ou contexto Spring inteiro.
- Adapters com pouco mapeamento porque a sujeira externa está entrando no domínio.

## Camada Anticorrupção

Adaptadores de saída devem absorver formatos externos:

- strings mágicas como `"NA"`, `"N/A"` ou `""`;
- paginação técnica quando o domínio precisa de coleção sem detalhe de página;
- campos quebrados, datas mal formatadas e tipos inconsistentes;
- retries e timeouts específicos de protocolo;
- diferenças de contrato entre APIs externas e linguagem do domínio.

O domínio deve receber tipos limpos e significativos.

## Evite Hexágono de Fachada

Não basta criar pacotes `domain`, `application` e `infrastructure` se:

- as classes internas continuam importando frameworks;
- portas só repetem repositories;
- adaptadores são pass-through sem tradução;
- a regra segue em controllers e DAOs;
- testes seguem lentos e dependentes de infraestrutura.

Hexagonal é fronteira de dependência, não decoração de diretório.

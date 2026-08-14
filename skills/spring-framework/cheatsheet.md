# Spring Framework Cheatsheet

## Core Container

| Necessidade | Use |
|---|---|
| Dependência obrigatória | Constructor injection |
| Dependência opcional | `ObjectProvider`, `Optional`, setter ou configuração explícita |
| Múltiplos beans do mesmo tipo | `@Qualifier`, `@Primary`, `@Fallback` |
| Criar beans manualmente | `@Bean` em `@Configuration` |
| Componentes por scan | `@Component`, `@Service`, `@Repository`, `@Controller` |
| Config por ambiente | `Environment`, profiles, property sources |

## Transações

| Caso | Caminho |
|---|---|
| Serviço de aplicação com unidade de trabalho | `@Transactional` |
| Fluxo precisa controle fino | `TransactionTemplate` |
| Evento após commit | transaction-bound events |
| Chamada interna no mesmo bean | cuidado: proxy não intercepta self-invocation |
| Exceção checked deve rollbackar | configurar rollback rules |

## Web

| Caso | Escolha |
|---|---|
| Aplicação Servlet tradicional | Spring MVC |
| Stack reativa fim-a-fim | WebFlux |
| Cliente HTTP moderno | `RestClient` ou `WebClient` conforme stack |
| Controller REST simples | `@RestController` + `ResponseEntity` quando precisar controle |
| Erros consistentes | `@ControllerAdvice` / error responses |

## Testing

| Teste | Ferramenta |
|---|---|
| Lógica de domínio | JUnit/Mockito sem Spring |
| MVC sem servidor real | `MockMvc` |
| WebFlux ou client HTTP | `WebTestClient` |
| Integração com contexto | Spring TestContext |
| Banco em teste | transações de teste, SQL scripts, test property sources |

## Armadilhas Rápidas

- `@Transactional` em método `private` ou self-call não faz o que você imagina.
- Misturar blocking JDBC em WebFlux pode destruir o modelo reativo.
- `@Autowired` em campo dificulta teste e imutabilidade.
- Contexto Spring em todo teste deixa suite lenta.
- AOP/proxy pode mudar comportamento de chamadas internas e final classes/methods.

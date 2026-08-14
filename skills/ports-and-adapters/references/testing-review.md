# Testes e Critérios de Qualidade

## Pirâmide Hexagonal

- **Domínio**: testes rápidos, sem Spring, sem banco, com stubs/fakes simples.
- **Adaptadores de entrada**: testes de contrato HTTP/mensagem, validação de DTO, status code, serialização.
- **Adaptadores de saída**: testes de integração com banco/API/broker ou doubles externos como MockServer/Testcontainers quando necessário.
- **Arquitetura**: testes ArchUnit ou regras de build impedindo dependências indevidas.

## Teste de Domínio com Stub

```java
final class InMemoryVehicleRegistry implements VehicleRegistry {
    private final Map<String, Vehicle> vehicles = new HashMap<>();

    @Override
    public boolean plateExists(Plate plate) {
        return vehicles.containsKey(plate.value());
    }

    @Override
    public void save(Vehicle vehicle) {
        vehicles.put(vehicle.plate().value(), vehicle);
    }
}
```

```java
@Test
void registersVehicleWhenPlateIsAvailable() {
    VehicleRegistry registry = new InMemoryVehicleRegistry();
    RegisterVehicle useCase = new RegisterVehicleService(registry);

    VehicleId id = useCase.register(new RegisterVehicleCommand("owner-1", "ABC1D23"));

    assertThat(id).isNotNull();
}
```

Esse teste deve rodar em milissegundos e não exigir contexto Spring.

## Testes de Adaptador

Para entrada:

- verifique request/response;
- garanta mapeamento para command;
- valide códigos HTTP e erros;
- não reteste regra de negócio completa.

Para saída:

- verifique queries, mapeamentos e transações;
- cubra conversão de tipos externos para tipos de domínio;
- simule respostas ruins de APIs externas;
- teste retry/timeout no adaptador, não no domínio.

## ArchUnit Essencial

```java
@Test
void domainShouldNotDependOnInfrastructure() {
    noClasses()
        .that().resideInAPackage("..domain..")
        .should().dependOnClassesThat()
        .resideInAnyPackage(
            "org.springframework..",
            "jakarta.persistence..",
            "com.fasterxml.jackson..",
            "..infrastructure.."
        )
        .check(importedClasses);
}
```

## Checklist de Pronto

- [ ] O caso de uso é expresso por uma porta de entrada.
- [ ] O domínio usa apenas tipos próprios ou tipos Java estáveis.
- [ ] Toda dependência externa entra por uma porta de saída.
- [ ] Controllers e consumers só traduzem e delegam.
- [ ] Repositories/adapters implementam SPIs e fazem mapeamento explícito.
- [ ] DTOs/resources não são entidades de domínio.
- [ ] Testes do domínio não sobem Spring.
- [ ] Testes de adaptadores validam tradução técnica.
- [ ] Há barreira automática contra importações proibidas.
- [ ] A equipe sabe dizer onde uma nova regra de negócio deve entrar.

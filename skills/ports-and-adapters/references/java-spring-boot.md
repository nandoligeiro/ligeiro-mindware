# Implementação em Java/Spring Boot

## Estrutura Recomendada

Prefira separar por módulo quando a proteção arquitetural importa:

```text
app/
  domain/
    model/
    api/
    spi/
    service/
  infrastructure/
    web/
    persistence/
    messaging/
    config/
```

Em projetos menores, pacotes bem delimitados podem bastar, mas use ArchUnit para impedir importações técnicas no domínio.

## Regra de Dependência

`infrastructure` pode depender de `domain`.

`domain` não pode depender de `infrastructure`, Spring MVC, Spring Data, Jackson, Kafka, Redis, JDBC, JPA ou clientes HTTP.

## Exemplo de Portas

```java
package com.acme.fleet.domain.api;

public interface RegisterVehicle {
    VehicleId register(RegisterVehicleCommand command);
}
```

```java
package com.acme.fleet.domain.spi;

public interface VehicleRegistry {
    boolean plateExists(Plate plate);
    void save(Vehicle vehicle);
}
```

## Exemplo de Serviço de Aplicação

```java
package com.acme.fleet.domain.service;

public final class RegisterVehicleService implements RegisterVehicle {
    private final VehicleRegistry registry;

    public RegisterVehicleService(VehicleRegistry registry) {
        this.registry = registry;
    }

    @Override
    public VehicleId register(RegisterVehicleCommand command) {
        Plate plate = Plate.from(command.plate());
        if (registry.plateExists(plate)) {
            throw new PlateAlreadyRegistered(plate);
        }
        Vehicle vehicle = Vehicle.register(command.ownerId(), plate);
        registry.save(vehicle);
        return vehicle.id();
    }
}
```

## Adaptador de Entrada

```java
@RestController
@RequestMapping("/vehicles")
final class VehicleController {
    private final RegisterVehicle registerVehicle;

    VehicleController(RegisterVehicle registerVehicle) {
        this.registerVehicle = registerVehicle;
    }

    @PostMapping
    ResponseEntity<VehicleResource> register(@RequestBody RegisterVehicleRequest request) {
        VehicleId id = registerVehicle.register(request.toCommand());
        return ResponseEntity.created(URI.create("/vehicles/" + id.value()))
            .body(new VehicleResource(id.value()));
    }
}
```

O controller traduz HTTP para comando de domínio e domínio para resource HTTP. Ele não decide regra.

## Adaptador de Saída

```java
@Repository
final class JpaVehicleRegistry implements VehicleRegistry {
    private final SpringDataVehicleRepository repository;

    JpaVehicleRegistry(SpringDataVehicleRepository repository) {
        this.repository = repository;
    }

    @Override
    public boolean plateExists(Plate plate) {
        return repository.existsByPlate(plate.value());
    }

    @Override
    public void save(Vehicle vehicle) {
        repository.save(VehicleJpaEntity.fromDomain(vehicle));
    }
}
```

O adaptador sabe JPA. O domínio não sabe.

## Injeção sem Poluir o Domínio

Use configuração na infraestrutura:

```java
@Configuration
class DomainConfiguration {
    @Bean
    RegisterVehicle registerVehicle(VehicleRegistry registry) {
        return new RegisterVehicleService(registry);
    }
}
```

Alternativa: criar uma anotação própria como `@DomainService` no domínio e configurar `@ComponentScan` filtrado na infraestrutura. Só faça isso se a equipe entender que a anotação é do domínio, não do Spring.

## DTOs e Resources

Não exponha entidades de domínio diretamente:

- request DTO entra pelo adaptador;
- command/value object cruza para o domínio;
- domain result volta;
- response resource sai pelo adaptador.

Isso permite versionar API e manter retrocompatibilidade sem renomear campos internos do domínio por medo de quebrar clientes externos.

## Transações

Mantenha a intenção transacional no caso de uso, mas a mecânica de transação pode ficar na borda de aplicação/infrastructure. Se usar `@Transactional`, evite espalhar no modelo de domínio puro; prefira aplicar no service de aplicação quando ele vive no módulo de aplicação ou no bean/configuração que o expõe.

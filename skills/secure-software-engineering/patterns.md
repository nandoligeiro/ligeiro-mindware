# Secure Software Engineering — Patterns e anti-patterns

## Patterns

### Threat-Control-Evidence
Converta cada ameaça relevante em um controle explícito e uma evidência verificável. Isso evita recomendações abstratas como "melhorar segurança".

### Resource-level authorization
Autorize no recurso e na operação, não apenas no endpoint ou papel global. Teste acessos positivos e negativos.

### Ephemeral credentials
Prefira credenciais curtas e emitidas sob demanda para CI/CD e automações, reduzindo blast radius e necessidade de rotação manual.

### Immutable artifact promotion
Promova o mesmo artefato entre ambientes. Evite rebuild para produção. Registre digest, provenance e identidade de build.

### Verify-before-deploy
Assinatura e provenance só viram controle quando o consumidor verifica identidade, digest e política antes do deploy.

### Secret lifecycle
Descoberta -> contenção -> revogação/rotação -> remoção -> prevenção de recorrência. Não pare em apagar do repositório.

### Security test as executable requirement
Transforme requisito sensível em teste ou policy: acesso negado, token expirado, input malicioso, artifact sem assinatura, identidade inesperada.

## Anti-patterns

### Checklist theater
Marcar controles sem relacioná-los a ameaça, asset ou evidência.

### Scanner absolution
Tratar SAST/SCA/DAST sem findings como prova de segurança.

### Role-only authorization
Usar apenas papéis amplos quando a decisão depende do recurso, tenant, ownership ou estado.

### Client-side security boundary
Confiar em campo oculto, UI, mobile app ou frontend para impedir operação sensível.

### Secret relocation
Mover segredo do código para variável de ambiente e considerar o problema encerrado sem rotação, acesso mínimo e redaction.

### Unsigned trust
Confiar em nome/tag de artefato sem digest e verificação de origem.

### Signed-but-unverified
Assinar artefatos, mas não aplicar policy de verificação no deploy.

### SBOM equals integrity
Confundir inventário de componentes com prova de origem ou não adulteração.

### Long-lived CI super-token
Usar token permanente com privilégios amplos em pipelines ou actions de terceiros.

### Security by obscurity as primary control
Esconder endpoint, nome de bucket, formato ou header sem controle real de autenticação/autorização.

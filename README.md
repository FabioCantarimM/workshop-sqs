# Workshop SQS

Passos detalhados para o desenvolvimento do projeto.

## Índice

- [Etapas de Desenvolvimento](#etapas-de-desenvolvimento)
- [Contato](#contato)

## Etapas de Desenvolvimento

1. **Criar o Bucket**
   - Configurar o bucket no AWS S3.

2. **Criar a Sub-Pasta**
   - Criar sub-pastas `raw` e `processed` dentro do bucket.

3. **Criar o Evento de Put e Post File**
   - Configurar eventos S3 para `put` e `post` de arquivos.

4. **Criar Fila SQS**
   - Criar a fila SQS no console da AWS.

5. **Adicionar Permissão na Fila**
   - Configurar permissões necessárias na fila SQS.

6. **Criar Lambda da Função**
   - Criar a função Lambda no console da AWS.

7. **Adicionar Layer do Pandas**
   - Adicionar a layer do Pandas na função Lambda para processamento de dados.

8. **Adicionar o Código que Será Executado**
   - Escrever e adicionar o código Python que será executado pela Lambda.

9. **Configurar Recursos do Lambda**
   - Configurar memória, timeout e outras propriedades da função Lambda.

10. **Adicionar Permissões no Lambda**
    - Configurar as permissões necessárias para a função Lambda acessar outros recursos AWS.

11. **Criar Evento de Teste**
    - Configurar um evento de teste para verificar o funcionamento da função Lambda.

## Contato

Para mais informações ou perguntas:

- Nome: Fabio Melo
- Email: fabio.cantarim@gmail.com
- LinkedIn: [seu-linkedin](https://www.linkedin.com/in/fabiocmelo))

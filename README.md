<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SPACE NEBULAS V.2</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #0b0c1f;
            color: #ffffff;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }
        h1 {
            color: #ffcc00;
            text-align: center;
        }
        h2 {
            color: #ffcc00;
            margin-top: 20px;
        }
        p {
            margin: 10px 0;
        }
        ul {
            list-style-type: disc;
            padding-left: 20px;
            margin: 10px 0;
        }
        a {
            color: #ffcc00;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>SPACE NEBULAS V.2</h1>
        <p>Space Nebulas é um projeto desenvolvido para fins de estudo de Python, com Framework Django e uma pequena introdução a HTML e CSS.</p>
        
        <p>A primeira versão foi disponibilizada em produção em <a href="https://space-nebula.vercel.app/" target="_blank">https://space-nebula.vercel.app/</a>.</p>

        <h2>Novidades na V.2</h2>
        <ul>
            <li>Implementação de Painel ADMIN</li>
            <li>Possibilidade de criação de usuários</li>
            <li>Autenticação de usuários registrados</li>
            <li>Funcionamento dos filtros e da função de busca</li>
            <li>Inclusão, edição e remoção de imagens pelos usuários (CRUD)</li>
            <li>Persistência das imagens em diversos ambientes de teste por meio do S3 da AWS</li>
        </ul>

        <h2>Próximos passos</h2>
        <p>Melhorar a aparência, experiência do usuário, funções e colocar a nova versão em produção.</p>
    </div>
</body>
</html>

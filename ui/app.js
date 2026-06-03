document.getElementById('pipelineForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const btn = document.getElementById('btnDisparar');
    const statusSucesso = document.getElementById('statusSucesso');
    const statusErro = document.getElementById('statusErro');

    // Pegando valores
    const path = document.getElementById('caminhoArquivo').value;
    const kindle = document.getElementById('kindleMode').checked;
    const title = document.getElementById('metaTitle').value;
    const author = document.getElementById('metaAuthor').value;

    btn.innerText = "Processando...";
    btn.disabled = true;

    // A MÁGICA: Chamando a função definida no seu main.py
    const resultado = await eel.processar_livro_gui(path, kindle, title, author)();

    btn.innerText = "⚡ Iniciar Processamento";
    btn.disabled = false;

    if (resultado.status === "success") {
        statusSucesso.innerText = resultado.message;
        statusSucesso.style.display = 'block';
        statusErro.style.display = 'none';
    } else {
        statusErro.innerText = "Erro: " + resultado.message;
        statusErro.style.display = 'block';
        statusSucesso.style.display = 'none';
    }
});
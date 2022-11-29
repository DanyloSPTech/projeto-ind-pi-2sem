let {spawn} = require('child_process');

function chamarApi(req, res){
    var link = req.params.link;

    let scriptPython = spawn('python', ['public/js/caca-reclamacao/main.py'], { encoding : 'utf8' });

    scriptPython.stdout.on('data', (data) => {
        // Saida do console da API
        console.log(`Saida do Terminal: ${data}`)
    });
    
    scriptPython.stderr.on('data', (data) => {
        // Saida de erros da API
        console.log(`Erros: ${data}`)
    });
    
    scriptPython.on('close', (code) => {
        // Saida da API
        console.log(`Script Executado!`)
        res.status(204).send("API Executada com sucesso!")
    });
}

module.exports = {
    chamarApi
}
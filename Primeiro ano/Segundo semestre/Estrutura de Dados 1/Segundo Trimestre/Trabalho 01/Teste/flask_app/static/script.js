document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('data-form');
    const dataList = document.getElementById('data-list');

    // Função para carregar os dados do servidor
    const loadData = async () => {
        const response = await fetch('/get_data');
        const data = await response.json();
        dataList.innerHTML = '';
        data.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.name}: ${item.value}`;
            dataList.appendChild(li);
        });
    };

    // Enviar novos dados ao servidor
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById('input-name').value;
        const value = document.getElementById('input-value').value;

        const response = await fetch('/save_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, value }),
        });

        if (response.ok) {
            document.getElementById('input-name').value = '';
            document.getElementById('input-value').value = '';
            loadData();
        }
    });

    // Carregar dados ao carregar a página
    loadData();
});

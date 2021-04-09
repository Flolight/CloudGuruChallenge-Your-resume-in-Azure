window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
});

const apiGateway = 'https://getresumeuserscounter.azurewebsites.net/api/getresumeuserscounter'

const getVisitCount = () => {
    let count = 0;

    fetch(apiGateway, {
        node: 'cors',
    }).then(response => {
        return response.json
    }).then(res => {
        const count = res;
        document.getElementById('counter').innerText = count;
    });
    return count;
}
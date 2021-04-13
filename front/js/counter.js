window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
});

const apiGateway = '/api/getcounter'
const getVisitCount = () => {
    let count = 0;

    fetch(apiGateway, {
        node: 'cors',
    }).then(response => {
        return response.json()
    }).then(res => {
        const count = res;
        document.getElementById('counter').innerText = count;
    });
    return count;
}
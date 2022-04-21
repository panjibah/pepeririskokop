const searchField = document.querySelector("#searchWord");
const tableOutput = document.querySelector(".table-output");
// tableOutput.style.display = "none";
const appTable = document.querySelector(".app-table");
// appTable.style.display = "none";
// const pageContainer = document.querySelector(".page-container");

// console.log(s);
// console.log(searchField)

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;
    const csrftoken = Cookies.get('csrftoken');

    if (searchValue.trim().length > 0) {
       
        console.log("searchValue", searchValue);
        fetch("/library/apiGetIdn/", {
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'searchText': searchValue }),
            method: 'POST',
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                console.log("data.length", data.length);


            });
    }

});
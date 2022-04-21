const searchField = document.querySelector("#searchWord");
const tableOutput = document.querySelector(".table-output");
tableOutput.style.display = "none";
const appTable = document.querySelector(".app-table");
appTable.style.display = "none";
const pageContainer = document.querySelector(".page-container");

// console.log(s);
// console.log(searchField)

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;
    const csrftoken = Cookies.get('csrftoken');

    if (searchValue.trim().length > 0) {
        ageContainer.style.display = "none";p
        console.log("searchValue", searchValue);
        fetch("http://127.0.0.1:8000/library/apix/", {
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body: JSON.stringify({ 'searchText': searchValue }),
            method: 'POST',
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                appTable.style.display = "none";
                tableOutput.style.display = "block";
                

                console.log("data.length", data.length);

                if(data.length === 0){
                    tableOutput.innerHTML="No result Found";

                   

                }else{
                    
                }
            });
    }else{
        tableOutput.style.display = "none";
        appTable.style.display="block";
        pageContainer.style.display="block"

    }

});
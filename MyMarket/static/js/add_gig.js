document.getElementById("gigPic").addEventListener("change", (event) => {
    filename = event.target.files[0].name;
    document.getElementById("image").innerText = filename
});